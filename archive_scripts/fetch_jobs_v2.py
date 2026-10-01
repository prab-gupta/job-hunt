#!/usr/bin/env python3
import subprocess
import json
import re
import sys
import time

def fetch_jobs(start):
    url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Implementation%20Consultant&geoId=103350119&f_TPR=r86400&start={start}"
    try:
        result = subprocess.run(['curl', '-s', '-A', 'Mozilla/5.0', url], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode != 0:
            return None
        html = result.stdout
        # Check if we got HTML with job listings
        if '<li>' not in html:
            return None
        return html
    except Exception as e:
        print(f"Error fetching start={start}: {e}", file=sys.stderr)
        return None

def parse_jobs(html):
    jobs = []
    # Split by <li> tags
    li_blocks = re.split(r'<li[^>]*>', html)[1:]  # Skip before first <li>
    
    for block in li_blocks:
        job = {}
        
        # Extract job ID from data-entity-urn
        id_match = re.search(r'data-entity-urn="urn:li:jobPosting:(\d+)"', block)
        if id_match:
            job['id'] = id_match.group(1)
        else:
            continue  # Skip if no ID found
        
        # Extract title - look for base-search-card__title
        title_match = re.search(r'class="[^"]*base-search-card__title[^"]*"[^>]*>([^<]+)', block)
        if title_match:
            job['title'] = title_match.group(1).strip()
        
        # Extract company - look for base-search-card__subtitle  
        company_match = re.search(r'class="[^"]*base-search-card__subtitle[^"]*"[^>]*>([^<]+)', block)
        if company_match:
            job['company'] = company_match.group(1).strip()
        
        # Extract location - look for job-search-card__location
        location_match = re.search(r'class="[^"]*job-search-card__location[^"]*"[^>]*>([^<]+)', block)
        if location_match:
            job['location'] = location_match.group(1).strip()
        
        if 'title' in job and 'company' in job:
            job['url'] = f"https://www.linkedin.com/jobs/view/{job['id']}/"
            job['dedupe'] = None
            jobs.append(job)
    
    return jobs

all_jobs = []
for start in [0, 25, 50]:
    html = fetch_jobs(start)
    if html is None:
        print(f"No response for start={start}, retrying...", file=sys.stderr)
        time.sleep(5)
        html = fetch_jobs(start)
    
    if html:
        jobs = parse_jobs(html)
        print(f"Got {len(jobs)} jobs for start={start}", file=sys.stderr)
        all_jobs.extend(jobs)
    else:
        print(f"Failed to get jobs for start={start}", file=sys.stderr)
    
    if start < 50:
        time.sleep(1)

print(json.dumps(all_jobs, indent=2), file=sys.stdout)
