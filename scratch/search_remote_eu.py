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

# LinkedIn Search: Remote Europe
linkedin_queries = [
    'bun run .agents/skills/linkedin-search/cli/src/cli.ts search -q "Automation Engineer" -l "European Union" --remote remote --jobage 7 --limit 20',
    'bun run .agents/skills/linkedin-search/cli/src/cli.ts search -q "Integration Engineer" -l "European Union" --remote remote --jobage 7 --limit 20',
    'bun run .agents/skills/linkedin-search/cli/src/cli.ts search -q "Automation Engineer" -l "Europe" --remote remote --jobage 7 --limit 20',
    'bun run .agents/skills/linkedin-search/cli/src/cli.ts search -q "Integration Engineer" -l "Europe" --remote remote --jobage 7 --limit 20',
    'bun run .agents/skills/linkedin-search/cli/src/cli.ts search -q "AI Automation" -l "Europe" --jobage 14 --limit 20',
    'bun run .agents/skills/linkedin-search/cli/src/cli.ts search -q "Solutions Engineer" -l "Europe" --remote remote --jobage 7 --limit 20'
]

for cmd in linkedin_queries:
    data = run_cmd(cmd)
    if data and "results" in data:
        for item in data["results"]:
            candidates.append({
                "portal": "linkedin",
                "title": item.get("title", ""),
                "company": item.get("company", ""),
                "location": item.get("location", ""),
                "url": item.get("url", "")
            })

# Freehire Search: Europe Remote
freehire_queries = [
    'bun run .agents/skills/freehire-search/cli/src/cli.ts search -q "automation engineer" --region europe --limit 25',
    'bun run .agents/skills/freehire-search/cli/src/cli.ts search -q "integration engineer" --region europe --limit 25',
    'bun run .agents/skills/freehire-search/cli/src/cli.ts search -q "solutions engineer" --region europe --limit 25',
    'bun run .agents/skills/freehire-search/cli/src/cli.ts search -q "n8n" --region europe --limit 25'
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

# Deduplicate
unique_candidates = []
seen = set()

neg_keywords = [
    "plc", "siemens", "scada", "geoscada", "industrial", "robotics", "mechanical", "electrical",
    "hardware", "building automation", "bacnet", "hvac", "colombia", "mexico", "india", "vietnam",
    "australia", "singapore", "bogota", "querétaro", "pune", "sydney", "ho chi minh", "san antonio",
    "seattle", "greater seattle", "minneapolis", "ingénieur", "ingénieure", "automaticien", "stage", "alternance"
]

for c in candidates:
    u = (c.get("url") or "").lower().strip()
    co = (c.get("company") or "").lower().strip()
    title = (c.get("title") or "").lower()
    full_text = f"{title} {co} {c.get('location', '').lower()} {u}"
    
    if any(k in full_text for k in neg_keywords):
        continue

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

print(f"Total raw: {len(candidates)} | Valid Remote EU leads: {len(unique_candidates)}")
with open("scratch/remote_eu_leads.json", "w", encoding="utf-8") as f:
    json.dump(unique_candidates, f, indent=2)

for i, c in enumerate(unique_candidates[:20]):
    print(f"[{i+1}] {c['portal'].upper()} | {c['company']} | {c['title']} | {c['location']}")
    print(f"     URL: {c['url']}")
