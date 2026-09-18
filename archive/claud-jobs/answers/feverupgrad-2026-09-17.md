# FeverUp - Graduate Software Engineer - Madrid, Spain

URL: https://job-boards.eu.greenhouse.io/feverup/jobs/4951979101
Status: NEEDS YOU (facts not on file). Not submitted.

## Dedupe
`python3 loop/dedupe.py --check "feverup" "https://job-boards.eu.greenhouse.io/feverup/jobs/4951979101"` -> NEW.
`grep -i "fever" applications.csv` found one prior row: FeverUp, "AI Engineer - Internal Automation (Forward Deployed)", 2026-08-26, SUBMITTED, https://job-boards.greenhouse.io/feverup/jobs/4940097101. Different requisition ID, different role/title, so it does not block this row per the dedupe rule (a SUBMITTED row only blocks the same requisition or a same-level role within 60 days; "Graduate Software Engineer" and "AI Engineer - Internal Automation" are different levels/roles). Per the task note, Fever's other postings were dropped earlier for 6+ years; this Graduate posting is different and was not previously killed.

## Live JD read in the browser (Chrome, direct navigation)
This job-boards.eu.greenhouse.io posting renders ONLY the application form (Fever logo -> "Apply for this job" -> fields). There is no descriptive job-description body (no About/Responsibilities/Requirements text) anywhere on the page above or below the form; confirmed by scrolling to the very top and reading the full page text twice. This matches the task note that "the verifier could not read the live JD" - there is no JD prose to read, only the form fields, which double as the only disclosed requirements:
- First/Last Name, Email, Country, Phone, Resume/CV*, Cover Letter (optional)
- Are you available to work onsite in the Madrid offices?* -> confirms Madrid onsite, matches the row's "likely Madrid" note.
- LinkedIn Profile (optional)
- Are you studying (or have you studied) an engineering degree or similar (mathematics, physics...)?* Yes/No -> honest answer would be No (Prabhavit's Bachelor's is Philosophy, International Studies & Economics with a minor in Entrepreneurship, not engineering/maths/physics).
- When are you able to start?*
- What is your average grade? (Out of 10)* -> dropdown, options are numeric BUCKETS ONLY: 5-6, 6-7, 7-7.5, 7.5-8, 8-8.5, 8.5-9, 9-10. No "N/A" or "not applicable" option exists.
- What's your level of proficiency in English?* / What is your level of proficiency in Spanish?* -> dropdowns (Spanish options include "Less than a B1", so an honest low-Spanish answer IS selectable; this field alone does not force a false claim or auto-kill).
- Will you now or in the future require visa sponsorship?* -> would answer Yes (Spain is not Italy; per answers/work-authorisation.md standard table).
- GDPR/privacy-consent dropdown* (required Yes/No).
- Could you upload your Transcript of Records (Expediente Academico)?* -> marked required (red asterisk), file upload only, no "skip"/"not available" option visible.
- Have you previously been employed by this company?* -> would answer No.

## Why this is NEEDS YOU (facts not on file), not a hard-gate KILL
Two required data points cannot be answered honestly from anything in OUTREACH_FACTS.md, the Master Experience file, or the JD, and cannot be invented per the material rules:
1. "What is your average grade? (Out of 10)" is a required dropdown of fixed numeric buckets (5-6 through 9-10). Prabhavit's Ca' Foscari degree would be graded out of 110 (Italian university scale), not out of 10, and no converted average grade exists anywhere in the source files. Picking any bucket would be a fabricated numeric claim.
2. "Could you upload your Transcript of Records (Expediente Academico)?" is a required file upload for an official academic transcript. No such document exists in ROOT or anywhere this session can access, and it cannot be fabricated.
Neither is a hard-gate kill in the "required years/title/degree/language/stack" sense (this is not a strict MSc/PhD gate, and the Spanish field has an honest selectable option), so this is logged as a "facts not on file" stop per the brief, not KILLED.

Note also: the "engineering degree or similar" Yes/No question is not itself a blocker (honest "No" is selectable), and is not treated as a hard gate here since it is a self-reported screening question, not a stated hard JD requirement in prose (there is no JD prose at all).

## Materials saved (ready for the user to submit manually or resume once the two facts are supplied)
- Prabhavit_CV_FeverUpGrad.tex/.pdf: built fresh from Prabhavit_CV_EN.tex (parity-diffed, no invented claims), 2 pages. Career Summary kept bullets 2+3 (AI-assisted development/API integration; business requirements to production-ready features). Technical Skills reordered Development first. FlowSpace: migration-to-Laravel + platform-scaling bullets under Product Responsibilities, OfficeRnD/Nexudus API integration + commute-time tool under Technical Responsibilities (dedup/CRM/GTM bullets dropped as in the Tanso/Konfetti passes this session). Tractionboard "Google Ads 4" bullet dropped. Additional Information: "Low code development/" dropped (JD/form has no low-code relation), Tools reordered Typescript/Laravel first.
- CoverLetter_FeverUpGrad.tex/.pdf/.txt: honest opening paragraph naming the mismatch up front (3 years professional experience, not zero; Bachelor's in Philosophy/International Studies/Economics, not engineering). Two proof paragraphs: FlowSpace (live migration, production ownership, OfficeRnD/Nexudus integrations) and Urlink (full-stack platform build, AI-assisted development, client automations, PM role) - FlowSpace is not the only proof paragraph. Madrid onsite acceptance stated. Spanish honestly described as basic. Spain work-authorisation transparency line (Italian EU LTR, not authorised in Spain, needs employer-side permit/sponsorship, ready to relocate). `grep -c` for U+2014 on the .txt returned 0.
- Standing answers ready for whoever fills the rest: years = 3 (if asked elsewhere), salary not asked on this form, English proficiency = high/advanced (no explicit C2 option seen yet, form not filled in far enough to confirm exact dropdown wording), Spanish proficiency = "Less than a B1" (honest), engineering-degree question = No, visa sponsorship = Yes, previously employed by this company = No.

Nothing was typed into Name/Email/Phone or any other field; only two dropdowns were opened to inspect their option lists (Spanish proficiency, average grade), then closed without selecting, to confirm the blocker before stopping. No data was submitted.
