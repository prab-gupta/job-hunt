import glob

for filepath in glob.glob("cover_letters/cover_*_*.tex"):
    with open(filepath, "r") as f:
        lines = f.readlines()
        
    out = []
    in_namesection = False
    name = ""
    contact = ""
    
    # We'll just replace the entire \namesection block with a static header
    for line in lines:
        if "\\documentclass[]{cover}" in line or "\\documentclass{cover}" in line:
            out.append("\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{parskip}\n")
        elif "namesection" in line:
            # Skip the namesection and just put a hardcoded header
            out.append("{\\Large \\textbf{Prabhavit Gupta}} \\\\[1ex]\n")
            out.append("\\href{mailto:prabhavitg@gmail.com}{prabhavitg@gmail.com} | +39 351 610 7807 | \\urlstyle{same}\\href{https://www.linkedin.com/in/prabhavit/}{LinkedIn} \\\\[2ex]\n")
            out.append("\\noindent\\rule{\\textwidth}{0.4pt} \\\\[2ex]\n")
            in_namesection = True
        elif in_namesection and "}" in line:
            in_namesection = False # End of namesection
        elif in_namesection:
            continue
        elif "\\currentdate{" in line:
            out.append(line.replace("\\currentdate{", "").replace("}", " \\\\[2ex]\n"))
        elif "\\lettercontent{" in line:
            out.append(line.replace("\\lettercontent{", "").replace("}", "\n"))
        elif "\\closing{" in line:
            out.append(line.replace("\\closing{", "").replace("}", " \\\\[3ex]\n"))
        elif "\\signature{" in line:
            out.append(line.replace("\\signature{", "").replace("}", "\n"))
        elif "fontspec" in line and "Raleway" in line:
            continue
        elif "\\end{itemize}\\par}" in line:
            out.append("\\end{itemize}\n")
        else:
            out.append(line)
            
    with open(filepath, "w") as f:
        f.writelines(out)

