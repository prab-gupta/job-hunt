import json
import glob

files = glob.glob("/Users/prab/.gemini/antigravity/brain/*/.system_generated/logs/transcript.jsonl")
for f in files:
    with open(f, 'r') as fh:
        content = fh.read()
        if "telnyx" in content.lower():
            # Check if this subagent was spawned by checking ef77eada... for its id
            print(f"Found in {f}")
            # print the first USER_INPUT which usually has the prompt
            fh.seek(0)
            for line in fh:
                obj = json.loads(line)
                if obj.get("type") == "USER_INPUT":
                    print(obj.get("content")[:150])
                    break
