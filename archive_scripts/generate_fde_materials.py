import os
import subprocess

targets = [
    ("Nutrient", "Forward Deployed Engineer, Customer Success"),
    ("Epiq", "Forward Deployed Legal Engineer"),
    ("Cursor", "Forward Deployed Engineer, EMEA"),
    ("Kota", "Forward Deployed Engineer"),
    ("Runpod", "Forward Deployed Engineer EMEA")
]

cv_template = r"""\documentclass[a4paper,10pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\usepackage{lmodern}
\usepackage[top=1.4cm,bottom=1.5cm,left=1.6cm,right=1.6cm]{geometry}
\usepackage{titlesec,enumitem,xcolor,graphicx,lastpage,fancyhdr}
\usepackage{fontawesome5}
\usepackage[hidelinks]{hyperref}
\hypersetup{colorlinks=true,urlcolor=blue!70!black,linkcolor=blue!70!black}

\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\small\color{gray}Page \thepage\ of \pageref{LastPage}}
\setlength{\parindent}{0pt}
\titleformat{\section}{\large\bfseries}{}{0em}{}[\vspace{-0.6em}\rule{\textwidth}{0.5pt}]
\titlespacing{\section}{0pt}{8pt}{4pt}
\setlist[itemize]{leftmargin=1.1em,itemsep=1.5pt,topsep=1.5pt,parsep=0pt}
\newcommand{\role}[4]{\vspace{2pt}\noindent\parbox[t]{0.48\textwidth}{\raggedright\textbf{#1} \textbar\ \textit{#2}}\hfill\parbox[t]{0.49\textwidth}{\raggedleft\textit{#3} \textbar\ \textit{#4}}\vspace{1pt}}

\begin{document}
\noindent
\begin{minipage}[t]{0.78\textwidth}
\vspace{0pt}
{\huge\bfseries Prabhavit Gupta}\\[4pt]
{\large\bfseries {title} \textbar\ {company}}\\[4pt]
{\small \faPhone\ +39 351 610 7807 \quad \faEnvelope\ \href{mailto:prabhavitg@gmail.com}{prabhavitg@gmail.com} \quad \faLinkedin\ \href{https://www.linkedin.com/in/prabhavit-gupta/}{LinkedIn} \quad \faGithub\ \href{https://github.com/prab-gupta}{GitHub} \quad \faMapMarker*\ Venice / Milan, Italy}
\end{minipage}\hfill
\begin{minipage}[t]{0.18\textwidth}
\vspace{0pt}\raggedleft\includegraphics[width=2.1cm]{photo_small.jpg}
\end{minipage}

\section*{Profile}
Full-Stack and AI Engineer with ~3 years building production LLM pipelines, RAG systems, and API integrations in TypeScript and Python. Highly autonomous, with a proven ability to interface directly with clients to translate business pain points into robust, deployed technical solutions. Authorized to work in the EU (Italian Long-Term Residence Permit) without sponsorship.

\section*{Experience}
\role{Full-Stack \& AI Engineer}{UltraStrategy (Contract)}{Sep 2023 - Present}{Venice, Italy (Remote)}
\begin{itemize}
\item Engineered production multi-agent LLM pipelines using Claude, OpenAI, and LangChain to automate data ingestion and document processing across massive corpora.
\item Deployed asynchronous job queues via Node.js, Python, and PostgreSQL, cutting API latency.
\item Engineered \texttt{llm-doc-parser}, an open-source parsing engine for converting complex PDF structures into structured, vector-ready Markdown context.
\end{itemize}

\role{Solutions Engineer / Workflow Automation}{FlowSpace.co}{Mar 2024 - Present}{Remote}
\begin{itemize}
\item Designed custom API integrations, webhooks, and n8n/Make automation flows, bridging disparate enterprise SaaS tools (CRM, ERP, and bespoke client portals).
\item Led technical discovery sessions with clients to scope integration requirements, drastically reducing onboarding time.
\end{itemize}

\role{Integration Developer}{Clubee}{Nov 2024 - Present}{Remote}
\begin{itemize}
\item Implemented resilient REST and GraphQL API adapters, synchronizing sports club data across international federations with stringent latency requirements.
\end{itemize}

\role{AI \& Web Developer}{Get2Germany}{Oct 2023 - Jun 2024}{Remote}
\begin{itemize}
\item Architected an interactive web portal using Next.js and Firebase to streamline the immigration and placement of healthcare professionals.
\item Implemented RAG-powered chatbot interfaces for real-time multilingual candidate support.
\end{itemize}

\role{Lead Web Developer}{Urlink (Acquired)}{Aug 2023 - Jun 2024}{Remote}
\begin{itemize}
\item Led the end-to-end development of a bespoke networking platform (React, Node, MongoDB).
\item Spearheaded the core product architecture, directly resulting in its successful acquisition.
\end{itemize}

\section*{Skills}
\textbf{Languages \& Core:} Python, TypeScript, JavaScript, SQL, HTML/CSS.\\\\
\textbf{Frameworks \& Tools:} Next.js, Node.js, FastAPI, Flask, React, Laravel, Supabase, PostgreSQL.\\\\
\textbf{AI \& Infrastructure:} LLM Orchestration, RAG Pipelines, Docker, Git, REST, GraphQL, Webhooks.
\end{document}
"""

