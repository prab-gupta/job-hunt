import csv

with open('loop/queue.csv', 'r') as f:
    reader = csv.DictReader(f)
    offsite_fde = []
    for row in reader:
        if row['status'] == 'TO APPLY':
            # Not easy apply
            if 'EASY' not in row['form_type'].upper() and 'LINKEDIN_EASY' not in row['form_type'].upper() and 'EASY_APPLY' not in row['form_type'].upper():
                offsite_fde.append(row)

print(f"Total Offsite (not Easy Apply) FDE targets?: {len(offsite_fde)}")
for t in offsite_fde:
    print(f"- {t['company']}: {t['role']}")
