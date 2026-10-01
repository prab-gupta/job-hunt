import json

transcript_path = "/Users/prab/.gemini/antigravity/brain/c2d21c02-8e2b-4cfb-8f7b-a923b5605b38/.system_generated/logs/transcript_full.jsonl"
with open(transcript_path, 'r') as fh:
    for line in fh:
        obj = json.loads(line)
        if obj.get("type") == "PLANNER_RESPONSE":
            content = obj.get("content", "")
            if "\\documentclass" in content or "latex" in content.lower():
                print("Found LaTeX!")
                import re
                match = re.search(r'```(?:latex)?(.*?)```', content, re.DOTALL)
                if match:
                    latex = match.group(1).strip()
                    with open("cv/main_Telnyx.tex", "w") as f_out:
                        f_out.write(latex)
                    print("Saved to cv/main_Telnyx.tex")
                    break
