import json
import re
import os

def extract(transcript_path, cv_file, cover_file):
    if not os.path.exists(transcript_path):
        return
    with open(transcript_path, 'r') as f:
        for line in f:
            if not line.strip(): continue
            item = json.loads(line)
            if item.get("type") == "PLANNER_RESPONSE" and item.get("tool_calls"):
                for tc in item["tool_calls"]:
                    if tc["name"] == "send_message":
                        msg = tc["args"].get("Message", "")
                        matches = re.findall(r'```latex\n(.*?)\n```', msg, re.DOTALL)
                        if len(matches) >= 2:
                            with open(cv_file, 'w') as out_cv:
                                out_cv.write(matches[0])
                            with open(cover_file, 'w') as out_cover:
                                out_cover.write(matches[1])
                            print(f"Extracted {cv_file}")

# Prosper AI
extract('/Users/prab/.gemini/antigravity/brain/aac4eab8-e95d-4b84-9bd5-4142949d3ecc/.system_generated/logs/transcript_full.jsonl',
        'cv/main_ProsperAI_FDE.tex', 'cover_letters/cover_ProsperAI_FDE.tex')

# Salesforce
extract('/Users/prab/.gemini/antigravity/brain/dd3409be-b876-4181-8f9f-a97f4d36dde6/.system_generated/logs/transcript_full.jsonl',
        'cv/main_Salesforce_SeniorFDE.tex', 'cover_letters/cover_Salesforce_SeniorFDE.tex')

# Kinaxis
extract('/Users/prab/.gemini/antigravity/brain/c09dae7e-9e79-4d18-94ee-1436165e5ee1/.system_generated/logs/transcript_full.jsonl',
        'cv/main_Kinaxis_FDEI.tex', 'cover_letters/cover_Kinaxis_FDEI.tex')

# Airweave
extract('/Users/prab/.gemini/antigravity/brain/d81c398f-9375-4b84-b6d2-7018358d309f/.system_generated/logs/transcript_full.jsonl',
        'cv/main_Airweave_FoundingFDE.tex', 'cover_letters/cover_Airweave_FoundingFDE.tex')

# United Digital Group
extract('/Users/prab/.gemini/antigravity/brain/312e17a6-4c7d-4bf9-8d08-09d4b27dd2b5/.system_generated/logs/transcript_full.jsonl',
        'cv/main_UnitedDigitalGroup_FDAIEngineer.tex', 'cover_letters/cover_UnitedDigitalGroup_FDAIEngineer.tex')
