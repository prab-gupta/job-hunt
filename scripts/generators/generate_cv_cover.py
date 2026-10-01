import os

cv_content = r"""\documentclass[11pt,a4paper,sans]{moderncv}
\moderncvstyle{banking}
\moderncvcolor{blue}

\renewcommand*{\namefont}{\fontsize{34}{36}\bfseries\upshape}
\colorlet{firstnamecolor}{color1}
\colorlet{lastnamecolor}{color1}
\colorlet{namecolor}{color1}
\renewcommand*{\sectionstyle}[1]{{\sectionfont\color{color1}#1}}

\usepackage[utf8]{inputenc}
\AtEndPreamble{\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,
    urlcolor=blue,
    pdftitle={Prabhavit Gupta - CV},
    pdfpagemode=UseNone,
}}
\usepackage[scale=0.80]{geometry}
\usepackage{import}

\name{Prabhavit}{Gupta}
\address{Venice, Italy}{}{}
\phone[mobile]{+39 351 610 7807}
\email{prabhavitg@gmail.com}
\extrainfo{\href{https://www.linkedin.com/in/prabhavit/}{LinkedIn}, \href{https://github.com/prab-gupta}{GitHub}}

\begin{document}
\makecvtitle

Backend Software Engineer specialized in high-performance distributed systems, API integrations, and event-driven architectures. At FlowSpace, I built and scaled backend architectures that orchestrate complex asynchronous workflows, handling high-throughput rate limits, and webhook retry logic to ensure fault tolerance. I am highly adaptable, leveraging AI-assisted workflows to rapidly master new tech stacks and frameworks. With a strong track record of building resilient, scalable systems, I am eager to bring my backend engineering expertise to KarrotPay's mission-critical payment infrastructure, ensuring stable and reliable fintech experiences.

\section{Core Competencies}
\begin{itemize}
\item \textbf{Backend \& Infrastructure:} Python, TypeScript, Node.js, PostgreSQL, AWS, CI/CD. Proven ability to rapidly adapt to JVM-based environments (Kotlin, Spring Boot, gRPC).
\item \textbf{Distributed Systems:} REST API design, event-driven architectures, webhooks, asynchronous job processing, fault tolerance, high-availability, Docker.
\item \textbf{AI \& Orchestration:} AI-assisted coding for accelerated development, multi-agent workflow design, LLM tool use.
\end{itemize}

\section{Professional Experience}
\cventry{Mar 2024 - Aug 2026}{Full-Stack \& Backend Engineer}{FlowSpace.co}{London, UK (Remote)}{}{
\begin{itemize}
\item Designed event-driven architectures integrating complex APIs, handling rate limits, webhooks, and retry logic across service boundaries to serve high-throughput workloads with strict fault tolerance.
\item Built and scaled data pipelines orchestrating multi-step integrations with asynchronous job processing, ensuring strong data consistency and system resilience.
\item Migrated a legacy system to a modern stack (Next.js, PostgreSQL), optimizing database performance and scaling the active user base from 2,000 to over 4,500.
\item Leveraged AI agents and AI-assisted coding workflows to significantly improve development velocity and maintain high code quality across the platform.
\end{itemize}}

\vspace{3pt}
\cventry{Jan 2024 - May 2024}{Developer \& Automation Specialist}{Get2Germany.com}{Berlin, Germany}{}{
\begin{itemize}
\item Integrated third-party APIs and built robust data extraction workflows, optimizing underlying PostgreSQL database performance for concurrent access and large-scale data processing.
\end{itemize}}

\vspace{3pt}
\cventry{Sep 2023 - Aug 2024}{Developer \& QA}{Clubee.com}{Foetz, Luxembourg}{}{
\begin{itemize}
\item Spearheaded the integration of the Clubee API, ensuring reliable system performance and data integrity in a highly distributed environment.
\end{itemize}}

\section{Independent Projects}
\cventry{2024 - 2025}{Backend Developer}{UltraStrategy}{Freelance}{}{
\begin{itemize}
\item Built a scalable data extraction tool serving multiple user profiles, directly collaborating with stakeholders to translate requirements into deployed features.
\end{itemize}}

\vspace{3pt}
\cventry{2025}{Project Manager \& Backend Developer}{Urlink}{Freelance}{}{
\begin{itemize}
\item Led the end-to-end development of a platform, deploying client-driven automations, establishing secure data handling, and optimizing backend services.
\end{itemize}}

\section{Education}
\cventry{Oct 2020 - Jun 2024}{BA Philosophy, International Studies \& Economics}{Ca' Foscari University of Venice}{Venice, Italy}{}{\vspace{1pt}Minor: Entrepreneurship. Developed strong logical thinking and a collaborative mindset.}

\vspace{5pt}
{\small \textbf{Work authorization:} EU Long Term Residence Permit (Italy). Open to relocation to Seoul, South Korea.}

\end{document}
"""

