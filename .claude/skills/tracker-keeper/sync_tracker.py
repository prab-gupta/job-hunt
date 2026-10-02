#!/usr/bin/env python3
"""Single-tracker helpers for applications.csv.

Proof and view regeneration never add, remove, or edit application rows.
Write the root CSV first, then copy those bytes onto the other two paths.
"""

from __future__ import annotations

import csv
import hashlib
import io
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[3]
CSV_REL = (
    Path("applications.csv"),
    Path("data/csvs/applications.csv"),
    Path("loop/applications.csv"),
)
VIEW_REL = Path("docs/needs-you.md")
HEADER = [
    "company",
    "role",
    "url",
    "source",
    "status",
    "fit_score",
    "date_added",
    "date_applied",
    "salary_or_rate",
    "notes",
    "blocker",
]
ALLOWED = ("needs_you", "submitted", "skipped", "failed")
STATUS_MAP = {
    "submitted": "submitted",
    "sent": "submitted",
    "confirmed": "submitted",
    "applied": "submitted",
    "application_sent": "submitted",
    "needs_you": "needs_you",
    "needs_human": "needs_you",
    "blocked": "needs_you",
    "blocked_by_company": "needs_you",
    "held": "needs_you",
    "action_required": "needs_you",
    "captcha": "needs_you",
    "skipped": "skipped",
    "skip": "skipped",
    "closed": "skipped",
    "dropped": "skipped",
    "dead": "skipped",
    "dead_link": "skipped",
    "not_a_fit": "skipped",
    "duplicate": "skipped",
    "do_not_apply": "skipped",
    "failed": "failed",
    "submit_failed": "failed",
    "error": "failed",
}
HUMAN_GATE = re.compile(
    r"captcha|login|upload|eligib|document|hcaptcha|recaptcha|turnstile|visa|sponsor",
    re.I,
)
SKIP_FACT = re.compile(r"closed|not a fit|not_a_fit|duplicate|expired posting|no longer", re.I)


def collapse(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip().lower())


def norm_url(url: str) -> str:
    raw = (url or "").strip().lower()
    if not raw:
        return ""
    parts = urlsplit(raw)
    if parts.scheme and parts.netloc:
        return f"{parts.scheme}://{parts.netloc}{parts.path.rstrip('/')}"
    return raw.split("#", 1)[0].split("?", 1)[0].rstrip("/")


def dedupe_key(row: dict) -> tuple[str, str]:
    url = (row.get("url") or "").strip()
    if url:
        return ("url", norm_url(url))
    return ("cr", collapse(row.get("company", "")) + "\n" + collapse(row.get("role", "")))


def tokenize_status(value: str) -> str:
    return re.sub(r"[\s-]+", "_", (value or "").strip().lower())


def map_status(row: dict) -> str:
    """Map an incoming status onto the four allowed values. Never invent submitted."""
    token = tokenize_status(row.get("status", ""))
    if token in STATUS_MAP:
        return STATUS_MAP[token]
    blob = f"{row.get('blocker', '')}\n{row.get('notes', '')}"
    if SKIP_FACT.search(blob):
        return "skipped"
    return "needs_you"


def unmapped_note(row: dict) -> str:
    token = tokenize_status(row.get("status", ""))
    if token in STATUS_MAP or not token:
        return row.get("notes", "") or ""
    note = (row.get("notes") or "").strip()
    tag = f"unmapped_status:{token}"
    return f"{note} | {tag}" if note else tag


