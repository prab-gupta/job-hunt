#!/usr/bin/env python3
"""Turn a verified list of roles into a formatted .xlsx shortlist.

Usage:
    python3 scripts/build_shortlist.py --in roles.json --out "shortlist.xlsx"

Why this exists: every job sweep otherwise reinvents the same openpyxl formatting, and
inconsistent columns make two shortlists impossible to compare week to week. Write the
roles as JSON, let this handle the spreadsheet.

Input JSON:
{
  "search_label": "AI + automation, remote-eligible from Italy - 5 Aug 2026",
  "candidate": "Prabhavit Gupta",
  "sweep_notes": {
      "raw_candidates": 62, "after_gates": 28, "verified_live": 19,
      "sources_searched": ["Ashby via allowed_domains", "euremotejobs Europe region"],
      "queries": ["AI automation engineer remote Europe"],
      "dropped_examples": ["Acme AI Engineer - US-only, no contractors"]
  },
  "roles": [{
      "title": "AI Solutions Engineer", "company": "Camunda", "url": "https://...",
      "fit": 87, "track": "A - AI/Automation", "basis": "Employee",
      "location": "Remote - EMEA", "eligibility": "Tier 1",
      "comp": "EUR 65,000-80,000", "posted": "2026-07-29 (7d)",
      "why": "...", "watch_outs": "...", "source": "Ashby search",
      "verified": "fetched 2026-08-05 - live"
  }]
}

Only title, company and url are required. Everything else degrades to "-".
"""

import argparse
import json
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

COLUMNS = [
    ("fit", "Fit", 6),
    ("title", "Role", 38),
    ("company", "Company", 20),
    ("track", "Track", 16),
    ("basis", "Basis", 11),
    ("location", "Location / remote", 24),
    ("eligibility", "Eligibility", 13),
    ("comp", "Comp / rate", 20),
    ("posted", "Posted", 16),
    ("why", "Why it fits", 52),
    ("watch_outs", "Watch-outs", 34),
    ("url", "Link", 14),
    ("source", "Found via", 18),
    ("verified", "Verified", 22),
]

WRAPPED = {"title", "why", "watch_outs", "location", "comp", "verified"}

HEADER_FILL = PatternFill("solid", fgColor="1F3864")
HEADER_FONT = Font(bold=True, color="FFFFFF", size=11)
TITLE_FONT = Font(bold=True, size=14, color="1F3864")
LINK_FONT = Font(color="0563C1", underline="single")
THIN = Side(style="thin", color="D9D9D9")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

TIER_FILLS = {
    "1": PatternFill("solid", fgColor="E2EFDA"),  # workable from Italy today
    "2": PatternFill("solid", fgColor="DDEBF7"),  # non-EU Europe, remote
    "3": PatternFill("solid", fgColor="FFF2CC"),  # relocation / sponsorship
}


def tier_key(value):
    """Pull a tier digit out of free text like 'Tier 1 - workable from Italy'."""
    for ch in str(value):
        if ch in "123":
            return ch
    return None


def clean_roles(roles):
    """Drop unusable rows, dedupe, clamp fit, sort best-first."""
    seen, out, problems = set(), [], []
    for i, r in enumerate(roles):
        missing = [f for f in ("title", "company", "url") if not str(r.get(f, "")).strip()]
        if missing:
            problems.append(f"row {i + 1}: missing {', '.join(missing)} - skipped")
            continue
        key = (r["company"].strip().lower(), r["title"].strip().lower())
        if key in seen:
            problems.append(f"duplicate dropped: {r['title']} @ {r['company']}")
            continue
        seen.add(key)
        try:
            r["fit"] = max(0, min(100, int(round(float(r.get("fit", 0))))))
        except (TypeError, ValueError):
            r["fit"] = 0
            problems.append(f"{r['title']} @ {r['company']}: unreadable fit score, set to 0")
        if not str(r.get("url", "")).startswith(("http://", "https://")):
            problems.append(f"{r['title']} @ {r['company']}: link is not a URL - check it")
        out.append(r)
    out.sort(key=lambda r: (-r["fit"], r["company"].lower()))
    return out, problems


