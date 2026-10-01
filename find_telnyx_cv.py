import json
import glob

files = glob.glob("/Users/prab/.gemini/antigravity/brain/*/.system_generated/logs/transcript_full.jsonl")
for f in files:
    with open(f, 'r') as fh:
        for line in fh:
            obj = json.loads(line)
            if obj.get("type") == "PLANNER_RESPONSE":
                content = obj.get("content", "")
                if "documentclass" in content and "telnyx" in content.lower():
                    print(f"Found Telnyx CV in {f}")
                    import re
                    match = re.search(r'```(?:latex)?(.*?)```', content, re.DOTALL)
                    if match:
                        with open("cv/main_Telnyx.tex", "w") as f_out:
                            f_out.write(match.group(1).strip())
                        print("Saved to cv/main_Telnyx.tex")
                    break
