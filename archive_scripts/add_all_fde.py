import csv
import datetime

# 1. From the search we did earlier
search_fdes = [
    ("fonio.ai", "Forward Deployed Engineer (Polish)", "https://www.linkedin.com/jobs/view/4460351104", "Warsaw, Poland"),
    ("Keyrus", "Forward Deployed Engineer (H/F/NB)", "https://www.linkedin.com/jobs/view/4440754242", "Bordeaux, France"),
    ("Keyrus", "Forward deployment engineer (H/F/NB)", "https://www.linkedin.com/jobs/view/4440795499", "Aix-en-Provence, France"),
    ("Harmattan AI", "Forward Deployed Software Engineer", "https://www.linkedin.com/jobs/view/4469555061", "Paris, France"),
    ("Taxbit", "Forward Deployed Engineer", "https://www.linkedin.com/jobs/view/4419328245", "Madrid, Spain"),
    ("ICEYE", "Forward Deployed AI Engineer, Portugal", "https://www.linkedin.com/jobs/view/4432971674", "Portugal"),
    ("VOIDS", "Forward Deployed Engineer - Integrations", "https://www.linkedin.com/jobs/view/4466968847", "Hamburg, Germany"),
    ("Lithosquare", "Forward Deployed Engineer", "https://www.linkedin.com/jobs/view/4417098641", "Paris, France")
]

# 2. Extract from candidates.csv
candidates_fdes = []
with open("loop/candidates.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 3 and "forward deployed" in row[3].lower():
            candidates_fdes.append((row[2], row[3], row[4], row[5]))

all_fdes = search_fdes + candidates_fdes

# Deduplicate by URL
seen_urls = set()
unique_fdes = []

# Load existing queue.csv to avoid appending duplicates
try:
    with open("loop/queue.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 2:
                seen_urls.add(row[2])
except FileNotFoundError:
    pass

for co, role, url, loc in all_fdes:
    if url not in seen_urls:
        seen_urls.add(url)
        unique_fdes.append((co, role, url, loc))

print(f"Found {len(unique_fdes)} new FDE roles to add.")

today = datetime.date.today().isoformat()
with open("loop/queue.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for co, role, url, loc in unique_fdes:
        writer.writerow([co, role, url, "LinkedIn Easy Apply", "FDE", "90", today, "EasyApply", "TO APPLY", f"Added via manual override 'no exceptions'. Location: {loc}"])

