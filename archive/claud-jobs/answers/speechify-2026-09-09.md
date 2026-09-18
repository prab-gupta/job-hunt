# Speechify - Software Engineer, Platform - 2026-09-09

URL: https://job-boards.greenhouse.io/speechify/jobs/5976192004
ATS: Greenhouse (job-boards.greenhouse.io/speechify)
Fit: 78

## Gate re-check on live JD (curl boards-api.greenhouse.io/v1/boards/speechify/jobs/5976192004)
- No numeric years-of-experience threshold stated.
- Title: "Software Engineer, Platform" - not Senior/Staff/Lead/Principal/Manager.
- No MSc/PhD requirement.
- JD in English, no German/French language requirement stated anywhere (company is 100% distributed, no office).
- Core stack: "Proven experience in backend development: TS/Node (required)" - directly claimable. GCP is listed as wanted but not claimed (see below).
- Location: same requisition (id 5976192004) is cross-posted for Berlin/Frankfurt/Toulouse/Paris; applied ONCE per instructions.
- No kill gate hit. Posting live and rendering (not a 404/closed board).

## Dedupe
`python3 loop/dedupe.py --check "Speechify" "https://job-boards.greenhouse.io/speechify/jobs/5976192004"` -> NEW.
`grep -i speechify applications.csv` -> no prior rows.

## Fields entered
- First Name: Prabhavit / Last Name: Gupta
- Email: prabhavitg@gmail.com
- Country: +39 (Italy) / Phone: 351 610 7807
- Resume/CV: Prabhavit_CV_Original_EN.pdf (removed a MyGreenhouse-autofilled stale "Prabhavit_CV-.pdf" first, per the known Greenhouse trap)
- Cover Letter: CoverLetter_Speechify.pdf (built from CoverLetter_eduBITES.tex template via tectonic, 1 page, no em-dashes)
- LinkedIn Profile: https://www.linkedin.com/in/prabhavit (pre-filled by MyGreenhouse autofill, left as-is, correct)
- How did you hear about this opportunity?: LinkedIn
- Why do you want to work at Speechify? (free text, 658 chars): Speechify's mission (turning any document into audio so reading is never a barrier) tied to FlowSpace backend ownership - TS/Node APIs, Supabase/PostgreSQL booking flows, OfficeRnD/Nexudus integrations - mapped to the Platform team's mandate (payments, subscriptions, auth, APIs); closed with wanting to work on a fully distributed team.
- What is one of the hard technical problems you have worked on? (free text, 703 chars): FlowSpace's AI listing pipeline - multi-format ingestion (PDF/website/spreadsheet/photo) to structured, validated listing; hard part was orchestration (format classification, multi-step agentic extraction, fact/photo verification, recovering from incomplete/contradictory sources), now running across 900+ listings. Traces to Prabhavit - Master Experience.md "AI listing bot" section.
- Where are you located?: Western Europe (only region-level dropdown offered, no city/country granularity; Venice, Italy falls under this)

## Voluntary Self-Identification (EEO)
- Gender: Decline To Self Identify
- Are you Hispanic/Latino?: Decline To Self Identify
- Veteran Status: I am not a protected veteran (factually true, not a demographic guess)
- Disability Status: I do not want to answer

## Work authorisation / location note
Not asked as a separate explicit Yes/No field on this form (no such question rendered). Location answered as Western Europe / cover letter and free-text answers state Venice, Italy base, remote-from-Italy, authorised under Italian EU long-term residence, no sponsorship needed. Did not claim Germany/France residence anywhere. GCP/cloud-admin experience NOT claimed anywhere (guardrail: never claim cloud admin AWS/GCP/Azure) - answers stayed to TS/Node, Supabase/PostgreSQL, OfficeRnD/Nexudus, LLM pipeline, which are all claimable per the brief and Master Experience file.

## Salary
Not asked on this form. JD states "Germany Based Salary range... 30,000-120,000 USD/Year + Bonus + Stock depending on experience" (wide/likely templated range) - no field to enter a figure, so standing EUR 50,000 answer not needed.

## Outcome
Submitted successfully. Confirmation page at /confirmation: "Thanks for applying... Your application has been successfully submitted." Optional post-submit coding-exam Google Form link shown but not completed (out of scope, Prabhavit's call).
