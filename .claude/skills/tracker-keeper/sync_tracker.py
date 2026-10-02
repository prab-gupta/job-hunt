#!/usr/bin/env python3
"""Single-tracker helpers for applications.csv.

`check` reports the three CSV paths and does not edit rows.
`streamline` merges duplicate keys and reclassifies blockers, then
writes the root CSV and copies those bytes onto the other two paths.
"""

from __future__ import annotations

import csv
import hashlib
import io
import re
import sys
from datetime import date
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
    """Normalized URL, else company + role.

    `norm_url` lowercases, drops the fragment, and drops the whole query
    string, so `?language=en` and any other query cannot make a second key.
    A trailing slash is stripped.
    """
    url = (row.get("url") or "").strip()
    if url:
        return ("url", norm_url(url))
    return ("cr", collapse(row.get("company", "")) + "\n" + collapse(row.get("role", "")))


# Furthest actionable state. submitted beats a still-blocked row.
# needs_you beats failed and skipped so a live blocker is not buried.
STATUS_RANK = {"submitted": 3, "needs_you": 2, "failed": 1, "skipped": 0}
BLOCKER_TYPES = ("login", "upload", "eligibility", "no_confirm", "other", "captcha")
CAPTCHA_RE = re.compile(r"captcha|recaptcha|hcaptcha|turnstile|anti-spam|anti spam", re.I)
LOGIN_RE = re.compile(
    r"\blogin\b|account required|account creation|create account|teamtailor connect|"
    r"join\.com|sign[- ]in|workday|successfactors|taleo|linkedin|indeed",
    re.I,
)
UPLOAD_RE = re.compile(
    r"upload|docs_gated|employment reference|transcript|diploma|certificate|cv widget",
    re.I,
)
ELIG_RE = re.compile(
    r"eligib|sponsor|right to work|work authorisation|work authorization|seniority gate|"
    r"lisbon_hybrid|hybrid only",
    re.I,
)
NOCONF_RE = re.compile(r"no_confirm|no confirm|did not confirm", re.I)
HUMAN_LOGIN_RE = re.compile(
    r"linkedin|indeed|apply with google|apply with linkedin|\boauth\b|ai interview|"
    r"\bmfa\b|bot detection",
    re.I,
)
CLOSED_RE = re.compile(
    r"form closed|not accepting|position no longer active|no longer active|"
    r"posting removed|410 gone|job closed|board no longer active",
    re.I,
)
MONTHS = {
    "jan": 1, "january": 1, "feb": 2, "february": 2, "mar": 3, "march": 3,
    "apr": 4, "april": 4, "may": 5, "jun": 6, "june": 6, "jul": 7, "july": 7,
    "aug": 8, "august": 8, "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "october": 10, "nov": 11, "november": 11, "dec": 12, "december": 12,
}


def past_deadline(text: str, today: date | None = None) -> str:
    """Return an ISO date when the row itself states a deadline before today."""
    today = today or date.today()
    for match in re.finditer(r"deadline was (\d{1,2}) ([A-Za-z]+) (\d{4})", text or "", re.I):
        month = MONTHS.get(match.group(2).lower())
        if not month:
            continue
        try:
            found = date(int(match.group(3)), month, int(match.group(1)))
        except ValueError:
            continue
        if found < today:
            return found.isoformat()
    return ""


def remember_blocker(row: dict, new_blocker: str) -> None:
    old = (row.get("blocker") or "").strip()
    notes = row.get("notes") or ""
    if old and old != new_blocker and old.lower() != new_blocker and old not in notes:
        notes = f"{notes} | prior_blocker: {old}".strip(" |")
        row["notes"] = notes
    row["blocker"] = new_blocker


