import csv
import re
import os

# 1. Map URLs to locations from content.md
url_to_loc = {}
if os.path.exists('/Users/prab/.gemini/antigravity/brain/ef77eada-777c-44ce-be2a-d6a8b4c47c87/.system_generated/steps/15526/content.md'):
    with open('/Users/prab/.gemini/antigravity/brain/ef77eada-777c-44ce-be2a-d6a8b4c47c87/.system_generated/steps/15526/content.md', 'r') as f:
        html = f.read()
    
    # Each job block looks like:
    # <a href="/jobs/..." ...>
    # ...
    # <span class="job-item__tag">Location</span> OR <span class="job-item__tag job-item__tag--remote">Remote</span>
    
    blocks = re.split(r'<a href="(/jobs/[^"]+)"', html)
    # blocks[0] is garbage, blocks[1] is href, blocks[2] is inner HTML, blocks[3] is href, etc.
    for i in range(1, len(blocks), 2):
        href = blocks[i]
        inner = blocks[i+1]
        
        # Check for remote
        is_remote = "job-item__tag--remote" in inner
        
        # Check for location
        loc_match = re.search(r'<span class="job-item__tag">(.*?)</span>', inner)
        loc = loc_match.group(1) if loc_match else ""
        
        url_to_loc[f"https://fdepulse.com{href}"] = {"remote": is_remote, "loc": loc.lower()}

eu_keywords = [
    "remote", "italy", "germany", "france", "spain", "netherlands", "sweden", 
    "denmark", "finland", "ireland", "poland", "portugal", "belgium", "austria", 
    "switzerland", "uk", "united kingdom", "london", "berlin", "paris", "amsterdam", 
    "stockholm", "copenhagen", "madrid", "barcelona", "milan", "rome", "munich", 
    "frankfurt", "dublin", "warsaw", "lisbon", "vienna", "zurich", "geneva", "europe"
]

def is_eu_or_remote(title, loc_str, is_remote):
    if is_remote or "remote" in title.lower() or "remote" in loc_str.lower():
        # Make sure it doesn't say "Remote - US Only"
        if "us only" in title.lower() or "us only" in loc_str.lower() or "usa only" in loc_str.lower():
            return False
        return True
    
    for kw in eu_keywords:
        if kw in loc_str.lower() or kw in title.lower():
            return True
            
    return False

# 2. Filter queue.csv
rows = []
seen_urls = set()
dropped_count = 0
dup_count = 0

with open("loop/queue.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows.append(header)
    for row in reader:
        if len(row) < 9:
            continue
            
        url = row[2]
        title = row[1]
        status = row[8]
        
        # Check duplicates
        if url in seen_urls:
            dup_count += 1
            if status == "TO APPLY":
                status = "DUP"
                row[8] = status
        else:
            seen_urls.add(url)
            
        # Check location if it's FDEPulse and TO APPLY
        if status == "TO APPLY" and "fdepulse.com" in url:
            loc_data = url_to_loc.get(url, {"remote": False, "loc": ""})
            if not is_eu_or_remote(title, loc_data["loc"], loc_data["remote"]):
                status = "SKIPPED - NON-EU/NON-REMOTE"
                row[8] = status
                dropped_count += 1
        
        # Also check non-FDEPulse just by title if we have no location
        elif status == "TO APPLY":
            # If we didn't scrape location, we'll give it the benefit of the doubt unless it explicitly says US
            if "us only" in title.lower() or "usa only" in title.lower():
                status = "SKIPPED - US ONLY"
                row[8] = status
                dropped_count += 1
                
        rows.append(row)

with open("loop/queue.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"Removed {dup_count} duplicates.")
print(f"Skipped {dropped_count} non-EU/non-Remote jobs.")

# Count remaining TO APPLY
with open("loop/queue.csv", "r") as f:
    remaining = sum(1 for row in csv.DictReader(f) if row["status"] == "TO APPLY")
print(f"Remaining TO APPLY: {remaining}")
