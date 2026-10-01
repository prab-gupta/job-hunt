with open("cv/main_Antigravity_Sample.tex", "r") as f:
    content = f.read()

start_idx = content.find(r"\section{Professional Experience}")
end_idx = content.find(r"\section{Education}")

if start_idx != -1 and end_idx != -1:
    new_experience = r"""\section{Professional Experience}

\role{\href{https://flowspace.co}{FlowSpace.co}}{Mar 2024 -- Present}{Lead Developer (Full-time, Freelance)}{London, UK (remote)}
\textit{Own product and automation end to end for a workspace marketplace.}
\begin{itemize}
 \item Built GTM automations for the sales funnel: lead enrichment, routing, and outbound.
 \item Automated CRM lead capture by integrating the company CRM with the platform.
 \item Cut manual support work with AI agents that handle customer queries.
 \item Own the API integrations with OfficeRnD and Nexudus for automated bookings.
 \item Led the migration from a legacy no-code stack to a Next.js and Laravel stack. Scaled from 2,000 to 4,500+ users.
 \item Triage and resolve customer issues end to end.
\end{itemize}
\vspace{6pt}

\role{Urlink}{Apr 2025 -- Jul 2025}{Project Manager \& AI-Assisted Developer (Freelance)}{Barcelona, Spain}
\begin{itemize}
 \item Built the platform and its logic with AI-assisted development; implemented client-driven automations. Stack: GitHub, Netlify, Supabase, bolt.new.
\end{itemize}
\vspace{6pt}

\role{\href{https://get2germany.com}{Get2Germany.com}}{Jan 2024 -- May 2024}{Lead Developer \& Automation Specialist (Part-time)}{Berlin, Germany}
\begin{itemize}
 \item Integrated Google APIs, built AI automation tools to find courses, internships, and jobs, and optimized the database. Stack: n8n, Figma, Google APIs.
\end{itemize}
\vspace{6pt}

% ================= PROJECTS =================
\section{Selected Projects}
\begin{itemize}
 \item \textbf{AI Listing Bot for FlowSpace (Product):} Built an AI pipeline processing 900+ verified workspace listings for FlowSpace. The bot ingests client PDFs and spreadsheets, extracts structured location/amenity data via Claude, and routes it to an n8n webhook for human-in-the-loop review before publishing to the live marketplace.
 \item \textbf{AI CV-Parser for UltraStrategy (Agent):} Developed an automated CV-parsing tool mapping applicant data to fixed schemas. Uses Eden AI and n8n to ingest PDFs, extract key entities via LLM, and populate client databases.
\end{itemize}
\vspace{6pt}

"""
    content = content[:start_idx] + new_experience + content[end_idx:]

with open("cv/main_Antigravity_Sample.tex", "w") as f:
    f.write(content)