NOTE_CAPTCHA_RE = re.compile(r"captcha|recaptcha|hcaptcha|turnstile", re.I)
NOTE_UPLOAD_RE = re.compile(
    r"docs_gated|employment reference|file upload|diploma|\btranscripts?\b|"
    r"certificate required|cv widget",
    re.I,
)
NOTE_ELIG_RE = re.compile(
    r"right to work|work authorisation|work authorization|not eligible|"
    r"seniority gate|uk work eligibility|requires sponsorship|sponsorship required",
    re.I,
)
NOTE_LOGIN_RE = re.compile(
    r"\blogin\b|account wall|account creation|account required|create account|"
    r"workday|successfactors|taleo|teamtailor connect|join\.com account|sign-in wall",
    re.I,
)


def classify_blocker(row: dict) -> str:
    """Map an existing blocker onto the six-type vocabulary. Does not invent a gate."""
    blocker = row.get("blocker") or ""
    notes = row.get("notes") or ""
    generic = collapse(blocker) in {"", "needs_human", "needs you", "blocked", "action_required", "needs_you"}
    if NOCONF_RE.search(blocker) or (generic and NOCONF_RE.search(notes)):
        return "no_confirm"
    if not generic:
        if CAPTCHA_RE.search(blocker):
            return "captcha"
        if UPLOAD_RE.search(blocker):
            return "upload"
        if ELIG_RE.search(blocker):
            if NOTE_CAPTCHA_RE.search(notes) and not re.search(r"not eligible|right to work", blocker, re.I):
                return "captcha"
            return "eligibility"
        if LOGIN_RE.search(blocker):
            return "login"
        return "other"
    if NOTE_CAPTCHA_RE.search(notes):
        return "captcha"
    if NOTE_UPLOAD_RE.search(notes):
        return "upload"
    if NOTE_ELIG_RE.search(notes):
        return "eligibility"
    if NOTE_LOGIN_RE.search(notes):
        return "login"
    return "other"


def login_is_autonomous(row: dict) -> bool:
    blob = f"{row.get('url') or ''} {row.get('blocker') or ''} {row.get('notes') or ''}"
    return not HUMAN_LOGIN_RE.search(blob)


def verifiable_stop(row: dict) -> str:
    """closed or expired only when this row's own text says so."""
    blob = f"{row.get('blocker') or ''} {row.get('notes') or ''}"
    if past_deadline(blob):
        return "expired"
    if re.search(r"401 vs 404|404 vs 429", blob, re.I):
        return ""
    if CLOSED_RE.search(blob):
        return "closed"
    return ""


def account_skip_should_reopen(row: dict) -> bool:
    """True when a skip's own text says the only gate was account creation."""
    blob = f"{row.get('blocker') or ''} {row.get('notes') or ''}"
    if re.search(
        r"no longer active|form closed|not a fit|not a single role|reposter|aggregator|"
        r"channel finding|not a role",
        blob,
        re.I,
    ):
        return False
    return bool(re.search(r"account creation required", blob, re.I))


