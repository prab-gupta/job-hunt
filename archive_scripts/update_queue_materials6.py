import csv

with open('loop/queue.csv', 'r') as f:
    rows = list(csv.reader(f))

updated_count = 0
for row in rows:
    if len(row) > 9:
        if "Celonis" in row[0] and "Orbit" in row[1]:
            row[9] += " | MATERIALS READY: Prabhavit_CV_CelonisOrbit.tex + CoverLetter_CelonisOrbit.tex"
            updated_count += 1

with open('loop/queue.csv', 'w', newline='') as f:
    csv.writer(f).writerows(rows)

print(f"Updated {updated_count} queue rows.")
