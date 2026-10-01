#!/usr/bin/env python3
import subprocess
import json
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urljoin
import time

class JobParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.jobs = []
        self.in_li = False
        self.current_job = {}
        self.in_title = False
        self.in_subtitle = False
        self.in_location = False
        self.entity_urn = None
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        if tag == 'li':
            self.in_li = True
            self.current_job = {}
            
        elif tag == 'div' and self.in_li:
            if 'data-entity-urn' in attrs_dict:
                urn = attrs_dict['data-entity-urn']
                if 'jobPosting:' in urn:
                    match = re.search(r'jobPosting:(\d+)', urn)
                    if match:
                        self.current_job['id'] = match.group(1)
                        
        elif tag == 'h3' and self.in_li and 'base-search-card__title' in attrs_dict.get('class', ''):
            self.in_title = True
            
        elif tag == 'h4' and self.in_li and 'base-search-card__subtitle' in attrs_dict.get('class', ''):
            self.in_subtitle = True
            
        elif tag == 'span' and self.in_li and 'job-search-card__location' in attrs_dict.get('class', ''):
            self.in_location = True
    
    def handle_endtag(self, tag):
        if tag == 'li' and self.in_li:
            if 'id' in self.current_job and 'title' in self.current_job:
                self.jobs.append(self.current_job)
            self.in_li = False
            self.current_job = {}
            
        elif tag == 'h3' and self.in_title:
            self.in_title = False
            
        elif tag == 'h4' and self.in_subtitle:
            self.in_subtitle = False
            
        elif tag == 'span' and self.in_location:
            self.in_location = False
    
    def handle_data(self, data):
        data = data.strip()
        if not data:
            return
            
        if self.in_title and 'title' not in self.current_job:
            self.current_job['title'] = data
            
        elif self.in_subtitle and 'company' not in self.current_job:
            self.current_job['company'] = data
            
        elif self.in_location and 'location' not in self.current_job:
            self.current_job['location'] = data

def fetch_page(start):
    url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=AI%20Product%20Manager&geoId=91000002&f_TPR=r86400&start={start}"
    try:
        result = subprocess.run(
            ['curl', '-s', '-A', 'Mozilla/5.0', url],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout
    except Exception as e:
        print(f"Error fetching page {start}: {e}", file=sys.stderr)
        return ""

def filter_title(title):
    """Check if title should be dropped based on criteria"""
    # Drop titles with these patterns (but allow Product Manager / Technical Product Manager)
    drop_patterns = [
        r'(?i)\bSenior\b(?!\s+Product\s+Manager)',
        r'(?i)\bSr\.',
        r'(?i)\bStaff\b',
        r'(?i)\bPrincipal\b',
        r'(?i)\bLead\b(?!\s+Product)',
        r'(?i)\bHead\b',
        r'(?i)\bDirector\b',
        r'(?i)\bManager\b(?!\s+Product)',
        r'(?i)\bArchitect\b',
        r'(?i)\bIntern\b',
        r'(?i)\bWorking\s+Student\b',
        r'(?i)\bPraktikum\b',
        r'(?i)\bWerkstudent\b',
        r'(?i)\bStage\b',
        r'(?i)\bTirocinio\b',
    ]
    
    for pattern in drop_patterns:
        if re.search(pattern, title):
            return False
    
    # Check for non-English words
    non_english_words = [
        r'\bEntwickler\b',
        r'\bSoftwareentwickler\b',
        r'\bIngénieur\b',
        r'\bProgramista\b',
        r'\bSviluppatore\b',
    ]
    
    for word in non_english_words:
        if re.search(word, title):
            return False
    
    return True

def dedupe_lead(company, url):
    """Run dedupe.py and return the result"""
    try:
        result = subprocess.run(
            ['python3', 'loop/dedupe.py', '--check', company, url],
            capture_output=True,
            text=True,
            timeout=10,
            cwd='/Users/prab/Downloads/claud jobs'
        )
        lines = result.stdout.strip().split('\n')
        return lines[0] if lines else "UNKNOWN"
    except Exception as e:
        print(f"Error running dedupe for {company} {url}: {e}", file=sys.stderr)
        return "ERROR"

def main():
    all_jobs = []
    
    for start in [0, 25, 50]:
        print(f"Fetching page with start={start}...", file=sys.stderr)
        html = fetch_page(start)
        
        if not html or '<li>' not in html:
            print(f"No results or rate limited at start={start}, retrying...", file=sys.stderr)
            time.sleep(5)
            html = fetch_page(start)
            
            if not html or '<li>' not in html:
                print(f"Still no results at start={start}, skipping.", file=sys.stderr)
                continue
        
        parser = JobParser()
        try:
            parser.feed(html)
            all_jobs.extend(parser.jobs)
            print(f"Found {len(parser.jobs)} jobs at start={start}", file=sys.stderr)
        except Exception as e:
            print(f"Error parsing page {start}: {e}", file=sys.stderr)
    
    print(f"Total jobs found: {len(all_jobs)}", file=sys.stderr)
    
    # Filter by title
    filtered_jobs = []
    for job in all_jobs:
        if filter_title(job.get('title', '')):
            filtered_jobs.append(job)
    
    print(f"After title filter: {len(filtered_jobs)}", file=sys.stderr)
    
    # Run dedupe and build final list
    leads = []
    for job in filtered_jobs:
        job_id = job['id']
        title = job['title']
        company = job['company']
        location = job.get('location', '')
        url = f"https://www.linkedin.com/jobs/view/{job_id}/"
        
        print(f"Checking dedupe: {company} {url}", file=sys.stderr)
        dedupe = dedupe_lead(company, url)
        
        # Filter based on dedupe result
        if dedupe.startswith("HIT URL"):
            print(f"  Skipping: HIT URL", file=sys.stderr)
            continue
        elif dedupe == "HIT COMPANY":
            print(f"  Skipping: HIT COMPANY", file=sys.stderr)
            continue
        
        # Keep: NEW or HIT COMPANY~
        print(f"  Keeping: {dedupe}", file=sys.stderr)
        leads.append({
            "id": job_id,
            "title": title,
            "company": company,
            "location": location,
            "url": url,
            "dedupe": dedupe
        })
    
    print(f"Final leads: {len(leads)}", file=sys.stderr)
    return leads

if __name__ == '__main__':
    leads = main()
    print(json.dumps(leads, indent=2))
