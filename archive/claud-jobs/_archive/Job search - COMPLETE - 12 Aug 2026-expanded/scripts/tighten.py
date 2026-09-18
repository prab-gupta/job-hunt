"""Normalise the oversized location-line -> first-bullet gap (36pt) down to the
   CV's own inter-bullet spacing (22.5pt), cascading the shift down each page.
   Only touches gaps that follow the company/location pattern, never section breaks."""
from pikepdf import Pdf, parse_content_stream, unparse_content_stream, ContentStreamInstruction, Operator

SRC, OUT = "Prabhavit_CV.pdf", "Prabhavit_CV_tight.pdf"
TARGET = 22.5
FOOTER_MAX = 45.0

pdf = Pdf.open(SRC)
total_saved = 0
for pi, page in enumerate(pdf.pages):
    ops = parse_content_stream(page)
    ys = sorted({round(float(o.operands[5]), 2) for o in ops if str(o.operator) == "Tm"}, reverse=True)
    body = [y for y in ys if y > FOOTER_MAX]
    shift_from = []                     # (y_below_which_to_shift, delta)
    for i in range(1, len(body) - 1):
        gap_prev = body[i-1] - body[i]
        gap_here = body[i] - body[i+1]
        if 34.0 <= gap_here <= 38.0 and 12.5 <= gap_prev <= 14.5:
            shift_from.append((body[i+1], gap_here - TARGET))
    if not shift_from:
        continue
    def newy(y):
        if y <= FOOTER_MAX:
            return y
        d = sum(delta for thresh, delta in shift_from if y <= thresh + 0.01)
        return y + d
    out = []
    for inst in ops:
        op = str(inst.operator)
        if op == "Tm":
            o2 = [float(x) for x in inst.operands]
            o2[5] = newy(round(o2[5], 2))
            inst = ContentStreamInstruction(o2, Operator("Tm"))
        elif op == "cm":
            o2 = [float(x) for x in inst.operands]
            if len(o2) == 6 and o2[5] > FOOTER_MAX:
                o2[5] = newy(round(o2[5], 2))
                inst = ContentStreamInstruction(o2, Operator("cm"))
        out.append(inst)
    parts = []
    for inst in out:
        b = unparse_content_stream([inst])
        parts.append((b.decode() if isinstance(b, bytes) else b).strip())
    page.Contents = pdf.make_stream(("\n".join(parts) + "\n").encode())
    saved = sum(d for _, d in shift_from)
    total_saved += saved
    print(f"page {pi+1}: normalised {len(shift_from)} gaps, reclaimed {saved:.1f}pt")
pdf.save(OUT)
print(f"total reclaimed: {total_saved:.1f}pt")
