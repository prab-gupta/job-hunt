import csv
from datetime import datetime

# Update applications.csv
new_row = ["MSD Czech Republic", "Platform AI Engineer", "Submitted", "Completed manually by user", datetime.now().strftime("%Y-%m-%d")]
with open('loop/applications.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(new_row)

# Update queue.csv
with open('loop/queue.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

for row in rows:
    if "MSD" in row[0] and "Platform AI Engineer" in row[1]:
        row[8] = "SUBMITTED"
        row[9] = row[9] + f" | 2026-09-26 user submitted manually"

with open('loop/queue.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("Updated MSD successfully.")
