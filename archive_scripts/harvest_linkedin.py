import json
import subprocess
import re
import sys

def fetch_jobs(start):
    url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=AI%20engineer&geoId=103350119&f_TPR=r86400&start={start}'
    try:
        result = subprocess.run(
            ['curl', '-s', '-A', 'Mozilla/5.0', url],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout
    except Exception as e:
        print(f"Error fetching: {e}", file=sys.stderr)
        return ""

def parse_jobs(html):
    jobs = []
    
    # Split by job posting divs
    job_blocks = re.split(r'data-entity-urn="urn:li:jobPosting:', html)
    
    for block in job_blocks[1:]:  # Skip first empty split
        # Extract job ID
        job_id_match = re.search(r'^(\d+)', block)
        if not job_id_match:
            continue
        job_id = job_id_match.group(1)
        
        # Extract title from <h3 class="base-search-card__title">
        title_match = re.search(r'<h3\s+class="base-search-card__title">\s*\n\s*(.*?)\s*\n\s*</h3>', block, re.DOTALL)
        title = title_match.group(1).strip() if title_match else ''
        
        # Extract company from <h4 class="base-search-card__subtitle">
        company_match = re.search(r'<h4\s+class="base-search-card__subtitle">.*?>(.*?)</a>', block, re.DOTALL)
        company = company_match.group(1).strip() if company_match else ''
        
        # Extract location from <span class="job-search-card__location">
        location_match = re.search(r'<span\s+class="job-search-card__location">\s*\n\s*(.*?)\s*\n\s*</span>', block, re.DOTALL)
        location = location_match.group(1).strip() if location_match else ''
        
        if job_id:
            jobs.append({
                'id': job_id,
                'title': title,
                'company': company,
                'location': location
            })
    
    return jobs

jobs = []
for start in [0, 25, 50]:
    print(f"Fetching start={start}...", file=sys.stderr)
    html = fetch_jobs(start)
    
    if not html or 'data-entity-urn="urn:li:jobPosting:' not in html:
        print(f"No results for start={start}, retrying in 5s...", file=sys.stderr)
        import time
        time.sleep(5)
        html = fetch_jobs(start)
    
    if html and 'data-entity-urn="urn:li:jobPosting:' in html:
        batch = parse_jobs(html)
        jobs.extend(batch)
        print(f"Got {len(batch)} jobs from start={start}", file=sys.stderr)
    else:
        print(f"Empty or no data for start={start}", file=sys.stderr)

# Filter: drop Senior, Sr., Staff, Principal, Lead, Head, Director, Manager, Architect, Intern, Working Student, Praktikum, Werkstudent, Stage, Tirocinio
# But keep "Product Manager" and "Technical Product Manager"
filtered = []
for job in jobs:
    title = job['title']
    
    # Skip if contains these words (case-insensitive)
    skip_words = [
        r'\bSenior\b', r'\bSr\.\b', r'\bStaff\b', r'\bPrincipal\b', 
        r'\bLead\b', r'\bHead\b', r'\bDirector\b', r'\bArchitect\b',
        r'\bIntern\b', r'\bWorking\s+Student\b', r'\bPraktikum\b', 
        r'\bWerkstudent\b', r'\bStage\b', r'\bTirocinio\b'
    ]
    
    skip = False
    for pattern in skip_words:
        if re.search(pattern, title, re.IGNORECASE):
            # Exception: keep Product Manager and Technical Product Manager
            if re.search(r'\b(?:Product|Technical\s+Product)\s+Manager\b', title, re.IGNORECASE):
                skip = False
            else:
                skip = True
                break
    
    if skip:
        print(f"SKIP (title): {title}", file=sys.stderr)
        continue
    
    # Skip if title contains German/Polish/French words (but Italian is OK)
    non_english = [
        r'\bEntwickler\b', r'\bSoftwareentwickler\b', r'\bIngénieur\b', 
        r'\bProgramista\b', r'\bInżynier\b'
    ]
    skip = False
    for pattern in non_english:
        if re.search(pattern, title):
            skip = True
            break
    
    if skip:
        print(f"SKIP (language): {title}", file=sys.stderr)
        continue
    
    job['url'] = f"https://www.linkedin.com/jobs/view/{job['id']}/"
    filtered.append(job)

print(json.dumps(filtered, indent=2), file=sys.stdout)
