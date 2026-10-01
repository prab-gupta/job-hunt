import json
import re

with open("scratch/search_results.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

# Negative keywords (industrial/hardware/PLC/manufacturing/non-EU)
neg_keywords = [
    "plc", "siemens", "scada", "geoscada", "industrial", "robotics", "mechanical", "electrical",
    "hardware", "building automation", "bacnet", "hvac", "colombia", "mexico", "india", "vietnam",
    "australia", "singapore", "bogota", "querétaro", "pune", "sydney", "ho chi minh", "san antonio",
    "seattle", "greater seattle", "minneapolis"
]

# Positive keywords for Prabhavit
pos_keywords = [
    "ai", "automation", "integration", "software", "workflow", "n8n", "python", "typescript",
    "api", "developer", "solutions", "agent", "cloud", "remote", "europe", "italy", "germany",
    "netherlands", "spain", "denmark", "sweden", "uk"
]

ranked = []
for c in candidates:
    text = (str(c.get("title") or "") + " " + str(c.get("company") or "") + " " + str(c.get("location") or "") + " " + str(c.get("url") or "")).lower()
    
    # Check negative
    if any(k in text for k in neg_keywords):
        continue
    
    # Exclude french titles if candidate has no french
    if any(fr in text for fr in ["ingénieur", "ingénieure", "automaticien", "stage", "alternance"]):
        continue

    # Score
    score = 0
    for pos in pos_keywords:
        if pos in text:
            score += 1
            
    c["score"] = score
    ranked.append(c)

ranked.sort(key=lambda x: x["score"], reverse=True)

print(f"Filtered down to {len(ranked)} relevant software/automation/integration roles.")
for i, c in enumerate(ranked[:15]):
    print(f"[{i+1}] {c['portal'].upper()} (score: {c['score']}) | {c['company']} | {c['title']} | {c['location']}")
    print(f"     URL: {c['url']}")

with open("scratch/ranked_leads.json", "w", encoding="utf-8") as f:
    json.dump(ranked, f, indent=2)
