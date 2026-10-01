#!/usr/bin/env python3
import json
import re
import sys

# Load jobs from raw_jobs.json
with open('raw_jobs.json', 'r') as f:
    all_jobs = json.load(f)

# Titles to drop (exact or contains)
drop_keywords = [
    r'\bSenior\b',
    r'\bSr\.\b',
    r'\bStaff\b',
    r'\bPrincipal\b',
    r'\bLead\b',
    r'\bHead\b',
    r'\bDirector\b',
    r'\bManager\b',  # But keep "Product Manager" and "Technical Product Manager"
    r'\bArchitect\b',
    r'\bIntern\b',
    r'\bWorking Student\b',
    r'\bPraktikum\b',
    r'\bWerkstudent\b',
    r'\bStage\b',
    r'\bTirocinio\b',
]

# Non-English language markers (Italian, German, French, Polish)
non_english_markers = {
    r'[Cc]onsulente',  # Italian consultant
    r'[Aa]nalista',    # Italian analyst
    r'[Ff]unzionale',  # Italian functional
    r'[Ss]viluppatore', # Italian developer
    r'[Ee]ntwickler',   # German developer
    r'[Ss]oftwareentwickler',  # German developer
    r'[Ii]ngénieur',   # French engineer
    r'[Pp]rogramista',  # Polish programmer
    r'[Gg]estione',    # Italian management
    r'[Aa]pplicativo', # Italian application
    r'[Dd]inamiche',   # Italian dynamics
}

filtered_jobs = []
keep_count = 0
drop_count = 0

for job in all_jobs:
    title = job.get('title', '')
    
    # Check if it's a Product Manager or Technical Product Manager - keep these even if they contain Manager
    if 'Product Manager' in title or 'Technical Product Manager' in title:
        filtered_jobs.append(job)
        keep_count += 1
        continue
    
    # Check if title contains drop keywords
    should_drop = False
    for keyword in drop_keywords:
        if re.search(keyword, title):
            should_drop = True
            print(f"Dropping (keyword): {title}", file=sys.stderr)
            break
    
    if should_drop:
        drop_count += 1
        continue
    
    # Check if title contains non-English language markers
    has_non_english = False
    for marker in non_english_markers:
        if re.search(marker, title):
            has_non_english = True
            print(f"Dropping (non-English): {title}", file=sys.stderr)
            break
    
    if has_non_english:
        drop_count += 1
        continue
    
    # Keep this job
    filtered_jobs.append(job)
    keep_count += 1

print(f"Kept {keep_count}, dropped {drop_count}", file=sys.stderr)
print(json.dumps(filtered_jobs, indent=2))
