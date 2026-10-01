import json
import re
import sys
import os
import subprocess

def extract_and_compile(conversation_id, company, role):
    log_file = f"/Users/prab/.gemini/antigravity/brain/{conversation_id}/.system_generated/logs/transcript_full.jsonl"
    
    latex_content = ""
    if not os.path.exists(log_file):
        print(f"Transcript not found for {conversation_id}")
        return
        
    with open(log_file, "r") as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                if data.get("type") == "PLANNER_RESPONSE":
                    # Look for tool calls to send_message
                    if "tool_calls" in data:
                        for tc in data["tool_calls"]:
                            if tc.get("name") == "send_message" or tc.get("name") == "default_api:send_message":
                                args = tc.get("args", {})
                                msg = args.get("Message", "")
                                # extract everything between \documentclass and \end{document}
                                matches = re.findall(r'\\documentclass\[.*?\]\{.*?\}[\s\S]*?\\end\{document\}', msg)
                                if matches:
                                    latex_content = "\n\n".join(matches)
                                    break
                                # If no \documentclass found, maybe it's just raw code
                                matches_raw = re.findall(r'```(?:latex)?(.*?)```', msg, re.DOTALL)
                                if matches_raw:
                                    latex_content = "\n\n".join(matches_raw)
                                    break
            except Exception as e:
                pass

    if not latex_content:
        print(f"Could not extract LaTeX for {company}")
        return
        
    base_name = f"cv_cl_{company.replace(' ', '_')}"
    tex_file = f"loop/{base_name}.tex"
    with open(tex_file, "w") as f:
        f.write(latex_content)
        
    print(f"Compiling {tex_file}...")
    subprocess.run(["/opt/homebrew/bin/tectonic", "--outdir=loop", tex_file], capture_output=True)
    print(f"Done compiling {base_name}.pdf")

if __name__ == "__main__":
    # Expecting args: script.py <conv_id1> <company1> <conv_id2> <company2> ...
    args = sys.argv[1:]
    for i in range(0, len(args), 2):
        extract_and_compile(args[i], args[i+1], "role")
