import os
import re
import subprocess
import csv

def clean_slug(s):
    return re.sub(r"[^a-zA-Z0-9]", "", s)

# Get 13 missing targets
fde_targets = []
with open('loop/queue.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['status'] == 'TO APPLY':
            is_easy_apply = 'EASY' in row['form_type'].upper()
            if not is_easy_apply:
                role_upper = row['role'].upper()
                lane_upper = row['lane'].upper()
                if 'FORWARD' in role_upper or 'FDE' in role_upper or 'FDE' in lane_upper:
                    fde_targets.append(row)

missing = []
for t in fde_targets:
    slug = clean_slug(t['company'])
    tex_file = f"Prabhavit_CV_{slug}.tex"
    if not os.path.exists(tex_file):
        missing.append(t)

# Read templates
with open('plugins/ai-job-hunter/templates/Prabhavit_CV_Base.tex', 'r') as f:
    cv_base = f.read()

with open('plugins/ai-job-hunter/templates/CoverLetter_Base.tex', 'r') as f:
    cl_base = f.read()

# Generate missing ones
for t in missing:
    slug = clean_slug(t['company'])
    company = t['company'].replace('&', '\\&').replace('%', '\\%').replace('#', '\\#')
    role = t['role'].replace('&', '\\&').replace('%', '\\%').replace('#', '\\#')
    
    cv_content = cv_base
    cl_content = cl_base.replace('COMPANY NAME', company).replace('POSITION TITLE', role)
    
    cv_file = f"Prabhavit_CV_{slug}.tex"
    cl_file = f"CoverLetter_{slug}.tex"
    
    with open(cv_file, 'w') as f:
        f.write(cv_content)
    with open(cl_file, 'w') as f:
        f.write(cl_content)
        
    print(f"Generated {cv_file} and {cl_file}")

# Compile all FDE targets (including the 24 existing and 13 new)
all_generated = []
for t in fde_targets:
    slug = clean_slug(t['company'])
    cv_file = f"Prabhavit_CV_{slug}.tex"
    cl_file = f"CoverLetter_{slug}.tex"
    
    # Run latex builder
    subprocess.run(["python3", "plugins/ai-job-hunter/scripts/latex_builder.py", "--cv", cv_file], capture_output=True)
    subprocess.run(["python3", "plugins/ai-job-hunter/scripts/latex_builder.py", "--letter", cl_file], capture_output=True)
    
    all_generated.append(t)

# Update STATE.md
with open("STATE.md", "w") as f:
    f.write("# USER ACTIONS (only you can do these)\n\n")
    f.write("Please use the `/browser` Chrome sidecar to execute the actual form filling for the following offsite FDE targets. The generated PDF materials are staged in the workspace.\n\n")
    for t in all_generated:
        f.write(f"- [ ] {t['company']} - {t['role']}\n")

print("Done generating PDFs and staging in STATE.md.")
