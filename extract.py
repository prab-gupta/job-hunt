import json
import re
import os

transcript_file = '/Users/prab/.gemini/antigravity/brain/b9980823-16df-4c45-994b-9db5342a9a47/.system_generated/logs/transcript_full.jsonl'

with open(transcript_file, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'PLANNER_RESPONSE':
            for tool_call in data.get('tool_calls', []):
                if tool_call.get('function', {}).get('name') == 'default_api:send_message':
                    message = tool_call.get('function', {}).get('arguments', {}).get('Message', '')
                    matches = re.findall(r'```latex\n(.*?)\n```', message, re.DOTALL)
                    if len(matches) == 2:
                        with open('cv/cv_Zurich.tex', 'w') as out_cv:
                            out_cv.write(matches[0])
                        with open('cover_letters/cl_Zurich.tex', 'w') as out_cl:
                            out_cl.write(matches[1])
                        print("Successfully extracted Zurich CV and CL.")
                        exit(0)
print("Failed to extract.")
