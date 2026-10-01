import sys

jobs = [
    {"Company": "QuantumBlack, AI by McKinsey", "Role": "Senior Forward Deployed Engineer - QuantumBlack, AI by McKinsey", "Notes": "McKinsey careers account wall"},
    {"Company": "Nordea", "Role": "Senior Forward Deployed AI Engineer", "Notes": "SuccessFactors wall"},
    {"Company": "Dataminr", "Role": "Forward Deployed Engineer", "Notes": "Workday wall JR2082"},
    {"Company": "EY", "Role": "FS Technology Consulting - AI and Data - Forward Deployed AI Engineer - Manager - Dublin", "Notes": "SuccessFactors wall"},
    {"Company": "SAP", "Role": "Forward Deployed AI Engineer Expert / Senior (f/m/d)", "Notes": "SuccessFactors wall"}
]

date_str = "2026-09-28"

with open("loop/applications.csv", "a") as f:
    for job in jobs:
        # User requested: Company, Role, Status, Notes, Date
        # Example: "QuantumBlack, Senior Forward Deployed Engineer, NEEDS_HUMAN, Account wall, 2026-09-28"
        
        # But we'll format it exactly as requested in the text.
        # Actually I will quote the fields to avoid CSV issues
        company = job['Company'].replace('"', '""')
        role = job['Role'].replace('"', '""')
        notes = job['Notes'].replace('"', '""')
        f.write(f'"{company}","{role}",NEEDS_HUMAN,"{notes}","{date_str}"\n')

print("Done appending to CSV")
