#!/usr/bin/env python3
import subprocess
import json
import re
import sys
from html.parser import HTMLParser

# Titles to drop
drop_title_keywords = [
    'Senior', 'Sr.', 'Sr ', 'Staff', 'Principal', 'Lead', 'Head', 'Director', 'Manager',
    'Architect', 'Intern', 'Working Student', 'Praktikum', 'Werkstudent', 'Stage', 'Tirocinio'
]

# Keep these even if they contain "Manager"
keep_patterns = ['Product Manager', 'Technical Product Manager']

# Non-English indicators (German, Polish, French words)
non_english_keywords = [
    'Entwickler', 'Softwareentwickler', 'Ingénieur', 'Programista',
    'Développeur', 'Ingenieur', 'Ingeniero', 'Développeuse'
]

class JobParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.jobs = []
        self.current_job = {}
        self.in_title = False
        self.in_company = False
        self.in_location = False
        self.in_li = False
        self.in_base_search_card = False
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        if tag == 'li':
            self.in_li = True
            self.current_job = {}
            
        if tag == 'div' and self.in_li:
            class_attr = attrs_dict.get('class', '')
            if 'base-search-card' in class_attr and 'data-entity-urn' in attrs_dict:
                # Extract job ID from data-entity-urn
                entity_urn = attrs_dict.get('data-entity-urn', '')
                match = re.search(r'urn:li:jobPosting:(\d+)', entity_urn)
                if match:
                    self.current_job['id'] = match.group(1)
                    self.in_base_search_card = True
                    
        if tag == 'h3' and self.in_li:
            if 'base-search-card__title' in attrs_dict.get('class', ''):
                self.in_title = True
                
        if tag == 'h4' and self.in_li:
            if 'base-search-card__subtitle' in attrs_dict.get('class', ''):
                self.in_company = True
                
        if tag == 'span' and self.in_li:
            if 'job-search-card__location' in attrs_dict.get('class', ''):
                self.in_location = True
    
    def handle_data(self, data):
        data = data.strip()
        if not data:
            return
            
        if self.in_title:
            if 'title' not in self.current_job:
                self.current_job['title'] = data
            
        elif self.in_company:
            if 'company' not in self.current_job:
                self.current_job['company'] = data
            
        elif self.in_location:
            if 'location' not in self.current_job:
                self.current_job['location'] = data
    
    def handle_endtag(self, tag):
        if tag == 'h3' and self.in_title:
            self.in_title = False
        elif tag == 'h4' and self.in_company:
            self.in_company = False
        elif tag == 'span' and self.in_location:
            self.in_location = False
        elif tag == 'li' and self.in_li:
            if 'id' in self.current_job and 'title' in self.current_job:
                self.jobs.append(self.current_job)
            self.in_li = False
            self.in_base_search_card = False
            self.current_job = {}

def should_drop_title(title):
    # Check for keep patterns first
    for pattern in keep_patterns:
        if pattern in title:
            return False
    
    # Check for drop keywords
    for keyword in drop_title_keywords:
        if keyword in title:
            return True
    
    # Check for non-English words
    for keyword in non_english_keywords:
        if keyword in title:
            return True
    
    return False

def fetch_jobs(start):
    url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Workflow%20Automation&geoId=103350119&f_TPR=r86400&start={start}'
    try:
        result = subprocess.run(
            ['curl', '-s', '-A', 'Mozilla/5.0', url],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if not result.stdout or '<li>' not in result.stdout:
            return None
        
        parser = JobParser()
        parser.feed(result.stdout)
        return parser.jobs
    except Exception as e:
        print(f"Error fetching start={start}: {e}", file=sys.stderr)
        return None

# Fetch all pages
all_jobs = []
for start in [0, 25, 50]:
    jobs = fetch_jobs(start)
    if jobs:
        all_jobs.extend(jobs)
    else:
        print(f"Empty result at start={start}, retrying...", file=sys.stderr)
        import time
        time.sleep(5)
        jobs = fetch_jobs(start)
        if jobs:
            all_jobs.extend(jobs)

# Dedupe by ID first
seen_ids = set()
unique_jobs = []
for job in all_jobs:
    if job['id'] not in seen_ids:
        seen_ids.add(job['id'])
        unique_jobs.append(job)

# Filter jobs
filtered_jobs = []
for job in unique_jobs:
    if should_drop_title(job.get('title', '')):
        continue
    
    job['url'] = f"https://www.linkedin.com/jobs/view/{job['id']}/"
    filtered_jobs.append(job)

# Dedupe with dedupe.py
kept_jobs = []
for job in filtered_jobs:
    company = job.get('company', 'UNKNOWN')
    result = subprocess.run(
        ['python3', 'loop/dedupe.py', '--check', company, job['url']],
        capture_output=True,
        text=True,
        cwd='/Users/prab/Downloads/claud jobs'
    )
    
    dedupe_status = result.stdout.strip().split('\n')[0] if result.stdout else 'UNKNOWN'
    job['dedupe'] = dedupe_status
    
    # Keep NEW and HIT COMPANY~ (fuzzy)
    if dedupe_status == 'NEW' or dedupe_status.startswith('HIT COMPANY~'):
        kept_jobs.append(job)

# Output as JSON
for job in kept_jobs:
    print(json.dumps(job))
