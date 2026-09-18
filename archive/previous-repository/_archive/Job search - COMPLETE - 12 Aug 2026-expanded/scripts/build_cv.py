"""One clean pass over the pristine CV:
   1. delete the AliCreates entry from the text layer on page 3
   2. shift everything below it up so the gap closes, footer stays put
   3. add clickable work links, NO drawn underlines (the CV already rules its company names)
   4. drop annotations orphaned by the deletion, and duplicates
"""
import pdfplumber
from pikepdf import Pdf, parse_content_stream, unparse_content_stream
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
from pypdf.generic import ArrayObject, NameObject

SRC, MID, OUT = "cv_original.pdf", "cv_step1.pdf", "Prabhavit_CV.pdf"
H = 841.89
BAND_LO, BAND_HI = 512.0, 650.0     # the AliCreates entry
FOOTER_MAX = 100.0                  # anything below this is the page footer, never moves
GAP_AFTER = 20.0                    # spacing the CV uses between a bullet and the next heading

# ---------- 1 + 2 : delete, then close the gap ----------
pdf = Pdf.open(SRC)
page = pdf.pages[2]
ops = parse_content_stream(page)

last_kept_y = min(float(o.operands[5]) for o in ops
                  if str(o.operator) == "Tm" and float(o.operands[5]) >= BAND_HI)
first_below_y = max(float(o.operands[5]) for o in ops
                    if str(o.operator) == "Tm" and FOOTER_MAX < float(o.operands[5]) <= BAND_LO)
SHIFT = (last_kept_y - GAP_AFTER) - first_below_y
print(f"last kept y={last_kept_y}  first below y={first_below_y}  shift=+{SHIFT:.1f}pt")

out, suppress, dropped = [], False, 0
i = 0
while i < len(ops):
    inst = ops[i]
    op = str(inst.operator)
    if op == "Tm":
        y = float(inst.operands[5])
        if BAND_LO < y < BAND_HI:
            suppress = True; dropped += 1; i += 1; continue
        suppress = False
        if FOOTER_MAX < y <= BAND_LO:                      # move it up
            o2 = list(inst.operands); o2[5] = float(y) + SHIFT
            from pikepdf import ContentStreamInstruction, Operator
            inst = ContentStreamInstruction(o2, Operator("Tm"))
    elif op == "ET":
        suppress = False
    elif op in ("TJ", "Tj", "'", '"') and suppress:
        i += 1; continue
    elif op == "cm":
        nums = [float(x) for x in inst.operands]
        if len(nums) == 6 and FOOTER_MAX < nums[5] <= BAND_LO:   # section rules ride on a cm
            from pikepdf import ContentStreamInstruction, Operator
            nums[5] += SHIFT
            inst = ContentStreamInstruction(nums, Operator("cm"))
        elif len(nums) == 6 and BAND_LO < nums[5] < BAND_HI:
            j = i
            while j < len(ops) and str(ops[j].operator) != "Q": j += 1
            i = j + 1; continue
    out.append(inst)
    i += 1

parts = []
for inst in out:
    b = unparse_content_stream([inst])
    parts.append((b.decode() if isinstance(b, bytes) else b).strip())
page.Contents = pdf.make_stream(("\n".join(parts) + "\n").encode())
pdf.save(MID)
print(f"deleted {dropped} text runs, shifted the tail up")

# ---------- 3 : links, no underlines ----------
SIMPLE = {
    "prabhavitg@gmail.com": "mailto:prabhavitg@gmail.com",
    "linkedin":          "https://www.linkedin.com/in/prabhavit/",
    "flowspace.co":      "https://www.flowspace.co",
    "urlink":            "https://smarturlink.com/",
    "ultrastrategy.com": "http://ultrastrategy.com",
    "qomodo":            "https://www.qomodo.me/",
    "get2germany.com":   "https://www.get2germany.com/",
    "clubee":            "https://www.clubee.com/",
    "tractionboard.co":  "https://tractionboard.co/",
}
TRAY = ["https://523efce9-b15b-458d-9fec-2731553dc1f5.trayapp.io?credential_id=6dd6b1dc-c648-4c39-8181-682cec6ae209",
        "https://523efce9-b15b-458d-9fec-2731553dc1f5.trayapp.io/?credential_id=3fed4800-e85a-4257-8b41-8ded1b27d4a1"]

found, tray_seen = [], 0
with pdfplumber.open(MID) as p:
    for pi, pg in enumerate(p.pages):
        for w in pg.extract_words():
            key = w["text"].strip(" ,.;:()[]").lower()
            url = SIMPLE.get(key)
            if key == "tray.ai" and tray_seen < 2:
                url = TRAY[tray_seen]; tray_seen += 1
            if url:
                found.append((pi, w["x0"], pg.height - w["bottom"], w["x1"], pg.height - w["top"], url, w["text"]))

r = PdfReader(MID); wr = PdfWriter()
for pg in r.pages: wr.add_page(pg)
for pi, x0, y0, x1, y1, url, raw in found:
    wr.add_annotation(page_number=pi, annotation=Link(rect=(x0-1, y0-2, x1+1, y1+1), url=url))
wr.write(OUT)

# ---------- 4 : drop orphaned + duplicate annotations ----------
GONE = ("vistack", "lamiadomiciliare", "gomadthinking", "alicreates")
r = PdfReader(OUT); wr = PdfWriter()
removed = 0
for pi, pg in enumerate(r.pages):
    an = pg.get("/Annots")
    if an is not None:
        an = an.get_object() if hasattr(an, "get_object") else an
    if an:
        keep, seen = [], set()
        for a in an:
            o = a.get_object()
            uri = str((o.get("/A") or {}).get("/URI") or "")
            rect = [float(x) for x in (o.get("/Rect") or [0,0,0,0])]
            k = (uri, round(rect[0]), round(rect[1]))
            if any(g in uri.lower() for g in GONE) or k in seen:
                removed += 1
            else:
                seen.add(k); keep.append(a)
        pg[NameObject("/Annots")] = ArrayObject(keep)
    wr.add_page(pg)
wr.write(OUT)
print(f"links added: {len(found)} | orphaned/duplicate annotations removed: {removed}")