cover_content = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[scale=0.80]{geometry}
\usepackage{hyperref}
\usepackage{parskip}

\begin{document}

\begin{flushright}
\textbf{Prabhavit Gupta}\\
Venice, Italy\\
+39 351 610 7807\\
prabhavitg@gmail.com\\
\href{https://www.linkedin.com/in/prabhavit/}{LinkedIn} | \href{https://github.com/prab-gupta}{GitHub}
\end{flushright}

\vspace{2em}

\textbf{To:} Hiring Manager, KarrotPay\\
\textbf{Date:} \today\\
\textbf{Subject:} Application for Software Engineer, Backend

\vspace{1em}

Dear Hiring Manager,

I am writing to express my strong interest in the Backend Software Engineer role at KarrotPay. I am deeply inspired by KarrotPay's mission to transform neighborhood commerce by creating a seamless, reliable fintech experience that connects local businesses and users. The opportunity to contribute to a mission-critical platform that powers the daily transactions of millions---whether in the Offline Payment team, Payment Core, or Service Core---perfectly aligns with my passion for building resilient, high-performance distributed systems.

At FlowSpace, I specialized in designing and scaling event-driven architectures capable of handling high-throughput workloads. I built robust data pipelines and orchestrated complex API integrations with strict fault tolerance, implementing rate limiting, webhook retry logic, and asynchronous job processing to ensure system stability. I understand that processing financial transactions requires zero compromise on data consistency and reliability. I have tackled similar challenges in concurrent database optimization and distributed architecture design, ensuring that my systems could gracefully recover from failures without dropping a single event.

While my recent professional experience has centered around Python, Node.js, and PostgreSQL, I am highly adaptable and have a strong foundation in the principles of mission-critical systems. I actively use AI-assisted coding tools like Claude Code to rapidly master new technologies. I am confident in my ability to quickly ramp up in a Kotlin and Spring Boot ecosystem, leveraging my deep understanding of REST, gRPC, distributed data streaming, and AWS infrastructure to deliver immediate value to the KarrotPay team. 

I thrive in collaborative, fast-paced environments where engineers take ownership of the entire product lifecycle---from domain modeling to deploying on Kubernetes. I am excited about the prospect of joining a team that values continuous learning and proactive problem-solving.

Thank you for considering my application. I am currently based in Italy but am fully open to relocating to Seoul for this opportunity. I look forward to the possibility of discussing how my background, adaptability, and drive for engineering excellence can contribute to the continued growth of KarrotPay.

Sincerely,

\vspace{1em}
Prabhavit Gupta

\end{document}
"""

os.makedirs("cv", exist_ok=True)
os.makedirs("cover_letters", exist_ok=True)

with open("cv/main_KarrotPay_SoftwareEngineerBackend.tex", "w") as f:
    f.write(cv_content)

with open("cover_letters/cover_KarrotPay_SoftwareEngineerBackend.tex", "w") as f:
    f.write(cover_content)

print("Files written successfully.")
