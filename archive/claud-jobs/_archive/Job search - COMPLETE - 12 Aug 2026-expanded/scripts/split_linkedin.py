"""Move every LinkedIn-sourced row out of 'New leads' onto its own tab.
Run with the workbook at /home/claude/sheet/wb.xlsx.
Identification is exact: a row belongs to LinkedIn if its Apply link is a
linkedin.com/jobs/view/ URL. No guessing, no keyword matching."""
import re
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

TITLE = Font(name="Arial", size=15, bold=True, color="1F3864")
NOTE  = Font(name="Arial", size=9, italic=True, color="595959")
HEADF = Font(name="Arial", size=10, bold=True, color="FFFFFF")
BODY  = Font(name="Arial", size=10)
BOLD  = Font(name="Arial", size=10, bold=True)
LINK  = Font(name="Arial", size=10, color="0563C1", underline="single")
HEADFILL = PatternFill("solid", fgColor="1F3864")
T1 = PatternFill("solid", fgColor="E2EFDA")
T2 = PatternFill("solid", fgColor="FFF2CC")
T3 = PatternFill("solid", fgColor="FCE4E4")
thin = Side(style="thin", color="BFBFBF")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")
CTR  = Alignment(horizontal="center", vertical="top", wrap_text=True)

def tf(t):
    t = str(t)
    return T1 if t.startswith("1") else (T2 if t.startswith("2") else T3)

wb = openpyxl.load_workbook("/home/claude/sheet/wb.xlsx")
src = wb["New leads"]

COLS = ["Fit /100","Role","Company","Where / eligibility","Tier","Basis","Language requirement","Pay",
        "Posted","Why it fits him","Watch-outs (the honest gaps)","Apply link","Verification"]
W = [8, 46, 26, 46, 7, 13, 34, 34, 22, 74, 74, 50, 60]

keep, moved = [], []
for row in src.iter_rows(min_row=5, max_col=13):
    if row[2].value is None:
        continue
    vals = [c.value for c in row]
    url = str(vals[11] or "")
    (moved if "linkedin.com/jobs/view/" in url else keep).append(vals)

keep.sort(key=lambda x: -(x[0] or 0))
moved.sort(key=lambda x: -(x[0] or 0))

def paint(ws, rows, start):
    r = start
    for row in rows:
        for i, v in enumerate(row, start=1):
            c = ws.cell(row=r, column=i, value=v)
            c.font = BODY; c.alignment = WRAP; c.border = BOX
            if i == 1: c.font = BOLD; c.alignment = CTR; c.fill = tf(row[4])
            if i == 5: c.alignment = CTR; c.fill = tf(row[4])
            if i == 12 and isinstance(v, str) and v.startswith("http"):
                c.font = LINK; c.hyperlink = v
        r += 1
    return r

# wipe and rewrite New leads without the LinkedIn rows
for r in range(5, src.max_row + 2):
    for c in range(1, 14):
        cell = src.cell(row=r, column=c)
        cell.value = None; cell.fill = PatternFill(fill_type=None); cell.border = Border()
END_KEEP = paint(src, keep, 5)
src.auto_filter.ref = f"A4:M{END_KEEP-1}"

# new tab, placed straight after New leads
pos = wb.sheetnames.index("New leads") + 1
ws = wb.create_sheet("LinkedIn finds", pos)
ws.sheet_view.showGridLines = False
ws["A1"] = "LinkedIn finds"; ws["A1"].font = TITLE
ws["A2"] = ("Harvested from LinkedIn job search in a signed-in browser on 6 August 2026. Every row was confirmed "
            "present and dated on LinkedIn, but the posting bodies were NOT opened one by one, so eligibility, "
            "language and pay on this tab are unverified and the tier is inferred from the LinkedIn location field "
            "alone. Treat this tab as a queue to open, not as vetted rows. LinkedIn holds far more than this: the "
            "n8n search alone returned 936 EU roles posted in one week.")
ws["A2"].font = NOTE
r = 4
for i, (c, w) in enumerate(zip(COLS, W), start=1):
    cell = ws.cell(row=r, column=i, value=c)
    cell.font = HEADF; cell.fill = HEADFILL; cell.alignment = CTR; cell.border = BOX
    ws.column_dimensions[get_column_letter(i)].width = w
ws.row_dimensions[r].height = 30
ws.freeze_panes = ws.cell(row=5, column=1)
END_LI = paint(ws, moved, 5)
ws.auto_filter.ref = f"A4:M{END_LI-1}"

# repoint every Summary formula that referenced New leads, and add LinkedIn lines
s = wb["Summary"]
for row in s.iter_rows(min_row=5, max_row=26, max_col=2):
    f = row[1].value
    if isinstance(f, str) and "'New leads'" in f:
        row[1].value = re.sub(r"(New leads'!\w)\d+:(\w)\d+", rf"\g<1>5:\g<2>{END_KEEP-1}", f)

target = None
for i, row in enumerate(s.iter_rows(min_row=5, max_row=26, max_col=1), start=5):
    if row[0].value and str(row[0].value).startswith("  FlowSpace-like platform leads"):
        target = i
if target:
    s.insert_rows(target + 1, 2)
    adds = [("  LinkedIn finds, unopened queue", f"=COUNTA('LinkedIn finds'!C5:C{END_LI-1})", "'LinkedIn finds' tab"),
            ("    of those, tier 1", f"=COUNTIF('LinkedIn finds'!E5:E{END_LI-1},\"1*\")", "'LinkedIn finds' tab, filter Tier = 1")]
    for off, (label, formula, where) in enumerate(adds):
        rr = target + 1 + off
        c1 = s.cell(row=rr, column=1, value=label); c1.font = BODY; c1.alignment = WRAP; c1.border = BOX
        c2 = s.cell(row=rr, column=2, value=formula); c2.font = BOLD; c2.alignment = CTR; c2.border = BOX
        c3 = s.cell(row=rr, column=3, value=where); c3.font = BODY; c3.alignment = WRAP; c3.border = BOX
    # total-leads line must now count three lead tabs
    for row in s.iter_rows(min_row=5, max_row=26, max_col=2):
        if row[0].value == "Total leads on this workbook":
            row[1].value = (f"=COUNTA('New leads'!C5:C{END_KEEP-1})"
                            f"+COUNTA('LinkedIn finds'!C5:C{END_LI-1})"
                            f"+COUNTA('FlowSpace-like platforms'!C5:C{END_LI-1})")

wb.save("/home/claude/sheet/Prabhavit_job_leads_2026-08-06.xlsx")
print(f"moved to LinkedIn finds: {END_LI-5} | remaining on New leads: {END_KEEP-5}")
