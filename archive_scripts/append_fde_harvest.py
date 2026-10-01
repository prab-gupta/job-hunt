import csv
import datetime

today = datetime.date.today().isoformat()
now_iso = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")

new_candidates = [
    [now_iso, "linkedin:harvest", "MarvelX AI", "Forward Deployed Engineer", "https://nl.linkedin.com/jobs/view/forward-deployed-engineer-at-marvelx-ai-4467866066", "Amsterdam, Netherlands", today, "True"],
    [now_iso, "linkedin:harvest", "Arke", "Forward Deployed Engineer (Manufacturing)", "https://it.linkedin.com/jobs/view/forward-deployed-engineer-manufacturing-at-arke-4468372914", "Milan, Italy", today, "True"],
    [now_iso, "linkedin:harvest", "Joppy", "AI Solutions Engineer (Forward Deployed Engineer / FDE)", "https://es.linkedin.com/jobs/view/ai-solutions-engineer-forward-deployed-engineer-fde-at-joppy-4467832927", "Madrid, Spain", today, "True"]
]

with open('loop/candidates.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for row in new_candidates:
        writer.writerow(row)
        print(f"Added to candidates.csv: {row[2]} - {row[3]}")

new_queue_entries = [
    [
        "MarvelX AI",
        "Forward Deployed Engineer",
        "https://nl.linkedin.com/jobs/view/forward-deployed-engineer-at-marvelx-ai-4467866066",
        "LinkedIn",
        "A",
        "87",
        today,
        "EXT",
        "TO APPLY",
        "Harvested FDE (Tick 3): Amsterdam, AI enterprise deployment. Dedupe: NEW."
    ],
    [
        "Arke",
        "Forward Deployed Engineer (Manufacturing)",
        "https://it.linkedin.com/jobs/view/forward-deployed-engineer-manufacturing-at-arke-4468372914",
        "LinkedIn",
        "A",
        "90",
        today,
        "EXT",
        "TO APPLY",
        "Harvested FDE (Tick 3): Milan, Italy. Direct local fit. Dedupe: NEW."
    ],
    [
        "Joppy",
        "AI Solutions Engineer (Forward Deployed Engineer / FDE)",
        "https://es.linkedin.com/jobs/view/ai-solutions-engineer-forward-deployed-engineer-fde-at-joppy-4467832927",
        "LinkedIn",
        "A",
        "88",
        today,
        "EXT",
        "TO APPLY",
        "Harvested FDE (Tick 3): Madrid, AI solutions & FDE. Dedupe: NEW."
    ]
]

with open('loop/queue.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for row in new_queue_entries:
        writer.writerow(row)
        print(f"Added to queue.csv: {row[0]} - {row[1]}")

