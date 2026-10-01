import csv
import datetime

updates = {
    "topdesk": {"status": "INTERVIEWING", "note": "On-site interview scheduled (Aug 24)"},
    "veeva": {"status": "INTERVIEWING", "note": "Next Steps email received (Aug 21)"},
    "clera": {"status": "INTERVIEWING", "note": "Got your application for Full Stack Engineer (Aug 23)"},
    "lucid": {"status": "REJECTED", "note": "Update about your application (Aug 24)"},
    "meticulous": {"status": "REJECTED", "note": "Meticulous Application Update (Aug 21)"},
    "viktor": {"status": "REJECTED", "note": "Application update from Steven Smith (Aug 22)"},
    "crossover": {"status": "ACTION_REQUIRED", "note": "Application about to expire (Aug 23)"},
    "leadtech": {"status": "ACTION_REQUIRED", "note": "Complete the application (Aug 21)"},
    "essilorluxottica": {"status": "ACTION_REQUIRED", "note": "Request to complete application (Aug 22)"}
}

rows = []
with open('applications.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows.append(header)
    for row in reader:
        if len(row) < 10:
            row.extend([''] * (10 - len(row)))
        
        company = row[1].lower().strip()
        
        for key, update_data in updates.items():
            if key in company:
                row[5] = update_data["status"]
                
                # Append note with date
                existing_notes = row[9]
                new_note = f"[{datetime.date.today()}] {update_data['note']}"
                if new_note not in existing_notes:
                    if existing_notes:
                        row[9] = f"{existing_notes} | {new_note}"
                    else:
                        row[9] = new_note
                break
        rows.append(row)

with open('applications.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("Tracker updated successfully!")
