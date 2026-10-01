import csv

jobs = []
with open("loop/applications.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 8 and "NEEDS_HUMAN" in row[8].upper():
            # Company, Role, URL, Wall Reason
            jobs.append((row[0], row[1], row[2], row[9]))

for i, job in enumerate(jobs[:5]):
    print(f"{i+1}. {job[0]} - {job[1]}")
    print(f"   URL: {job[2]}")
    print(f"   Block: {job[3]}")
    print(f"   CV: /Users/prab/Downloads/claud jobs/cv/main_{job[0].replace(' ', '').replace(',', '')}_FDE.pdf")
    print(f"   CL: /Users/prab/Downloads/claud jobs/cover_letters/cover_{job[0].replace(' ', '').replace(',', '')}_FDE.pdf\n")
