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
        if '<li>' not in html:
            return None
        return html
    except Exception as e:
        print(f"Error fetching start={start}: {e}", file=sys.stderr)
        return None

def parse_jobs(html):
    jobs = []
    li_blocks = re.split(r'<li[^>]*>', html)[1:]
    
    for block in li_blocks:
        job = {}
        
        # Extract job ID
        id_match = re.search(r'data-entity-urn="urn:li:jobPosting:(\d+)"', block)
        if id_match:
            job['id'] = id_match.group(1)
        else:
            continue
        
        # Extract title - more flexible regex
        title_match = re.search(r'base-search-card__title[^>]*>([^<]+)<', block)
        if title_match:
            job['title'] = title_match.group(1).strip()
        else:
            # Try alternative pattern
            title_match = re.search(r'class="[^"]*base-search-card__title[^"]*"\s*>([^<]+)', block)
            if title_match:
                job['title'] = title_match.group(1).strip()
        
        # Extract company - more flexible search
        company_match = re.search(r'base-search-card__subtitle[^>]*>([^<]+)<', block)
        if company_match:
            job['company'] = company_match.group(1).strip()
        else:
            # Try nested span
            company_match = re.search(r'class="[^"]*base-search-card__subtitle[^"]*"[^>]*>\s*<span[^>]*>([^<]+)', block)
            if company_match:
                job['company'] = company_match.group(1).strip()
        
        # Extract location
        location_match = re.search(r'job-search-card__location[^>]*>([^<]+)<', block)
        if location_match:
            job['location'] = location_match.group(1).strip()
        
        if 'title' in job and 'location' in job:
            job['url'] = f"https://www.linkedin.com/jobs/view/{job['id']}/"
            job['dedupe'] = None
            # Set company to company name if found, else empty string
            if 'company' not in job:
                job['company'] = ""
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
    
    if start < 50:
        time.sleep(1)

print(json.dumps(all_jobs, indent=2))
