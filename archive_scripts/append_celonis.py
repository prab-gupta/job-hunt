import csv
import datetime

today = datetime.date.today().isoformat()
now_iso = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")

new_cand = [now_iso, "linkedin:harvest", "Celonis", "Associate Applied (AI) Value Engineer - Orbit Program", "https://es.linkedin.com/jobs/view/associate-applied-ai-value-engineer-uk-orbit-program-at-celonis-4457791949", "Madrid, Spain", today, "True"]

with open('loop/candidates.csv', 'a', newline='') as f:
    csv.writer(f).writerow(new_cand)
    print("Added to candidates.csv: Celonis")

new_queue = [
    "Celonis",
    "Associate Applied (AI) Value Engineer - Orbit Program",
    "https://es.linkedin.com/jobs/view/associate-applied-ai-value-engineer-uk-orbit-program-at-celonis-4457791949",
    "LinkedIn",
    "A",
    "85",
    today,
    "EXT",
    "TO APPLY",
    "Harvested Orbit Program (Tick 9): Madrid, AI value & solutions engineering. Dedupe: NEW REQ."
]

with open('loop/queue.csv', 'a', newline='') as f:
    csv.writer(f).writerow(new_queue)
    print("Added to queue.csv: Celonis Orbit Program")

