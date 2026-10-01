import csv

with open('loop/queue.csv', 'r') as f:
    reader = csv.DictReader(f)
    targets = []
    for row in reader:
        if row['status'] == 'TO APPLY':
            # Identify if it's offsite (not LinkedIn Easy Apply) and if it's FDE or something? 
            # FDE can mean lane contains 'FDE' or title contains 'Forward Deployed' or maybe all offsite targets are needed.
            # Let's print out the company, role, ats, form_type, lane for all TO APPLY
            targets.append(row)

offsite_fde = []
for t in targets:
    if 'EASY_APPLY' not in t['form_type']:
        offsite_fde.append(t)

print(f"Total TO APPLY: {len(targets)}")
print(f"Total Offsite (not Easy Apply): {len(offsite_fde)}")
for t in offsite_fde:
    print(f"- {t['company']}: {t['role']} | Form: {t['form_type']} | ATS: {t['ats']}")
