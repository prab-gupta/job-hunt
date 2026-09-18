"""Anchor, colour and underline the CV's work links. Matching is by exact token AND
   x position, so a company name mentioned in a bullet can never be mistaken for its header."""
import pdfplumber
from pikepdf import Pdf, parse_content_stream, unparse_content_stream, ContentStreamInstruction, Operator
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
from pypdf.generic import ArrayObject, NameObject

BASE, OUT = "base.pdf", "Prabhavit_CV.pdf"
BLUE = (0.05, 0.28, 0.63)

# (page index, x0, exact token) -> url.  Headers sit at x0 70.94; the Tray certs at 67.94.
ANCHORS = [
    (0, 200.85, "prabhavitg@gmail.com", "mailto:prabhavitg@gmail.com"),
    (0, 338.56, "Linkedin",             "https://www.linkedin.com/in/prabhavit/"),
    (0,  70.94, "FlowSpace.co",         "https://www.flowspace.co"),
    (1,  70.94, "Urlink",               "https://smarturlink.com/"),
    (1,  70.94, "UltraStrategy.com",    "http://ultrastrategy.com"),
    (1,  70.94, "Qomodo",               "https://www.qomodo.me/"),
    (1,  70.94, "Get2Germany.com",      "https://www.get2germany.com/"),
    (1,  70.94, "Clubee.com",           "https://www.clubee.com/"),
    (1,  70.94, "Tractionboard.co",     "https://tractionboard.co/"),
    (2,  67.94, "Tray.AI", "https://523efce9-b15b-458d-9fec-2731553dc1f5.trayapp.io?credential_id=6dd6b1dc-c648-4c39-8181-682cec6ae209"),
    (2,  67.94, "Tray.AI", "https://523efce9-b15b-458d-9fec-2731553dc1f5.trayapp.io/?credential_id=3fed4800-e85a-4257-8b41-8ded1b27d4a1"),
]

matched, used = [], set()
with pdfplumber.open(BASE) as p:
    for pi, x0, token, url in ANCHORS:
        pg = p.pages[pi]
        for w in pg.extract_words():
            if w["text"] != token or abs(w["x0"] - x0) > 0.6:
                continue
            key = (pi, round(w["x0"], 1), round(w["top"], 1))
            if key in used:
                continue
            used.add(key)
            matched.append(dict(page=pi, x0=w["x0"], x1=w["x1"],
                                ybase=pg.height - w["bottom"], text=token, url=url))
            break
print(f"anchored {len(matched)} of {len(ANCHORS)}")
for m in matched:
    print(f"   p{m['page']+1} {m['text']:<22} -> {m['url'][:52]}")

# ---- colour the text blue and rule an underline ----
pdf = Pdf.open(BASE)
for pi, page in enumerate(pdf.pages):
    hits = [m for m in matched if m["page"] == pi]
    if not hits:
        continue
    ops = parse_content_stream(page)
    out, pending = [], False
    for inst in ops:
        op = str(inst.operator)
        if op == "Tm":
            x, y = float(inst.operands[4]), float(inst.operands[5])
            hit = next((h for h in hits if abs(h["x0"] - x) < 0.7 and abs(h["ybase"] - y) < 4.5), None)
            out.append(inst)
            if hit:
                out.append(ContentStreamInstruction(list(BLUE), Operator("rg")))
                pending = True
            continue
        out.append(inst)
        if pending and op in ("TJ", "Tj"):
            out.append(ContentStreamInstruction([0], Operator("g")))
            pending = False
    ul = ["q", f"{BLUE[0]} {BLUE[1]} {BLUE[2]} RG", "0.6 w"]
    for h in hits:
        yy = h["ybase"] - 1.2
        ul.append(f"{h['x0']:.2f} {yy:.2f} m {h['x1']:.2f} {yy:.2f} l S")
    ul.append("Q")
    parts = []
    for inst in out:
        b = unparse_content_stream([inst])
        parts.append((b.decode() if isinstance(b, bytes) else b).strip())
    page.Contents = pdf.make_stream(("\n".join(parts) + "\n" + "\n".join(ul) + "\n").encode())
pdf.save("styled.pdf")

# ---- clickable annotations on exactly the same boxes ----
r = PdfReader("styled.pdf"); w = PdfWriter()
for pg in r.pages:
    pg[NameObject("/Annots")] = ArrayObject()
    w.add_page(pg)
for m in matched:
    w.add_annotation(page_number=m["page"],
                     annotation=Link(rect=(m["x0"]-1, m["ybase"]-2.5, m["x1"]+1, m["ybase"]+9), url=m["url"]))
w.write(OUT)
print("done")
