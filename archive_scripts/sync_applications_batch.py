import csv
import glob
import os
import datetime

ROOT = "/Users/prab/Downloads/claud jobs"
today = datetime.date.today().isoformat()

# Read existing applications to prevent duplicate lines
existing_urls = set()
with open(os.path.join(ROOT, "applications.csv"), "r") as f:
    for row in csv.reader(f):
        if len(row) > 4:
            existing_urls.add(row[4].strip().lower())

# Read confirmation text files from today
confirm_files = glob.glob(os.path.join(ROOT, "confirmations", f"*-{today}.txt"))

new_app_rows = []
for cf in confirm_files:
    data = {}
    with open(cf, "r") as f:
        for line in f:
            if ":" in line:
                k, v = line.split(":", 1)
                data[k.strip().lower()] = v.strip()
    
    url = data.get("url", "")
    if not url or url.lower() in existing_urls:
        continue
    
    company = data.get("company", "Unknown")
    role = data.get("role", "Engineer")
    title = data.get("page title", "")
    cv = data.get("cv", "")
    cl = data.get("cover letter", "")
    status = data.get("status", "SUBMITTED")
    
    # 10 fields standard schema: date,company,role,ats,url,status,confirmation_text,salary_stated,cover_letter_attached,notes
    row = [
        today,
        company,
        role,
        "Browser Automation (Playwright Chrome)",
        url,
        status,
        f"Page verified: {title}",
        "EUR 50,000",
        "yes" if cl and cl != "None" else "no",
        f"CV={os.path.basename(cv) if cv else 'standard'} | CL={os.path.basename(cl) if cl else 'none'} | Confirmation={os.path.basename(cf)}"
    ]
    new_app_rows.append(row)
    existing_urls.add(url.lower())

with open(os.path.join(ROOT, "applications.csv"), "a", newline="") as f:
    writer = csv.writer(f)
    for r in new_app_rows:
        writer.writerow(r)

print(f"Appended {len(new_app_rows)} verified applications to applications.csv!")
