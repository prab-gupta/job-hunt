import os
import re

def clean_slug(s):
    return re.sub(r"[^a-zA-Z0-9]", "", s)

# Using get_targets3.py logic
import csv
with open('loop/queue.csv', 'r') as f:
    reader = csv.DictReader(f)
    fde_targets = []
    for row in reader:
        if row['status'] == 'TO APPLY':
            is_easy_apply = 'EASY' in row['form_type'].upper()
            if not is_easy_apply:
                role_upper = row['role'].upper()
                lane_upper = row['lane'].upper()
                if 'FORWARD' in role_upper or 'FDE' in role_upper or 'FDE' in lane_upper:
                    fde_targets.append(row)

missing = []
found = []
for t in fde_targets:
    slug = clean_slug(t['company'])
    tex_file = f"Prabhavit_CV_{slug}.tex"
    if os.path.exists(tex_file):
        found.append(t['company'])
    else:
        missing.append(t['company'])

print(f"Found: {len(found)}")
print(f"Missing: {len(missing)}")
for m in missing:
    print(f"Missing: {m}")
