"""Colour every hyperlinked word link-blue and rule a matching underline beneath it."""
import pdfplumber
from pikepdf import Pdf, parse_content_stream, unparse_content_stream, ContentStreamInstruction, Operator

SRC = OUT = "Prabhavit_CV.pdf"
BLUE = (0.05, 0.28, 0.63)
LINKW = {"prabhavitg@gmail.com","linkedin","flowspace.co","urlink","ultrastrategy.com",
         "qomodo","get2germany.com","clubee","tractionboard.co","tray.ai"}

# 1. collect the linked words with their boxes
words = {}
with pdfplumber.open(SRC) as p:
    for pi, pg in enumerate(p.pages):
        hits = []
        for w in pg.extract_words():
            if w["text"].strip(" ,.;:()[]").lower() in LINKW:
                hits.append(dict(x0=w["x0"], x1=w["x1"],
                                 ybase=pg.height - w["bottom"], text=w["text"]))
        words[pi] = hits

pdf = Pdf.open(SRC)
coloured = underlined = 0
for pi, page in enumerate(pdf.pages):
    hits = words.get(pi, [])
    if not hits:
        continue
    ops = parse_content_stream(page)
    out = []
    for i, inst in enumerate(ops):
        op = str(inst.operator)
        if op == "Tm":
            x, y = float(inst.operands[4]), float(inst.operands[5])
            match = next((h for h in hits if abs(h["x0"] - x) < 0.7 and abs(h["ybase"] - y) < 4.5), None)
            if match:
                out.append(inst)
                out.append(ContentStreamInstruction(list(BLUE), Operator("rg")))
                coloured += 1
                continue
        out.append(inst)
        if op in ("TJ", "Tj") and out and coloured:
            # reset to black straight after a text run we just coloured
            prev_col = any(str(o.operator) == "rg" for o in out[-3:-1])
            if prev_col:
                out.append(ContentStreamInstruction([0], Operator("g")))
    # 2. underlines, appended after all page content
    ul = ["q", f"{BLUE[0]} {BLUE[1]} {BLUE[2]} RG", "0.6 w"]
    for h in hits:
        yy = h["ybase"] - 1.2
        ul.append(f"{h['x0']:.2f} {yy:.2f} m {h['x1']:.2f} {yy:.2f} l S")
        underlined += 1
    ul.append("Q")
    parts = []
    for inst in out:
        b = unparse_content_stream([inst])
        parts.append((b.decode() if isinstance(b, bytes) else b).strip())
    page.Contents = pdf.make_stream(("\n".join(parts) + "\n" + "\n".join(ul) + "\n").encode())

pdf.save("cv_styled.pdf")
print(f"coloured {coloured} runs, drew {underlined} underlines")