def read_csv(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        header = list(reader.fieldnames or [])
        rows = [dict(row) for row in reader]
    return header, rows


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def flatten(value: str) -> str:
    text = (value or "").replace("\r\n", "\n").replace("\r", "\n").replace("\n", " ")
    return text


def md_cell(value: str) -> str:
    text = flatten(value).replace("\\", "\\\\").replace("|", "\\|")
    return text


def md_url(url: str) -> str:
    raw = flatten(url).strip()
    if not raw:
        return ""
    target = raw.replace(">", "%3E")
    return f"[{md_cell(raw)}](<{target}>)"


def render_view(rows: list[dict]) -> str:
    blocked = [row for row in rows if row.get("status") == "needs_you"]
    lines = [
        "# Needs you — blocked applications",
        "",
        "View of `applications.csv` rows with `status=needs_you`. "
        "This file is not a second database. Edit the CSV, then regenerate this page. "
        "Facts in the table are the CSV `blocker` and `notes` cells only.",
        "",
        f"**{len(blocked)}** rows, in CSV order.",
        "",
        "| Company | Role | Blocker | URL | Notes |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in blocked:
        cells = [
            md_cell(row.get("company", "")),
            md_cell(row.get("role", "")),
            md_cell(row.get("blocker", "")),
            md_url(row.get("url", "")),
            md_cell(row.get("notes", "")),
        ]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    return "\n".join(lines)


def unescape_cell(value: str) -> str:
    out: list[str] = []
    index = 0
    while index < len(value):
        if value[index] == "\\" and index + 1 < len(value):
            out.append(value[index + 1])
            index += 2
        else:
            out.append(value[index])
            index += 1
    return "".join(out)


def parse_view(text: str) -> list[dict]:
    rows = []
    for line in text.splitlines():
        if not line.startswith("| "):
            continue
        if line.startswith("| ---") or line.startswith("| Company"):
            continue
        parts = re.split(r"(?<!\\)\|", line)
        cells = [unescape_cell(part.strip()) for part in parts[1:-1]]
        if len(cells) != 5:
            rows.append({"_broken": True, "raw": line})
            continue
        url = cells[3]
        match = re.fullmatch(r"\[(.*)\]\(<(.*)>\)", url)
        if match:
            url = match.group(2).replace("%3E", ">")
        rows.append(
            {
                "company": cells[0],
                "role": cells[1],
                "blocker": cells[2],
                "url": url,
                "notes": cells[4],
            }
        )
    return rows


def normalized_fact(value: str) -> str:
    return flatten(value).strip()


def view_gaps(csv_rows: list[dict], view_text: str) -> list[str]:
    expected = [row for row in csv_rows if row.get("status") == "needs_you"]
    parsed = parse_view(view_text)
    problems = []
    if any(row.get("_broken") for row in parsed):
        problems.append(f"broken markdown rows: {sum(1 for row in parsed if row.get('_broken'))}")
    parsed = [row for row in parsed if not row.get("_broken")]
    if len(parsed) != len(expected):
        problems.append(f"view rows {len(parsed)} != needs_you rows {len(expected)}")
    limit = min(len(parsed), len(expected))
    for index in range(limit):
        got = parsed[index]
        want = expected[index]
        for field in ("company", "role", "blocker", "url", "notes"):
            if normalized_fact(got.get(field, "")) != normalized_fact(want.get(field, "")):
                label = f"{want.get('company', '')} / {want.get('role', '')}".strip()
                problems.append(f"row {index + 1} {label}: {field} differs")
                if len(problems) > 12:
                    return problems
    return problems


def duplicate_report(rows: list[dict]) -> list[str]:
    seen: dict[tuple[str, str], int] = {}
    lines = []
    for index, row in enumerate(rows, start=2):
        key = dedupe_key(row)
        if key in seen:
            lines.append(
                f"duplicate {key[0]} {key[1]!r} lines {seen[key]} and {index} "
                f"status={row.get('status')} company={row.get('company')!r} role={row.get('role')!r} "
                f"url={row.get('url')!r}"
            )
        else:
            seen[key] = index
    return lines


def check(root: Path = ROOT) -> int:
    paths = [root / rel for rel in CSV_REL]
    hashes = {path: sha256(path) for path in paths}
    print("sha256")
    for path, digest in hashes.items():
        print(f"  {digest}  {path.relative_to(root)}  bytes={path.stat().st_size}")
    identical = len(set(hashes.values())) == 1
    print(f"byte_identical: {identical}")
    header, rows = read_csv(paths[0])
    header_ok = header == HEADER
    print(f"header_ok: {header_ok} {header}")
    counts: dict[str, int] = {status: 0 for status in ALLOWED}
    bad = []
    for index, row in enumerate(rows, start=2):
        status = row.get("status", "")
        if status in counts:
            counts[status] += 1
        else:
            bad.append(f"line {index}: {status!r} {row.get('company')!r} / {row.get('role')!r}")
    print(f"data_rows: {len(rows)}")
    print("status_counts: " + ", ".join(f"{status}={counts[status]}" for status in ALLOWED))
    print(f"bad_status: {len(bad)}")
    for line in bad[:20]:
        print(f"  {line}")
    dups = duplicate_report(rows)
    print(f"duplicate_keys: {len(dups)}")
    for line in dups:
        print(f"  {line}")
    view_path = root / VIEW_REL
    view_text = view_path.read_text(encoding="utf-8")
    expected = render_view(rows)
    fresh = view_text == expected
    gaps = view_gaps(rows, view_text)
    print(f"needs_you_view_fresh: {fresh}")
    print(f"needs_you_view_gaps: {len(gaps)}")
    for line in gaps[:20]:
        print(f"  {line}")
    if not identical or not header_ok or bad:
        return 1
    if dups or not fresh:
        return 2
    return 0


def regenerate_view(root: Path = ROOT) -> int:
    _, rows = read_csv(root / CSV_REL[0])
    text = render_view(rows)
    path = root / VIEW_REL
    current = path.read_text(encoding="utf-8") if path.exists() else None
    if current == text:
        print(f"unchanged {VIEW_REL} needs_you={sum(1 for row in rows if row.get('status') == 'needs_you')}")
        return 0
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"regenerated {VIEW_REL} needs_you={sum(1 for row in rows if row.get('status') == 'needs_you')}")
    return 0


def copy_paths(root: Path = ROOT) -> int:
    source = root / CSV_REL[0]
    data = source.read_bytes()
    for rel in CSV_REL[1:]:
        dest = root / rel
        dest.write_bytes(data)
        print(f"copied {source.relative_to(root)} -> {rel}")
    return 0


def plan_change(rows: list[dict], incoming: dict, operation: str) -> dict:
    """Decide insert, update, or reject. Does not write."""
    mapped = dict(incoming)
    mapped["status"] = map_status(incoming)
    mapped["notes"] = unmapped_note(incoming)
    if mapped["status"] == "needs_you" and not (mapped.get("blocker") or "").strip():
        token = tokenize_status(incoming.get("status", ""))
        mapped["blocker"] = token if token and token not in STATUS_MAP else "needs_human"
    key = dedupe_key(mapped)
    matches = [(index, row) for index, row in enumerate(rows) if dedupe_key(row) == key]
    if not matches:
        if operation == "insert":
            return {"action": "insert", "row": mapped, "key": key}
        return {"action": "reject", "reason": "missing_key", "key": key}
    if len(matches) > 1:
        return {"action": "reject", "reason": "duplicate_key_in_csv", "key": key}
    index, current = matches[0]
    current_status = current.get("status")
    if operation == "insert":
        return {"action": "reject", "reason": "existing_key", "key": key, "status": current_status}
    if operation == "reapply" and current_status in {"submitted", "skipped"}:
        return {"action": "reject", "reason": "do_not_reapply", "key": key, "status": current_status}
    if operation == "audit_confirm":
        if current_status != "submitted":
            return {"action": "reject", "reason": "not_submitted", "key": key, "status": current_status}
        return {"action": "update", "index": index, "status": "submitted", "key": key}
    if operation == "audit_missing":
        if current_status != "submitted":
            return {"action": "reject", "reason": "not_submitted", "key": key, "status": current_status}
        return {"action": "update", "index": index, "status": "needs_you", "blocker": "no_confirm", "key": key}
    if current_status in {"submitted", "skipped"} and operation != "note_only":
        return {"action": "reject", "reason": "do_not_reapply", "key": key, "status": current_status}
    return {"action": "update", "index": index, "status": mapped["status"], "key": key}


def self_test() -> int:
    rows = [
        {
            "company": "Acme",
            "role": "AI Engineer",
            "url": "https://Example.com/jobs/1/?lang=en",
            "source": "test",
            "status": "submitted",
            "fit_score": "",
            "date_added": "2026-10-02",
            "date_applied": "2026-10-02",
            "salary_or_rate": "",
            "notes": "sent",
            "blocker": "",
        },
        {
            "company": "Beta",
            "role": "Konsultuppdrag | AI / Platform Engineer",
            "url": "",
            "source": "test",
            "status": "needs_you",
            "fit_score": "",
            "date_added": "2026-10-02",
            "date_applied": "",
            "salary_or_rate": "",
            "notes": "line\nbreak",
            "blocker": "login",
        },
    ]
    same = dedupe_key({"url": "https://example.com/jobs/1"}) == dedupe_key(rows[0])
    cr = dedupe_key({"company": "Beta", "role": "Konsultuppdrag | AI / Platform Engineer", "url": ""})
    cr2 = dedupe_key({"company": " beta ", "role": "Konsultuppdrag |  AI / Platform Engineer", "url": "  "})
    view = render_view(rows)
    gaps = view_gaps(rows, view)
    plans = [
        plan_change(rows, {"company": "Acme", "role": "AI Engineer", "url": "https://example.com/jobs/1/", "status": "needs_you"}, "insert"),
        plan_change(rows, {"company": "Gamma", "role": "PM", "url": "https://gamma.example/j/2", "status": "APPLYING"}, "insert"),
        plan_change(rows, {"company": "Beta", "role": "Other", "url": "", "status": "skipped", "blocker": "not_a_fit: 5+ years"}, "insert"),
        plan_change(rows, rows[0], "reapply"),
        plan_change(rows, rows[0], "audit_missing"),
        plan_change(rows, rows[1], "update"),
    ]
    expected_actions = ["reject", "insert", "insert", "reject", "update", "update"]
    ok = same and cr == cr2 and not gaps and [item["action"] for item in plans] == expected_actions
    mapped = map_status({"status": "confirmed"}) == "submitted"
    unknown = map_status({"status": "mystery", "blocker": "", "notes": ""}) == "needs_you"
    print(f"self_test: {'ok' if ok and mapped and unknown else 'failed'}")
    if not (ok and mapped and unknown):
        print("gaps", gaps)
        print("plans", plans)
        print("keys", same, cr == cr2, mapped, unknown)
        return 1
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=HEADER, lineterminator="\n")
    writer.writeheader()
    writer.writerow({key: rows[1].get(key, "") for key in HEADER})
    parsed = list(csv.DictReader(io.StringIO(buffer.getvalue())))
    if parsed[0]["notes"] != "line\nbreak":
        print("csv roundtrip failed")
        return 1
    return 0


def main(argv: list[str]) -> int:
    command = argv[1] if len(argv) > 1 else "check"
    if command == "check":
        return check()
    if command == "regenerate-view":
        return regenerate_view()
    if command == "copy-paths":
        return copy_paths()
    if command == "self-test":
        return self_test()
    print("usage: sync_tracker.py [check|regenerate-view|copy-paths|self-test]", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
