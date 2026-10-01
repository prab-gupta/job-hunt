with open("cv/main_Antigravity_Sample.tex", "r") as f:
    content = f.read()

# Fix summary
old_summary_start = "\\vspace{10pt}\nSenior Agentic Engineer"
old_summary_end = "measurable customer value."

new_summary = """\\section{Summary}
I build AI agents and ship them in production. I write real code — TypeScript, Laravel, Next.js, Python — and wire LLMs, APIs, and data pipelines end to end. At FlowSpace I led the migration of a live marketplace onto a coded Next.js + Laravel stack and own the AI features on top."""

import re
content = re.sub(r'\\vspace{10pt}\nSenior Agentic Engineer.*?measurable customer value\.', new_summary, content, flags=re.DOTALL)


# Fix FlowSpace section
content = re.sub(r'\\role{Full-Stack \\& AI Engineer.*?\\vspace{6pt}', r'''\role{Full-Stack \& AI Engineer (Freelance)}{Mar 2024 - Aug 2026}{FlowSpace.co}{London, UK (Remote)}
\begin{itemize}
\item Led the migration of a live marketplace onto a modern, coded Next.js + Laravel stack, fundamentally improving platform scalability.
\item Embedded AI into the core product by shipping customer support agents that query live database records and intelligently escalate to human teams.
\item Built a custom AI pipeline using Python, TypeScript, Claude, and n8n to extract structured data from PDFs and client spreadsheets with human-in-the-loop review, drafting over 900 verified platform listings.
\item Architected API integrations with third-party providers (OfficeRnD, Nexudus) to automate external bookings and build resilient CRM workflows.
\end{itemize}
\vspace{6pt}''', content, flags=re.DOTALL)

with open("cv/main_Antigravity_Sample.tex", "w") as f:
    f.write(content)