def merge_duplicate_keys(rows: list[dict]) -> tuple[list[dict], list[str]]:
    grouped: dict[tuple[str, str], list[dict]] = {}
    order: list[tuple[str, str]] = []
    for row in rows:
        key = dedupe_key(row)
        if key not in grouped:
            grouped[key] = []
            order.append(key)
        grouped[key].append(row)
    merged_rows: list[dict] = []
    reports: list[str] = []
    for key in order:
        group = grouped[key]
        if len(group) == 1:
            merged_rows.append(group[0])
            continue
        ranked = sorted(group, key=lambda item: STATUS_RANK.get(item.get("status", ""), -1), reverse=True)
        winner = dict(ranked[0])
        pieces: list[str] = []
        seen: set[str] = set()
        for item in ranked:
            for part in re.split(r"\s+\|\s+", item.get("notes") or ""):
                part = part.strip()
                if part and part not in seen:
                    seen.add(part)
                    pieces.append(part)
            other_url = (item.get("url") or "").strip()
            winner_url = (winner.get("url") or "").strip()
            if other_url and other_url != winner_url:
                bit = f"also_url: {other_url}"
                if bit not in seen:
                    seen.add(bit)
                    pieces.append(bit)
            other_blocker = (item.get("blocker") or "").strip()
            if other_blocker and other_blocker != (winner.get("blocker") or "").strip():
                bit = f"prior_blocker: {other_blocker}"
                if bit not in seen and other_blocker not in (winner.get("notes") or ""):
                    seen.add(bit)
                    pieces.append(bit)
            if not (winner.get("date_applied") or "").strip() and (item.get("date_applied") or "").strip():
                winner["date_applied"] = item["date_applied"]
            if not (winner.get("salary_or_rate") or "").strip() and (item.get("salary_or_rate") or "").strip():
                winner["salary_or_rate"] = item["salary_or_rate"]
            if not (winner.get("fit_score") or "").strip() and (item.get("fit_score") or "").strip():
                winner["fit_score"] = item["fit_score"]
        winner["notes"] = " | ".join(pieces)
        merged_rows.append(winner)
        statuses = ",".join(item.get("status", "") for item in group)
        reports.append(
            f"merged {key[0]} {key[1]} kept {winner.get('status')} from [{statuses}] "
            f"{winner.get('company')} / {winner.get('role')}"
        )
    return merged_rows, reports


def streamline_rows(rows: list[dict]) -> tuple[list[dict], dict]:
    """Merge duplicate keys, then apply only repo-verifiable status fixes."""
    merged, merge_reports = merge_duplicate_keys(rows)
    reopened: list[str] = []
    stopped: list[str] = []
    for row in merged:
        if row.get("status") == "skipped" and account_skip_should_reopen(row):
            row["status"] = "needs_you"
            remember_blocker(row, "login")
            reopened.append(f"{row.get('company')} / {row.get('role')}")
        elif row.get("status") == "needs_you":
            reason = verifiable_stop(row)
            if reason:
                remember_blocker(row, reason)
                row["status"] = "skipped"
                stopped.append(f"{reason}: {row.get('company')} / {row.get('role')}")
    classified: dict[str, int] = {kind: 0 for kind in BLOCKER_TYPES}
    for row in merged:
        if row.get("status") != "needs_you":
            continue
        kind = classify_blocker(row)
        remember_blocker(row, kind)
        classified[kind] += 1
    thin: list[str] = []
    for row in merged:
        if row.get("status") != "skipped":
            continue
        blocker = collapse(row.get("blocker") or "")
        notes = collapse(row.get("notes") or "")
        if blocker in {"closed", "expired"}:
            continue
        if notes in {"", "fde", "eligibility", "personio empty"} and blocker in {"", "eligibility"}:
            thin.append(
                f"{row.get('company')} / {row.get('role')} | blocker={row.get('blocker') or ''} | notes={row.get('notes') or ''}"
            )
    report = {
        "merged": merge_reports,
        "reopened": reopened,
        "stopped": stopped,
        "classified": classified,
        "thin_skips": thin,
    }
    return merged, report


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


def human_line(row: dict) -> str:
    """One line for Prabhavit when a person must act. Empty when the drainer can try."""
    kind = row.get("blocker") or ""
    blob = f"{row.get('notes') or ''} {row.get('url') or ''}"
    if kind == "login" and login_is_autonomous(row):
        return ""
    if kind == "captcha":
        return "Solve the captcha on this posting."
    if kind == "login":
        if re.search(r"linkedin", blob, re.I):
            return "Sign in to LinkedIn in the Chrome window on your machine."
        if re.search(r"indeed", blob, re.I):
            return "Finish the Indeed sign-in on your machine."
        if re.search(r"ai interview", blob, re.I):
            return "Sit the AI interview named in the notes."
        return "Sign in on this site yourself."
    if kind == "upload":
        return "Upload the document named in the notes."
    if kind == "eligibility":
        if re.search(r"seniority|\d\+ years", blob, re.I):
            return "The notes say the years bar is above the profile. Decide whether to skip it."
        return "Decide the location or work-authorization point in the notes."
    if kind == "no_confirm":
        return "Check Gmail and the portal. There is no application confirmation on file."
    if re.search(r"essay|anti-ai|own words", blob, re.I):
        return "Write the required answer yourself."
    if re.search(r"cooldown|90-day", blob, re.I):
        return "Wait until the date in the notes, then retry."
    return ""


