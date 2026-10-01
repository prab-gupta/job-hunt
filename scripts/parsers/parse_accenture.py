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
                        matches = re.findall(r'```latex\s*(.*?)\s*```', msg, re.DOTALL)
                        if len(matches) >= 2:
                            with open(cv_file, 'w') as out_cv:
                                out_cv.write(matches[-2].strip())
                            with open(cover_file, 'w') as out_cover:
                                out_cover.write(matches[-1].strip())
                            print(f"Extracted Accenture!")

extract('/Users/prab/.gemini/antigravity/brain/03031f0e-e7cd-46de-82c6-61aeaa5aa481/.system_generated/logs/transcript_full.jsonl',
        'cv/main_AccentureItalia_ForwardDeployedEngineerManager.tex', 'cover_letters/cover_AccentureItalia_ForwardDeployedEngineerManager.tex')

