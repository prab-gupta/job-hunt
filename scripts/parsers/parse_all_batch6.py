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

# Analog
extract('/Users/prab/.gemini/antigravity/brain/cb434447-43f1-4c91-b4ec-acb40c3c0e62/.system_generated/logs/transcript_full.jsonl',
        'cv/main_AnalogDevices_SeniorPrincipalFDE.tex', 'cover_letters/cover_AnalogDevices_SeniorPrincipalFDE.tex')

# OMMAX
extract('/Users/prab/.gemini/antigravity/brain/45409bcf-7b6f-4665-af3a-3f64d1be51d1/.system_generated/logs/transcript_full.jsonl',
        'cv/main_OMMAX_ForwardDeployedAIEngineer.tex', 'cover_letters/cover_OMMAX_ForwardDeployedAIEngineer.tex')


# Cloudera
extract('/Users/prab/.gemini/antigravity/brain/aa855296-0a1f-491a-bb1a-a8e1d068c9b7/.system_generated/logs/transcript_full.jsonl',
        'cv/main_Cloudera_ForwardDeployedAIEngineer.tex', 'cover_letters/cover_Cloudera_ForwardDeployedAIEngineer.tex')

# BCG X
extract('/Users/prab/.gemini/antigravity/brain/f4ffc5a7-f90a-4bf7-843e-a5b38de4ddcf/.system_generated/logs/transcript_full.jsonl',
        'cv/main_BCGX_VisitingForwardDeployedAIEngineer.tex', 'cover_letters/cover_BCGX_VisitingForwardDeployedAIEngineer.tex')

# Accenture Italia
extract('/Users/prab/.gemini/antigravity/brain/03031f0e-e7cd-46de-82c6-61aeaa5aa481/.system_generated/logs/transcript_full.jsonl',
        'cv/main_AccentureItalia_ForwardDeployedEngineerManager.tex', 'cover_letters/cover_AccentureItalia_ForwardDeployedEngineerManager.tex')

