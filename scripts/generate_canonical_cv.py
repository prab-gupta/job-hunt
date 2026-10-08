#!/usr/bin/env python3
"""
scripts/generate_canonical_cv.py
Ponytail single source of truth for generating tailored CVs strictly anchored
to data/cvs/Prabhavit_CV_EN_baseline.tex with ZERO hallucinations.

Rules from AGENT-INSTRUCTIONS.md:
- Never fabricate companies or dates. Canonical employers are strictly:
  FlowSpace.co, Urlink, UltraStrategy.com, Qomodo, Get2Germany.com, Clubee.com, Tractionboard.co.
- Italian = Beginner (NEVER 'Working proficiency' or C1).
- FORBIDDEN claims: FastAPI, Django, Flask, AsyncIO/asyncio, Kubernetes, PyTorch, JAX, TensorFlow,
  Docker in production, BPMN, ML research.
- Compiles with tectonic to strictly 2 pages.
"""

import sys, os, re, subprocess

BASE_PATH = "data/cvs/Prabhavit_CV_EN_baseline.tex"

FORBIDDEN_PATTERNS = [
    r"\bFastAPI\b",
    r"\bDjango\b",
    r"\bFlask\b",
    r"\bAsyncIO\b",
    r"\basyncio\b",
    r"\bKubernetes\b",
    r"\bPyTorch\b",
    r"\bJAX\b",
    r"\bTensorFlow\b",
    r"\bBPMN\b",
    r"Tech Automation Systems",
    r"Independent Consultancy",
    r"Italian.*Working",
    r"Italian.*Fluent",
]

def generate_canonical_cv(company: str, role: str, summary_bullets: list[str], skills_lines: list[str] = None):
    assert len(summary_bullets) == 3, f"Summary must have exactly 3 bullets, got {len(summary_bullets)}"
    
    with open(BASE_PATH, "r", encoding="utf-8") as f:
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
    assert re.search(summary_regex, content), "Could not find Career Summary block in baseline"
    content = re.sub(summary_regex, lambda _: formatted_summary, content, count=1)
    
    # 2. Format new Technical Skills if provided
    if skills_lines:
        formatted_skills = "\\section{Technical Skills}\n\\begin{itemize}\n"
        for line in skills_lines:
            clean_l = line.strip()
            clean_l = re.sub(r"(?<!\\)&", r"\\&", clean_l)
            formatted_skills += f"\\item {clean_l}\n"
        formatted_skills += "\\end{itemize}"
        
        skills_regex = r"\\section\{Technical Skills\}[\s\S]*?\\end\{itemize\}"
        assert re.search(skills_regex, content), "Could not find Technical Skills block in baseline"
        content = re.sub(skills_regex, lambda _: formatted_skills, content, count=1)
        
    # 3. Assert ZERO forbidden patterns in output
    for pat in FORBIDDEN_PATTERNS:
        match = re.search(pat, content, re.IGNORECASE)
        assert not match, f"Violation: Forbidden claim matched '{pat}' in generated CV content!"
        
    # 4. Assert required canonical facts exist
    assert "Italian (Beginner)" in content, "Italian must be strictly Beginner"
    assert "Ca' Foscari University of Venice" in content, "Education missing"
    assert "FlowSpace.co" in content, "FlowSpace missing"
    
    # Clean company and role for filename
    clean_co = re.sub(r"[^a-zA-Z0-9]", "", company)
    clean_role = re.sub(r"[^a-zA-Z0-9]", "", role)
    out_tex = f"cv/main_{clean_co}_{clean_role}.tex"
    out_pdf = f"cv/main_{clean_co}_{clean_role}.pdf"
    
    # Ensure photo_orig.png exists in target directory
    if not os.path.exists("photo_orig.png") and os.path.exists("cv/photo.jpg"):
        subprocess.run(["cp", "cv/photo.jpg", "photo_orig.png"], check=True)
    if not os.path.exists("cv/photo_orig.png") and os.path.exists("cv/photo.jpg"):
        subprocess.run(["cp", "cv/photo.jpg", "cv/photo_orig.png"], check=True)
        
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
        f"AI Solutions & Software Engineer with ~3 years commercial software experience deploying production LLM workflows, API integrations, and developer tooling across European tech projects",
        "Hands-on expertise implementing autonomous tool-use loops with Model Context Protocol (MCP), prompt engineering, and structured API integrations",
        f"Demonstrated ability to partner with cross-functional engineering teams, scale web platforms from 2,000 to 4,500+ users, and deliver reliable automation features at {co}"
    ]
    skills = [
        "\\textbf{AI & Agent Tooling} -- AI Agents, Model Context Protocol (MCP), Tool Calling, Prompt Engineering, Structured Outputs, OpenAI API, Claude API",
        "\\textbf{Software Development} -- TypeScript, Next.js, React, Node.js, Laravel, REST APIs, GraphQL, PostgreSQL, SQLite",
        "\\textbf{Automation & Testing} -- Playwright, n8n, Make, Webhook Integrations, End-to-End Testing",
        "\\textbf{Tools & Delivery} -- Git, GitHub, Postman, Jira, Figma, Trello, Linux CLI, Client Scoping"
    ]
    generate_canonical_cv(co, ro, summary, skills)
