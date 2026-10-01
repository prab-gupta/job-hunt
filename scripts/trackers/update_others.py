import csv

with open('loop/queue.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

updates = ['NCS Group', 'Nadara', 'Mercor']

for row in rows:
    if row[0] in updates:
        row[8] = "NEEDS YOU - account"
        row[9] = row[9] + f" | 2026-09-26 agent failed to automate account creation due to shadow-root/devtools locks"

with open('loop/queue.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("Updated queue successfully.")
