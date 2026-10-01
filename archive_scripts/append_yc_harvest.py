import csv
import datetime

today = datetime.date.today().isoformat()
now_iso = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")

new_candidates = [
    [now_iso, "linkedin:harvest", "haddock (YC W22)", "AI Engineer - Internal Agents & Automations", "https://es.linkedin.com/jobs/view/ai-engineer-internal-agents-automations-at-haddock-yc-w22-4467860766", "Barcelona, Spain", today, "True"],
    [now_iso, "linkedin:harvest", "Alice & Bob", "AI/Agentic Engineer", "https://fr.linkedin.com/jobs/view/ai-agentic-engineer-at-alice-bob-4469139061", "Paris, France", today, "True"]
]

with open('loop/candidates.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for row in new_candidates:
        writer.writerow(row)
        print(f"Added to candidates.csv: {row[2]} - {row[3]}")

new_queue_entries = [
    [
        "haddock (YC W22)",
        "AI Engineer - Internal Agents & Automations",
        "https://es.linkedin.com/jobs/view/ai-engineer-internal-agents-automations-at-haddock-yc-w22-4467860766",
        "LinkedIn",
        "A",
        "92",
        today,
        "EXT",
        "TO APPLY",
        "Harvested YC role (Tick 6): Barcelona, internal AI agents & automations. Dedupe: NEW."
    ],
    [
        "Alice & Bob",
        "AI/Agentic Engineer",
        "https://fr.linkedin.com/jobs/view/ai-agentic-engineer-at-alice-bob-4469139061",
        "LinkedIn",
        "A",
        "89",
        today,
        "EXT",
        "TO APPLY",
        "Harvested AI role (Tick 6): Paris, agentic systems engineering. Dedupe: NEW."
    ]
]

with open('loop/queue.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for row in new_queue_entries:
        writer.writerow(row)
        print(f"Added to queue.csv: {row[0]} - {row[1]}")

