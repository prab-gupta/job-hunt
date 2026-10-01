#!/usr/bin/env python3
import subprocess
import json
import re
import time
import sys
from bs4 import BeautifulSoup

def fetch_jobs(start):
    """Fetch jobs from LinkedIn API"""
    url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Junior%20Solutions%20Architect&geoId=103350119&f_TPR=r86400&start={start}'
    
    for attempt in range(2):
        result = subprocess.run(
            ['curl', '-s', '-A', 'Mozilla/5.0', url],
            capture_output=True,
            text=True
        )
        html = result.stdout
        
        # Check if we got valid response
        if '<li>' in html and 'data-entity-urn' in html:
            return html
        
        if attempt == 0:
            time.sleep(5)
    
    return None

def parse_jobs(html):
    """Parse job listings from HTML"""
    soup = BeautifulSoup(html, 'html.parser')
    jobs = []
    
    for li in soup.find_all('li'):
        card = li.find('div', class_='base-search-card')
        if not card:
            continue
        
        # Extract job ID
        entity_urn = card.get('data-entity-urn', '')
        match = re.search(r'urn:li:jobPosting:(\d+)', entity_urn)
        if not match:
            continue
        job_id = match.group(1)
        
        # Extract title
        title_elem = card.find('h3', class_='base-search-card__title')
        title = title_elem.get_text(strip=True) if title_elem else ''
        
        # Extract company
        company_elem = card.find('h4', class_='base-search-card__subtitle')
        company = company_elem.get_text(strip=True) if company_elem else ''
        
        # Extract location
        location_elem = card.find('span', class_='job-search-card__location')
        location = location_elem.get_text(strip=True) if location_elem else ''
        
        jobs.append({
            'id': job_id,
            'title': title,
            'company': company,
            'location': location
        })
    
    return jobs

def filter_title(title):
    """Check if title should be dropped"""
    exclude_keywords = [
        'senior', 'sr.', 'sr ', 'staff', 'principal', 'lead', 'head', 
        'director', 'manager', 'architect', 'intern', 'working student',
        'praktikum', 'werkstudent', 'stage', 'tirocinio'
    ]
    
    # Allow "Product Manager" and "Technical Product Manager"
    if 'product manager' in title.lower():
        return False
    
    title_lower = title.lower()
    for keyword in exclude_keywords:
        if keyword in title_lower:
            return True
    
    # Check for non-English words (simple heuristic)
    non_english = [
        'entwickler', 'softwareentwickler', 'ingénieur', 'programista',
        'sviluppatore'
    ]
    # Only drop if these are present AND not accompanied by English words
    # For now, be conservative and keep most
    
    return False

def dedupe_lead(company, url):
    """Run dedupe.py check"""
    try:
        result = subprocess.run(
            ['python3', 'loop/dedupe.py', '--check', company, url],
            capture_output=True,
            text=True,
            timeout=10
        )
        first_line = result.stdout.strip().split('\n')[0] if result.stdout else 'UNKNOWN'
        return first_line
    except Exception as e:
        return 'ERROR'

def main():
    all_jobs = []
    
    # Fetch all batches
    for start in [0, 25, 50]:
        print(f"Fetching batch starting at {start}...", file=sys.stderr)
        html = fetch_jobs(start)
        
        if not html:
            print(f"No data returned for start={start}", file=sys.stderr)
            continue
        
        jobs = parse_jobs(html)
        print(f"Parsed {len(jobs)} jobs from start={start}", file=sys.stderr)
        all_jobs.extend(jobs)
    
    # Filter and dedupe
    filtered_leads = []
    
    for job in all_jobs:
        if filter_title(job['title']):
            print(f"Filtered out: {job['title']}", file=sys.stderr)
            continue
        
        url = f"https://www.linkedin.com/jobs/view/{job['id']}/"
        dedupe = dedupe_lead(job['company'], url)
        
        # Drop if HIT URL or exact HIT COMPANY
        if dedupe.startswith('HIT URL') or dedupe == 'HIT COMPANY':
            print(f"Dropped (dedupe={dedupe}): {job['title']} at {job['company']}", file=sys.stderr)
            continue
        
        filtered_leads.append({
            'id': job['id'],
            'title': job['title'],
            'company': job['company'],
            'location': job['location'],
            'url': url,
            'dedupe': dedupe
        })
    
    # Output JSON
    print(json.dumps(filtered_leads, indent=2))

if __name__ == '__main__':
    main()
