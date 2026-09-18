# Openjobmetis SpA - Junior Software Engineer, AI-Assisted Development (Biella, agency posting)

URL: https://www.linkedin.com/jobs/view/4457622982/
Applied via: LinkedIn Easy Apply, 2026-09-16.

## Dedupe
`python3 loop/dedupe.py --check "Openjobmetis" "https://www.linkedin.com/jobs/view/4457622982/"` -> NEW.
`grep -i "Openjobmetis" applications.csv` -> no prior rows.

## Cheap check + live check
Guest API apply-button count = 1. Live job page showed "Easy Apply to this job", no "Not currently accepting applications" banner.

## Hard gates re-checked on the live JD
- Title: Junior, Seniority level "Not Applicable" -> no seniority kill.
- Years: none stated (junior role).
- Degree: "Formazione in ambito informatico, tecnico o scientifico" (a technical/scientific education background), not a strict MSc/PhD requirement -> passes.
- Language: Italian JD -> Italian letter per batch rule (English CV kept).
- Core stack: "conoscenza di almeno uno tra Java, PHP e Python" (knowledge of at least one of Java/PHP/Python) -> claimable, Prabhavit has real Python and PHP (Laravel) experience.
- Agency posting (Openjobmetis recruiting for an undisclosed software company client in Biella): per task instruction, planner override applies to junior Italy roles, not killed for being an agency posting.
- No anti-AI disclaimer found; JD explicitly wants AI-assisted development tools used daily.

## CV
Prabhavit_CV_Openjobmetis.tex/.pdf built from Prabhavit_CV_EN.tex (parity-diffed against the master, reorder/delete only, no invented lines, confirmed via `diff <(grep item EN) <(grep item Openjobmetis) | grep '^>'` = empty). 2 pages (pdfinfo confirmed).
- Career Summary trimmed to 2 bullets (AI Solutions & Automation Engineer bullet + AI-assisted development/API integration bullet), dropped the "Transformed business requirements..." bullet.
- FlowSpace Product Responsibilities reordered: AI agents bullet first, then migration to Next.js/Laravel (PHP relevance), documentation, scale; dropped the "Facilitated communication...Agency" bullet as least relevant.
- FlowSpace Technical Responsibilities deduped (dropped the repeated "AI tool for processing of data..." line and the repeated migration line) and pruned the commute-tool bullet; kept AI tool for processing/scraping data, API integrations (OfficeRnD/Nexudus), GTM automations, CRM automation.
- Urlink pruned to the two automation/AI-building bullets, dropped the "Implementing UIs made with AI" bullet.
- UltraStrategy: kept both existing bullets (CV-parsing tool + user-profiles platform) per the AI/automation trigger (JD asks for AI-assisted development).
- Qomodo: kept the dashboard bullet, dropped the Figma-implementation bullet.
- Get2Germany: kept AI automation tools bullet + Google APIs bullet (trigger minimum) + database optimization bullet (SQL relevance); dropped the Figma-to-Bubble UI bullet.
- Clubee: kept API integration + QA/testing bullets (Git/testing JD relevance), dropped the "domain integration, shop, federation dashboard" bullet.
- Tractionboard: kept ChatGPT/OpenAI integration + "Responsive designs, de-bugging" bullets, dropped Sendgrid/Figma/Google-Ads bullets.
- Additional Information IT Skills: dropped the "Low code development/" prefix (no relation to this JD).

## Letter
CoverLetter_Openjobmetis.tex/.pdf/.txt, Italian ("Cordiali saluti", formal register), 0 em-dashes (grep-verified). Two evidence paragraphs: FlowSpace lead (live migration off a legacy stack to Next.js/Laravel, AI listing bot with Claude API + n8n, OfficeRnD/Nexudus integrations) and UltraStrategy pair (CV-parsing/scoring pipeline, Affinda + Claude API, n8n/Eden AI). States 3 years honestly, Venice location, Italy work authorisation (no sponsorship), willingness to work hybrid from Biella.

## Form answers (LinkedIn Easy Apply, 5 pages)
- Email: prabhavitg@gmail.com (pre-selected, verified).
- Phone country code: Italy (+39). Mobile phone number: 3516107807.
- Resume: re-uploaded Prabhavit_CV_Openjobmetis.pdf explicitly (picker defaulted to the stale Prabhavit_CV_Edenity.pdf from a prior job in this session; replaced via Upload resume + file chooser, verified checked/selected before Next).
- "Mark job as a top choice": left unchecked (optional).
- Additional Questions (numeric, honest, no fact-on-file for exact per-language years so used a conservative real estimate): "Quanti anni di esperienza di lavoro hai con Python?" = 2 (LLM/automation pipeline work at UltraStrategy, Get2Germany, FlowSpace data tooling). "...con Java?" = 0 (never used, honest per standing rule). "...con PHP?" = 2 (Laravel at FlowSpace, migration work).
- "Follow Openjobmetis SpA" checkbox: left at its default (checked); not a marketing/newsletter opt-in, just a LinkedIn company-follow toggle.
- Salary: not asked on this form. If asked in a follow-up, standing answer is EUR 30,000 (junior role per task instruction override; JD's own indicative RAL is 23,000-25,000).

## Result
Submitted. "Application submitted" confirmed on the job page after Submit application. Screenshot confirmations/Openjobmetis-2026-09-16.png, text confirmations/Openjobmetis-2026-09-16.txt.
