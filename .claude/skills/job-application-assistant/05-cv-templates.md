---
framework_version: 1.5.0
---

# CV Templates and Tailoring Guide

**CRITICAL DIRECTIVE**: You are generating a highly tailored 2-page CV for a specific job application. You MUST strictly adhere to the `Prabhavit_CV` Original Layout (1:1 formatting). DO NOT use `moderncv` or any other template. 

## 1. Output Files & Compilation
- **Output file:** `cv/main_<company>_<role>.tex`
- **Compile command:** `tectonic cv/main_<company>_<role>.tex`

## 2. Master Reference Data
- **CRITICAL:** You MUST read `data/cvs/Prabhavit_CV_EN.tex.bak-0916` to source the user's raw experience, projects, education, and technical skills. 
- Do not make up experience. Do not pull from hallucinated memories. Only pull from this specific backup file.

## 3. The Strict Preamble & Header Boilerplate
You MUST start every generated CV with EXACTLY this code. Do not change margins, fonts, spacing, or colors.

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
```

## 4. Content & Tailoring Rules

### Career Summary
```latex
\section{Career Summary}
\begin{itemize}
\item [Bullet 1: 1-2 lines]
\item [Bullet 2: 1-2 lines]
\item [Bullet 3: 1-2 lines]
\end{itemize}
```
- Must be exactly 3 bullet points, highly tailored to the job description.

### Technical Skills & Visa
Include these exact sections, tailoring the `AI/ML` and `Development` bullets slightly if necessary to emphasize keywords from the job description:
```latex
\section{Technical Skills}
\begin{itemize}
\item \textbf{AI/ML} -- AI Agents, RAG, Chatbot development, API integration, Eden AI, OpenAI/ChatGPT integration
\item \textbf{Automation} -- n8n, Playwright
\item \textbf{Development} -- Claude Code, Laravel, Typescript
\item \textbf{Project/Design} -- Figma, Jira, GitHub, Postman, Trello
\end{itemize}

\section{Visa \& Language}
\begin{itemize}
\item \textbf{Language} -- Hindi (Native), English (Professional), Italian (Beginner)
\item \textbf{Work Authorization} -- European Long Term Residence Permit - No Sponsorship required.
\end{itemize}
```

### FlowSpace.co Experience (CRITICAL)
- The user's core experience is at FlowSpace.co. 
- You MUST preserve the exact structure of this section from the master file (`Prabhavit_CV_EN.tex.bak-0916`), including the split between **Product Responsibilities** and **Technical Responsibilities**. 
- Do not cut sub-bullets to save space. the core essence of the migration to Next.JS/Laravel and the AI Agents MUST remain intact. Do not aggressively prune this section.

### Other Experience & Education
- The CV is permitted to be up to 2 pages long. Do not aggressively prune experience to force a 1-page fit.
- Include ALL roles (`Urlink`, `UltraStrategy.com`, `Qomodo`, `Get2Germany.com`, `Clubee`, `Tractionboard`) as they appear in the master file.
- Always conclude with the `Education` and `Certifications` sections as found in the master reference.
