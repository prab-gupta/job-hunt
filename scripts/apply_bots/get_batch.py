import csv
import json

jobs = []
with open("loop/queue.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["status"] == "TO APPLY":
            jobs.append(row)
            if len(jobs) == 5:
                break

print(json.dumps(jobs, indent=2))
