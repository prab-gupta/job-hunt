import csv
from datetime import datetime

# Update applications.csv
new_row = ["Bamboo Works", "AI Automation Specialist", "Submitted", "Completed via AI-in-the-loop apply.mjs", datetime.now().strftime("%Y-%m-%d")]
with open('loop/applications.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(new_row)

# Update queue.csv
with open('loop/queue.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

for row in rows:
    if "Bamboo Works" in row[0]:
        row[8] = "SUBMITTED"
        row[9] = row[9] + f" | 2026-09-27 agent launched apply.mjs, user resolved NEEDS HUMAN"

with open('loop/queue.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("Updated Bamboo Works successfully.")
