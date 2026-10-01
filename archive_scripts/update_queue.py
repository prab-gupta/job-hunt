import csv

with open('loop/queue.csv', 'r') as f:
    rows = list(csv.reader(f))

for i, row in enumerate(rows):
    if row and row[0].startswith("Barden"):
        if row[8] == "TO APPLY":
            row[8] = "NEEDS YOU"
            row[9] += " | STATUS: NEEDS YOU (Playwright missing)"
            break

with open('loop/queue.csv', 'w', newline='') as f:
    csv.writer(f).writerows(rows)
