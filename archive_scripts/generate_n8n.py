import os
import subprocess

targets = [
    ("Bet Family", "AI Multi-Agent Engineer (n8n)", "https://djinni.co/jobs/848375-ai-multi-agent-engineer-n8n/"),
    ("Frozeneon", "AI Automation Engineer (n8n)", "https://djinni.co/jobs/846085-ai-automation-engineer-n8n-ai-video-pipeline-/")
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
{\small \faPhone\ +39 351 610 7807 \quad \faEnvelope\ \href{mailto:prabhavitg@gmail.com}{prabhavitg@gmail.com} \quad \faLinkedin\ \href{https://www.linkedin.com/in/prabhavit-gupta/}{LinkedIn} \quad \faGithub\ \href{https://github.com/prab-gupta}{GitHub} \quad \faMapMarker*\ Venice / Milan, Italy (EU Permanent Resident)}
\end{minipage}\hfill

\section*{Profile}
AI and Automation Engineer with ~3 years building production LLM pipelines, autonomous multi-agent systems, and robust API workflows using n8n, Make, Python, and TypeScript. Expert in orchestrating complex, fault-tolerant business logic (webhooks, OAuth, API integrations) to connect disparate platforms. Deep experience with RAG, custom Python/JS scripts in automation platforms, and prompt engineering. Authorized to work remotely across the EU (Italian Long-Term Residence Permit, Partita IVA ready) without sponsorship.

\section*{Experience}
\role{Solutions Engineer / Workflow Automation}{FlowSpace.co}{Mar 2024 - Present}{Remote}
\begin{itemize}
\item Designed and deployed end-to-end API integrations and complex automation pipelines using n8n and Make, bridging CRM, ERP, and bespoke client systems.
\item Built custom nodes/scripts (JS/Python) to handle parsing, data transformation, and conditional routing logic that standard low-code blocks couldn't handle.
\item Managed REST APIs, Webhooks, OAuth flows, and error handling (retries, logging, fault-tolerance).
\end{itemize}

\role{Full-Stack \& AI Engineer}{UltraStrategy (Contract)}{Sep 2023 - Present}{Venice, Italy (Remote)}
\begin{itemize}
\item Engineered production multi-agent LLM pipelines using Claude, OpenAI, and LangChain to automate business processes.
\item Built asynchronous job queues via Node.js, Python, and PostgreSQL.
\item Authored \texttt{llm-doc-parser}, an open-source parsing engine for extracting and vectorizing complex PDF structures for RAG systems.
\end{itemize}

\role{Integration Developer}{Clubee}{Nov 2024 - Present}{Remote}
\begin{itemize}
\item Implemented resilient REST and GraphQL API adapters, synchronizing sports club data across international federations with stringent latency requirements.
\end{itemize}

\role{Lead Web Developer}{Urlink (Acquired)}{Aug 2023 - Jun 2024}{Remote}
\begin{itemize}
\item Led end-to-end development of a bespoke platform (React, Node, MongoDB), directly resulting in its successful acquisition.
\end{itemize}

\section*{Skills}
\textbf{Automation \& APIs:} n8n, Make, Zapier, REST APIs, Webhooks, OAuth2, Playwright.\\\\
\textbf{AI \& LLMs:} Multi-Agent Systems, OpenAI, Claude, LangChain, RAG, Prompt Engineering.\\\\
\textbf{Languages \& Core:} Python, TypeScript, JavaScript, SQL (PostgreSQL).
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
{\color{accent}\large {title} ~$\vert$~ n8n \& API Integration Specialist}\\[4pt]
{\footnotesize Venice, Italy (CET / EU Remote) ~$\vert$~ +39 351 610 7807 ~$\vert$~ \href{mailto:prabhavitg@gmail.com}{prabhavitg@gmail.com} ~$\vert$~ \href{https://www.linkedin.com/in/prabhavit/}{linkedin.com/in/prabhavit}}
\vspace{4pt}
\hrule height 0.8pt
\vspace{10pt}

\textbf{To:} Hiring Team, {company}\\
\textbf{Role:} {title}

Dear Hiring Team,

I am writing to apply for the {title} role at {company}. With ~3 years of production experience building complex, fault-tolerant automations in n8n and Make, combined with deep engineering expertise in Python, TypeScript, and AI multi-agent systems, I am excited about the opportunity to build autonomous systems that handle real business logic.

In my recent work at FlowSpace.co and UltraStrategy, I have specialized in building robust API pipelines that go far beyond simple "linear automations." I regularly design n8n workflows that handle conditional routing, OAuth flows, and webhooks, writing custom JavaScript/Python nodes when out-of-the-box integrations fall short. I have also built end-to-end production LLM agents using Claude, OpenAI, and LangChain—systems that actually make decisions, parse complex JSON/XML, and write to PostgreSQL state without constant supervision. 

Whether it is connecting disparate CRMs, orchestrating RAG pipelines, or automating video/content pipelines via APIs, I am hands-on across the entire stack. I don't just prompt LLMs; I build the resilient architecture around them. I also authored \texttt{llm-doc-parser}, an open-source parsing engine, demonstrating my ability to build deep technical solutions.

I hold an Italian EU Long-Term Residence Permit (permanent resident, no sponsorship required) and operate as an independent contractor (Partita IVA), allowing for a highly flexible and immediate B2B remote engagement. I am completely self-directed and thrive in environments where I can take full ownership of the pipeline architecture.

Thank you for your time. I would love to show you some of the complex n8n workflows and agent architectures I've recently deployed.

Sincerely,\\
Prabhavit Gupta

\end{document}
"""

for co, role, url in targets:
    slug = co.replace(" ", "").replace("&", "")
    cv_path = f"Prabhavit_CV_{slug}.tex"
    cl_path = f"CoverLetter_{slug}.tex"
    
    co_tex = co.replace("&", r"\&")
    role_tex = role.replace("&", r"\&").replace("(", r"\(").replace(")", r"\)")
    
    with open(cv_path, "w") as f:
        f.write(cv_template.replace("{company}", co_tex).replace("{title}", role_tex))
        
    with open(cl_path, "w") as f:
        f.write(cl_template.replace("{company}", co_tex).replace("{title}", role_tex))
        
    subprocess.run(["tectonic", cv_path], check=True)
    subprocess.run(["tectonic", cl_path], check=True)
    
    print(f"Generated {slug}: {os.path.abspath(cv_path.replace('.tex', '.pdf'))}")
    print(f"Generated {slug}: {os.path.abspath(cl_path.replace('.tex', '.pdf'))}")
