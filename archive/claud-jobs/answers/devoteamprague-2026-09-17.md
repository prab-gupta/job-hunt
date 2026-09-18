# Devoteam - Forward Deployed Engineer, GenAI, Prague - 2026-09-17

URL: https://www.linkedin.com/jobs/view/4452358576/
ATS: LinkedIn Easy Apply (SmartRecruiters, 8-page flow)
Task: FDE-ALL rule row (agent C61). Prague/Czechia line; note that Devoteam Milan was applied to yesterday (different requisition, Italian JD) so this is a separate row.

## Dedupe
`python3 loop/dedupe.py --check "Devoteam" "https://www.linkedin.com/jobs/view/4452358576/"` -> HIT COMPANY
`grep -i "devoteam" applications.csv`: two prior rows, both for the Milan "AI Forward Deployed Engineer" requisition (URL .../4446991563/, Italian JD) - 2026-08-06 LEAD and 2026-09-16 SUBMITTED. Different URL, different city, different language from this Prague/GenAI requisition, so not a block per the brief (only a SUBMITTED row for the SAME requisition blocks).

## Hard gates
Cheap check + live page: Easy Apply present, no closed banner, no prior application-submitted state.
JD: "Fluency in English." is the only language requirement stated; "Google Cloud Experience is Helpful, but Not Required." No Czech mentioned anywhere in the JD body. Checked the full 8-page Easy Apply flow for a language screening question - none appeared. Requirements: multi-year experience (fits honest 3), degree or equivalent practical experience (not a hard MSc/PhD gate), Python + GenAI frameworks (LangGraph, LangChain, CrewAI, Google ADK) - claimable stack, no anti-AI disclaimer. Passed all gates.

## CV
Reused Prabhavit_CV_Devoteam.pdf/.tex from the 2026-09-16 Milan row per task instruction ("parity-check and reuse"). Re-diffed against the current Prabhavit_CV_EN.tex: only reordering and deletion, no invented text (Career Summary 2 bullets, FlowSpace Product Responsibilities led with the AI-agents bullet, Technical Responsibilities led with the AI listing tool, UltraStrategy both bullets kept, Get2Germany led with the AI-automation bullet, "Low code development/" prefix dropped). Re-uploaded through the Easy Apply Resume step (LinkedIn assigns a new timestamp on re-upload of the same filename/content); verified selected at the top of the resume list.

## Cover letter
New file: CoverLetter_DevoteamPrague.pdf/.txt/.tex, deliberately given a distinct slug from CoverLetter_Devoteam (the Italian Milan letter) to avoid the near-miss overwrite pattern documented in loop/LEARNINGS.md (2026-09-16 23:20 Accenture incident). 0 em-dashes grep-verified. English. FlowSpace lead paragraph (live migration off a legacy stack to Next.js/Laravel, 2,000 to 4,500+ users, support AI agent, AI listing bot 900+ drafts, TypeScript/Next.js/Node.js/Laravel/n8n/Claude API) paired with UltraStrategy (CV-parsing pipeline, Affinda + Claude API, n8n/Eden AI extraction tool) per the GenAI/agentic role mapping. Honest 3 years. Czechia work-authorisation transparency line: Italian EU LTR status, not currently authorised in Czechia, needs employer-side permit/sponsorship, ready to relocate or work on-site with clients.
Uploaded via a separate "Upload cover letter" control, found only by clicking Edit on the Review page's Cover letter section (not present as its own numbered page in the 8-page flow) - this differs from the other three rows today, which had no cover letter field at all.

## Standing answers given (page 6, Additional Questions)
- Availability (expected start date): "Immediately available; can start within two weeks of an offer."
- Salary expectations (monthly gross, CZK or EUR): "EUR 3,750 gross monthly (EUR 45,000 gross annually)" - computed from the standing EUR 45,000/year rule since the JD states no salary band.
- Type of cooperation: Employment (checked), Contractor (left unchecked).
- Why interested in this position: production GenAI systems, not just prototypes, working directly with client engineering teams.
- Why interested in the company: Devoteam's production GenAI/cloud scale and Google Cloud expertise, matching the AI-agent and migration work already done at FlowSpace.
- Hybrid model: "Yes, I am open to relocating to Prague and working the hybrid model."
- Required privacy-notice consent checkbox: ticked.
All six free-text fields were filled with `form_input` (not the `type` action) after the Cresta row showed `type` can silently drop characters under load on a long answer.

Work experience (page 4) and Education (page 5) were pre-filled accurately from the LinkedIn profile (FlowSpace/Ca' Foscari/G.D. Goenka/Millennium School Lucknow) and left unedited, matching the Milan row's precedent.

## Submission
Reviewed page 8/8 (contact info, CV filename Prabhavit_CV_Devoteam.pdf, cover letter filename CoverLetter_DevoteamPrague.pdf) before clicking Submit application. Job page's own Application status panel showed "Application submitted" immediately after.
