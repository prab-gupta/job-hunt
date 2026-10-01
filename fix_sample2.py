with open("cv/main_Antigravity_Sample.tex", "r") as f:
    content = f.read()

# Fix summary
start_str = r"\end{minipage}"
end_str = r"\section{Core Competencies}"
start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_summary = r"""\end{minipage}

\vspace{10pt}
\section{Summary}
I build AI agents and ship them in production. I write real code — TypeScript, Laravel, Next.js, Python — and wire LLMs, APIs, and data pipelines end to end. At FlowSpace I led the migration of a live marketplace onto a coded Next.js + Laravel stack and own the AI features on top.

"""
    content = content[:start_idx] + new_summary + content[end_idx:]

# Fix FlowSpace section
start_str_fs = r"\role{Full-Stack \& AI Engineer (Freelance)}{Mar 2024 - Aug 2026}{FlowSpace.co}{London, UK (Remote)}"
end_str_fs = r"\vspace{6pt}"
start_idx_fs = content.find(start_str_fs)
end_idx_fs = content.find(end_str_fs, start_idx_fs)

if start_idx_fs != -1 and end_idx_fs != -1:
    flowspace_new = r"""\role{Full-Stack \& AI Engineer (Freelance)}{Mar 2024 - Aug 2026}{FlowSpace.co}{London, UK (Remote)}
\begin{itemize}
\item Led the migration of a live marketplace onto a modern, coded Next.js + Laravel stack, fundamentally improving platform scalability.
\item Embedded AI into the core product by shipping customer support agents that query live database records and intelligently escalate to human teams.
\item Built a custom AI pipeline using Python, TypeScript, Claude, and n8n to extract structured data from PDFs and client spreadsheets with human-in-the-loop review, drafting over 900 verified platform listings.
\item Architected API integrations with third-party providers (OfficeRnD, Nexudus) to automate external bookings and build resilient CRM workflows.
\end{itemize}
"""
    content = content[:start_idx_fs] + flowspace_new + content[end_idx_fs:]

with open("cv/main_Antigravity_Sample.tex", "w") as f:
    f.write(content)
