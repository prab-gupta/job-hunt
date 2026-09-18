#!/usr/bin/env python3
"""Minimal SQLite state layer for the job-application pipeline."""

import argparse
import csv
import hashlib
import hmac
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

FIELDS = (
    "date", "company", "role", "ats", "url", "status",
    "confirmation_text", "salary_stated", "cover_letter_attached", "notes",
)
TERMINAL = {"DROPPED", "BLOCKED", "DEAD", "NEEDS_REVIEW"}
NEXT = {
    "NEW": "PREFLIGHTING",
    "PREFLIGHTING": "READY",
    "READY": "AWAITING_CONFIRMATION",
    "AWAITING_CONFIRMATION": "CONFIRMED",
    "CONFIRMED": "SUBMITTING",
    "SUBMITTING": "SUBMITTED",
}
STATE_PRIORITY = {
    "NEW": 0, "NEEDS_REVIEW": 1, "DEAD": 2, "DROPPED": 3, "BLOCKED": 4,
    "PREFLIGHTING": 5, "READY": 6, "AWAITING_CONFIRMATION": 7,
    "CONFIRMED": 8, "SUBMITTING": 9, "SUBMITTED": 10,
}
STATES = frozenset(STATE_PRIORITY)
PRODUCTION_BROWSER_IMAGE = "localhost/job-runner-browser:1"
TRACKING_KEYS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "source", "ref", "referrer", "trackingid", "trk", "gh_src",
}


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def key_text(value):
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def normalized_url(value):
    value = value.strip()
    if not re.match(r"^https?://", value, re.I):
        return None
    try:
        parts = urlsplit(value)
        host = (parts.hostname or "").casefold()
        if not host:
            return None
        port = f":{parts.port}" if parts.port else ""
        path = re.sub(r"/+", "/", parts.path).rstrip("/") or "/"
        query = urlencode(sorted(
            (k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
            if k.casefold() not in TRACKING_KEYS
        ))
        return urlunsplit(("https", host + port, path, query, ""))
    except ValueError:
        return None


def employer_role_key(company, role):
    return hashlib.sha256(f"{key_text(company)}\0{key_text(role)}".encode()).hexdigest()


def legacy_state(status):
    value = status.strip().upper()
    if "SUBMITTED" in value:
        return "SUBMITTED"
    if value.startswith(("DEAD", "CLOSED")) or "NO LONGER" in value:
        return "DEAD"
    if value.startswith(("DROP", "SKIP")):
        return "DROPPED"
    if value.startswith("BLOCKED"):
        return "BLOCKED"
    if value.startswith("NEEDS"):
        return "NEEDS_REVIEW"
    return "NEW"


def connect(db_path):
    db = sqlite3.connect(db_path)
    os.chmod(db_path, 0o600)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    db.execute("PRAGMA busy_timeout = 5000")
    return db


def init_db(db, schema_path):
    db.executescript(Path(schema_path).read_text(encoding="utf-8"))
    columns = {row[1] for row in db.execute("PRAGMA table_info(opportunities)")}
    additions = {
        "discovery_url": "TEXT NOT NULL DEFAULT ''",
        "source_id": "TEXT NOT NULL DEFAULT ''",
        "description": "TEXT NOT NULL DEFAULT ''",
        "verified_at": "TEXT",
    }
    for name, declaration in additions.items():
        if name not in columns:
            db.execute("ALTER TABLE opportunities ADD COLUMN %s %s" % (name, declaration))


def find_opportunity(db, url_key, role_key):
    if url_key:
        row = db.execute(
            "SELECT * FROM opportunities WHERE normalized_direct_url = ?", (url_key,)
        ).fetchone()
        if row:
            return row
    return db.execute(
        "SELECT * FROM opportunities WHERE employer_role_key = ?", (role_key,)
    ).fetchone()


def import_csv(db, csv_path):
    started = datetime.now(timezone.utc)
    source_file = str(Path(csv_path).resolve())
    seen = created = updated = submitted_rows = 0
    with open(csv_path, newline="", encoding="utf-8-sig") as handle, db:
        reader = csv.DictReader(handle, restkey="__extra__", restval="")
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise ValueError(f"expected columns {FIELDS}, got {reader.fieldnames}")
        for row_number, raw in enumerate(reader, 2):
            row = {field: raw[field] for field in FIELDS}
            extras = raw.get("__extra__") or []
            if extras:
                row["notes"] += "," + ",".join(extras)
            seen += 1
            state = legacy_state(row["status"])
            submitted_rows += state == "SUBMITTED"
            url_key = normalized_url(row["url"])
            role_key = employer_role_key(row["company"], row["role"])
            opportunity = find_opportunity(db, url_key, role_key)
            if opportunity is None:
                insert_state = "NEW" if state == "SUBMITTED" else state
                cursor = db.execute(
                    """INSERT INTO opportunities
                       (company, role, ats, direct_url, normalized_direct_url,
                        employer_role_key, compensation, state, legacy_status, updated_at)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (row["company"], row["role"], row["ats"], row["url"], url_key,
                     role_key, row["salary_stated"], insert_state, row["status"], now()),
                )
                opportunity_id = cursor.lastrowid
                created += 1
            else:
                opportunity_id = opportunity["id"]
                if state != "SUBMITTED" and STATE_PRIORITY[state] > STATE_PRIORITY[opportunity["state"]]:
                    db.execute(
                        "UPDATE opportunities SET state=?, legacy_status=?, updated_at=? WHERE id=?",
                        (state, row["status"], now(), opportunity_id),
                    )
                    updated += 1
            if state == "SUBMITTED":
                evidence = row["confirmation_text"].strip() or f"Legacy tracker status: {row['status']}"
                db.execute(
                    """INSERT OR IGNORE INTO applications
                       (opportunity_id, attempted_at, final_state, confirmation_evidence)
                       VALUES (?, ?, 'SUBMITTED', ?)""",
                    (opportunity_id, row["date"] or None, evidence),
                )
                previous_state = insert_state if opportunity is None else opportunity["state"]
                if previous_state != "SUBMITTED":
                    db.execute(
                        "UPDATE opportunities SET state='SUBMITTED', updated_at=? WHERE id=?",
                        (now(), opportunity_id),
                    )
                    updated += opportunity is not None
            encoded = json.dumps(row, ensure_ascii=False, sort_keys=True).encode()
            fingerprint = hashlib.sha256(encoded).hexdigest()
            values = [source_file, row_number, fingerprint, opportunity_id] + [row[f] for f in FIELDS]
            db.execute(
                f"""INSERT INTO source_rows
                    (source_file, row_number, row_fingerprint, opportunity_id, {','.join(FIELDS)})
                    VALUES ({','.join('?' for _ in values)})
                    ON CONFLICT(source_file, row_number) DO UPDATE SET
                    row_fingerprint=excluded.row_fingerprint,
                    opportunity_id=excluded.opportunity_id,
                    {','.join(f'{f}=excluded.{f}' for f in FIELDS)}
                    WHERE source_rows.row_fingerprint <> excluded.row_fingerprint
                       OR source_rows.opportunity_id <> excluded.opportunity_id""",
                values,
            )
        elapsed = int((datetime.now(timezone.utc) - started).total_seconds() * 1000)
        canonical = db.execute("SELECT count(*) FROM opportunities").fetchone()[0]
        db.execute(
            """INSERT INTO runs
               (kind, finished_at, input_count, output_count, elapsed_ms, details_json)
               VALUES ('import-csv', ?, ?, ?, ?, ?)""",
            (now(), seen, canonical, elapsed, json.dumps({
                "source_file": source_file, "created": created, "updated": updated,
                "submitted_containing_rows": submitted_rows,
            }, sort_keys=True)),
        )
    return {
        "source_rows_read": seen,
        "canonical_opportunities": canonical,
        "created": created,
        "state_upgrades": updated,
        "submitted_containing_rows": submitted_rows,
    }


def export_csv(db, output_path, source_file=None):
    args = []
    where = ""
    if source_file:
        where = "WHERE source_file = ?"
        args.append(str(Path(source_file).resolve()))
    rows = db.execute(
        f"SELECT {','.join(FIELDS)} FROM source_rows {where} ORDER BY source_file, row_number",
        args,
    )
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(FIELDS)
        count = 0
        for row in rows:
            writer.writerow([row[field] for field in FIELDS])
            count += 1
    os.chmod(output, 0o600)
    return {"exported_rows": count, "output": str(output)}


def status(db):
    counts = {
        row["state"]: row["count"]
        for row in db.execute("SELECT state, count(*) count FROM opportunities GROUP BY state")
    }
    return {
        "source_rows": db.execute("SELECT count(*) FROM source_rows").fetchone()[0],
        "canonical_opportunities": db.execute("SELECT count(*) FROM opportunities").fetchone()[0],
        "applications": db.execute("SELECT count(*) FROM applications").fetchone()[0],
        "submitted_opportunities": counts.get("SUBMITTED", 0),
        "states": counts,
        "journal_mode": db.execute("PRAGMA journal_mode").fetchone()[0],
        "foreign_keys": bool(db.execute("PRAGMA foreign_keys").fetchone()[0]),
        "awaiting_confirmation": counts.get("AWAITING_CONFIRMATION", 0),
        "confirmed": counts.get("CONFIRMED", 0),
        "needs_review": counts.get("NEEDS_REVIEW", 0),
    }


def _is_direct_url(url):
    host = (urlsplit(url).hostname or "").casefold()
    return bool(host and host not in {"linkedin.com", "www.linkedin.com", "freehire.me", "www.freehire.me"})


def store_candidates(db, candidates):
    created = revived = duplicates = rejected = 0
    with db:
        for item in candidates:
            company = str(item.get("company") or "").strip()
            role = str(item.get("role") or "").strip()
            discovered = str(item.get("direct_url") or "").strip()
            if not company or not role or not discovered.startswith("https://"):
                rejected += 1
                continue
            direct = discovered if _is_direct_url(discovered) else ""
            url_key = normalized_url(direct) if direct else None
            role_key = employer_role_key(company, role)
            existing = find_opportunity(db, url_key, role_key)
            if existing and existing["state"] == "DROPPED" and existing["legacy_status"] == "step3_uncapped_test":
                db.execute(
                    """UPDATE opportunities SET state='NEW', discovery_url=?, direct_url=?,
                       normalized_direct_url=?, source=?, location=?, source_id=?, legacy_status='', updated_at=?
                       WHERE id=?""",
                    (discovered, direct, url_key, str(item.get("source") or ""),
                     str(item.get("location") or ""), str(item.get("source_id") or ""), now(), existing["id"]),
                )
                revived += 1
                continue
            if existing:
                duplicates += 1
                continue
            db.execute(
                """INSERT INTO opportunities
                   (company, role, ats, discovery_url, direct_url, normalized_direct_url,
                    employer_role_key, source, location, fit, state, source_id, verified_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'NEW', ?, ?)""",
                (company, role, str(item.get("source") or ""), discovered, direct, url_key,
                 role_key, str(item.get("source") or ""), str(item.get("location") or ""),
                 item.get("fit"), str(item.get("source_id") or ""), now()),
            )
            created += 1
    return {"created": created, "revived": revived, "duplicates": duplicates, "rejected": rejected}


def sweep(db, lane, skills_root, bun):
    from plugin_workers import PluginWorkers, SOURCES
    from direct_ats import poll

    started = datetime.now(timezone.utc)
    if lane == "hot":
        requests = [
            {"source": "freehire", "query": "implementation engineer QA full stack AI automation", "limit": 25},
            {"source": "linkedin", "query": "software engineer", "location": "Italy", "limit": 10},
        ]
    elif lane == "denmark":
        requests = [
            {"source": "jobnet", "query": "softwareudvikler", "limit": 10},
            {"source": "jobindex", "query": "software developer", "limit": 10},
            {"source": "jobdanmark", "query": "softwareudvikler", "limit": 10},
            {"source": "jobbank", "query": "software developer", "limit": 10},
        ]
    else:
        raise ValueError("lane must be hot or denmark")
    health_row = db.execute(
        "SELECT details_json FROM runs WHERE kind='plugin-health' ORDER BY id DESC LIMIT 1"
    ).fetchone()
    disabled = []
    if health_row:
        try:
            health_state = json.loads(health_row[0])
            disabled = [request["source"] for request in requests
                        if request["source"] in health_state
                        and not health_state[request["source"]].get("healthy")]
            requests = [request for request in requests if request["source"] not in disabled]
        except (TypeError, json.JSONDecodeError):
            pass
    cooldowns = {}
    current = datetime.now(timezone.utc).timestamp()
    for request in requests:
        source = request["source"]
        row = db.execute(
            "SELECT finished_at FROM runs WHERE kind=? AND error_count=0 ORDER BY id DESC LIMIT 1",
            ("plugin:" + source,),
        ).fetchone()
        if row and row[0]:
            try:
                last = datetime.fromisoformat(row[0]).timestamp()
                cooldowns[source] = last + SOURCES[source].cooldown_seconds
            except ValueError:
                pass
    worker = PluginWorkers(skills_root, bun=bun, cooldowns=cooldowns)
    outcomes = worker.sweep(dict(request, now=current) for request in requests)
    candidates = []
    with db:
        for source, outcome in outcomes.items():
            candidates.extend(outcome["results"])
            db.execute(
                """INSERT INTO runs
                   (kind, finished_at, input_count, output_count, error_count, details_json)
                   VALUES (?, ?, 1, ?, ?, ?)""",
                ("plugin:" + source, now(), len(outcome["results"]), 0 if outcome["ok"] else 1,
                 json.dumps({"error": outcome.get("error", "")}, sort_keys=True)),
            )
    direct = {"boards": 0, "results": [], "errors": []}
    if lane == "hot":
        urls = [row[0] for row in db.execute(
            "SELECT direct_url FROM opportunities WHERE direct_url <> '' ORDER BY updated_at DESC LIMIT 500"
        )]
        direct = poll(urls)
        candidates.extend(direct["results"])
    if lane == "hot":
        non_eu_regions = {"north_america", "apac", "latam", "africa", "cis"}
        def eligible(item):
            raw = item.get("raw") if isinstance(item.get("raw"), dict) else {}
            regions = {str(value).casefold() for value in raw.get("regions", [])}
            if regions & non_eu_regions and not regions & {"eu", "global"}:
                return False
            return True
        candidates = [item for item in candidates if eligible(item)]
        def priority(item):
            location = str(item.get("location") or "").casefold()
            return (0 if "ital" in location else 1 if any(value in location for value in ("europe", "emea", " eu", "remote")) else 2)
        candidates = sorted(candidates, key=priority)[:30]
    stored = store_candidates(db, candidates)
    elapsed = int((datetime.now(timezone.utc) - started).total_seconds() * 1000)
    with db:
        db.execute(
            """INSERT INTO runs
               (kind, finished_at, input_count, output_count, error_count, elapsed_ms, details_json)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            ("sweep:" + lane, now(), len(requests), stored["created"],
             sum(not value["ok"] for value in outcomes.values()) + len(direct["errors"]), elapsed,
             json.dumps({"plugins": outcomes, "direct_ats": {"boards": direct["boards"], "errors": direct["errors"]}}, default=str, sort_keys=True)),
        )
    return {"lane": lane, "disabled_unhealthy": disabled, "sources": outcomes,
            "direct_ats": {"boards": direct["boards"], "errors": direct["errors"]}, **stored}


def plugin_health(db, skills_root, bun, sources):
    from plugin_workers import PluginWorkers
    sentinels = {
        "freehire": ("implementation engineer", None), "linkedin": ("software engineer", "Italy"),
        "jobnet": ("softwareudvikler", None), "jobindex": ("software developer", None),
        "jobdanmark": ("softwareudvikler", None), "jobbank": ("software developer", None),
    }
    worker = PluginWorkers(skills_root, bun=bun)
    result = {}
    for source in sources:
        try:
            query, location = sentinels[source]
            result[source] = worker.health(source, query, location)
        except Exception as exc:
            result[source] = {"source": source, "healthy": False, "error": str(exc)[:500]}
    with db:
        db.execute(
            """INSERT INTO runs (kind, finished_at, input_count, output_count, error_count, details_json)
               VALUES ('plugin-health', ?, ?, ?, ?, ?)""",
            (now(), len(sources), sum(bool(v.get("healthy")) for v in result.values()),
             sum(not bool(v.get("healthy")) for v in result.values()), json.dumps(result, default=str, sort_keys=True)),
        )
    return result


def preflight_queue(db, limit, opportunity_ids=None):
    from agent_tasks import build_preflight_task
    if opportunity_ids:
        ids = [int(value) for value in opportunity_ids]
        if len(ids) > 10:
            raise ValueError("preflight queue accepts at most 10 IDs")
        placeholders = ",".join("?" for _ in ids)
        rows = db.execute(
            """SELECT id opportunity_id, company, role, direct_url, location, source
               FROM opportunities WHERE id IN (%s) AND state='NEW' AND direct_url <> ''
               ORDER BY id""" % placeholders, ids
        ).fetchall()
        if len(rows) != len(set(ids)):
            raise ValueError("every requested preflight ID must be NEW with a direct URL")
    else:
        rows = db.execute(
            """SELECT id opportunity_id, company, role, direct_url, location, source
               FROM opportunities
               WHERE state='NEW' AND direct_url <> ''
               ORDER BY CASE WHEN lower(location) LIKE '%italy%' THEN 0 ELSE 1 END, id
               LIMIT ?""", (min(max(1, limit), 10),)
        ).fetchall()
    if not rows:
        return {"opportunities": [], "task": None}
    items = [dict(row) for row in rows]
    with db:
        db.executemany(
            "UPDATE opportunities SET state='PREFLIGHTING', updated_at=? WHERE id=? AND state='NEW'",
            [(now(), row["opportunity_id"]) for row in items],
        )
    task = build_preflight_task("preflight-" + uuid.uuid4().hex[:12], items)
    return {"opportunities": items, "task": task}


def record_preflights(db, payload):
    from agent_tasks import validate_preflight_result
    results = payload if isinstance(payload, list) else [payload]
    recorded = 0
    state_map = {"READY": "READY", "DEAD": "DEAD", "NEEDS_REVIEW": "NEEDS_REVIEW"}
    with db:
        for result in results:
            validate_preflight_result(result)
            opportunity_id = int(result["opportunity_id"])
            current = db.execute("SELECT state FROM opportunities WHERE id=?", (opportunity_id,)).fetchone()
            if not current or current[0] != "PREFLIGHTING":
                raise ValueError("preflight result is not for a PREFLIGHTING opportunity")
            decision = result["decision"]
            target = state_map.get(decision, "BLOCKED")
            db.execute(
                """INSERT INTO preflights
                   (opportunity_id, decision, required_fields_json, blockers_json, verified_at)
                   VALUES (?, ?, ?, ?, ?)""",
                (opportunity_id, decision, json.dumps(result["required_fields"]),
                 json.dumps(result["blockers"]), result["verified_at"]),
            )
            db.execute("UPDATE opportunities SET state=?, updated_at=? WHERE id=?", (target, now(), opportunity_id))
            recorded += 1
    return {"recorded": recorded}


def build_confirmation_batch(db, opportunity_ids):
    ids = [int(value) for value in opportunity_ids]
    if not ids or len(ids) > 10:
        raise ValueError("confirmation batch must contain 1 to 10 opportunity IDs")
    placeholders = ",".join("?" for _ in ids)
    rows = db.execute(
        "SELECT id, company, role, direct_url FROM opportunities WHERE id IN (%s) AND state='READY'" % placeholders,
        ids,
    ).fetchall()
    if len(rows) != len(set(ids)):
        raise ValueError("every batch member must exist exactly once in READY state")
    batch_id = datetime.now(timezone.utc).strftime("%Y-%m-%d") + "-" + uuid.uuid4().hex[:8]
    identity = "\n".join(
        "%s\0%s\0%s" % (row["id"], row["company"], row["role"])
        for row in sorted(rows, key=lambda item: item["id"])
    )
    digest = hashlib.sha256((batch_id + "\n" + identity).encode("utf-8")).hexdigest()[:16]
    confirmation_text = "CONFIRM %s %s" % (batch_id, digest)
    with db:
        db.execute(
            "INSERT INTO confirmation_batches (id, confirmation_text) VALUES (?, ?)",
            (batch_id, confirmation_text),
        )
        for row in rows:
            db.execute(
                "INSERT INTO confirmation_batch_items VALUES (?, ?, ?, ?)",
                (batch_id, row["id"], row["company"], row["role"]),
            )
            db.execute(
                "UPDATE opportunities SET state='AWAITING_CONFIRMATION', updated_at=? WHERE id=?",
                (now(), row["id"]),
            )
    return {
        "batch_id": batch_id, "items": [dict(row) for row in rows],
        "confirmation_text": confirmation_text,
    }


def confirm_batch(db, batch_id, confirmation_text):
    text = confirmation_text.strip()
    if not text:
        raise ValueError("confirmation text is required")
    row = db.execute(
        "SELECT confirmation_text, confirmed_at FROM confirmation_batches WHERE id=?", (batch_id,)
    ).fetchone()
    if not row:
        raise ValueError("confirmation batch not found")
    if not hmac_compare(text, row["confirmation_text"]):
        raise ValueError("confirmation text does not match this batch")
    with db:
        db.execute(
            "UPDATE confirmation_batches SET confirmed_at=? WHERE id=?",
            (now(), batch_id),
        )
        members = db.execute(
            "SELECT opportunity_id FROM confirmation_batch_items WHERE batch_id=?", (batch_id,)
        ).fetchall()
        for member in members:
            current = db.execute("SELECT state FROM opportunities WHERE id=?", (member[0],)).fetchone()[0]
            if current != "AWAITING_CONFIRMATION":
                raise ValueError("batch member is no longer awaiting confirmation")
            db.execute("UPDATE opportunities SET state='CONFIRMED', updated_at=? WHERE id=?", (now(), member[0]))
    return {"batch_id": batch_id, "confirmed": len(members), "confirmation_text": text}


def hmac_compare(left, right):
    return hmac.compare_digest(str(left).encode("utf-8"), str(right).encode("utf-8"))


def release_manifests(db, batch_id, cv_path, output_dir):
    cv = Path(cv_path)
    checksum = hashlib.sha256(cv.read_bytes()).hexdigest()
    rows = db.execute(
        """SELECT o.id opportunity_id, o.company, o.role, o.direct_url, o.state,
                  i.company confirmed_company, i.role confirmed_role
           FROM confirmation_batch_items i
           JOIN confirmation_batches b ON b.id=i.batch_id AND b.confirmed_at IS NOT NULL
           JOIN opportunities o ON o.id=i.opportunity_id
           WHERE i.batch_id=?""", (batch_id,)
    ).fetchall()
    if not rows:
        raise ValueError("batch is not confirmed or has no members")
    rows = [row for row in rows if row["state"] == "CONFIRMED"]
    if not rows:
        raise ValueError("batch has no remaining confirmed members")
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    manifests = []
    for row in rows:
        manifest = {
            "opportunity_id": row["opportunity_id"], "batch_id": batch_id,
            "company": row["company"], "role": row["role"], "direct_url": row["direct_url"],
            "state": "CONFIRMED", "released": True, "cv_checksum": checksum,
            "confirmed_item": {"company": row["confirmed_company"], "role": row["confirmed_role"]},
        }
        path = output / (str(row["opportunity_id"]) + ".json")
        path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
        os.chmod(path, 0o600)
        manifests.append(str(path))
    return {"batch_id": batch_id, "manifests": manifests, "cv_checksum": checksum}


def build_agent_tasks(profile_summary_path):
    from agent_tasks import LANES, build_sweep_task
    profile = json.loads(Path(profile_summary_path).read_text(encoding="utf-8"))
    run_id = "sweep-" + uuid.uuid4().hex[:12]
    return {
        "run_id": run_id,
        "tasks": [build_sweep_task(lane, run_id, profile) for lane in LANES],
    }


def record_agent_metrics(db, metrics_path):
    payload = json.loads(Path(metrics_path).read_text(encoding="utf-8"))
    tokens = payload.get("tokens", {})
    with db:
        db.execute(
            """INSERT INTO runs
               (kind, finished_at, elapsed_ms, token_count, details_json)
               VALUES (?, ?, ?, ?, ?)""",
            ("agent:" + str(payload.get("task_type", "unknown")), now(),
             int(payload.get("elapsed_ms", 0)), int(tokens.get("total", 0)),
             json.dumps(payload, sort_keys=True)),
        )
    return {"recorded": True, "run_id": payload.get("run_id"), "tokens": tokens.get("total", 0)}


def record_sweep_output(db, payload, lane="unknown"):
    from agent_tasks import validate_sweep_output
    validate_sweep_output(payload)
    candidates = [{
        "company": survivor["company"], "role": survivor["role"],
        "direct_url": survivor["direct_url"], "location": survivor["location"],
        "source": survivor["source_plugin"], "source_id": survivor["opportunity_id"],
        "fit": survivor["fit"],
    } for survivor in payload["survivors"]]
    stored = store_candidates(db, candidates)
    with db:
        db.execute(
            """INSERT INTO runs
               (kind, finished_at, input_count, output_count, details_json)
               VALUES (?, ?, ?, ?, ?)""",
            ("agent-sweep:" + lane, now(), len(payload["survivors"]),
             stored["created"] + stored["revived"],
             json.dumps({"lane": lane, "survivor_count": len(payload["survivors"])}, sort_keys=True)),
        )
    return {"lane": lane, "survivors": len(payload["survivors"]), **stored}


def _run_browser_container(manifest, profile_path, cv_path, evidence_dir, image, dry_run,
                           local_test=False):
    if not local_test and image != PRODUCTION_BROWSER_IMAGE:
        raise ValueError("production browser image is not allowlisted")
    command = [
        "podman", "--cgroup-manager=cgroupfs", "--events-backend=file",
        "run", "--rm", "--security-opt", "label=disable",
        "-v", str(Path(manifest).resolve()) + ":/work/manifest.json:ro",
        "-v", str(Path(profile_path).resolve()) + ":/work/profile.json:ro",
        "-v", str(Path(cv_path).resolve()) + ":/work/Prabhavit_CV.pdf:ro",
        "-v", str(Path(evidence_dir).resolve()) + ":/evidence",
        image, "python", "/app/browser_runner.py",
        "--manifest", "/work/manifest.json", "--profile", "/work/profile.json",
        "--cv", "/work/Prabhavit_CV.pdf", "--evidence-dir", "/evidence",
    ]
    if dry_run:
        command.append("--dry-run")
    if local_test:
        command.append("--local-test")
        command[4:4] = ["--add-host", "host.containers.internal:host-gateway"]
    run_env = {
        "HOME": "/var/lib/jobrunner",
        "PATH": os.environ.get("PATH", "/usr/local/bin:/usr/bin:/bin"),
        "XDG_RUNTIME_DIR": "/run/user/" + str(os.getuid()),
    }
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True, timeout=180, check=False, cwd="/var/lib/jobrunner",
                                env=run_env)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"state": "NEEDS_REVIEW", "error": str(exc)[:1000]}
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    if not lines:
        return {"state": "NEEDS_REVIEW",
                "error": (result.stderr or "browser returned no result")[:1000]}
    try:
        return json.loads(lines[-1])
    except json.JSONDecodeError:
        return {"state": "NEEDS_REVIEW", "error": "browser returned invalid JSON"}


