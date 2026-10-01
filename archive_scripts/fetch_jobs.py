#!/usr/bin/env python3
import subprocess
import json
import re
import sys
from html.parser import HTMLParser

class JobParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.jobs = []
        self.current_job = {}
        self.in_li = False
        self.in_title = False
        self.in_company = False
        self.in_location = False
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'li':
            self.in_li = True
            self.current_job = {}
        elif tag == 'div' and self.in_li:
            if 'data-entity-urn' in attrs_dict:
                match = re.search(r'urn:li:jobPosting:(\d+)', attrs_dict['data-entity-urn'])
                if match:
                    self.current_job['id'] = match.group(1)
        elif tag == 'span' and self.in_li and 'class' in attrs_dict:
            if 'base-search-card__title' in attrs_dict['class']:
                self.in_title = True
            elif 'base-search-card__subtitle' in attrs_dict['class']:
                self.in_company = True
            elif 'job-search-card__location' in attrs_dict['class']:
                self.in_location = True
    
    def handle_endtag(self, tag):
        if tag == 'li':
            self.in_li = False
            if 'id' in self.current_job:
                self.jobs.append(self.current_job)
            self.current_job = {}
        elif tag == 'span':
            self.in_title = False
            self.in_company = False
            self.in_location = False
    
    def handle_data(self, data):
        if self.in_title:
            self.current_job['title'] = data.strip()
        elif self.in_company:
            self.current_job['company'] = data.strip()
        elif self.in_location:
            self.current_job['location'] = data.strip()

def fetch_jobs(start):
    url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Implementation%20Consultant&geoId=103350119&f_TPR=r86400&start={start}"
    try:
        result = subprocess.run(['curl', '-s', '-A', 'Mozilla/5.0', url], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0 and result.stdout:
            parser = JobParser()
            parser.feed(result.stdout)
            return parser.jobs
    except Exception as e:
        print(f"Error fetching start={start}: {e}", file=sys.stderr)
    return []

all_jobs = []
for start in [0, 25, 50]:
    jobs = fetch_jobs(start)
    all_jobs.extend(jobs)
    if not jobs:
        print(f"No jobs for start={start}, retrying...", file=sys.stderr)
        import time
        time.sleep(5)
        jobs = fetch_jobs(start)
        all_jobs.extend(jobs)

# Add URLs and dedupe fields
for job in all_jobs:
    job['url'] = f"https://www.linkedin.com/jobs/view/{job['id']}/"
    job['dedupe'] = None

print(json.dumps(all_jobs, indent=2))
