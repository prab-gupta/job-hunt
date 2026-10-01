import csv
import datetime

today = datetime.date.today().isoformat()

new_queue_entries = [
    [
        "VOICEB.ai",
        "Forward Deployment Engineer",
        "https://es.linkedin.com/jobs/view/forward-deployment-engineer-at-voiceb-ai-4469133907",
        "LinkedIn",
        "A",
        "85",
        today,
        "EXT",
        "TO APPLY",
        "MATERIALS READY: Prabhavit_CV_VoiceB.tex + CoverLetter_VoiceB.tex. Barcelona, FDE voice/agent deployments. Remote EU authorized (Italy LTR)."
    ],
    [
        "VoiceLine",
        "Forward Deployed Engineer (f/m/d)",
        "https://de.linkedin.com/jobs/view/forward-deployed-engineer-f-m-d-at-voiceline-4417917540",
        "LinkedIn",
        "A",
        "88",
        today,
        "EXT",
        "TO APPLY",
        "MATERIALS READY: Prabhavit_CV_VoiceLine.tex + CoverLetter_VoiceLine.tex. Munich/Remote, FDE voice AI agent workflows. Remote EU authorized."
    ],
    [
        "Bentley Systems",
        "Forward Deployed Software Engineer",
        "https://ie.linkedin.com/jobs/view/forward-deployed-software-engineer-at-bentley-systems-4467862807",
        "LinkedIn",
        "A",
        "82",
        today,
        "EXT",
        "TO APPLY",
        "MATERIALS READY: Prabhavit_CV_Bentley.tex + CoverLetter_Bentley.tex. Dublin/Remote, enterprise API integrations and FDE software solutions."
    ],
    [
        "ERNI",
        "AI Agent Productivization Engineer",
        "https://es.linkedin.com/jobs/view/ai-agent-productivization-engineer-at-erni-4467860724",
        "LinkedIn",
        "A",
        "86",
        today,
        "EXT",
        "TO APPLY",
        "MATERIALS READY: Prabhavit_CV_ERNI.tex + CoverLetter_ERNI.tex. Madrid/Remote, autonomous agent productivization and LLM orchestration."
    ]
]

# Read existing URLs to prevent duplicate rows in queue
existing_urls = set()
with open('loop/queue.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 2:
            existing_urls.add(row[2].strip().lower())

with open('loop/queue.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for row in new_queue_entries:
        if row[2].strip().lower() not in existing_urls:
            writer.writerow(row)
            print(f"Appended {row[0]} - {row[1]} to queue.csv")

