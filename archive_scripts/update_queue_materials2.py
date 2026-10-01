import csv

with open('loop/queue.csv', 'r') as f:
    rows = list(csv.reader(f))

updated_count = 0
for row in rows:
    if len(row) > 9:
        if "Arke" in row[0]:
            row[9] += " | MATERIALS READY: Prabhavit_CV_Arke.tex + CoverLetter_Arke.tex"
            updated_count += 1
        elif "MarvelX" in row[0]:
            row[9] += " | MATERIALS READY: Prabhavit_CV_MarvelX.tex + CoverLetter_MarvelX.tex"
            updated_count += 1
        elif "Joppy" in row[0] and "4467832927" in row[2]:
            row[9] += " | MATERIALS READY: Prabhavit_CV_JoppyFDE.tex + CoverLetter_JoppyFDE.tex"
            updated_count += 1

with open('loop/queue.csv', 'w', newline='') as f:
    csv.writer(f).writerows(rows)

print(f"Updated {updated_count} queue rows.")
