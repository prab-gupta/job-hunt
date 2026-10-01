import subprocess
import json
import csv
import re
import os

applied_companies = set()
applied_urls = set()

# Load data/csvs/applications.csv
if os.path.exists("data/csvs/applications.csv"):
    with open("data/csvs/applications.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 4:
                applied_companies.add(row[1].strip().lower())
                applied_urls.add(row[4].strip().lower())

# Load loop/applications.csv
if os.path.exists("loop/applications.csv"):
    with open("loop/applications.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 2:
                applied_companies.add(row[0].strip().lower())
                applied_urls.add(row[2].strip().lower())

# Load loop/queue.csv
if os.path.exists("loop/queue.csv"):
    with open("loop/queue.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("status") in ["SUBMITTED", "DROPPED", "KILLED", "SKIPPED", "NEEDS_HUMAN", "NEEDS HUMAN"]:
                applied_companies.add(row.get("company", "").strip().lower())
                applied_urls.add(row.get("url", "").strip().lower())

def run_cmd(cmd):
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        if res.returncode == 0:
            return json.loads(res.stdout)
        else:
            return None
    except Exception as e:
        return None

candidates = []

# 1. LinkedIn Search
linkedin_queries = [
    'bun run .agents/skills/linkedin-search/cli/src/cli.ts search -q "Automation Engineer" -l "Remote" --jobage 7 --limit 15',
    'bun run .agents/skills/linkedin-search/cli/src/cli.ts search -q "Integration Engineer" -l "Remote" --jobage 7 --limit 15',
    'bun run .agents/skills/linkedin-search/cli/src/cli.ts search -q "AI Automation" -l "Remote" --jobage 14 --limit 15',
    'bun run .agents/skills/linkedin-search/cli/src/cli.ts search -q "Automation Engineer" -l "Italy" --jobage 14 --limit 15',
    'bun run .agents/skills/linkedin-search/cli/src/cli.ts search -q "Automation Engineer" -l "Netherlands" --jobage 7 --limit 10',
    'bun run .agents/skills/linkedin-search/cli/src/cli.ts search -q "Automation Engineer" -l "Germany" --jobage 7 --limit 10'
]

for cmd in linkedin_queries:
    data = run_cmd(cmd)
    if data and "results" in data:
        for item in data["results"]:
            url = item.get("url", "")
            comp = item.get("company", "")
            title = item.get("title", "")
            loc = item.get("location", "")
            candidates.append({
                "portal": "linkedin",
                "title": title,
                "company": comp,
                "location": loc,
                "url": url
            })

# 2. Freehire Search
freehire_queries = [
    'bun run .agents/skills/freehire-search/cli/src/cli.ts search -q "automation engineer" --region europe --limit 15',
    'bun run .agents/skills/freehire-search/cli/src/cli.ts search -q "integration engineer" --region europe --limit 15',
    'bun run .agents/skills/freehire-search/cli/src/cli.ts search -q "solutions engineer" --region europe --limit 15',
    'bun run .agents/skills/freehire-search/cli/src/cli.ts search -q "n8n" --region europe --limit 10'
]

for cmd in freehire_queries:
    data = run_cmd(cmd)
    if data and "results" in data:
        for item in data["results"]:
            candidates.append({
                "portal": "freehire",
                "title": item.get("title", ""),
                "company": item.get("company", ""),
                "location": str(item.get("work_mode") or "") + " " + ",".join(item.get("regions") or []),
                "url": item.get("url", "")
            })

# 3. Danish Jobindex
data = run_cmd('bun run .agents/skills/jobindex-search/cli/src/cli.ts search -q "automation engineer" --limit 10')
if data and "results" in data:
    for item in data["results"]:
        candidates.append({
            "portal": "jobindex",
            "title": item.get("title", ""),
            "company": item.get("company", ""),
            "location": item.get("location", "Denmark"),
            "url": item.get("url", "")
        })

# Deduplicate
unique_candidates = []
seen = set()

for c in candidates:
    u = c["url"].lower().strip()
    co = c["company"].lower().strip()
    # Normalize linkedin URL by job ID
    m = re.search(r'view/.*?(\d{8,})', u)
    key = m.group(1) if m else u

    if not key or key in seen:
        continue
    if u in applied_urls or any(u in x for x in applied_urls):
        continue
    if co in applied_companies:
        continue

    seen.add(key)
    unique_candidates.append(c)

print(f"Total found: {len(candidates)} | Unique unapplied candidates: {len(unique_candidates)}")
with open("scratch/search_results.json", "w", encoding="utf-8") as f:
    json.dump(unique_candidates, f, indent=2)

for i, c in enumerate(unique_candidates[:15]):
    print(f"[{i+1}] {c['portal'].upper()} | {c['company']} | {c['title']} | {c['location']} | {c['url']}")
