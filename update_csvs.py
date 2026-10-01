import csv
import sys
from datetime import datetime

date_today = datetime.now().strftime('%Y-%m-%d')

jobs = [
    {
        'company': 'Zurich Insurance',
        'role': 'AI & Process Automation Engineer (Agents, Automation & Digitalisation)',
        'ats': 'LinkedIn',
        'url': 'https://www.linkedin.com/jobs/view/4435258633/',
        'status': 'NEEDS_HUMAN',
        'confirmation': 'Requires LinkedIn login'
    },
    {
        'company': 'Greenvolt Group',
        'role': 'AI & Automation Developer',
        'ats': 'LinkedIn',
        'url': 'https://www.linkedin.com/jobs/view/4469757144/',
        'status': 'NEEDS_HUMAN',
        'confirmation': 'Requires LinkedIn login'
    }
]

# Update applications.csv
with open('data/csvs/applications.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for j in jobs:
        writer.writerow([
            date_today,
            j['company'],
            j['role'],
            j['ats'],
            j['url'],
            j['status'],
            j['confirmation'],
            '',
            'yes',
            ''
        ])

# Update loop/queue.csv
queue_rows = []
with open('loop/queue.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)
    queue_rows.append(headers)
    for row in reader:
        # url is index 2 usually
        if len(row) > 2:
            url = row[2]
            if url == 'https://www.linkedin.com/jobs/view/4435258633/' or url == 'https://www.linkedin.com/jobs/view/4469757144/':
                # find status index.
                status_idx = headers.index('status')
                row[status_idx] = 'NEEDS_HUMAN'
        queue_rows.append(row)

with open('loop/queue.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(queue_rows)

print("Updated CSVs successfully.")
