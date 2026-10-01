import glob
import re

for filepath in glob.glob("cover_letters/cover_*_*.tex"):
    with open(filepath, "r") as f:
        content = f.read()

    # If it uses namesection but article class, it's broken
    if "\\namesection" in content:
        # Replace \documentclass
        content = re.sub(r"\\documentclass.*?{article}", r"\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{parskip}", content)
        content = re.sub(r"\\documentclass.*?{cover}", r"\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{parskip}", content)
        
        # Replace \namesection{}{Name}{Contact}
        content = re.sub(r"\\namesection\{\}\{\\Huge\{(.*?)\}\}\{(.*?)\}", r"{\\Large \\textbf{\1}} \\\\[1ex]\n\2 \\\\[2ex]\n\\noindent\\rule{\\textwidth}{0.4pt} \\\\[2ex]", content, flags=re.DOTALL)
        
        # Replace \currentdate{...}
        content = re.sub(r"\\currentdate\{(.*?)\}", r"\1 \\\\[2ex]", content)
        
        # Replace \lettercontent{...}
        content = re.sub(r"\\lettercontent\{(.*?)\}", r"\1\n", content, flags=re.DOTALL)
        
        # Replace \closing{...}
        content = re.sub(r"\\closing\{(.*?)\}", r"\1 \\\\[3ex]", content)
        
        # Replace \signature{...}
        content = re.sub(r"\\signature\{(.*?)\}", r"\1", content)
        
        # Remove fonts
        content = re.sub(r"\{\\raggedright\\fontspec.*?\\selectfont\n", "", content)
        content = re.sub(r"\\end\{itemize\}\\par\}", r"\\end{itemize}", content)

        with open(filepath, "w") as f:
            f.write(content)

