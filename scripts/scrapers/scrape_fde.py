import re
import csv
import os

with open('/Users/prab/.gemini/antigravity/brain/ef77eada-777c-44ce-be2a-d6a8b4c47c87/.system_generated/steps/15526/content.md', 'r') as f:
    html = f.read()

# find all job links like href="/jobs/..."
# <a href="/jobs/gumloop-forward-deployed-agentic-engineer-38f75b/" class="job-item"
#           data-title="forward deployed agentic engineer"
#           data-company="gumloop"
matches = re.finditer(r'<a href="(/jobs/[^"]+)" class="job-item"[^>]*data-title="([^"]+)"[^>]*data-company="([^"]+)"', html, re.IGNORECASE)

existing_urls = set()
if os.path.exists("loop/queue.csv"):
    with open("loop/queue.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            existing_urls.add(row.get("url", ""))

new_jobs = []
for m in matches:
    path = m.group(1)
    title = m.group(2).title()
    company = m.group(3).title()
    url = f"https://fdepulse.com{path}"
    
    if url not in existing_urls:
        new_jobs.append((company, title, url))
        existing_urls.add(url)

if new_jobs:
    print(f"Adding {len(new_jobs)} new jobs to queue.csv")
    with open("loop/queue.csv", "a", newline="") as f:
        writer = csv.writer(f)
        for company, title, url in new_jobs:
            writer.writerow([
                company,
                title,
                url,
                "FDEPulse",
                "FDE", 
                "",
                "2026-09-29",
                "CV+CL",
                "TO APPLY"
            ])
else:
    print("No new jobs found.")
