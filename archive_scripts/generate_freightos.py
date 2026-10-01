import os
import subprocess

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
{\large\bfseries Customer Success Specialist \textbar\ Freightos}\\[4pt]
{\small \faPhone\ +39 351 610 7807 \quad \faEnvelope\ \href{mailto:prabhavitg@gmail.com}{prabhavitg@gmail.com} \quad \faLinkedin\ \href{https://www.linkedin.com/in/prabhavit-gupta/}{LinkedIn} \quad \faMapMarker*\ Venice / Milan, Italy (EU Permanent Resident, Barcelona Mobility)}
\end{minipage}\hfill

\section*{Profile}
Customer Success and Technical Operations Specialist with ~3 years building solutions, onboarding B2B clients, and managing complex technical escalations. Proven ability to own the post-go-live lifecycle, drive platform adoption, and act as a bridge between commercial strategy and engineering (Product, PMO, Ops). Fluent in English with a strong documentation and process mindset. Authorized to work in the EU (Italian Long-Term Residence Permit) without sponsorship and open to Hybrid in Barcelona.

\section*{Experience}
\role{Solutions Engineer / Workflow Automation}{FlowSpace.co}{Mar 2024 - Present}{Remote}
\begin{itemize}
\item Led post-onboarding technical discovery sessions to maximize user adoption, mapping complex workflows to SaaS capabilities and reducing churn risk.
\item Built automated workflows bridging CRM and bespoke platforms, acting as the primary point of contact for technical escalations.
\item Translated product feature gaps into structured feedback for the engineering team.
\end{itemize}

\role{Customer Operations Specialist}{Get2Germany}{Oct 2023 - Jun 2024}{Remote}
\begin{itemize}
\item Owned the post-onboarding lifecycle for healthcare professionals navigating complex relocation and compliance workflows.
\item Supported scalable education by implementing self-service chatbots and contributing to user training guides.
\end{itemize}

\role{Full-Stack \& AI Engineer}{UltraStrategy (Contract)}{Sep 2023 - Present}{Remote}
\begin{itemize}
\item Engineered production systems for enterprise clients, combining deep technical troubleshooting with proactive customer communication.
\item Authored \texttt{llm-doc-parser} to seamlessly structure complex documents, improving operational speed for client ingestion.
\end{itemize}

\role{Integration Developer}{Clubee}{Nov 2024 - Present}{Remote}
\begin{itemize}
\item Acted as the technical focal point for international sports federations, managing API integrations and ensuring seamless cross-functional delivery.
\end{itemize}

\section*{Skills}
\textbf{Customer Success:} B2B SaaS Onboarding, Post-Go-Live Lifecycle, Platform Adoption, Client Escalations, Technical Training.\\\\
\textbf{Technical Frameworks:} API Troubleshooting, Jira, Confluence, CRM (Salesforce/Zoho principles), Python, TypeScript, SQL.
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
{\color{accent}\large Customer Success Specialist ~$\vert$~ B2B SaaS \& Operations}\\[4pt]
{\footnotesize Venice, Italy (CET / EU Remote) ~$\vert$~ +39 351 610 7807 ~$\vert$~ \href{mailto:prabhavitg@gmail.com}{prabhavitg@gmail.com} ~$\vert$~ \href{https://www.linkedin.com/in/prabhavit/}{linkedin.com/in/prabhavit}}
\vspace{4pt}
\hrule height 0.8pt
\vspace{10pt}

\textbf{To:} Hiring Team, Freightos\\
\textbf{Role:} Customer Success Specialist - Europe

Dear Hiring Team,

I am writing to express my enthusiastic interest in the Customer Success Specialist role at Freightos. With ~3 years of experience managing post-go-live client lifecycles, leading technical escalations, and driving platform adoption in fast-moving B2B SaaS environments, I am eager to help your forwarder and shipper clients fully leverage the Freightos platform.

In my recent work at FlowSpace.co and Get2Germany, my core focus was on maximizing user adoption and managing complex operational workflows. At FlowSpace.co, I led enablement sessions, identified adoption gaps early, and acted as the primary point of contact for technical escalations—coordinating with engineering and product teams to resolve friction points. At Get2Germany, I owned the post-onboarding lifecycle for candidates navigating intricate compliance requirements, creating self-service documentation and proactive support structures.

My background equips me with a unique edge for this role: I combine a deep understanding of technical APIs and platform integrations (Python, SQL, webhooks) with the communication skills required to manage enterprise stakeholders. I thrive on translating commercial strategies into day-to-day execution and transforming complex escalations into seamless customer experiences.

I hold an Italian EU Long-Term Residence Permit (permanent resident, no sponsorship required), allowing me to operate flexibly across the EU, and I am entirely open to the hybrid arrangement in Barcelona. I am highly autonomous, proactive, and ready to champion value realization for Freightos’ enterprise accounts.

Thank you for your time and consideration. I would welcome the opportunity to discuss how my combination of technical problem-solving and customer-facing expertise aligns with your team in Europe.

Sincerely,\\
Prabhavit Gupta

\end{document}
"""

slug = "Freightos"
cv_path = f"Prabhavit_CV_{slug}.tex"
cl_path = f"CoverLetter_{slug}.tex"

with open(cv_path, "w") as f:
    f.write(cv_template)
    
with open(cl_path, "w") as f:
    f.write(cl_template)
    
subprocess.run(["tectonic", cv_path], check=True)
subprocess.run(["tectonic", cl_path], check=True)

