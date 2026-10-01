import json
import re
import os

def extract_latex(conv_id, company_name):
    transcript_path = f"/Users/prab/.gemini/antigravity/brain/{conv_id}/.system_generated/logs/transcript_full.jsonl"
    
    if not os.path.exists(transcript_path):
        print(f"Error: Transcript not found for {conv_id}")
        return False
        
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                step = json.loads(line)
                if step.get("type") == "PLANNER_RESPONSE":
                    tool_calls = step.get("tool_calls", [])
                    for call in tool_calls:
                        name = call.get("name", "")
                        if name == "send_message" or name == "default_api:send_message":
                            args = call.get("args", {})
                            message = args.get("Message", "")
                            
                            latex_blocks = re.findall(r"\\documentclass.*?\\end\{document\}", message, re.DOTALL)
                            
                            if len(latex_blocks) >= 2:
                                cv_code = latex_blocks[0]
                                cl_code = latex_blocks[1]
                                
                                if "Cover Letter" in cv_code and "Cover Letter" not in cl_code:
                                    cv_code, cl_code = cl_code, cv_code
                                    
                                safe_company = "".join(c for c in company_name if c.isalnum())
                                with open(f"loop/CV_{safe_company}.tex", "w", encoding="utf-8") as out:
                                    out.write(cv_code)
                                with open(f"loop/CL_{safe_company}.tex", "w", encoding="utf-8") as out:
                                    out.write(cl_code)
                                    
                                print(f"Successfully extracted LaTeX for {company_name}")
                                return True
                            elif len(latex_blocks) == 1:
                                safe_company = "".join(c for c in company_name if c.isalnum())
                                with open(f"loop/CV_CL_{safe_company}.tex", "w", encoding="utf-8") as out:
                                    out.write(latex_blocks[0])
                                print(f"Warning: Only one LaTeX block found for {company_name}")
                                return True
            except Exception as e:
                pass
            
    print(f"Failed to find LaTeX for {company_name} in {conv_id}")
    return False

if __name__ == "__main__":
    jobs = [
        ("03b86ae3-4150-4087-b5ec-4fe4faf3fe13", "Teradyne"),
        ("b983ed38-6cd1-4cd2-9f43-196ee8b89835", "UniCredit"),
        ("7463727d-57cf-4ff1-b8cf-97318a579780", "Google"),
        ("e351b740-c502-43aa-8374-283b434f8fff", "GlobalLogic"),
        ("7ecbe197-b127-4d63-bde4-91699aca6dd3", "Siemens Energy")
    ]
    for cid, comp in jobs:
        extract_latex(cid, comp)
