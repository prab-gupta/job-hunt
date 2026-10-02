#!/usr/bin/env python3
"""Stdio MCP server for the job-application tracker.

applications.csv is the stored data. This process is the only access layer
agents should use. It never reads or stores JOBS_ACCOUNT_PASSWORD.
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
import sys
from contextlib import contextmanager
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
_SPEC = importlib.util.spec_from_file_location(
    "sync_tracker",
    REPO / ".claude/skills/tracker-keeper/sync_tracker.py",
)
tracker = importlib.util.module_from_spec(_SPEC)
assert _SPEC.loader is not None
_SPEC.loader.exec_module(tracker)

CSV_REL = (
    Path("applications.csv"),
    Path("data/csvs/applications.csv"),
    Path("loop/applications.csv"),
)
LOCK_REL = Path("loop/.applications.lock")
CLAIMS_REL = Path("loop/.needs-you-claims.json")
SECRET_RE = re.compile(
    r"(?i)(password\s*[:=]|jobs_account_password\s*=|api[_-]?key\s*[:=]|"
    r"secret\s*[:=]|begin [a-z ]*private key)"
)
FORBIDDEN_FIELDS = {"password", "secret", "token", "jobs_account_password"}
GMAIL_NOTE_RE = re.compile(r"(?i)\bgmail\s*:")


class TrackerError(Exception):
    pass


def repo_root() -> Path:
    override = os.environ.get("TRACKER_ROOT")
    if override:
        return Path(override).resolve()
    return REPO


def _reject_secrets(payload: object) -> None:
    if isinstance(payload, dict):
        for key, value in payload.items():
            if str(key).strip().lower() in FORBIDDEN_FIELDS:
                raise TrackerError("refused: credential fields are not accepted")
            _reject_secrets(value)
        return
    if isinstance(payload, list):
        for item in payload:
            _reject_secrets(item)
        return
    if isinstance(payload, str) and SECRET_RE.search(payload):
        raise TrackerError("refused: a value looked like a credential")


def _sha256(path: Path) -> str:
    return tracker.sha256(path)


def _read_rows(root: Path) -> list[dict]:
    header, rows = tracker.read_csv(root / CSV_REL[0])
    if header != tracker.HEADER:
        raise TrackerError(f"bad header: {header}")
    return rows


def _write_root(root: Path, rows: list[dict]) -> None:
    tracker.write_csv(root / CSV_REL[0], rows)


def sync_paths(root: Path | None = None) -> dict:
    """Copy the root CSV onto the other two paths and require identical sha256."""
    root = root or repo_root()
    source = root / CSV_REL[0]
    if not source.is_file():
        raise TrackerError("applications.csv is missing")
    data = source.read_bytes()
    for rel in CSV_REL[1:]:
        dest = root / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    hashes = {str(rel): _sha256(root / rel) for rel in CSV_REL}
    if len(set(hashes.values())) != 1:
        raise TrackerError(f"sha256 mismatch after copy: {hashes}")
    return {"sha256": next(iter(hashes.values())), "paths": hashes}


def regenerate_needs_you(root: Path | None = None) -> dict:
    root = root or repo_root()
    rows = _read_rows(root)
    text = tracker.render_view(rows)
    path = root / tracker.VIEW_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    count = sum(1 for row in rows if row.get("status") == "needs_you")
    return {"path": str(tracker.VIEW_REL), "needs_you": count}


@contextmanager
def tracker_lock(root: Path):
    path = root / LOCK_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise TrackerError("tracker lock held; another writer is editing the CSV") from exc
    try:
        os.write(fd, f"pid={os.getpid()}\n".encode())
        yield
    finally:
        os.close(fd)
        path.unlink(missing_ok=True)


def _blank_row() -> dict:
    return {column: "" for column in tracker.HEADER}


def _clean_row(raw: dict) -> dict:
    _reject_secrets(raw)
    unknown = set(raw) - set(tracker.HEADER) - {"actor"}
    if unknown:
        raise TrackerError(f"unknown columns: {sorted(unknown)}")
    row = _blank_row()
    for column in tracker.HEADER:
        if column in raw and raw[column] is not None:
            row[column] = str(raw[column])
    status = row["status"].strip()
    if status not in tracker.ALLOWED:
        raise TrackerError(f"status {status!r} is not one of {tracker.ALLOWED}")
    row["status"] = status
    if not (row["url"].strip() or (row["company"].strip() and row["role"].strip())):
        raise TrackerError("a row needs a url, or both company and role")
    if status == "needs_you" and row["blocker"].strip() not in tracker.BLOCKER_TYPES:
        raise TrackerError(
            "needs_you blocker must be one of " + ", ".join(tracker.BLOCKER_TYPES)
        )
    if status == "skipped" and not (row["blocker"].strip() or row["notes"].strip()):
        raise TrackerError("skipped needs a reason in blocker or notes")
    return row


def _confirmation_ok(notes: str, date_applied: str, actor: str) -> None:
    if actor != "apply-auditor":
        raise TrackerError("submitted is only set by the apply-auditor flow")
    if not GMAIL_NOTE_RE.search(notes or ""):
        raise TrackerError("submitted requires a gmail confirmation note")
    if not (date_applied or "").strip():
        raise TrackerError("submitted requires date_applied")


def _check_transition(current: str, new: str, notes: str, date_applied: str, actor: str) -> None:
    if new not in tracker.ALLOWED:
        raise TrackerError(f"status {new!r} is not allowed")
    if new == "submitted":
        if current == "skipped":
            raise TrackerError("do not reapply a skipped row")
        _confirmation_ok(notes, date_applied, actor)
        return
    if current == "skipped" and new != "skipped":
        raise TrackerError("do not reapply a skipped row")
    if current == "submitted" and new == "needs_you":
        if actor != "apply-auditor":
            raise TrackerError("only apply-auditor can move submitted back to needs_you")
        return
    if current == "submitted" and new not in {"submitted", "needs_you"}:
        raise TrackerError("a submitted row cannot be reapplied")
    if new == "needs_you" and current == "needs_you":
        return
    if current == "needs_you" and new in {"failed", "skipped", "needs_you"}:
        if new == "skipped" and not (notes or "").strip():
            raise TrackerError("skipped needs a reason in notes")
        return
    if current == "failed" and new in {"failed", "needs_you", "skipped"}:
        return
    if new == current:
        return
    raise TrackerError(f"cannot move {current} to {new}")


def stats(root: Path | None = None) -> dict:
    root = root or repo_root()
    rows = _read_rows(root)
    counts = {status: 0 for status in tracker.ALLOWED}
    blockers = {kind: 0 for kind in tracker.BLOCKER_TYPES}
    other_blockers: dict[str, int] = {}
    for row in rows:
        status = row.get("status", "")
        if status in counts:
            counts[status] += 1
        if status == "needs_you":
            kind = (row.get("blocker") or "").strip()
            if kind in blockers:
                blockers[kind] += 1
            else:
                other_blockers[kind] = other_blockers.get(kind, 0) + 1
    return {
        "rows": len(rows),
        "status": counts,
        "needs_you_blockers": blockers,
        "unclassified_blockers": other_blockers,
    }


def search_rows(
    root: Path | None = None,
    status: str = "",
    blocker: str = "",
    company: str = "",
    text: str = "",
    limit: int = 20,
) -> dict:
    root = root or repo_root()
    _reject_secrets({"status": status, "blocker": blocker, "company": company, "text": text})
    if status and status not in tracker.ALLOWED:
        raise TrackerError(f"status {status!r} is not allowed")
    limit = max(1, min(int(limit or 20), 50))
    needle = (text or "").casefold()
    company_needle = (company or "").casefold()
    matched = []
    for index, row in enumerate(_read_rows(root), start=2):
        if status and row.get("status") != status:
            continue
        if blocker and (row.get("blocker") or "") != blocker:
            continue
        if company_needle and company_needle not in (row.get("company") or "").casefold():
            continue
        if needle:
            blob = " ".join(row.get(column) or "" for column in tracker.HEADER).casefold()
            if needle not in blob:
                continue
        item = dict(row)
        notes = item.get("notes") or ""
        if len(notes) > 400:
            item["notes"] = notes[:400] + "..."
        item["line"] = index
        matched.append(item)
    return {"total": len(matched), "rows": matched[:limit]}


def _load_claims(root: Path) -> list[dict]:
    path = root / CLAIMS_REL
    if not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise TrackerError("claims file is unreadable") from exc
    claims = data.get("claims", [])
    if not isinstance(claims, list):
        raise TrackerError("claims file is unreadable")
    return claims


def _save_claims(root: Path, claims: list[dict]) -> None:
    path = root / CLAIMS_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"claims": claims}, indent=2) + "\n", encoding="utf-8")


def _claim_id(row: dict) -> dict:
    kind, value = tracker.dedupe_key(row)
    return {"kind": kind, "value": value}


def _autonomous_queue(rows: list[dict]) -> list[dict]:
    queued = []
    for _key, _title, items in tracker.view_sections(rows):
        for row in items:
            if tracker.human_line(row):
                continue
            queued.append(row)
    return queued


def next_needs_you(agent: str, root: Path | None = None) -> dict:
    root = root or repo_root()
    agent = (agent or "").strip()
    if not agent:
        raise TrackerError("agent is required")
    _reject_secrets({"agent": agent})
    with tracker_lock(root):
        rows = _read_rows(root)
        queue = _autonomous_queue(rows)
        claims = _load_claims(root)
        live_keys = {_claim_id(row)["kind"] + "\n" + _claim_id(row)["value"] for row in queue}
        claims = [claim for claim in claims if claim.get("id") in live_keys]
        held = next((claim for claim in claims if claim.get("agent") == agent), None)
        if held:
            _save_claims(root, claims)
            for row in queue:
                ident = _claim_id(row)
                if ident["kind"] + "\n" + ident["value"] == held["id"]:
                    return {"row": row, "claim": held, "already_held": True}
        taken = {claim.get("id") for claim in claims}
        for row in queue:
            ident = _claim_id(row)
            claim_id = ident["kind"] + "\n" + ident["value"]
            if claim_id in taken:
                continue
            claim = {
                "id": claim_id,
                "kind": ident["kind"],
                "value": ident["value"],
                "agent": agent,
                "company": row.get("company", ""),
                "role": row.get("role", ""),
            }
            claims.append(claim)
            _save_claims(root, claims)
            return {"row": row, "claim": claim, "already_held": False}
        _save_claims(root, claims)
        return {"row": None, "claim": None, "already_held": False}


def release_claim(agent: str, claim_id: str = "", root: Path | None = None) -> dict:
    root = root or repo_root()
    agent = (agent or "").strip()
    if not agent:
        raise TrackerError("agent is required")
    _reject_secrets({"agent": agent, "claim_id": claim_id})
    with tracker_lock(root):
        claims = _load_claims(root)
        kept = []
        released = 0
        for claim in claims:
            same_agent = claim.get("agent") == agent
            same_id = not claim_id or claim.get("id") == claim_id
            if same_agent and same_id:
                released += 1
                continue
            kept.append(claim)
        _save_claims(root, kept)
        return {"released": released}


def _find_row(rows: list[dict], match_url: str, match_company: str, match_role: str) -> tuple[int, dict]:
    probe = _blank_row()
    probe["url"] = match_url or ""
    probe["company"] = match_company or ""
    probe["role"] = match_role or ""
    if not (probe["url"].strip() or (probe["company"].strip() and probe["role"].strip())):
        raise TrackerError("match_url or match_company and match_role is required")
    key = tracker.dedupe_key(probe)
    matches = [(index, row) for index, row in enumerate(rows) if tracker.dedupe_key(row) == key]
    if not matches:
        raise TrackerError("row not found")
    if len(matches) > 1:
        raise TrackerError("duplicate key; run tracker-keeper streamline before updating")
    return matches[0]


def add_row(raw: dict, actor: str = "", root: Path | None = None) -> dict:
    root = root or repo_root()
    raw = dict(raw)
    embedded = str(raw.pop("actor", "") or "")
    actor = (actor or embedded).strip()
    row = _clean_row(raw)
    if row["status"] == "submitted":
        _confirmation_ok(row["notes"], row["date_applied"], actor)
    with tracker_lock(root):
        rows = _read_rows(root)
        key = tracker.dedupe_key(row)
        for existing in rows:
            if tracker.dedupe_key(existing) == key:
                raise TrackerError(
                    f"duplicate key; existing status is {existing.get('status')}"
                )
        rows.append(row)
        _write_root(root, rows)
        hashes = sync_paths(root)
        view = regenerate_needs_you(root)
    return {"added": True, "key": {"kind": key[0], "value": key[1]}, "sync": hashes, "view": view}


def update_row(
    match_url: str = "",
    match_company: str = "",
    match_role: str = "",
    patch: dict | None = None,
    actor: str = "",
    root: Path | None = None,
) -> dict:
    root = root or repo_root()
    patch = dict(patch or {})
    actor = (actor or patch.pop("actor", "") or "").strip()
    _reject_secrets(patch)
    unknown = set(patch) - set(tracker.HEADER)
    if unknown:
        raise TrackerError(f"unknown columns: {sorted(unknown)}")
    with tracker_lock(root):
        rows = _read_rows(root)
        index, current = _find_row(rows, match_url, match_company, match_role)
        updated = dict(current)
        for column, value in patch.items():
            if value is None:
                continue
            updated[column] = str(value)
        _reject_secrets(updated)
        new_status = updated.get("status", "")
        if new_status not in tracker.ALLOWED:
            raise TrackerError(f"status {new_status!r} is not allowed")
        if new_status == "needs_you" and updated.get("blocker", "").strip() not in tracker.BLOCKER_TYPES:
            raise TrackerError(
                "needs_you blocker must be one of " + ", ".join(tracker.BLOCKER_TYPES)
            )
        _check_transition(
            current.get("status", ""),
            new_status,
            updated.get("notes", ""),
            updated.get("date_applied", ""),
            actor,
        )
        new_key = tracker.dedupe_key(updated)
        for other_index, other in enumerate(rows):
            if other_index != index and tracker.dedupe_key(other) == new_key:
                raise TrackerError("update would duplicate an existing key")
        rows[index] = updated
        _write_root(root, rows)
        hashes = sync_paths(root)
        view = regenerate_needs_you(root)
        if new_status != "needs_you":
            claims = _load_claims(root)
            claim_id = new_key[0] + "\n" + new_key[1]
            _save_claims(root, [claim for claim in claims if claim.get("id") != claim_id])
    return {"updated": True, "status": new_status, "sync": hashes, "view": view}


TOOLS = [
    {
        "name": "stats",
        "description": "Counts per status and per needs_you blocker type. Reads applications.csv.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
    {
        "name": "search_rows",
        "description": "Filter tracker rows by status, blocker type, company, or text.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "status": {"type": "string"},
                "blocker": {"type": "string"},
                "company": {"type": "string"},
                "text": {"type": "string"},
                "limit": {"type": "integer"},
            },
            "additionalProperties": False,
        },
    },
    {
        "name": "next_needs_you",
        "description": (
            "Claim the next needs_you row the autonomous drainer can work. "
            "Order matches the needs-you view: login/account rows with no human step, "
            "then other rows with no human step. Captcha, human sign-in, upload, "
            "eligibility, and no_confirm are not returned. Two agents cannot claim the same row."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {"agent": {"type": "string"}},
            "required": ["agent"],
            "additionalProperties": False,
        },
    },
    {
        "name": "release_claim",
        "description": "Release needs_you claims held by an agent, or one claim id.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "agent": {"type": "string"},
                "claim_id": {"type": "string"},
            },
            "required": ["agent"],
            "additionalProperties": False,
        },
    },
    {
        "name": "add_row",
        "description": (
            "Add one row. Validates columns and status. Rejects a duplicate normalized key "
            "(lowercase URL, query string and fragment removed, trailing slash stripped). "
            "submitted is rejected unless actor is apply-auditor and notes contain a gmail confirmation."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "company": {"type": "string"},
                "role": {"type": "string"},
                "url": {"type": "string"},
                "source": {"type": "string"},
                "status": {"type": "string"},
                "fit_score": {"type": "string"},
                "date_added": {"type": "string"},
                "date_applied": {"type": "string"},
                "salary_or_rate": {"type": "string"},
                "notes": {"type": "string"},
                "blocker": {"type": "string"},
                "actor": {"type": "string"},
            },
            "required": ["status"],
            "additionalProperties": False,
        },
    },
    {
        "name": "update_row",
        "description": (
            "Update one row by match_url or match_company plus match_role. "
            "Status transitions are validated. submitted is only set when actor is "
            "apply-auditor, notes contain a gmail: confirmation, and date_applied is set. "
            "A skipped row cannot be reapplied."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "match_url": {"type": "string"},
                "match_company": {"type": "string"},
                "match_role": {"type": "string"},
                "company": {"type": "string"},
                "role": {"type": "string"},
                "url": {"type": "string"},
                "source": {"type": "string"},
                "status": {"type": "string"},
                "fit_score": {"type": "string"},
                "date_added": {"type": "string"},
                "date_applied": {"type": "string"},
                "salary_or_rate": {"type": "string"},
                "notes": {"type": "string"},
                "blocker": {"type": "string"},
                "actor": {"type": "string"},
            },
            "additionalProperties": False,
        },
    },
    {
        "name": "regenerate_needs_you",
        "description": "Rewrite docs/needs-you.md from status=needs_you. The view is not a second database.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
    {
        "name": "sync_paths",
        "description": (
            "Copy applications.csv onto data/csvs/applications.csv and loop/applications.csv, "
            "then verify the three sha256 hashes match."
        ),
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
]


def _call_tool(name: str, arguments: dict) -> dict:
    arguments = arguments or {}
    _reject_secrets(arguments)
    if name == "stats":
        return stats()
    if name == "search_rows":
        return search_rows(
            status=arguments.get("status", ""),
            blocker=arguments.get("blocker", ""),
            company=arguments.get("company", ""),
            text=arguments.get("text", ""),
            limit=int(arguments.get("limit", 20)),
        )
    if name == "next_needs_you":
        return next_needs_you(arguments.get("agent", ""))
    if name == "release_claim":
        return release_claim(arguments.get("agent", ""), arguments.get("claim_id", ""))
    if name == "add_row":
        return add_row(dict(arguments), arguments.get("actor", ""))
    if name == "update_row":
        patch = {
            key: value
            for key, value in arguments.items()
            if key not in {"match_url", "match_company", "match_role", "actor"}
        }
        return update_row(
            match_url=arguments.get("match_url", ""),
            match_company=arguments.get("match_company", ""),
            match_role=arguments.get("match_role", ""),
            patch=patch,
            actor=arguments.get("actor", ""),
        )
    if name == "regenerate_needs_you":
        with tracker_lock(repo_root()):
            return regenerate_needs_you()
    if name == "sync_paths":
        with tracker_lock(repo_root()):
            return sync_paths()
    raise TrackerError(f"unknown tool {name}")


def _handle(message: dict) -> dict | None:
    method = message.get("method")
    msg_id = message.get("id")
    if method == "notifications/initialized":
        return None
    if method == "initialize":
        version = (message.get("params") or {}).get("protocolVersion") or "2024-11-05"
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": version,
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "tracker", "version": "1.0.0"},
            },
        }
    if method == "ping":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS}}
    if method == "tools/call":
        params = message.get("params") or {}
        try:
            result = _call_tool(params.get("name", ""), params.get("arguments") or {})
            payload = {"content": [{"type": "text", "text": json.dumps(result)}], "isError": False}
        except TrackerError as exc:
            payload = {"content": [{"type": "text", "text": str(exc)}], "isError": True}
        return {"jsonrpc": "2.0", "id": msg_id, "result": payload}
    if msg_id is None:
        return None
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "error": {"code": -32601, "message": f"method not found: {method}"},
    }


def main() -> int:
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            message = json.loads(line)
        except json.JSONDecodeError:
            continue
        response = _handle(message)
        if response is not None:
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
