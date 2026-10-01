import csv
import openpyxl

# Read last 29 rows of applications.csv
new_rows = []
with open('/Users/prab/Downloads/claud jobs/applications.csv', 'r') as f:
    reader = list(csv.reader(f))
    new_rows = reader[-29:] # The 29 new rows

wb = openpyxl.load_workbook('/Users/prab/Downloads/claud jobs/MASTER - every application - 13 Aug 2026.xlsx')
sheet = wb['Every application']

for row in new_rows:
    date = row[0]
    company = row[1]
    role = row[2]
    ats = row[3]
    link = row[4]
    status = row[5]
    confirmation = row[6]
    notes = row[9]
    
    found = False
    for i, existing_row in enumerate(sheet.iter_rows(min_row=5, values_only=False), start=5):
        if existing_row[1].value == company and existing_row[2].value == role:
            existing_row[0].value = date
            existing_row[3].value = ats
            existing_row[4].value = status
            existing_row[5].value = link
            existing_row[6].value = confirmation
            existing_row[7].value = notes
            found = True
            break
    if not found:
        sheet.append([date, company, role, ats, status, link, confirmation, notes])

wb.save('/Users/prab/Downloads/claud jobs/MASTER - every application - 13 Aug 2026.xlsx')
print(f"Added/updated {len(new_rows)} rows in MASTER")
