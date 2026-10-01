import subprocess
import json
import csv
import os

queries = [
    {"q": "Forward Deployed Engineer", "l": "Worldwide", "r": "remote"},
    {"q": "AI Engineer", "l": "Worldwide", "r": "remote"},
    {"q": "Forward Deployed Engineer", "l": "Italy", "r": ""},
]

jobs_found = []

for q in queries:
    print(f"Searching for {q['q']} in {q['l']} (remote={q['r']})...")
    cmd = [
        "bun", "run", ".agents/skills/linkedin-search/cli/src/cli.ts", "search",
        "-q", q["q"],
        "-l", q["l"],
        "--jobage", "7",
        "--format", "json",
        "--limit", "30"
    ]
    if q['r']:
        cmd.extend(["--remote", q['r']])
        
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        continue
        
    try:
        data = json.loads(result.stdout)
        results = data.get("results", [])
        print(f"Found {len(results)} jobs.")
        for r in results:
            jobs_found.append(r)
    except Exception as e:
        print(f"Parse error: {e}")

# Read existing queue to prevent exact duplicates by URL
existing_urls = set()
if os.path.exists("loop/queue.csv"):
    with open("loop/queue.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            existing_urls.add(row.get("url", ""))

new_jobs = []
for j in jobs_found:
    if j["url"] not in existing_urls:
        new_jobs.append(j)
        existing_urls.add(j["url"])

if new_jobs:
    print(f"Adding {len(new_jobs)} new jobs to queue.csv")
    with open("loop/queue.csv", "a", newline="") as f:
        writer = csv.writer(f)
        for j in new_jobs:
            writer.writerow([
                j["company"],
                j["title"],
                j["url"],
                "LinkedIn",
                "FDE", # or whatever
                "",
                j["date"],
                "CV+CL",
                "TO APPLY"
            ])
else:
    print("No new jobs found.")