def _verified_evidence_path(evidence_dir, evidence_path, started_at):
    root = Path(evidence_dir).resolve()
    raw = Path(str(evidence_path))
    if raw.is_absolute() and raw.parts[:2] == ("/", "evidence"):
        raw = root.joinpath(*raw.parts[2:])
    candidate = raw.resolve() if raw.is_absolute() else (root / raw).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None
    if not candidate.is_file() or candidate.stat().st_mtime < started_at:
        return None
    os.chmod(candidate, 0o600)
    return str(candidate)


def submit_batch(db, batch_id, cv_path, profile_path, evidence_dir, image, dry_run=False,
                 local_test=False):
    manifest_dir = Path(evidence_dir) / "manifests" / batch_id
    released = release_manifests(db, batch_id, cv_path, manifest_dir)
    results = []
    for manifest_path in released["manifests"]:
        manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
        opportunity_id = manifest["opportunity_id"]
        if not dry_run:
            transition(db, opportunity_id, "SUBMITTING")
            with db:
                db.execute(
                    """INSERT OR IGNORE INTO applications
                       (opportunity_id, batch_id, attempted_at, final_state, cv_checksum)
                       VALUES (?, ?, ?, 'SUBMITTING', ?)""",
                    (opportunity_id, batch_id, now(), released["cv_checksum"]),
                )
        started_at = time.time()
        outcome = _run_browser_container(
            manifest_path, profile_path, cv_path, evidence_dir, image, dry_run, local_test
        )
        state = outcome.get("state")
        if state == "SUBMITTED":
            verified_path = _verified_evidence_path(
                evidence_dir, outcome.get("evidence_path", ""), started_at
            )
            if not verified_path:
                outcome = {
                    **outcome, "state": "NEEDS_REVIEW",
                    "error": "submission evidence file is missing, stale, or outside evidence root",
                }
                state = "NEEDS_REVIEW"
            else:
                outcome["evidence_path"] = verified_path
        if not dry_run:
            with db:
                if state == "SUBMITTED" and str(outcome.get("evidence", "")).strip():
                    db.execute(
                        """INSERT OR REPLACE INTO applications
                           (opportunity_id, batch_id, attempted_at, final_state,
                            confirmation_evidence, evidence_path, cv_checksum)
                           VALUES (?, ?, ?, 'SUBMITTED', ?, ?, ?)""",
                        (opportunity_id, batch_id, now(), outcome["evidence"],
                         outcome.get("evidence_path", ""), released["cv_checksum"]),
                    )
                    transition(db, opportunity_id, "SUBMITTED")
                elif state == "RETRYABLE":
                    db.execute("UPDATE opportunities SET state='CONFIRMED', updated_at=? WHERE id=?",
                               (now(), opportunity_id))
                else:
                    db.execute("UPDATE opportunities SET state='NEEDS_REVIEW', updated_at=? WHERE id=?",
                               (now(), opportunity_id))
                    db.execute(
                        """INSERT OR REPLACE INTO applications
                           (opportunity_id, batch_id, attempted_at, final_state,
                            confirmation_evidence, evidence_path, cv_checksum)
                           VALUES (?, ?, ?, 'NEEDS_REVIEW', ?, ?, ?)""",
                        (opportunity_id, batch_id, now(), str(outcome.get("error", "")),
                         str(outcome.get("evidence_path", "")), released["cv_checksum"]),
                    )
        results.append({"opportunity_id": opportunity_id, **outcome})
    return {"batch_id": batch_id, "dry_run": dry_run, "results": results}


