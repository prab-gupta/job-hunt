import csv

with open('loop/queue.csv', 'r') as f:
    rows = list(csv.reader(f))

updated_count = 0
for row in rows:
    if len(row) > 9:
        if "haddock" in row[0]:
            row[9] += " | MATERIALS READY: Prabhavit_CV_Haddock.tex + CoverLetter_Haddock.tex"
            updated_count += 1

with open('loop/queue.csv', 'w', newline='') as f:
    csv.writer(f).writerows(rows)

print(f"Updated {updated_count} queue rows.")
