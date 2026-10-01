import csv
from datetime import datetime

queue_file = 'loop/queue.csv'
app_file = 'loop/applications.csv'

# Update queue.csv
rows = []
with open(queue_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        if row.get('status') == 'TO APPLY' and row.get('company') in ['Nebius', 'HAVI']:
            row['status'] = 'NEEDS_HUMAN'
            row['notes'] = row.get('notes', '') + ' | Hard block: MCP navigate_page hangs'
        rows.append(row)

with open(queue_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Append to applications.csv
today = datetime.now().strftime('%Y-%m-%d')
with open(app_file, 'a', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Nebius', 'Automation Engineer (Customer Service)', 'NEEDS_HUMAN', 'Hard block: MCP navigate_page hangs', today])
    writer.writerow(['HAVI', 'AI & Automation Engineer', 'NEEDS_HUMAN', 'Hard block: MCP navigate_page hangs', today])

print("Updated queue and applications.")
