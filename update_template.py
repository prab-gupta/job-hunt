with open(".claude/skills/job-application-assistant/05-cv-templates.md", "r") as f:
    content = f.read()

# Fix the minipage break
content = content.replace(r"""\end{minipage}
\begin{minipage}[c]{0.2\textwidth}""", r"""\end{minipage}%
\begin{minipage}[c]{0.2\textwidth}""")

# Adjust widths
content = content.replace(r"{0.8\textwidth}", r"{0.75\textwidth}")

with open(".claude/skills/job-application-assistant/05-cv-templates.md", "w") as f:
    f.write(content)

print("Template fixed.")
