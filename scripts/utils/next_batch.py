import csv
with open("loop/queue.csv", "r") as f:
    reader = csv.DictReader(f)
    pending = [row for row in reader if row["status"] == "TO APPLY"]
    
for row in pending[:5]:
    print(f"- {row['company']}: {row['role']}")
