import csv

with open('loop/queue.csv', 'r') as f:
    rows = list(csv.reader(f))

updated_count = 0
for row in rows:
    if len(row) > 9:
        if "Accenture" in row[0] and "4466268131" in row[2]:
            row[9] = row[9].replace("materials to build", "MATERIALS READY: Prabhavit_CV_AccentureDublin.tex + CoverLetter_AccentureDublin.tex")
            updated_count += 1
        elif "Carpiness" in row[0]:
            row[9] = row[9].replace("materials to build", "MATERIALS READY: Prabhavit_CV_Carpiness.tex + CoverLetter_Carpiness.tex")
            updated_count += 1

with open('loop/queue.csv', 'w', newline='') as f:
    csv.writer(f).writerows(rows)

print(f"Updated {updated_count} queue rows.")
