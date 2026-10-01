import csv

with open('loop/queue.csv', 'r') as f:
    rows = list(csv.reader(f))

updated_count = 0
for row in rows:
    if len(row) > 9:
        if "Luxoft" in row[0]:
            row[9] = row[9].replace("materials to build", "MATERIALS READY: Prabhavit_CV_Luxoft.tex + CoverLetter_Luxoft.tex")
            updated_count += 1
        elif "Bertrandt" in row[0]:
            row[9] = row[9].replace("materials to build", "MATERIALS READY: Prabhavit_CV_Bertrandt.tex + CoverLetter_Bertrandt.tex")
            updated_count += 1
        elif "Inetum" in row[0] and "4468643689" in row[2]:
            row[9] = row[9].replace("materials to build", "MATERIALS READY: Prabhavit_CV_InetumDataEng.tex + CoverLetter_InetumDataEng.tex")
            updated_count += 1

with open('loop/queue.csv', 'w', newline='') as f:
    csv.writer(f).writerows(rows)

print(f"Updated {updated_count} queue rows.")
