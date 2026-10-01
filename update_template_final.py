import re

with open(".claude/skills/job-application-assistant/05-cv-templates.md", "r") as f:
    content = f.read()

# Replace the old template section
new_template = r"""## Template: Prabhavit_CV Format (Strict 1:1)

**CRITICAL INSTRUCTION**: The user strictly demands 1:1 formatting with their custom `Prabhavit_CV` template. DO NOT use `moderncv`. You MUST use the `article` class and exactly match the formatting rules below. 
You MUST also include a photo using a side-by-side minipage layout in the header.

**Output file:** `cv/main_<company>_<role>.tex`
**Compile with:** `tectonic main_<company>_<role>.tex` (on this host)

### The Pre-approved Preamble & Header Template

You MUST start every generated CV with EXACTLY this code (do not change margins or colors):

```latex
\documentclass[a4paper,10pt]{article}

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[margin=1.5cm]{geometry}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{fontawesome5}
\usepackage{graphicx}

\definecolor{accent}{HTML}{1F4E78}
\hypersetup{colorlinks=true, urlcolor=accent, linkcolor=accent}
\pagestyle{empty}
\setlength{\parindent}{0pt}

\titleformat{\section}{\large\bfseries\color{accent}}{}{0em}{}[\vspace{-0.6em}\rule{\textwidth}{0.8pt}]
\titlespacing{\section}{0pt}{8pt}{4pt}

\newcommand{\role}[4]{%
 \textbf{#1} \hfill \textbf{#2}\\[1pt]%
 \textit{#3} \hfill \textit{#4}\\[2pt]%
}
\setlist[itemize]{leftmargin=1.2em, itemsep=1pt, topsep=2pt, parsep=0pt}

\begin{document}

% ================= HEADER =================
\begin{minipage}[c]{0.75\textwidth}
 {\Huge\bfseries Prabhavit Gupta}\\[3pt]
 {\color{accent}\large AI Solutions \& Automation Engineer}\\[5pt]
 \faPhone\ +39 351 610 7807 \quad
 \faEnvelope\ \href{mailto:prabhavitg@gmail.com}{prabhavitg@gmail.com} \quad
 \faLinkedin\ \href{https://www.linkedin.com/in/prabhavit/}{linkedin.com/in/prabhavit} \quad
 \faGithub\ \href{https://github.com/prab-gupta}{prab-gupta} \quad
 \faMapMarker*\ Venice, Italy
\end{minipage}%
\begin{minipage}[c]{0.25\textwidth}
 \begin{flushright}
  \vspace{-15pt}
  \includegraphics[width=2.5cm,height=2.5cm,keepaspectratio]{photo.jpg}
 \end{flushright}
\end{minipage}

\vspace{10pt}

% ================= SUMMARY =================
\section{Summary}
```
"""

content = re.sub(r'## Template: Prabhavit_CV Format \(Strict 1:1\).*?\\section{Summary}\n```', new_template, content, flags=re.DOTALL)

with open(".claude/skills/job-application-assistant/05-cv-templates.md", "w") as f:
    f.write(content)
