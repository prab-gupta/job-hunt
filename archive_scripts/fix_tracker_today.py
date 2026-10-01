import csv

with open('applications.csv', 'r') as f:
    rows = list(csv.reader(f))

# Remove rows from today (2026-09-19) that were logged during the guest browser staging pass
cleaned_rows = [rows[0]]
removed = 0
for r in rows[1:]:
    if len(r) > 0 and r[0] == "2026-09-19":
        removed += 1
        continue
    cleaned_rows.append(r)

with open('applications.csv', 'w', newline='') as f:
    csv.writer(f).writerows(cleaned_rows)

print(f"Removed {removed} unsubmitted guest-browser rows from applications.csv. Total rows now: {len(cleaned_rows)}")
