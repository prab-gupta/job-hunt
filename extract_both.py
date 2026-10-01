import json
import re
import sys
import os

def extract(transcript_file, company):
    with open(transcript_file, 'r') as f:
        for line in f:
            data = json.loads(line)
            if data.get('type') == 'PLANNER_RESPONSE':
                for tool_call in data.get('tool_calls', []):
                    if tool_call.get('name') == 'send_message' or tool_call.get('name') == 'default_api:send_message':
                        message = tool_call.get('args', {}).get('Message', '')
                        if not message:
                            message = tool_call.get('function', {}).get('arguments', {}).get('Message', '')
                        matches = re.findall(r'```latex\n(.*?)\n```', message, re.DOTALL)
                        if len(matches) >= 2:
                            with open(f'cv/cv_{company}.tex', 'w') as out_cv:
                                out_cv.write(matches[0])
                            with open(f'cover_letters/cl_{company}.tex', 'w') as out_cl:
                                out_cl.write(matches[1])
                            print(f"Successfully extracted {company} CV and CL.")
                            return True
    print(f"Failed to extract {company}")
    return False

extract('/Users/prab/.gemini/antigravity/brain/b9980823-16df-4c45-994b-9db5342a9a47/.system_generated/logs/transcript_full.jsonl', 'Zurich')
extract('/Users/prab/.gemini/antigravity/brain/ecd558bc-90a2-47e2-a082-089ae6943e15/.system_generated/logs/transcript_full.jsonl', 'Greenvolt')
