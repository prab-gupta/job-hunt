import csv

with open('loop/queue.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    jobs = []
    for row in reader:
        if row['status'] == 'TO APPLY':
            ats = row['ats'].lower()
            url = row['url'].lower()
            if 'indeed' not in ats and 'fdepulse' not in ats and 'indeed' not in url and 'fdepulse' not in url:
                jobs.append(row)
            if len(jobs) == 2:
                break

for j in jobs:
    print(f"{j['company']} | {j['role']} | {j['ats']} | {j['url']}")