def view_sections(rows: list[dict]) -> list[tuple[str, str, list[dict]]]:
    buckets: dict[str, list[dict]] = {
        "login_auto": [],
        "login_human": [],
        "upload": [],
        "eligibility": [],
        "no_confirm": [],
        "other": [],
        "captcha": [],
    }
    for row in rows:
        if row.get("status") != "needs_you":
            continue
        kind = row.get("blocker") or "other"
        if kind == "login" and login_is_autonomous(row):
            buckets["login_auto"].append(row)
        elif kind == "login":
            buckets["login_human"].append(row)
        elif kind in buckets:
            buckets[kind].append(row)
        else:
            buckets["other"].append(row)
    order = [
        ("login_auto", "Login / account — drainer can clear"),
        ("login_human", "Login / account — human sign-in"),
        ("upload", "Upload"),
        ("eligibility", "Eligibility"),
        ("no_confirm", "No confirmation"),
        ("other", "Other"),
        ("captcha", "Captcha"),
    ]
    return [(key, title, buckets[key]) for key, title in order if buckets[key]]


def render_view(rows: list[dict]) -> str:
    sections = view_sections(rows)
    total = sum(len(items) for _, _, items in sections)
    lines = [
        "# Needs you — blocked applications",
        "",
        "View of `applications.csv` rows with `status=needs_you`. "
        "This file is not a second database. Edit the CSV, then regenerate this page. "
        "Facts in the table are the CSV `blocker` and `notes` cells. "
        "The You column is one line for Prabhavit only where a human has to act.",
        "",
        f"**{total}** rows. Login/account rows the drainer can clear are first. Captcha rows are last.",
        "",
    ]
    for _key, title, items in sections:
        lines.append(f"## {title} ({len(items)})")
        lines.append("")
        lines.append("| Company | Role | Blocker | URL | Notes | You |")
        lines.append("| --- | --- | --- | --- | --- | --- |")
        for row in items:
            cells = [
                md_cell(row.get("company", "")),
                md_cell(row.get("role", "")),
                md_cell(row.get("blocker", "")),
                md_url(row.get("url", "")),
                md_cell(row.get("notes", "")),
                md_cell(human_line(row)),
            ]
            lines.append("| " + " | ".join(cells) + " |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


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
        if len(cells) not in {5, 6}:
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
    expected = [row for _key, _title, items in view_sections(csv_rows) for row in items]
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
    blocker_counts: dict[str, int] = {kind: 0 for kind in BLOCKER_TYPES}
    for row in rows:
        if row.get("status") == "needs_you":
            kind = row.get("blocker") or ""
            if kind in blocker_counts:
                blocker_counts[kind] += 1
            else:
                blocker_counts[kind] = blocker_counts.get(kind, 0) + 1
    print("needs_you_blockers: " + ", ".join(f"{kind}={blocker_counts[kind]}" for kind in blocker_counts))
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


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADER, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") or "" for key in HEADER})


def streamline(root: Path = ROOT, dry: bool = False) -> int:
    header, rows = read_csv(root / CSV_REL[0])
    if header != HEADER:
        print("bad header", header)
        return 1
    updated, report = streamline_rows(rows)
    counts: dict[str, int] = {status: 0 for status in ALLOWED}
    for row in updated:
        status = row.get("status", "")
        counts[status] = counts.get(status, 0) + 1
    print(f"merged: {len(report['merged'])}")
    for line in report["merged"]:
        print(f"  {line}")
    print(f"reopened: {len(report['reopened'])}")
    for line in report["reopened"]:
        print(f"  {line}")
    print(f"stopped: {len(report['stopped'])}")
    for line in report["stopped"]:
        print(f"  {line}")
    print("classified: " + ", ".join(f"{kind}={report['classified'][kind]}" for kind in BLOCKER_TYPES))
    print(f"thin_skips: {len(report['thin_skips'])}")
    for line in report["thin_skips"]:
        print(f"  {line}")
    print(f"rows: {len(rows)} -> {len(updated)}")
    print("status: " + ", ".join(f"{status}={counts[status]}" for status in ALLOWED))
    dups = duplicate_report(updated)
    print(f"dups_after: {len(dups)}")
    for line in dups:
        print(f"  {line}")
    if dry:
        return 0
    write_csv(root / CSV_REL[0], updated)
    copy_paths(root)
    regenerate_view(root)
    return check(root)


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
        if current_status in {"skipped", "failed"}:
            return {"action": "reject", "reason": "do_not_reapply", "key": key, "status": current_status}
        return {"action": "update", "index": index, "status": "submitted", "key": key}
    if operation == "audit_missing":
        if current_status == "skipped":
            return {"action": "reject", "reason": "do_not_reapply", "key": key, "status": current_status}
        return {"action": "update", "index": index, "status": "needs_you", "blocker": "no_confirm", "key": key}
    if mapped["status"] == "submitted":
        return {"action": "reject", "reason": "auditor_sets_submitted", "key": key, "status": current_status}
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
    language_same = dedupe_key(
        {"url": "https://saypien.jobs.personio.com/job/2443678?language=en"}
    ) == dedupe_key({"url": "https://Saypien.jobs.personio.com/job/2443678/"})
    merged, merge_notes = merge_duplicate_keys(
        [
            {"company": "Primefold", "role": "SE", "url": "https://saypien.jobs.personio.com/job/2443678", "status": "skipped", "notes": "superseded by language URL", "blocker": "superseded_language_en", "date_applied": "", "salary_or_rate": "", "fit_score": ""},
            {"company": "Primefold", "role": "SE", "url": "https://saypien.jobs.personio.com/job/2443678?language=en", "status": "needs_you", "notes": "submit disabled", "blocker": "captcha_or_submit_gate", "date_applied": "", "salary_or_rate": "", "fit_score": "70"},
        ]
    )
    merge_ok = len(merged) == 1 and merged[0]["status"] == "needs_you" and "submit disabled" in merged[0]["notes"] and "superseded" in merged[0]["notes"]
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
        plan_change(rows, rows[1], "audit_confirm"),
        plan_change(rows, {**rows[1], "status": "submitted"}, "update"),
    ]
    expected_actions = ["reject", "insert", "insert", "reject", "update", "update", "update", "reject"]
    ok = (
        same
        and language_same
        and merge_ok
        and cr == cr2
        and not gaps
        and [item["action"] for item in plans] == expected_actions
        and classify_blocker({"blocker": "Greenhouse reCAPTCHA", "notes": ""}) == "captcha"
        and classify_blocker({"blocker": "Teamtailor Connect login", "notes": ""}) == "login"
    )
    mapped = map_status({"status": "confirmed"}) == "submitted"
    unknown = map_status({"status": "mystery", "blocker": "", "notes": ""}) == "needs_you"
    print(f"self_test: {'ok' if ok and mapped and unknown else 'failed'}")
    if not (ok and mapped and unknown):
        print("gaps", gaps)
        print("plans", plans)
        print("keys", same, language_same, merge_ok, cr == cr2, mapped, unknown, merge_notes)
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
    if command == "streamline":
        return streamline(dry="--dry-run" in argv)
    print(
        "usage: sync_tracker.py [check|regenerate-view|copy-paths|self-test|streamline]",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
