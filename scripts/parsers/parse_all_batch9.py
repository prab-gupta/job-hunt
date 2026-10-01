import json
import re

transcript_file = "/Users/prab/.gemini/antigravity/brain/ef77eada-777c-44ce-be2a-d6a8b4c47c87/.system_generated/logs/transcript_full.jsonl"

def extract_latex(text):
    matches = re.findall(r"```latex\n(.*?)\n```", text, re.DOTALL)
    if len(matches) >= 2:
        return matches[0], matches[1]
    return None, None

def process_messages():
    roles = {
        "Accenture Baltics": ("main_AccentureBaltics_FDE.tex", "cover_AccentureBaltics_FDE.tex"),
        "Danfoss": ("main_Danfoss_FDE.tex", "cover_Danfoss_FDE.tex"),
        "QuantumBlack": ("main_QuantumBlack_FDE.tex", "cover_QuantumBlack_FDE.tex"),
        "Fujitsu": ("main_Fujitsu_FDE.tex", "cover_Fujitsu_FDE.tex"),
        "Atlassian": ("main_Atlassian_FDE.tex", "cover_Atlassian_FDE.tex")
    }
    
    with open(transcript_file, "r") as f:
        for line in f:
            item = json.loads(line)
            content = item.get("content", "")
            if "```latex" in content and ("Here are the highly tailored" in content or "Here are the tailored" in content or "Here is the highly tailored" in content or "Here is the tailored" in content or "Here are the precise" in content or "I have created the highly tailored" in content):
                for company, files in roles.items():
                    if company.lower() in content.lower():
                        cv, cl = extract_latex(content)
                        if cv and cl:
                            with open("cv/" + files[0], "w") as out:
                                out.write(cv)
                            with open("cover_letters/" + files[1], "w") as out:
                                out.write(cl)
                            print(f"Extracted {files[0]} and {files[1]}")
                            # we don't break because there might be multiple matches in different lines
                            # but we can remove it from roles to not process it again
                            roles.pop(company)
                            break

process_messages()
