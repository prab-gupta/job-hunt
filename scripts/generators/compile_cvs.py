import json
import re
import os
import subprocess
import sys

if len(sys.argv) > 1:
    subagents = json.loads(sys.argv[1])
else:
    print("Please provide a JSON string mapping company to subagent ID")
    sys.exit(1)

app_data_dir = "/Users/prab/.gemini/antigravity/brain"
os.makedirs("loop/pdfs", exist_ok=True)

for company, conv_id in subagents.items():
    transcript_path = os.path.join(app_data_dir, conv_id, ".system_generated/logs/transcript_full.jsonl")
    
    with open(transcript_path, 'r') as f:
        lines = f.readlines()
        
    message_content = ""
    for line in lines:
        try:
            step = json.loads(line)
            if step.get("type") == "PLANNER_RESPONSE":
                tool_calls = step.get("tool_calls", [])
                for tc in tool_calls:
                    if tc.get("name") == "send_message":
                        message_content = tc.get("args", {}).get("Message", "")
                        break
        except Exception as e:
            pass
            
    if message_content:
        # Find LaTeX blocks
        latex_blocks = re.findall(r'```latex\n(.*?)\n```', message_content, re.DOTALL)
        if len(latex_blocks) >= 2:
            # First is usually CV, Second is Cover Letter, but let's check content to be sure
            # Or just use the order
            cv_code = latex_blocks[0]
            cl_code = latex_blocks[1]
            
            # If cover letter string is in the first block, swap
            if "Dear" in cv_code or "Subject:" in cv_code or "Hiring Manager" in cv_code:
                cv_code, cl_code = cl_code, cv_code
                
            cv_path = f"loop/pdfs/CV_{company}.tex"
            cl_path = f"loop/pdfs/CoverLetter_{company}.tex"
            
            with open(cv_path, "w") as f:
                f.write(cv_code)
            with open(cl_path, "w") as f:
                f.write(cl_code)
                
            # Compile
            subprocess.run(["tectonic", "-o", "loop/pdfs", cv_path])
            subprocess.run(["tectonic", "-o", "loop/pdfs", cl_path])
            
            print(f"Compiled {company}")
        else:
            print(f"Could not find 2 LaTeX blocks for {company}")
    else:
        print(f"No send_message found for {company}")
