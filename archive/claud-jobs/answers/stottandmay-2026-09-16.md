# Stott and May - Forward Deployed Engineer (Helsinki) - 2026-09-16

USER FDE-ALL rule 2026-09-16: rows 1-2 apply regardless of fit/years/seniority/agency/stack; agency posting per task note, apply anyway.

## Dedupe
`python3 loop/dedupe.py --check "Stott and May" "https://www.linkedin.com/jobs/view/4459983157/"` -> NEW. `grep -i stott applications.csv` -> no prior rows.

## Hard gates
No anti-AI disclaimer. English JD. No hard MSc/PhD requirement. On-site Helsinki, Finland. JD asks 5+ years and mentions "2+ years of work experience with AI Solutions" as poster-added requirement (not a kill under FDE-ALL rule). No core-stack disqualifier (general software engineering / systems / integrations). Finnish proficiency asked as a dropdown with a "None" option, not a hard requirement, so not a language kill. Cheap check apply-button count = 1, live Easy Apply button present, no prior application-submitted banner before this run.

## CV
Prabhavit_CV_StottAndMay.tex/.pdf built fresh by copying the already parity-verified Prabhavit_CV_Triple.tex content (identical FDE/AI-agent/enterprise-integration JD theme, same tailoring decisions apply, no company-specific text inside the CV body) and compiling with tectonic: 2 pages, photo included. Diffed again against Prabhavit_CV_EN.tex to confirm every line still traces verbatim (same deltas as the Triple build: Career Summary trimmed to 2 bullets, FlowSpace AI-agent bullet led, dedup of the duplicate Bubble.io migration bullet, dropped the commute-times bullet, Urlink automations bullet led). Uploaded explicitly via the Easy Apply "Upload resume" control (library default had defaulted to a stale Prabhavit_CV_RecT.pdf from a different concurrent application); verified Prabhavit_CV_StottAndMay.pdf selected and shown on the Review page.

## Letter
CoverLetter_StottAndMay.tex/.pdf/.txt built fresh. Lead FlowSpace (production support AI agents, OfficeRnD/Nexudus integrations, live migration) paired with Urlink (client-driven automations, PM on client requirements), matching the JD's customer-facing AI-agent deployment theme. Honest 3 years vs JD's 5+ ask. Finland work-authorisation transparency line included (Italian EU LTR does not auto-extend to Finland, ready to relocate to Helsinki). Em-dash check: grep count on U+2014 = 0. No cover-letter field on this Easy Apply form, kept on file.

## Form fields (4-page Easy Apply)
1. Contact info: email prabhavitg@gmail.com (pre-selected correct), phone country code Italy +39 (pre-selected correct), mobile number field was empty, filled 3516107807.
2. Resume: library defaulted to a different stale CV (Prabhavit_CV_RecT.pdf, presumably from a concurrent application in this session); clicked Upload resume, uploaded Prabhavit_CV_StottAndMay.pdf, verified checked/selected.
3. Additional Questions: "How many years of work experience do you have with AI Solutions?" = 3 (standing years answer). "Will you now or in the future require sponsorship for employment visa status?" = Yes (Finland is not Italy, per answers/work-authorisation.md). "What is your level of proficiency in Finnish?" = None.
4. Review: verified all fields correct (contact info, resume filename, all three additional-question answers). Unchecked the default-ticked "Follow Stott and May" checkbox.

## Result
SUBMITTED. Job page Application status panel shows "Application submitted" (success toast not captured in the post-submit snapshot but the status panel confirms). Screenshot: confirmations/StottAndMay-2026-09-16.png, text record confirmations/StottAndMay-2026-09-16.txt.

## Note for LEARNINGS
Confirms the 08:15 shared-browser-surface learning: this row's resume-library default (Prabhavit_CV_RecT.pdf) was not the last file this agent uploaded (Prabhavit_CV_Triple.pdf from row 1 immediately prior), meaning another concurrent apply agent was uploading resumes to the same LinkedIn account's shared resume library in parallel. Explicit re-upload + verify-selected remains mandatory every time; no new LEARNINGS line needed since this is the same documented failure mode.