cl_template = r"""\documentclass[a4paper,10pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[top=1.2cm,bottom=1.2cm,left=1.5cm,right=1.5cm]{geometry}
\usepackage{hyperref}
\usepackage{xcolor}

\definecolor{accent}{HTML}{1E3A8A}
\hypersetup{colorlinks=true, urlcolor=accent, linkcolor=accent}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{8pt}

\begin{document}

{\Huge\bfseries Prabhavit Gupta}\\[4pt]
{\color{accent}\large {title} ~$\vert$~ Agentic LLM Pipelines \& API Integrations}\\[4pt]
{\footnotesize Venice, Italy (CET / EU Remote) ~$\vert$~ +39 351 610 7807 ~$\vert$~ \href{mailto:prabhavitg@gmail.com}{prabhavitg@gmail.com} ~$\vert$~ \href{https://www.linkedin.com/in/prabhavit/}{linkedin.com/in/prabhavit}}
\vspace{4pt}
\hrule height 0.8pt
\vspace{10pt}

\textbf{To:} Hiring Team, {company}\\
\textbf{Role:} {title}\\
\textbf{Re:} Application for {title}

Dear Hiring Team,

I am writing to express my enthusiastic interest in the {title} role at {company}. With ~3 years of production experience designing and deploying end-to-end AI systems, API integrations, and resilient automated workflows across Python, TypeScript, and PostgreSQL, I am eager to help {company} deliver world-class technical solutions directly to clients.

In my recent work at UltraStrategy and FlowSpace.co, I have specialized in building robust multi-agent LLM pipelines and complex API automations that solve concrete business problems. I have consistently operated as a Forward Deployed Engineer: leading technical discovery, architecting the integration strategy, and writing the production code (Next.js, Python, Supabase) to connect bespoke enterprise systems. I also built \texttt{llm-doc-parser}, an open-source parsing engine for converting complex PDF structures into structured Markdown context.

My background is rooted in delivering immediate value to clients, whether by streamlining data synchronization for international federations at Clubee or architecting full-stack web platforms at Urlink. I thrive in customer-facing technical roles where I can bridge the gap between engineering capabilities and client needs.

I hold an Italian EU Long-Term Residence Permit (permanent resident, no sponsorship required), allowing me to operate flexibly across the EU. I am highly autonomous, comfortable with ambiguity, and ready to deploy rapidly.

Thank you for your time and consideration. I would welcome the opportunity to discuss how my hands-on integration experience and AI expertise align with the engineering goals at {company}.

Sincerely,\\
Prabhavit Gupta

\end{document}
"""

for co, role in targets:
    slug = co.replace(" ", "").replace("&", "")
    cv_path = f"Prabhavit_CV_{slug}.tex"
    cl_path = f"CoverLetter_{slug}.tex"
    
    co_tex = co.replace("&", r"\&")
    role_tex = role.replace("&", r"\&")
    
    with open(cv_path, "w") as f:
        f.write(cv_template.replace("{company}", co_tex).replace("{title}", role_tex))
        
    with open(cl_path, "w") as f:
        f.write(cl_template.replace("{company}", co_tex).replace("{title}", role_tex))
        
    subprocess.run(["tectonic", cv_path], check=True)
    subprocess.run(["tectonic", cl_path], check=True)
    
    print(f"Generated {slug}: {os.path.abspath(cv_path.replace('.tex', '.pdf'))}")
    print(f"Generated {slug}: {os.path.abspath(cl_path.replace('.tex', '.pdf'))}")
