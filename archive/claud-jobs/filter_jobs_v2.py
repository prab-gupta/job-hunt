#!/usr/bin/env python3
import json
import re
import sys

# Load jobs from raw_jobs.json
with open('raw_jobs.json', 'r') as f:
    all_jobs = json.load(f)

# Titles to drop (exact or contains) - use case-insensitive matching
drop_keywords = [
    r'Senior',
    r'Sr\.',
    r'Staff',
    r'Principal',
    r'Lead',
    r'Head',
    r'Director',
    r'Manager',  # But keep "Product Manager" and "Technical Product Manager"
    r'Architect',
    r'Intern',
    r'Working Student',
    r'Praktikum',
    r'Werkstudent',
    r'Stage',
    r'Tirocinio',
]

# Non-English language markers (Italian, German, French, Polish) - case-insensitive
non_english_markers = [
    r'Consulente',  # Italian consultant
    r'Analista',    # Italian analyst
    r'Funzionale',  # Italian functional
    r'Sviluppatore', # Italian developer
    r'Entwickler',   # German developer
    r'Softwareentwickler',  # German developer
    r'Ingénieur',   # French engineer
    r'Programista',  # Polish programmer
    r'Gestione',    # Italian management
    r'Applicativo', # Italian application
    r'Dinamiche',   # Italian dynamics
]

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
    
    # Check if title contains drop keywords (case-insensitive)
    should_drop = False
    for keyword in drop_keywords:
        if re.search(keyword, title, re.IGNORECASE):
            should_drop = True
            print(f"Dropping (keyword '{keyword}'): {title}", file=sys.stderr)
            break
    
    if should_drop:
        drop_count += 1
        continue
    
    # Check if title contains non-English language markers (case-insensitive)
    has_non_english = False
    for marker in non_english_markers:
        if re.search(marker, title, re.IGNORECASE):
            has_non_english = True
            print(f"Dropping (non-English '{marker}'): {title}", file=sys.stderr)
            break
    
    if has_non_english:
        drop_count += 1
        continue
    
    # Keep this job
    filtered_jobs.append(job)
    keep_count += 1

print(f"Kept {keep_count}, dropped {drop_count}", file=sys.stderr)
print(json.dumps(filtered_jobs, indent=2))
