with open(".claude/skills/job-application-assistant/05-cv-templates.md", "r") as f:
    content = f.read()

import re

new_rules = r"""## Template: Prabhavit_CV Format (Strict 1:1)

**CRITICAL INSTRUCTION**: The user strictly demands 1:1 formatting with their original 3-page `Prabhavit_CV` template. DO NOT use `moderncv`. You MUST use the `article` class and exactly match the formatting rules below, including the blue text, the horizontal lines under sections, and the photo layout.

**Output file:** `cv/main_<company>_<role>.tex`
**Compile with:** `tectonic main_<company>_<role>.tex` (on this host)

### The Pre-approved Preamble & Header Template

You MUST start every generated CV with EXACTLY this code:

```latex
\documentclass[a4paper,10pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\usepackage{lmodern}
\usepackage[top=1.6cm,bottom=1.8cm,left=1.9cm,right=1.9cm]{geometry}
\usepackage{titlesec,enumitem,xcolor,graphicx,lastpage,fancyhdr}
\usepackage{fontawesome5}
\usepackage[hidelinks]{hyperref}
\hypersetup{colorlinks=true,urlcolor=blue!70!black,linkcolor=blue!70!black}
\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\small\color{gray}Page \thepage\ of \pageref{LastPage}}
\setlength{\parindent}{0pt}
\titleformat{\section}{\large\bfseries\color{blue!70!black}}{}{0em}{}[\vspace{-0.7em}\rule{\textwidth}{0.5pt}]
\titlespacing{\section}{0pt}{9pt}{5pt}
\setlist[itemize]{leftmargin=1.1em,itemsep=2pt,topsep=2pt,parsep=0pt}
\newcommand{\role}[4]{\vspace{3pt}\noindent\hspace{0.6em}\parbox[t]{0.38\textwidth}{\raggedright\textbf{#1}}\hfill\parbox[t]{0.58\textwidth}{\raggedleft\textit{#2}}\\{\textit{#3}\hfill\textit{#4}}\vspace{1pt}}

\begin{document}
\noindent
\begin{minipage}[t]{0.78\textwidth}
\vspace{0pt}
{\huge\bfseries Prabhavit Gupta}\\[8pt]
{\small \faPhone\ +39-351-610-7807 \quad \faEnvelope\ \href{mailto:prabhavitg@gmail.com}{prabhavitg@gmail.com} \quad \faLinkedin\ \href{https://www.linkedin.com/in/prabhavit/}{Linkedin} \quad \faMapMarker*\ Venice, Italy}
\end{minipage}\hfill
\begin{minipage}[t]{0.18\textwidth}
\vspace{0pt}\raggedleft\includegraphics[width=2.3cm,height=2.3cm,keepaspectratio]{photo.jpg}
\end{minipage}

\section{Career Summary}
\begin{itemize}
\item [INSERT TAILORED PUNCHY SUMMARY BULLETS HERE, MAX 3 LINES]
\end{itemize}
```

### Critical Content & Tailoring Rules (DO NOT IGNORE)

1. **Master Reference Data:**
   - **CRITICAL:** You MUST read `data/cvs/Prabhavit_CV_EN.tex.bak-0916` to source the user's actual experience and projects.
2. **FlowSpace.co Experience:**
   - You MUST preserve the length and core product/technical responsibilities of the FlowSpace experience from the master file `Prabhavit_CV_EN.tex.bak-0916`.
   - Do NOT aggressively cut the "Product Responsibilities" or "Technical Responsibilities" sub-bullets. The user wants the Flowspace section to remain highly detailed as it is their core experience.
"""

content = re.sub(r'## Template: Prabhavit_CV Format \(Strict 1:1\).*?(?=\n\n## Template)', new_rules, content, flags=re.DOTALL)
# if the regex fails because there is no other ## Template, replace to end of file
if "## Template: Prabhavit_CV Format" in content and "Master Reference Data:" not in content:
    content = re.sub(r'## Template: Prabhavit_CV Format \(Strict 1:1\).*', new_rules, content, flags=re.DOTALL)

with open(".claude/skills/job-application-assistant/05-cv-templates.md", "w") as f:
    f.write(content)
