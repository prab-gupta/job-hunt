import csv
import datetime

today = datetime.date.today().isoformat()

new_rows = [
    [
        today,
        "Hays",
        "AI Engineer - Generative AI & Autonomous Agents",
        "",
        "https://www.linkedin.com/jobs/view/...", 
        "drafted",
        "",
        "",
        "yes",
        "drafted via AI. fit_rating: 85, cv_file: cv/main_hays_ai_engineer.tex, cover_letter_file: cover_letters/cover_hays_ai_engineer.tex"
    ],
    [
        today,
        "WeHunt",
        "Backend Developer Node.js / TypeScript",
        "",
        "https://www.linkedin.com/jobs/view/...", 
        "drafted",
        "",
        "",
        "yes",
        "drafted via AI. fit_rating: 74, cv_file: cv/main_wehunt_backend_developer.tex, cover_letter_file: cover_letters/cover_wehunt_backend_developer.tex"
    ]
]

# Read existing to ensure we don't duplicate
existing_companies = []
with open('applications.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            existing_companies.append(row[1].lower())

with open('applications.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for row in new_rows:
        if row[1].lower() not in existing_companies:
            writer.writerow(row)

print("Drafts appended to tracker!")