def transition(db, opportunity_id, target):
    target = target.upper()
    if target not in STATES:
        raise ValueError(f"unknown state: {target}")
    with db:
        row = db.execute("SELECT state FROM opportunities WHERE id=?", (opportunity_id,)).fetchone()
        if not row:
            raise ValueError(f"opportunity not found: {opportunity_id}")
        current = row["state"]
        allowed = target in TERMINAL and current != "SUBMITTED"
        allowed = allowed or NEXT.get(current) == target
        if not allowed:
            raise ValueError(f"invalid transition: {current} -> {target}")
        db.execute(
            "UPDATE opportunities SET state=?, updated_at=? WHERE id=?",
            (target, now(), opportunity_id),
        )
    return {"opportunity_id": opportunity_id, "from": current, "to": target}


def backup(db, output_path):
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    target = sqlite3.connect(output)
    try:
        db.backup(target)
    finally:
        target.close()
    os.chmod(output, 0o600)
    return {"backup": str(output), "bytes": output.stat().st_size}


def parser():
    root = argparse.ArgumentParser(prog="jobctl")
    root.add_argument("--db", default=os.environ.get("JOBCTL_DB", "/opt/job-runner/data/job_hunt.db"))
    root.add_argument("--schema", default=str(Path(__file__).with_name("schema.sql")))
    commands = root.add_subparsers(dest="command", required=True)
    commands.add_parser("init")
    imp = commands.add_parser("import-csv")
    imp.add_argument("csv_path")
    exp = commands.add_parser("export-csv")
    exp.add_argument("output_path")
    exp.add_argument("--source-file")
    commands.add_parser("status")
    trans = commands.add_parser("transition")
    trans.add_argument("opportunity_id", type=int)
    trans.add_argument("target_state")
    back = commands.add_parser("backup")
    back.add_argument("output_path")
    sweep_cmd = commands.add_parser("sweep")
    sweep_cmd.add_argument("--lane", choices=("hot", "denmark"), default="hot")
    sweep_cmd.add_argument("--skills-root", default="/opt/job-runner/plugins")
    sweep_cmd.add_argument("--bun", default="/opt/job-runner/bin/bun")
    health = commands.add_parser("plugin-health")
    health.add_argument("sources", nargs="*", default=["freehire", "linkedin", "jobnet", "jobindex", "jobdanmark", "jobbank"])
    health.add_argument("--skills-root", default="/opt/job-runner/plugins")
    health.add_argument("--bun", default="/opt/job-runner/bin/bun")
    queue = commands.add_parser("preflight-queue")
    queue.add_argument("--limit", type=int, default=10)
    queue.add_argument("--ids", nargs="*")
    record = commands.add_parser("record-preflights")
    record.add_argument("json_path")
    tasks = commands.add_parser("agent-tasks")
    tasks.add_argument("profile_summary_path")
    metrics = commands.add_parser("record-agent-metrics")
    metrics.add_argument("json_path")
    sweep_output = commands.add_parser("record-sweep-output")
    sweep_output.add_argument("json_path")
    sweep_output.add_argument("--lane", default="unknown")
    batch = commands.add_parser("build-confirmation-batch")
    batch.add_argument("opportunity_ids", nargs="+")
    confirm = commands.add_parser("confirm-batch")
    confirm.add_argument("batch_id")
    confirm.add_argument("--text", required=True)
    release = commands.add_parser("release-batch")
    release.add_argument("batch_id")
    release.add_argument("--cv", required=True)
    release.add_argument("--output-dir", default="/opt/job-runner/data/manifests")
    submit = commands.add_parser("submit-batch")
    submit.add_argument("batch_id")
    submit.add_argument("--cv", required=True)
    submit.add_argument("--profile", required=True)
    submit.add_argument("--evidence-dir", default="/opt/job-runner/data/evidence")
    submit.add_argument("--image", default=PRODUCTION_BROWSER_IMAGE)
    submit.add_argument("--dry-run", action="store_true")
    submit.add_argument("--local-test", action="store_true")
    return root


