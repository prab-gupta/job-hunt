import json
import re
import sys
import os

def extract_from_transcript(transcript_path, output_dir, company_role):
    cv_latex = ""
    cl_latex = ""
    
    with open(transcript_path, 'r') as f:
        for line in f:
            try:
                step = json.loads(line)
                if step.get('type') == 'PLANNER_RESPONSE':
                    tool_calls = step.get('tool_calls', [])
                    for tc in tool_calls:
                        if tc.get('name') == 'send_message' or tc.get('name') == 'default_api:send_message':
                            args = tc.get('args', {})
                            message = args.get('Message', '')
                            
                            cv_match = re.search(r'<CV_LATEX>(.*?)</CV_LATEX>', message, re.DOTALL)
                            if cv_match:
                                cv_latex = cv_match.group(1).strip()
                            
                            cl_match = re.search(r'<CL_LATEX>(.*?)</CL_LATEX>', message, re.DOTALL)
                            if cl_match:
                                cl_latex = cl_match.group(1).strip()
            except json.JSONDecodeError:
                continue

    if cv_latex:
        cv_path = os.path.join(output_dir, f'main_{company_role}.tex')
        with open(cv_path, 'w') as f:
            f.write(cv_latex)
        print(f"Wrote {cv_path}")
    
    if cl_latex:
        cl_path = os.path.join(output_dir, f'cover_{company_role}.tex')
        with open(cl_path, 'w') as f:
            f.write(cl_latex)
        print(f"Wrote {cl_path}")

if __name__ == "__main__":
    transcript_file = sys.argv[1]
    company_role = sys.argv[2]
    
    os.makedirs('cv', exist_ok=True)
    os.makedirs('cover_letters', exist_ok=True)
    
    extract_from_transcript(transcript_file, 'cv', company_role)
    extract_from_transcript(transcript_file, 'cover_letters', company_role)
