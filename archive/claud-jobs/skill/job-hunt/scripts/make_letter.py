#!/usr/bin/env python3
"""Build a one-page motivation letter PDF in Prabhavit's own layout.

Usage:
    python3 scripts/make_letter.py --in letter.json --out "Company_Motivation_Letter.pdf"

letter.json:
{
  "role": "Agent Harness Engineer",
  "location": "Remote (Europe)",
  "date": "5th August 2026",
  "opening": "I am writing to express my interest in ...",
  "role_specific": "My daily engineering workflow revolves around ...",
  "closing": "I would welcome the opportunity to discuss ...",
  "core": ["optional override of the reusable paragraphs, in order"]
}

Only `role`, `opening`, `role_specific` and `closing` are required. The reusable paragraphs and
the Italian GDPR authorisation come from his real letter — see assets/motivation-letter.md.
Dates must be passed in; this script does not read the clock.
"""

import argparse
import json
import sys
from pathlib import Path

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

HEADER = (
    "<b><u>Prabhavit Gupta</u></b><br/>"
    "Venice, Italy +39 3516107807 | prabhavitg@gmail.com<br/>"
    "LinkedIn: <a href='https://www.linkedin.com/in/prabhavit'>"
    "<font color='#0563C1'>https://www.linkedin.com/in/prabhavit</font></a>"
)

CORE = [
    "Over the past three years, I have successfully transformed abstract business requirements "
    "into production-ready features across multiple European technology projects spanning "
    "different countries and sectors; from a sports management platform in Luxembourg to "
    "strategic consultant platforms in France and Spain.",
    "Operating extensively as a freelance AI Solutions Developer, I engineered AI-based data "
    "parsing tools using n8n for UltraStrategy, automated complex workflows for Get2Germany, and "
    "executed rigorous quality assurance and API integrations for Clubee.",
    "During my tenure at FlowSpace (based in London), I took over an already built system and "
    "managed it until its eventual migration to Next.JS and Laravel. Alongside debugging the "
    "system, I also partook in GTM automations using their CRM. I engineered AI agents and "
    "automated data parsing tools that directly contributed to scaling the platform from 2,000 to "
    "over 4,500 active users.",
    "I extensively leverage AI coding assistants like Claude Code and bolt.new alongside low-code "
    "platforms and modern frameworks (TypeScript, Next.JS, Laravel, Supabase) to rapidly test "
    "hypotheses and deploy MVP architectures. I am also open to learning new systems and tech "
    "stacks; I recently completed a course in Microsoft Copilot and AI agent orchestration.",
    "As a graduate of Ca' Foscari University, I have been living in Venice for 5 years, hold a "
    "European Long-Term Residence Permit requiring no visa sponsorship, and have the professional "
    "English proficiency required for international collaboration. I am also fully available for "
    "short and medium-term business travel as project demands.",
]

GDPR = (
    "<i>I hereby authorize the processing of my personal data contained in this document in "
    "compliance with the European General Data Protection Regulation (EU Regulation 2016/679) and "
    "Italian Legislative Decree 196/2003, as modified by Legislative Decree 101/2018, for the "
    "purposes of recruitment and selection.</i>"
)


def build(data, out_path):
    styles = getSampleStyleSheet()
    body = ParagraphStyle("body", parent=styles["Normal"], fontName="Helvetica", fontSize=10.5,
                          leading=15, alignment=TA_JUSTIFY, spaceAfter=8)
    head = ParagraphStyle("head", parent=body, alignment=0, spaceAfter=2, leading=14)
    bold = ParagraphStyle("bold", parent=body, fontName="Helvetica-Bold", alignment=0, spaceAfter=10)
    small = ParagraphStyle("small", parent=body, fontSize=8.5, leading=11)

    core = data.get("core") or CORE
    subject = f"Motivation letter for Application for {data['role']}"
    if data.get("location"):
        subject += f" – {data['location']}"

    flow = [
        Paragraph(HEADER, head), Spacer(1, 10 * mm),
        Paragraph(data.get("date", ""), body), Spacer(1, 4 * mm),
        Paragraph(f"<b>{subject}</b>", bold),
        Paragraph("Dear Hiring Manager,", body), Spacer(1, 2 * mm),
        Paragraph(data["opening"], body),
        Paragraph(core[0], body), Paragraph(core[1], body), Paragraph(core[2], body),
        Paragraph(data["role_specific"], body),
        Paragraph(core[3], body), Paragraph(core[4], body), Spacer(1, 2 * mm),
        Paragraph(data["closing"], body),
        Paragraph("Thank you for your time and consideration.", body),
        Paragraph("Sincerely,", body), Spacer(1, 3 * mm),
        Paragraph("Prabhavit Gupta", body), Spacer(1, 8 * mm),
        Paragraph(GDPR, small),
    ]
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    SimpleDocTemplate(str(out), pagesize=A4, leftMargin=22 * mm, rightMargin=22 * mm,
                      topMargin=20 * mm, bottomMargin=18 * mm,
                      title=subject).build(flow)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="infile", required=True)
    ap.add_argument("--out", dest="outfile", required=True)
    args = ap.parse_args()
    data = json.loads(Path(args.infile).read_text())
    for field in ("role", "opening", "role_specific", "closing"):
        if not data.get(field):
            print(f"missing required field: {field}", file=sys.stderr)
            return 1
    print(f"Wrote {build(data, args.outfile)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
