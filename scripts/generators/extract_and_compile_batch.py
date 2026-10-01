import json
import re
import os
import subprocess
import sys

mapping = {
    "Lindus": "a27b62b8-0d20-4930-8d5e-e4e56e0b0a1d",
    "Revstar": "89dcc8df-c7ec-4a0c-8347-ae00df576b55"
}

app_data_dir = "/Users/prab/.gemini/antigravity/brain"
os.makedirs("loop/pdfs", exist_ok=True)

def get_page_count(pdf_path):
    try:
        out = subprocess.check_output(["pdfinfo", pdf_path]).decode("utf-8")
        for line in out.splitlines():
            if line.startswith("Pages:"):
                return int(line.split(":")[1].strip())
    except Exception as e:
        return None

for company, conv_id in mapping.items():
    transcript_path = os.path.join(app_data_dir, conv_id, ".system_generated/logs/transcript_full.jsonl")
    if not os.path.exists(transcript_path):
        transcript_path = os.path.join(app_data_dir, conv_id, ".system_generated/logs/transcript.jsonl")
    
    if not os.path.exists(transcript_path):
        print(f"Waiting for {company} transcript...")
        continue

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
        except Exception:
            pass
            
    if not message_content:
        # Check if content has LaTeX blocks directly
        for line in lines:
            try:
                step = json.loads(line)
                c = step.get("content", "")
                if "```latex" in c and "\\begin{document}" in c:
                    message_content = c
            except Exception:
                pass

    if message_content:
        latex_blocks = re.findall(r'```(?:latex)?\n(.*?)\n```', message_content, re.DOTALL)
        if len(latex_blocks) >= 2:
            b1, b2 = latex_blocks[0], latex_blocks[1]
            if "moderncv" in b1 or "cventry" in b1:
                cv_code, cl_code = b1, b2
            elif "moderncv" in b2 or "cventry" in b2:
                cv_code, cl_code = b2, b1
            elif "Dear" in b1:
                cl_code, cv_code = b1, b2
            else:
                cv_code, cl_code = b1, b2
                
            for out_dir in ["loop", "loop/pdfs"]:
                cv_tex = os.path.join(out_dir, f"CV_{company}.tex")
                cl_tex = os.path.join(out_dir, f"CL_{company}.tex")
                cv_pdf = os.path.join(out_dir, f"CV_{company}.pdf")
                cl_pdf = os.path.join(out_dir, f"CL_{company}.pdf")
                
                with open(cv_tex, "w") as f:
                    f.write(cv_code)
                with open(cl_tex, "w") as f:
                    f.write(cl_code)
                    
                subprocess.run(["tectonic", "-o", out_dir, cv_tex], check=True)
                subprocess.run(["tectonic", "-o", out_dir, cl_tex], check=True)
                
            cv_pages = get_page_count(f"loop/CV_{company}.pdf")
            cl_pages = get_page_count(f"loop/CL_{company}.pdf")
            print(f"SUCCESS {company}: CV compiled ({cv_pages} pages), CL compiled ({cl_pages} pages)")
        else:
            print(f"Pending/Incomplete: Found {len(latex_blocks)} LaTeX blocks for {company}")
    else:
        print(f"Subagent {company} still generating...")
