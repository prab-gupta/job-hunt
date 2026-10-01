import csv

def update():
    with open('loop/queue.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)

    updates = {
        'MSD Czech Republic': 'NEEDS YOU - account',
        'NCS Group': 'NEEDS YOU - account',
        'Nadara': 'NEEDS YOU - account',
        'Mercor': 'NEEDS YOU - account',
        'MC Engineering': 'CLOSED'
    }

    for row in rows:
        company = row[0]
        if company in updates:
            # The status column is usually the 9th column (index 8)
            row[8] = updates[company]
            # Add a note to the last column (index 9)
            note = row[9] + f" | Agent hit account wall / closed on 2026-09-26"
            row[9] = note

    with open('loop/queue.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

update()
