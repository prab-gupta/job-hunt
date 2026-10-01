import re

with open('loop/CL_SAP.tex', 'r') as f:
    content = f.read()

# Replace \documentclass[]{cover} with article
content = content.replace(r'\documentclass[]{cover}', r'\documentclass[11pt,a4paper]{article}')
content = content.replace(r'\namesection{}{\Huge{Prabhavit Gupta}}{  \href{mailto:prabhavitg@gmail.com}{prabhavitg@gmail.com} | +39 351 610 7807 |  \urlstyle{same}\href{https://www.linkedin.com/in/prabhavit/}{LinkedIn}', r'\begin{center}{\Huge Prabhavit Gupta} \\ \href{mailto:prabhavitg@gmail.com}{prabhavitg@gmail.com} | +39 351 610 7807 | \href{https://www.linkedin.com/in/prabhavit/}{LinkedIn}\end{center}')
content = content.replace(r'\currentdate{\today}', r'\today\\')
content = content.replace(r'\lettercontent{', r'\noindent ')
content = content.replace(r'}', '')
content = re.sub(r'\\closing\{.*?\}', 'Kind regards,\\\\', content)
content = re.sub(r'\\signature\{.*?\}', 'Prabhavit Gupta', content)

# A bit hacky, let's just generate a simple CL for SAP from scratch using basic article class to be safe.
