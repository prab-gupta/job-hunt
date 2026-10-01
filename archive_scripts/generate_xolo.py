import os
import subprocess

targets = [
    ("Xolo", "Customer Success Specialist")
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
Customer Success and Technical Specialist with ~3 years building solutions, automating workflows, and directly supporting B2B and B2C users in diverse tech environments. Highly autonomous with a proven ability to interface directly with clients to translate business pain points into robust technical and operational solutions. Fluent in English and highly empathetic. Authorized to work in the EU (Italian Long-Term Residence Permit) without sponsorship, open to hybrid in Estonia.

\section*{Experience}
\role{Solutions Engineer / Workflow Automation}{FlowSpace.co}{Mar 2024 - Present}{Remote}
\begin{itemize}
\item Led technical discovery sessions directly with clients to map requirements and optimize onboarding workflows.
\item Built custom automated workflows using n8n and Make, bridging gaps between CRM and bespoke client portals to improve end-user success and lower churn.
\end{itemize}

\role{Full-Stack \& AI Engineer}{UltraStrategy (Contract)}{Sep 2023 - Present}{Remote}
\begin{itemize}
\item Engineered production systems to automate data ingestion, acting as a technical liaison to clarify complex technical concepts to non-technical stakeholders.
\end{itemize}

\role{Integration Developer}{Clubee}{Nov 2024 - Present}{Remote}
\begin{itemize}
\item Implemented REST APIs and synchronized sports club data for international federations, providing dedicated support for seamless adoption.
\end{itemize}

\role{Customer Operations \& Web Developer}{Get2Germany}{Oct 2023 - Jun 2024}{Remote}
\begin{itemize}
\item Streamlined the onboarding, placement, and success of healthcare professionals relocating to Germany.
\item Implemented chatbots and provided hands-on support for real-time multilingual candidate resolution.
\end{itemize}

\role{Lead Web Developer}{Urlink (Acquired)}{Aug 2023 - Jun 2024}{Remote}
\begin{itemize}
\item Led end-to-end development while incorporating continuous user feedback into the product roadmap, resulting in a successful acquisition.
\end{itemize}

\section*{Skills}
\textbf{Customer Success:} Client Onboarding, Technical Support, Workflow Automation, Troubleshooting, Requirements Gathering.\\\\
\textbf{Technical Frameworks:} Python, TypeScript, SQL, Node.js, API Integrations, Webhooks, CRM tools.
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
{\color{accent}\large {title} ~$\vert$~ Workflow Automation \& Technical Support}\\[4pt]
{\footnotesize Venice, Italy (CET / EU Remote) ~$\vert$~ +39 351 610 7807 ~$\vert$~ \href{mailto:prabhavitg@gmail.com}{prabhavitg@gmail.com} ~$\vert$~ \href{https://www.linkedin.com/in/prabhavit/}{linkedin.com/in/prabhavit}}
\vspace{4pt}
\hrule height 0.8pt
\vspace{10pt}

\textbf{To:} Hiring Team, {company}\\
\textbf{Role:} {title}

Dear Hiring Team,

I am writing to express my enthusiastic interest in the {title} role at {company}. With ~3 years of experience operating at the intersection of technical engineering, workflow automation, and direct client support, I am eager to help {company}'s customers succeed and thrive using your product.

In my recent work at FlowSpace.co and Get2Germany, my core focus was on technical discovery and customer success. At FlowSpace.co, I led onboarding sessions to map out client requirements and built resilient automated workflows to resolve their operational pain points. At Get2Germany, I personally supported healthcare professionals through their relocation, creating user-friendly portals and chatbots to ensure a smooth, successful transition. 

My background gives me a unique edge in customer success: I don't just troubleshoot issues, I understand the underlying APIs, webhooks, and product logic (Python, TypeScript, SQL). This allows me to communicate effectively with engineering teams while maintaining a highly empathetic, clear, and proactive relationship with users. I thrive on translating complex technical concepts into actionable solutions for customers.

I hold an Italian EU Long-Term Residence Permit (permanent resident, no sponsorship required), allowing me to operate flexibly across the EU, and I am entirely open to the hybrid arrangement in Estonia. 

Thank you for your time and consideration. I would love the opportunity to discuss how my combination of technical depth and customer-facing empathy makes me a perfect fit for {company}.

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
