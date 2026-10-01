import csv

with open('loop/queue.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

updates = ['Workday', 'kausable', 'Bamboo Works', 'scandiweb', 'Capgemini']

for row in rows:
    if row[0] in updates:
        row[8] = "NEEDS YOU"
        row[9] = row[9] + f" | 2026-09-26 batch failed due to unsupported ATS edges (Workday/JazzHR/EasyApply) and Chrome CDP locks"

with open('loop/queue.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("Updated queue successfully.")
