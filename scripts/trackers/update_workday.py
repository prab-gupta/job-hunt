import csv
from datetime import datetime

# Update applications.csv
new_row = ["Workday", "Software Engineer - Agentic AI & API Platform", "Submitted", "Completed via Antigravity browser agent (AI-in-the-loop)", datetime.now().strftime("%Y-%m-%d")]
with open('loop/applications.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(new_row)

# Update queue.csv
with open('loop/queue.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

for row in rows:
    if "Workday" in row[0] and "Agentic AI" in row[1]:
        row[8] = "SUBMITTED"
        row[9] = row[9] + f" | 2026-09-27 agent autonomously submitted via Workday portal"

with open('loop/queue.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("Updated Workday successfully.")
