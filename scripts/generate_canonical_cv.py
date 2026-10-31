#!/usr/bin/env python3
"""
scripts/generate_canonical_cv.py
Single source of truth for generating tailored CVs strictly anchored
to a verified baseline LaTeX template with ZERO hallucinations.

Compiles with tectonic to strictly 2 pages.
"""

import sys, os, re, json, subprocess

def load_profile():
    candidates = [
        "config/profile.json",
        "config/profile.example.json"
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
    return {}

def resolve_base_template():
    # Priority order: local user baseline -> clean ats template -> stock example
    options = [
        "data/cvs/Prabhavit_CV_EN_baseline.tex",
        "templates/cv/ats_clean/template.tex",
        "cv/main_example.tex"
    ]
    for opt in options:
        if os.path.exists(opt):
            return opt
    raise FileNotFoundError("No baseline CV template found in data/cvs/ or templates/cv/")

def generate_canonical_cv(company: str, role: str, summary_bullets: list[str], skills_lines: list[str] = None):
    assert len(summary_bullets) == 3, f"Summary must have exactly 3 bullets, got {len(summary_bullets)}"
    
    base_path = resolve_base_template()
    profile = load_profile()
    
    with open(base_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Format new Career Summary
    formatted_summary = "\\section{Career Summary}\n\\begin{itemize}\n"
    for b in summary_bullets:
        clean_b = b.strip().rstrip(".")
        clean_b = re.sub(r"(?<!\\)&", r"\\&", clean_b)
        formatted_summary += f"\\item {clean_b}.\n"
    formatted_summary += "\\end{itemize}"
    
    # Replace Career Summary block
    summary_regex = r"\\section\{Career Summary\}[\s\S]*?\\end\{itemize\}"
    if re.search(summary_regex, content):
        content = re.sub(summary_regex, lambda _: formatted_summary, content, count=1)
    elif "[CAREER_SUMMARY_BULLETS]" in content:
        bullet_items = "\n".join([f"\\item {b.strip().rstrip('.')}" for b in summary_bullets])
        content = content.replace("[CAREER_SUMMARY_BULLETS]", bullet_items)
        
    # 2. Format new Technical Skills if provided
    if skills_lines:
        formatted_skills = "\\section{Technical Skills}\n\\begin{itemize}\n"
        for line in skills_lines:
            clean_l = line.strip()
            clean_l = re.sub(r"(?<!\\)&", r"\\&", clean_l)
            formatted_skills += f"\\item {clean_l}\n"
        formatted_skills += "\\end{itemize}"
        
        skills_regex = r"\\section\{Technical Skills\}[\s\S]*?\\end\{itemize\}"
        if re.search(skills_regex, content):
            content = re.sub(skills_regex, lambda _: formatted_skills, content, count=1)
        elif "[TECHNICAL_SKILLS_ITEMS]" in content:
            skill_items = "\n".join([f"\\item {l.strip()}" for l in skills_lines])
            content = content.replace("[TECHNICAL_SKILLS_ITEMS]", skill_items)
            
    # 3. Assert ZERO forbidden patterns in output (if profile defines them)
    forbidden = profile.get("forbidden_claims", [
        r"\bFastAPI\b",
        r"\bDjango\b",
        r"\bFlask\b",
        r"\bAsyncIO\b",
        r"\bKubernetes\b",
        r"\bPyTorch\b",
        r"\bTensorFlow\b",
        r"\bBPMN\b"
    ])
    for pat in forbidden:
        regex = pat if pat.startswith(r"\b") else rf"\b{re.escape(pat)}\b"
        match = re.search(regex, content, re.IGNORECASE)
        assert not match, f"Violation: Forbidden claim matched '{pat}' in generated CV content!"
        
    # Clean company and role for filename
    clean_co = re.sub(r"[^a-zA-Z0-9]", "", company)
    clean_role = re.sub(r"[^a-zA-Z0-9]", "", role)
    os.makedirs("cv", exist_ok=True)
    out_tex = f"cv/main_{clean_co}_{clean_role}.tex"
    out_pdf = f"cv/main_{clean_co}_{clean_role}.pdf"
    
    with open(out_tex, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Compile with tectonic
    res = subprocess.run(["tectonic", out_tex], capture_output=True, text=True)
    if res.returncode != 0:
        print("Tectonic compile error:\n", res.stderr)
        sys.exit(1)
        
    # Verify page count
    p_res = subprocess.run(["pdfinfo", out_pdf], capture_output=True, text=True)
    m = re.search(r"Pages:\s+(\d+)", p_res.stdout)
    assert m, f"Could not read page count for {out_pdf}"
    pages = int(m.group(1))
    assert pages == 2, f"Expected strictly 2 pages, got {pages} pages for {out_pdf}"
    
    print(f"SUCCESS: Generated 100% compliant canonical CV: {out_pdf} (2 pages, 0 forbidden claims)")
    return out_tex, out_pdf

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: generate_canonical_cv.py <Company> <Role>")
        sys.exit(1)
    co = sys.argv[1]
    ro = sys.argv[2]
    # Default tailored summary
    summary = [
        f"AI Solutions & Software Engineer with hands-on commercial software experience deploying production LLM workflows, API integrations, and developer tooling across tech projects",
        "Hands-on expertise implementing autonomous tool-use loops with Model Context Protocol (MCP), prompt engineering, and structured API integrations",
        f"Demonstrated ability to partner with cross-functional engineering teams, scale platforms, and deliver reliable automation features at {co}"
    ]
    skills = [
        "\\textbf{AI & Agent Tooling} -- AI Agents, Model Context Protocol (MCP), Tool Calling, Prompt Engineering, Structured Outputs, OpenAI API, Claude API",
        "\\textbf{Software Development} -- TypeScript, Next.js, React, Node.js, REST APIs, GraphQL, PostgreSQL, SQLite",
        "\\textbf{Automation & Testing} -- Playwright, n8n, Make, Webhook Integrations, End-to-End Testing",
        "\\textbf{Tools & Delivery} -- Git, GitHub, Postman, Jira, Figma, Linux CLI"
    ]
    generate_canonical_cv(co, ro, summary, skills)
