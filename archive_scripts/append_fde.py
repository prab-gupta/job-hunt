import csv
import datetime

companies = [
    ("Cohere", "Forward Deployed Engineer", "https://www.linkedin.com/jobs/view/4413844238"),
    ("Luma", "Forward Deployed Engineer", "https://www.linkedin.com/jobs/view/4460501193"),
    ("altermAInd", "Forward Deployed AI Engineer", "https://it.linkedin.com/jobs/view/forward-deployed-ai-engineer-at-altermaind-4469167699"),
    ("Arke", "Forward Deployed Engineer", "https://it.linkedin.com/jobs/view/forward-deployed-engineer-manufacturing-at-arke-4468372914"),
    ("MarvelX AI", "Forward Deployed Engineer", "https://nl.linkedin.com/jobs/view/forward-deployed-engineer-at-marvelx-ai-4467866066"),
    ("Joppy", "AI Solutions Engineer", "https://es.linkedin.com/jobs/view/ai-solutions-engineer-forward-deployed-engineer-fde-at-joppy-4467832927"),
    ("VoiceLine", "Forward Deployed Engineer", "https://de.linkedin.com/jobs/view/forward-deployed-engineer-f-m-d-at-voiceline-4417917540"),
    ("startupjobs.pt", "Forward Deployed Engineer", "https://pt.linkedin.com/jobs/view/forward-deployed-engineer-professional-services-at-startupjobs-pt-4469512940")
]

today = datetime.date.today().isoformat()

with open("loop/queue.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for c, r, u in companies:
        writer.writerow([c, r, u, "LinkedIn Easy Apply", "FDE", "90", today, "EasyApply", "TO APPLY", "Added via manual override"])

