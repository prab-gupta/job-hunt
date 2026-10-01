import csv

with open('loop/queue.csv', 'r') as f:
    reader = csv.DictReader(f)
    fde_targets = []
    for row in reader:
        if row['status'] == 'TO APPLY':
            is_easy_apply = 'EASY' in row['form_type'].upper()
            if not is_easy_apply:
                # Check if it's an FDE target
                role_upper = row['role'].upper()
                lane_upper = row['lane'].upper()
                if 'FORWARD' in role_upper or 'FDE' in role_upper or 'FDE' in lane_upper:
                    fde_targets.append(row)

print(f"Total Offsite FDE targets: {len(fde_targets)}")
for t in fde_targets:
    print(f"- {t['company']}: {t['role']}")