def estimate_height(role):
    """Rough row height so wrapped text isn't clipped."""
    lines = 1
    for field, width in (("why", 52), ("watch_outs", 34), ("title", 38)):
        text = str(role.get(field, ""))
        lines = max(lines, -(-len(text) // max(width - 4, 10)))
    return min(120, max(30, lines * 14))


def write_shortlist(ws, roles, label):
    ws.cell(row=1, column=1, value=label).font = TITLE_FONT
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(COLUMNS))
    ws.row_dimensions[1].height = 24

    for c, (_, header, width) in enumerate(COLUMNS, start=1):
        cell = ws.cell(row=2, column=c, value=header)
        cell.fill, cell.font, cell.border = HEADER_FILL, HEADER_FONT, BORDER
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(c)].width = width
    ws.row_dimensions[2].height = 28

    for r, role in enumerate(roles, start=3):
        fill = TIER_FILLS.get(tier_key(role.get("eligibility", "")))
        for c, (field, _, _) in enumerate(COLUMNS, start=1):
            value = role.get(field, "")
            cell = ws.cell(row=r, column=c)
            if field == "url":
                cell.value = "Open posting"
                cell.hyperlink = str(value)
                cell.font = LINK_FONT
            elif field == "fit":
                cell.value = role["fit"]
                cell.font = Font(bold=True)
            else:
                cell.value = str(value) if str(value).strip() else "-"
            cell.border = BORDER
            cell.alignment = Alignment(
                vertical="top",
                wrap_text=field in WRAPPED,
                horizontal="center" if field in {"fit", "eligibility", "basis"} else "left",
            )
            if fill and field in {"eligibility", "basis"}:
                cell.fill = fill
        ws.row_dimensions[r].height = estimate_height(role)

    last = len(roles) + 2
    if roles:
        ws.auto_filter.ref = f"A2:{get_column_letter(len(COLUMNS))}{last}"
        ws.conditional_formatting.add(
            f"A3:A{last}",
            ColorScaleRule(
                start_type="num", start_value=40, start_color="F8696B",
                mid_type="num", mid_value=65, mid_color="FFEB84",
                end_type="num", end_value=90, end_color="63BE7B",
            ),
        )
    ws.freeze_panes = "C3"


def write_notes(ws, data, roles, problems):
    notes = data.get("sweep_notes", {}) or {}
    ws.column_dimensions["A"].width = 26
    ws.column_dimensions["B"].width = 96
    row = 1

    def line(k, v, bold_key=True):
        nonlocal row
        a = ws.cell(row=row, column=1, value=k)
        if bold_key:
            a.font = Font(bold=True)
        a.alignment = Alignment(vertical="top")
        b = ws.cell(row=row, column=2, value=v)
        b.alignment = Alignment(vertical="top", wrap_text=True)
        row += 1

    ws.cell(row=row, column=1, value="How this shortlist was built").font = TITLE_FONT
    row += 2

    line("Search", data.get("search_label", "-"))
    line("Candidate", data.get("candidate", "-"))
    line("Roles in sheet", len(roles))
    for key, human in (
        ("raw_candidates", "Raw candidates seen"),
        ("after_gates", "Survived the filters"),
        ("verified_live", "Verified live before listing"),
    ):
        if notes.get(key) is not None:
            line(human, notes[key])
    row += 1

    tiers = {}
    for r in roles:
        tiers[str(r.get("eligibility", "-"))] = tiers.get(str(r.get("eligibility", "-")), 0) + 1
    line("Eligibility mix", "; ".join(f"{k}: {v}" for k, v in sorted(tiers.items())) or "-")
    bases = {}
    for r in roles:
        bases[str(r.get("basis", "-"))] = bases.get(str(r.get("basis", "-")), 0) + 1
    line("Work basis mix", "; ".join(f"{k}: {v}" for k, v in sorted(bases.items())) or "-")
    row += 1

    for key, human in (
        ("sources_searched", "Sources swept"),
        ("queries", "Queries run"),
        ("dropped_examples", "Notable drops"),
    ):
        items = notes.get(key) or []
        if items:
            line(human, "")
            row -= 1
            for item in items:
                ws.cell(row=row, column=2, value=f"- {item}").alignment = Alignment(
                    vertical="top", wrap_text=True
                )
                row += 1
            row += 1

    line("Scoring", "Fit = role match 30 + eligibility & work basis 25 + stack overlap 20 "
                    "+ seniority realism 15 + signal quality 10. 80+ apply now; 65-79 solid; "
                    "50-64 worth a look.")
    line("Colour key", "Green = workable from Italy today. Blue = non-EU Europe, remote. "
                       "Amber = needs relocation or sponsorship.")
    if problems:
        row += 1
        line("Data notes", "")
        row -= 1
        for p in problems:
            ws.cell(row=row, column=2, value=f"- {p}").alignment = Alignment(wrap_text=True)
            row += 1


