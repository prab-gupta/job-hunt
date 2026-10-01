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

extract('/Users/prab/.gemini/antigravity/brain/bf411700-5fab-4c34-8d2c-de24203c8507/.system_generated/logs/transcript_full.jsonl',
        'cv/main_Allianz_FDE.tex', 'cover_letters/cover_Allianz_FDE.tex')
extract('/Users/prab/.gemini/antigravity/brain/a067824d-1846-4ff7-851c-2930ead9b11b/.system_generated/logs/transcript_full.jsonl',
        'cv/main_AccentureUK_FDE.tex', 'cover_letters/cover_AccentureUK_FDE.tex')
extract('/Users/prab/.gemini/antigravity/brain/b592553e-0ed6-4139-b7bb-93048dc07214/.system_generated/logs/transcript_full.jsonl',
        'cv/main_LiveKit_FDE.tex', 'cover_letters/cover_LiveKit_FDE.tex')
extract('/Users/prab/.gemini/antigravity/brain/505df2b8-1ae4-47c7-9701-b6a4cd2a194a/.system_generated/logs/transcript_full.jsonl',
        'cv/main_Keyrus_FDAIEngineer.tex', 'cover_letters/cover_Keyrus_FDAIEngineer.tex')
extract('/Users/prab/.gemini/antigravity/brain/2ad0115a-411f-4b4a-98e3-59e549acdaba/.system_generated/logs/transcript_full.jsonl',
        'cv/main_AccentureES_FDE.tex', 'cover_letters/cover_AccentureES_FDE.tex')

