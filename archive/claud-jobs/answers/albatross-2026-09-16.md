# Albatross AI - Forward Deployed Engineer - 2026-09-16

URL: https://www.linkedin.com/jobs/view/4467739665/
ATS: LinkedIn Easy Apply
Task: LI-PICK-style FDE-sweep row. An earlier Albatross posting (Himalayas, 2026-08-24) was DROPPED for "posting requires engineering or computer science degree; candidate has a non-technical BA". Task instructs applying anyway and answering the degree question honestly (Bachelor).

## Dedupe
`python3 loop/dedupe.py --check "Albatross AI" "https://www.linkedin.com/jobs/view/4467739665/"` -> HIT COMPANY
`grep -i "albatross" applications.csv`:
- 2026-08-24 Albatross AI, Forward Deployed Engineer, Himalayas, DROPPED - technical degree required (different ATS/posting, not SUBMITTED/INTERVIEW/REJECTED)
- 2026-08-26 Albatross, Forward Deployed Engineer, Workable (Spain), LEAD (different posting, not blocking)
Neither row is SUBMITTED/NEEDS YOU/INTERVIEW/REJECTED for this exact requisition, and DROPPED/LEAD do not block per the brief. Proceeding per task's explicit instruction to apply anyway.

## Cheap check + hard gates
`curl -s -A "Mozilla/5.0" jobPosting/4467739665 | grep -c apply-button` = 1 (live). Easy Apply button present on the live page, no "no longer accepting applications" banner.
JD (About the job, read live via Playwright): Remote, right to work and travel in Europe. Requirements: Degree in engineering or computer science; Python or another scripting language; strong analytical skills; customer-facing technical role experience; excellent communication; comfortable in fast-paced environment; product/business judgment; Fluent English (other languages an advantage, none required); Eligible to work in Europe. Salary band EUR 50k-60k.
- Degree clause present as in the earlier DROPPED Himalayas posting -> per this task's explicit instruction, apply anyway and answer the degree question honestly as Bachelor's (Philosophy, International Studies & Economics, Ca' Foscari University of Venice) if/when asked, no fabrication of a CS/engineering degree.
- No language kill (English only required).
- No anti-AI disclaimer found in the JD text.

## CV
Prabhavit_CV_Albatross.tex/.pdf built from Prabhavit_CV_EN.tex (parity-diffed, reorder/delete only, verified via diff against EN.tex - only deletions and the standing "Low code development/" prefix drop, no added text). Career Summary trimmed to 2 bullets (dropped the prompt-engineering/API-orchestration bullet). FlowSpace Product Responsibilities led with AI agents/scale/migration, dropped the Agency-communication bullet. FlowSpace Technical Responsibilities led with OfficeRnD/Nexudus + AI listing tool + CRM/GTM, deduped the two repeated lines in the master doc, dropped the commute-calculator bullet. Get2Germany reordered to lead with AI automation tools + Google APIs, dropped the Figma/UI bullet. UltraStrategy kept both bullets (AI/automation trigger). Tractionboard trimmed to ChatGPT/OpenAI integration + Responsive designs/de-bugging. Qomodo and Clubee unchanged (already minimal, both relevant). Compiled with tectonic, 2 pages verified via pypdf.

## Cover letter
CoverLetter_Albatross.tex/.txt/.pdf built, English, 0 em-dashes (grep-verified). Lead role FlowSpace (legacy-stack migration, AI listing bot 900+ drafts, support AI agents) paired with Get2Germany (Google APIs integration, AI discovery tools for courses/internships/jobs, database optimisation) per the OUTREACH_FACTS role-to-JD map ("API integrations, search or discovery automations, Google APIs -> Get2Germany"), a good match for Albatross's "real-time discovery" platform. Honest 3-years framing implicit (no explicit years claim beyond "three years of experience"). Closing uses the remote-from-Italy work-authorisation transparency line (role is remote-across-Europe with right to work and travel in Europe, not tied to one specific non-Italy country, so the Italy-remote line applies rather than a single-country sponsorship line).

## Standing answers for the Easy Apply form
- Years of experience: 3
- Salary: EUR 50,000 (bottom of the JD's own 50k-60k band per the standing rule to align to the bottom of a higher band)
- Degree: Bachelor's (Philosophy, International Studies & Economics) - answered honestly if a degree-field question appears, per task instruction
- Work authorisation / eligible to work in Europe: Yes (Italian EU long-term resident, authorised to work from Italy)
- Relocation: Yes, anywhere in EU
- Phone: +39 351 610 7807
- Language: English C2/fluent, Italian conversational