NEAR_MISS_COLS = [
    ("company", "Company", 22),
    ("role", "Role", 40),
    ("where", "Where", 26),
    ("why_not", "Why it isn't a row", 46),
    ("action", "Worth doing anyway?", 42),
]


def write_near_misses(ws, items):
    """Roles that failed a gate but tell him something true about the market.

    These are worth keeping visible: a role he can't get today still shows that his
    profile is in demand, and an unverifiable posting is a lead he can chase by hand.
    """
    ws.cell(row=1, column=1, value="Near misses and unresolved leads").font = TITLE_FONT
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(NEAR_MISS_COLS))
    ws.row_dimensions[1].height = 24

    for c, (_, header, width) in enumerate(NEAR_MISS_COLS, start=1):
        cell = ws.cell(row=2, column=c, value=header)
        cell.fill, cell.font, cell.border = HEADER_FILL, HEADER_FONT, BORDER
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(c)].width = width
    ws.row_dimensions[2].height = 28

    for r, item in enumerate(items, start=3):
        for c, (field, _, _) in enumerate(NEAR_MISS_COLS, start=1):
            value = str(item.get(field, "") or "-")
            cell = ws.cell(row=r, column=c)
            if field == "role" and item.get("url"):
                cell.value = value
                cell.hyperlink = str(item["url"])
                cell.font = LINK_FONT
            else:
                cell.value = value
            cell.border = BORDER
            cell.alignment = Alignment(vertical="top", wrap_text=True)
        ws.row_dimensions[r].height = max(
            30, min(110, 14 * max(1, -(-len(str(item.get("why_not", ""))) // 42)))
        )
    if items:
        ws.auto_filter.ref = f"A2:{get_column_letter(len(NEAR_MISS_COLS))}{len(items) + 2}"
    ws.freeze_panes = "A3"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="infile", required=True, help="roles JSON")
    ap.add_argument("--out", dest="outfile", required=True, help="destination .xlsx")
    ap.add_argument("--label", help="override the sheet title")
    args = ap.parse_args()

    data = json.loads(Path(args.infile).read_text())
    roles, problems = clean_roles(data.get("roles", []))
    if not roles:
        print("No usable roles - nothing written.", file=sys.stderr)
        for p in problems:
            print("  " + p, file=sys.stderr)
        return 1

    label = args.label or data.get("search_label") or "Role shortlist"
    wb = Workbook()
    write_shortlist(wb.active, roles, label)
    wb.active.title = "Shortlist"
    near = data.get("near_misses") or []
    if near:
        write_near_misses(wb.create_sheet("Near misses"), near)
    write_notes(wb.create_sheet("Search notes"), data, roles, problems)
    out = Path(args.outfile)
    out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out)

    print(f"Wrote {out} - {len(roles)} roles")
    for r in roles[:5]:
        print(f"  {r['fit']:>3}  {r['title']} @ {r['company']}  [{r.get('basis','-')}, "
              f"{r.get('eligibility','-')}]")
    if len(roles) > 5:
        print(f"  ... and {len(roles) - 5} more")
    for p in problems:
        print("  note: " + p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
