import re
import os

transcript_file = '/Users/prab/.gemini/antigravity/brain/b9980823-16df-4c45-994b-9db5342a9a47/.system_generated/logs/transcript_full.jsonl'
cv_latex = ""
cl_latex = ""

with open(transcript_file, 'r', encoding='utf-8') as f:
    content = f.read()
    
# Extract using regex from the raw json content which contains the response.
# Wait, it's easier to just parse the last PLANNER_RESPONSE.
