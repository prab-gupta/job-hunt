import re
import sys

def rewrite(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Extract date
    date_match = re.search(r'\\currentdate\{(.*?)\}', content)
    date_str = date_match.group(1) if date_match else "\\today"

    # Extract body items (everything between MAIN COVER LETTER CONTENT and \begin{flushright})
    body_match = re.search(r'MAIN COVER LETTER CONTENT.*?\%(.*?)\\begin\{flushright\}', content, re.DOTALL)
    body = body_match.group(1) if body_match else content.split('MAIN COVER LETTER CONTENT')[1].split(r'\begin{flushright}')[0]
    
    # Strip \lettercontent
    body = re.sub(r'\\lettercontent\{(.*?)\}', r'\1\n\n', body)
    # Strip fontspec
    body = re.sub(r'\{\\raggedright\\fontspec.*?\\begin\{itemize\}', r'\\begin{itemize}', body, flags=re.DOTALL)
    body = re.sub(r'\\end\{itemize\}\\par\}', r'\\end{itemize}', body)
    
    new_tex = f"""\\documentclass[11pt,a4paper]{{article}}
\\usepackage[margin=1in]{{geometry}}
\\usepackage{{hyperref}}

\\begin{{document}}

\\begin{{flushleft}}
\\textbf{{Prabhavit Gupta}} \\\\
\\href{{mailto:prabhavitg@gmail.com}}{{prabhavitg@gmail.com}} | +39 351 610 7807 | \\href{{https://www.linkedin.com/in/prabhavit/}}{{LinkedIn}}
\\end{{flushleft}}

\\vspace{{5mm}}
\\begin{{flushright}}
{date_str}
\\end{{flushright}}

\\vspace{{5mm}}
{body}

\\vspace{{5mm}}
\\begin{{flushright}}
Kind regards,\\\\
\\vspace{{3mm}}
Prabhavit Gupta
\\end{{flushright}}

\\end{{document}}
"""
    with open(file_path, 'w') as f:
        f.write(new_tex)

rewrite('cover_letters/IdMe_CL.tex')
rewrite('cover_letters/Marsh_CL.tex')
