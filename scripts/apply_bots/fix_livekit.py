with open("cv/main_LiveKit_FDE.tex", "r") as f:
    lines = f.readlines()
with open("cv/main_LiveKit_FDE.tex", "w") as f:
    for line in lines:
        if line.startswith(r"\item{\cventry"):
            line = line.replace(r"\item{\cventry", r"\cventry")
        elif line.strip() == "}}":
            line = "}\n"
        f.write(line)
