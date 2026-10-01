import csv

applications = []
with open("loop/applications.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 3:
            applications.append(row)

queue_pending = 0
with open("loop/queue.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["status"] == "TO APPLY":
            queue_pending += 1

submitted = [a for a in applications if "Submitted" in a or "SUBMITTED" in a]
closed = [a for a in applications if "CLOSED" in a]
needs_human = [a for a in applications if "NEEDS_HUMAN" in a]

print(f"Total Applications Tracked: {len(applications)}")
print(f"Successfully Submitted: {len(submitted)}")
print(f"Closed / Unavailable: {len(closed)}")
print(f"Needs Human Intervention (CAPTCHA etc.): {len(needs_human)}")
print(f"Remaining in Queue to apply later: {queue_pending}")

print("\n--- NEEDS HUMAN (Action Required) ---")
for a in needs_human:
    print(f"- {a[0]} ({a[1]}): {a[-1]}")

print("\n--- CLOSED / SKIPPED ---")
for a in closed:
    print(f"- {a[0]} ({a[1]}): {a[-1]}")

print("\n--- RECENTLY SUBMITTED (Last 15) ---")
for a in submitted[-15:]:
    print(f"- {a[0]} ({a[1]})")
