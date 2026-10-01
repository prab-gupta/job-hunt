import csv

# read applications
apps = set()
with open("loop/applications.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 0:
            apps.add(row[0].strip().lower()) # add company name

# update queue
rows = []
with open("loop/queue.csv", "r") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        if row["status"] == "TO APPLY" and row["company"].strip().lower() in apps:
            row["status"] = "SUBMITTED" # or skipped, doesn't matter for the queue
        rows.append(row)

with open("loop/queue.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
