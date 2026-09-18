from pikepdf import Pdf, parse_content_stream, unparse_content_stream

SRC = "/home/claude/work/Prabhavit_CV.pdf"
OUT = "/home/claude/sheet/cv_noalicreates.pdf"
Y_LO, Y_HI = 512.0, 650.0          # pdf y band holding the whole AliCreates entry
TEXT_SHOW = {"TJ", "Tj", "'", '"'}

pdf = Pdf.open(SRC)
page = pdf.pages[2]
ops = parse_content_stream(page)

out, suppress = [], False
dropped, kept_lines = 0, []
i = 0
while i < len(ops):
    inst = ops[i]
    op = str(inst.operator)
    if op == "Tm":
        y = float(inst.operands[5])
        suppress = Y_LO < y < Y_HI
        if suppress:
            dropped += 1
            i += 1
            continue
    elif op == "ET":
        suppress = False
    elif op in TEXT_SHOW and suppress:
        i += 1
        continue
    elif op == "m":
        # a rule; drop it (and its l/S partners) when it sits in the band
        y = float(inst.operands[1])
        if Y_LO < y < Y_HI:
            j = i
            while j < len(ops) and str(ops[j].operator) in ("m", "l", "S", "s", "h"):
                j += 1
            i = j
            continue
    out.append(inst)
    i += 1

raw = unparse_content_stream(out)
if isinstance(raw, str):
    raw = raw.encode()
# pikepdf can emit adjacent operators with no separator (e.g. "ETQ"); rebuild with newlines
parts = []
for inst in out:
    ops_txt = " ".join(unparse_content_stream([inst]).decode() if isinstance(unparse_content_stream([inst]), bytes) else unparse_content_stream([inst]) for _ in [0])
    parts.append(ops_txt.strip())
page.Contents = pdf.make_stream(("\n".join(parts) + "\n").encode())
pdf.save(OUT)
print(f"dropped {dropped} text runs in the band")
