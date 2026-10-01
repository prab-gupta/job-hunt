import re
import os

def convert_to_article(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Replace class
    content = re.sub(r'\\documentclass.*', r'\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n', content)
    
    # Remove custom commands
    content = re.sub(r'\\usepackage\{fancyhdr\}.*?\\begin\{document\}', r'\\begin{document}', content, flags=re.DOTALL)
    
    # Replace namesection
    content = re.sub(r'\\namesection\{\}\{\\Huge\{(.*?)\}\}\{(.*?)\}', r'\\begin{flushleft}\n\\textbf{\1} \\\\\n\\href{mailto:prabhavitg@gmail.com}{prabhavitg@gmail.com} | +39 351 610 7807 | \\href{https://www.linkedin.com/in/prabhavit/}{LinkedIn}\n\\end{flushleft}', content, flags=re.DOTALL)
    
    # Replace currentdate
    content = re.sub(r'\\currentdate\{(.*?)\}', r'\\vspace{5mm}\n\\begin{flushright}\n\1\n\\end{flushright}\n\\vspace{5mm}\n', content)
    
    # Replace lettercontent
    content = re.sub(r'\\lettercontent\{(.*?)\}', r'\1\n\n', content)
    
    # Replace closing
    content = re.sub(r'\\closing\{(.*?)\}', r'\1\\\\', content)
    
    # Replace signature
    content = re.sub(r'\\signature\{(.*?)\}', r'\1', content)
    
    # Remove fontspec block for list
    content = re.sub(r'\{\\raggedright\\fontspec.*?\\begin\{itemize\}', r'\\begin{itemize}', content, flags=re.DOTALL)
    content = re.sub(r'\\end\{itemize\}\\par\}', r'\\end{itemize}', content)

    with open(file_path, 'w') as f:
        f.write(content)

convert_to_article('cover_letters/IdMe_CL.tex')
convert_to_article('cover_letters/Marsh_CL.tex')
