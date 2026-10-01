import csv
from datetime import datetime

date_str = datetime.now().strftime("%Y-%m-%d")

# Jobs to update
urls_to_update = {
    "https://fdepulse.com/jobs/id-me-manager-forward-deployed-engineering-57ba42/": ("Id.Me", "Manager, Forward Deployed Engineering"),
    "https://fdepulse.com/jobs/nice-forward-deployed-engineer-03e36f/": ("Nice", "Forward Deployed Engineer")
}

# Update queue.csv
rows = []
with open('loop/queue.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows.append(header)
    for row in reader:
        url = row[2]
        if url in urls_to_update and row[8] == 'TO APPLY':
            row[8] = 'EXTERNAL'
            row[9] = 'Redirects to Indeed'
        rows.append(row)

with open('loop/queue.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Append to applications.csv
with open('loop/applications.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for url, (company, role) in urls_to_update.items():
        writer.writerow([company, role, 'EXTERNAL', 'Redirects to Indeed', date_str])

