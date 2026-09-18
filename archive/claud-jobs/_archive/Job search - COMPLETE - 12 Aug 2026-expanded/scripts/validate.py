#!/usr/bin/env python3
"""Folder self-consistency check. Run from the folder root: python3 validate.py"""
import csv, hashlib, sys
from pathlib import Path

ROOT = Path(__file__).parent
CV = "Prabhavit_CV.pdf"
CV_SHA256 = "e18579bb9bcffee3db285bc699c354b357dd6efa8485ab0dac1544fcecceeb81"  # current CV (edited 6 Aug 2026: clickable blue links, AliCreates removed, spacing evened, icon glyphs no longer parse as words)
# previous: 150206f4f02d23785bfb7e37ac2f6eaa9283a950acad8cdc7420608384743fd0 - the CV the first 9 apps of 6 Aug and all of 5 Aug were sent with
# previous: fe1e893f24d347197f2f7934181851397d3137f4838e89f849dcbe5307b50d93 - the CV the 15 apps of 5 Aug were sent with

fails, warns = [], []

# required files
for p in ["README.md", "applications.csv", CV, "claude/application-rules.md",
          "skill/job-hunt/SKILL.md", "follow-ups.md", "form-quirks.md"]:
    if not (ROOT / p).exists():
        fails.append(f"missing file: {p}")

# CV hash — the file on disk must be the exact one recorded as sent
if (ROOT / CV).exists():
    h = hashlib.sha256((ROOT / CV).read_bytes()).hexdigest()
    if h != CV_SHA256:
        fails.append(f"CV hash mismatch: on-disk CV is NOT the one recorded as current ({h[:12]}…)")

rows = []
if (ROOT / "applications.csv").exists():
    rows = list(csv.DictReader(open(ROOT / "applications.csv")))

# every submitted row has confirmation text
for r in rows:
    if r["status"] == "submitted" and not r["confirmation_text"].strip():
        fails.append(f"submitted without confirmation: {r['company']} — {r['role']}")

# no duplicate company+role
seen = {}
for r in rows:
    k = (r["company"].lower(), r["role"].lower())
    if k in seen:
        fails.append(f"duplicate row: {r['company']} — {r['role']}")
    seen[k] = True

# every letter maps to an application; flag letters written but not attached
companies = {r["company"].lower(): r for r in rows}
for pdf in sorted((ROOT / "letters").glob("*.pdf")):
    prefix = pdf.name.split("_")[0].lower()
    match = next((r for c, r in companies.items() if c.startswith(prefix)), None)
    if match is None:
        fails.append(f"orphan letter, no matching application: {pdf.name}")
    elif match["cover_letter_attached"].startswith("no"):
        warns.append(f"letter exists but was NOT attached: {pdf.name} ({match['company']}) — follow-up owed")

print(f"applications.csv: {len(rows)} rows "
      f"({sum(r['status'] == 'submitted' for r in rows)} submitted, "
      f"{sum(r['status'] == 'blocked-needs-signin' for r in rows)} blocked)")
for w in warns: print(f"WARN  {w}")
for f_ in fails: print(f"FAIL  {f_}")
if not fails and not warns: print("all checks pass")
sys.exit(1 if fails else 0)
