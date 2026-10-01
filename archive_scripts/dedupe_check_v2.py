#!/usr/bin/env python3
import json
import subprocess
import sys

# Load filtered jobs
with open('filtered_jobs.json', 'r') as f:
    jobs = json.load(f)

final_leads = []

for job in jobs:
    company = job.get('company', '')
    url = job.get('url', '')
    
    # Run dedupe check
    try:
        result = subprocess.run(
            ['python3', 'loop/dedupe.py', '--check', company, url],
            capture_output=True,
            text=True,
            timeout=5,
            cwd='/Users/prab/Downloads/claud jobs'
        )
        dedupe_result = result.stdout.strip()
    except Exception as e:
        print(f"Error checking {url}: {e}", file=sys.stderr)
        dedupe_result = "ERROR"
    
    # Determine if we should keep this job
    job['dedupe'] = dedupe_result
    
    if dedupe_result.startswith("HIT URL"):
        print(f"Dropping (HIT URL): {url}", file=sys.stderr)
        continue
    elif dedupe_result == "HIT COMPANY":
        print(f"Dropping (HIT COMPANY): {company}", file=sys.stderr)
        continue
    else:
        # Keep NEW and HIT COMPANY~
        final_leads.append(job)

print(f"Final leads: {len(final_leads)}", file=sys.stderr)

# Save to file for StructuredOutput
with open('final_leads.json', 'w') as f:
    json.dump(final_leads, f, indent=2)
