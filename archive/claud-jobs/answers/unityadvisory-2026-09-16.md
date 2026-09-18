# Unity Advisory - GTM Engineer - 2026-09-16

LI-PICK row. LinkedIn job: https://www.linkedin.com/jobs/view/4437981280/
ATS: Ashby, https://jobs.ashbyhq.com/unity-advisory/f998f73a-0671-4262-8a5b-7eebd38d8008/application?src=linkedin
Location: London, Mayfair, Hybrid, Full time, department Enablement.

## Dedupe
`python3 loop/dedupe.py --check "Unity Advisory" "https://www.linkedin.com/jobs/view/4437981280/"` -> NEW. No prior row in applications.csv.

## JD checks
`curl jobPosting/4437981280` apply-button count = 1 (open). No anti-AI disclaimer found. Required years 3-5 (LI-PICK overrides the >3 gate). Title not senior/lead/principal. Stack claimable (GTM automation, APIs, n8n, Python/JS).

## Form answers given
- Name: Prabhavit Gupta
- Email: prabhavitg@gmail.com
- Resume: Prabhavit_CV_UnityAdvisory.pdf
- Current Location: Venice, Italy
- Do you need Unity Advisory to sponsor a work visa: Yes (UK role, standing rule: any non-Italy country = sponsorship Yes)
- Expected annual base salary: 50000 (numeric-only field; standing band EUR 45-55k aligned to bottom, no explicit posted band to align against)
- "In two sentences, tell us why you're interested in working at Unity Advisory": "Unity Advisory is building the commercial infrastructure a lean, AI enabled firm needs, and that is exactly the kind of pipeline and automation work I already do day to day. I want to keep building GTM systems that turn manual outreach into something scored, enriched and automated."
- Contact-for-18-months marketing checkbox: left unticked (not required, standing rule: talent-pool checkboxes unticked).

## CV tailoring (Prabhavit_CV_UnityAdvisory.tex, from Prabhavit_CV_EN.tex)
- Career Summary: dropped the third bullet (AI agents/LLM data parsing/QA testing bullet), kept the automation-workflows and API-integration bullets.
- Technical Skills: moved Automation (n8n, Playwright) ahead of AI/ML.
- FlowSpace Technical Responsibilities: reordered so "GTM automations for sales funnel, lead enrichment and outbound" and the CRM/lead-capture bullet lead, followed by the OfficeRnD/Nexudus integration bullet.
- Additional Information: reordered IT Skills/Tools to put Automation/n8n first.
- No bullets deleted outright, no sentences rewritten, no claims added. Compiled 2 pages with tectonic.

## Cover letter (CoverLetter_UnityAdvisory.tex/.txt/.pdf)
Two-role proof: FlowSpace (CRM/GTM automations, OfficeRnD/Nexudus API integrations, AI listing tool, support AI agents) paired with Get2Germany (Google API integration, n8n automation, AI tools for finding courses/jobs). UK work-authorisation transparency line included (Italian EU long-term resident, not authorised in UK, open to remote-from-Italy). No em-dash (checked, count 0). No cover letter upload field existed on this Ashby form, so it was not attached; letter still produced per brief and kept on file.

## Result
SUBMITTED. Success banner: "Many thanks for your interest in Unity Advisory. Your application was successfully submitted and one of our Talent Acquisition team will contact you in due course regarding any next steps." Confirmation saved to confirmations/UnityAdvisory-2026-09-16.txt (PNG screenshot save not available in Claude in Chrome).
