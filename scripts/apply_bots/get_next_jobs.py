import csv

with open('loop/queue.csv', 'r') as f:
    reader = csv.DictReader(f)
    count = 0
    for row in reader:
        if row['status'].strip() == 'TO APPLY':
            print(f"{row['company']} | {row['role']} | ATS: {row['ats']} | Type: {row['form_type']}")
            count += 1
            if count == 5:
                break
