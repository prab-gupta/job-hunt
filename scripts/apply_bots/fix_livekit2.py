with open("cv/main_LiveKit_FDE.tex", "r") as f:
    text = f.read()

text = text.replace("pdfpagemode=UseNone,\n}", "pdfpagemode=UseNone,\n}}")

with open("cv/main_LiveKit_FDE.tex", "w") as f:
    f.write(text)
