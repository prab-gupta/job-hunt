import csv
with open("loop/queue.csv", "r") as f:
    reader = csv.DictReader(f)
    pending = [row for row in reader if row["status"] == "TO APPLY"]
    
for i, row in enumerate(pending[:5]):
    print(f"{i+1}. {row['company']} ({row['role']}): {row['url']}")