def main():
    args = parser().parse_args()
    Path(args.db).parent.mkdir(parents=True, exist_ok=True)
    db = connect(args.db)
    try:
        init_db(db, args.schema)
        if args.command == "init":
            result = status(db)
        elif args.command == "import-csv":
            result = import_csv(db, args.csv_path)
        elif args.command == "export-csv":
            result = export_csv(db, args.output_path, args.source_file)
        elif args.command == "status":
            result = status(db)
        elif args.command == "transition":
            result = transition(db, args.opportunity_id, args.target_state)
        elif args.command == "backup":
            result = backup(db, args.output_path)
        elif args.command == "sweep":
            result = sweep(db, args.lane, args.skills_root, args.bun)
        elif args.command == "plugin-health":
            result = plugin_health(db, args.skills_root, args.bun, args.sources)
        elif args.command == "preflight-queue":
            result = preflight_queue(db, args.limit, args.ids)
        elif args.command == "record-preflights":
            result = record_preflights(db, json.loads(Path(args.json_path).read_text(encoding="utf-8")))
        elif args.command == "agent-tasks":
            result = build_agent_tasks(args.profile_summary_path)
        elif args.command == "record-agent-metrics":
            result = record_agent_metrics(db, args.json_path)
        elif args.command == "record-sweep-output":
            result = record_sweep_output(
                db, json.loads(Path(args.json_path).read_text(encoding="utf-8")), args.lane
            )
        elif args.command == "build-confirmation-batch":
            result = build_confirmation_batch(db, args.opportunity_ids)
        elif args.command == "confirm-batch":
            result = confirm_batch(db, args.batch_id, args.text)
        elif args.command == "release-batch":
            result = release_manifests(db, args.batch_id, args.cv, args.output_dir)
        elif args.command == "submit-batch":
            result = submit_batch(db, args.batch_id, args.cv, args.profile,
                                  args.evidence_dir, args.image, args.dry_run, args.local_test)
        print(json.dumps(result, indent=2, sort_keys=True))
    except (ValueError, sqlite3.Error, OSError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 1
    finally:
        db.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
