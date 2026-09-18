import io
import pdfplumber
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
from pypdf.generic import ArrayObject, FloatObject, NameObject, DictionaryObject, TextStringObject, NumberObject
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color

SRC = "/home/claude/sheet/cv_noalicreates.pdf"
OUT = "/home/claude/sheet/Prabhavit_CV.pdf"

# word (lowercased, punctuation-stripped) -> URL. Order-sensitive entries handled below.
SIMPLE = {
    "prabhavitg@gmail.com": "mailto:prabhavitg@gmail.com",
    "linkedin":             "https://www.linkedin.com/in/prabhavit/",
    "flowspace.co":         "https://www.flowspace.co",
    "urlink":               "https://smarturlink.com/",
    "ultrastrategy.com":    "http://ultrastrategy.com",
    "qomodo":               "https://www.qomodo.me/",
    "get2germany.com":      "https://www.get2germany.com/",
    "clubee":               "https://www.clubee.com/",
    "tractionboard.co":     "https://tractionboard.co/",
    "alicreates.com":       "https://alicreates.com/",
}
# the two Tray certifications carry his own credential-verification URLs, in order
TRAY = [
    "https://523efce9-b15b-458d-9fec-2731553dc1f5.trayapp.io?credential_id=6dd6b1dc-c648-4c39-8181-682cec6ae209",
    "https://523efce9-b15b-458d-9fec-2731553dc1f5.trayapp.io/?credential_id=3fed4800-e85a-4257-8b41-8ded1b27d4a1",
]

found = []   # (page_index, x0, y0, x1, y1, url)
tray_seen = 0
with pdfplumber.open(SRC) as pdf:
    for pi, page in enumerate(pdf.pages):
        H = page.height
        for w in page.extract_words():
            raw = w["text"]
            key = raw.strip(" ,.;:()[]").lower()
            url = None
            if key in SIMPLE:
                url = SIMPLE[key]
            elif key == "tray.ai" and tray_seen < len(TRAY):
                url = TRAY[tray_seen]; tray_seen += 1
            elif key == "linkedin" and raw.isupper():
                url = SIMPLE["linkedin"]
            if url:
                found.append((pi, w["x0"], H - w["bottom"], w["x1"], H - w["top"], url, raw))

# collapse the duplicate LINKEDIN icon + word into one link region per page
print(f"link targets found: {len(found)}")
for f in found:
    print(f"  p{f[0]} {f[6]:<22} -> {f[5]}")

reader = PdfReader(SRC)
writer = PdfWriter()
LINKBLUE = Color(0.02, 0.29, 0.60)

for pi, page in enumerate(reader.pages):
    hits = [f for f in found if f[0] == pi]
    if hits:
        w = float(page.mediabox.width); h = float(page.mediabox.height)
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=(w, h))
        c.setStrokeColor(LINKBLUE); c.setLineWidth(0.5)
        for _, x0, y0, x1, y1, url, raw in hits:
            c.line(x0, y0 - 0.6, x1, y0 - 0.6)      # underline, so a reader can see it is a link
        c.save(); buf.seek(0)
        page.merge_page(PdfReader(buf).pages[0])
    writer.add_page(page)

for _, x0, y0, x1, y1, url, raw in found:
    ann = Link(rect=(x0 - 1, y0 - 2, x1 + 1, y1 + 1), url=url)
    writer.add_annotation(page_number=_, annotation=ann)

with open(OUT, "wb") as fh:
    writer.write(fh)
print("written:", OUT)
