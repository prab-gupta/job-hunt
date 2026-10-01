import csv
import datetime

today = datetime.date.today().isoformat()

# Updates based on the Gmail scan from tonight
updates = {
    # INTERVIEWS - active pipeline
    "lexroom": {"status": "INTERVIEWING", "note": f"[{today}] Round 2 live coding interview scheduled Mon Sep 21 15:15-16:00 (Gloria Tortorelli)"},
    "lumapps": {"status": "INTERVIEWING", "note": f"[{today}] Hiring Manager interview - availability requested (Tifanie Titone)"},
    "fever": {"status": "INTERVIEWING", "note": f"[{today}] Interview link exchanged (Patricia Fernandez)"},
    
    # STATUS UPDATES - likely rejections
    "accesa": {"status": "REJECTED", "note": f"[{today}] Update re Senior FDE application"},
    "momence": {"status": "REJECTED", "note": f"[{today}] Update on application"},
    "camunda": {"status": "REJECTED", "note": f"[{today}] Candidacy Update - Senior PM Core Platform"},
    "supabase": {"status": "REJECTED", "note": f"[{today}] Update on application"},
    
    # Soft rejections from 'Other'
    "thought machine": {"status": "REJECTED", "note": f"[{today}] Maria Jaramillo re recent application"},
    "solvd": {"status": "REJECTED", "note": f"[{today}] Can we keep your details on file"},
    "gravity9": {"status": "REJECTED", "note": f"[{today}] Application response - Forward Deployed AI Engineer"},
}

rows = []
updated_companies = []
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
                # Only update if currently SUBMITTED (don't downgrade INTERVIEWING to REJECTED)
                if row[5].strip().upper() == "SUBMITTED":
                    row[5] = update_data["status"]
                    existing_notes = row[9]
                    new_note = update_data['note']
                    if new_note not in existing_notes:
                        if existing_notes:
                            row[9] = f"{existing_notes} | {new_note}"
                        else:
                            row[9] = new_note
                    updated_companies.append(f"{row[1]} -> {update_data['status']}")
                break
        rows.append(row)

with open('applications.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"Updated {len(updated_companies)} rows:")
for c in updated_companies:
    print(f"  {c}")
