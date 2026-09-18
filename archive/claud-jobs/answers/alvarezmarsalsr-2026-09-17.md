# Alvarez & Marsal (Madrid) - Senior AI Forward-Deployed Engineer / Architect - 2026-09-17

URL: https://www.linkedin.com/jobs/view/4458007625/
Apply routes to: https://careers.alvarezandmarsal.com/jobs/18176752-senior-ai-forward-deployed-engineer-slash-architect -> Talemetry embedded apply widget (cross-origin iframe), same tenant as the AI Forward-Deployed Engineer role (job 18176750) submitted an hour earlier.

## Dedupe
`python3 loop/dedupe.py --check "Alvarez & Marsal" <url>` = HIT COMPANY (existing SUBMITTED row for job 18176750, a different requisition). Confirmed different LinkedIn URL (4458007625 vs 4457793675) and different careers.alvarezandmarsal.com job slug (18176752 vs 18176750). Not blocking per task instruction; proceeded.

## Hard gates
No anti-AI disclaimer. English JD. No hard MSc/PhD (just "several years" experience, no number). "Fluent English; Spanish strongly advantageous" - advantageous not required, not a language kill. Senior/Architect title explicitly included per USER RULE 2026-09-16 (apply to every FDE posting, seniority no kill).

## CV reuse (parity check)
`diff <(grep -o '\item.*' Prabhavit_CV_EN.tex | sort) <(grep -o '\item.*' Prabhavit_CV_AlvarezMarsal.tex | sort)` showed ONLY deletions from the EN.tex master (bullets dropped, none added/invented) - clean parity pass. Reused Prabhavit_CV_AlvarezMarsal.pdf as-is, no rebuild needed.

## Cover letter (new: CoverLetter_AlvarezMarsalSr.pdf/.txt)
Lead FlowSpace (sole technical ownership of the AI listing bot + support agents architecture, end to end) paired with UltraStrategy (CV-parsing pipeline: Affinda + Claude API + n8n + Eden AI orchestration). Honest paragraph: 3 years experience, no team-leadership track record, no enterprise-platform (SAP BTP/Salesforce Agentforce/Microsoft Copilot Studio) architectural sign-off - stated plainly rather than inflated against the senior/architect title. Spain work-authorisation transparency line. 0 em-dashes (grep-verified before use).

## Talemetry resume-parser trap (matches LEARNINGS 2026-09-17 00:10 and the earlier AlvarezMarsal submission)
Of 8 parsed Work History rows:
- 1 pure junk row (Company Name - Job Title, 2000-Current) - deleted.
- FlowSpace.co - Lead Developer (2024-03 - Current) - parsed correctly, left as-is.
- Qomodo - AI and Low-Code Developer (2024 - 2025-01) - parsed correctly, left as-is.
- "Company Name - Automation Developer" (2024-12 - 2025-05, flagged Requires Attention) - fixed to Company=UltraStrategy, City=France (matches OUTREACH_FACTS dates).
- "Get2Germany.com - Project Manager and AI Assisted Developer" (2025-04 - 2025-07) - dates/title actually match Urlink, company mislabelled; fixed Company=Urlink, City=Barcelona.
- "Qomodo - Low Code Developer & Quality Assurance" (2023-09 - 2024-08) - dates/title actually match Clubee, company mislabelled; fixed Company=Clubee, Job Title=Developer and QA, City=Foetz, Luxembourg.
- "Company Name - Lead Developer and Automation Specialist" (2024-01 - 2024-05, flagged Requires Attention) - dates match Get2Germany; fixed Company=Get2Germany, Job Title=Developer and Automation Specialist (dropped the mashed "Lead"), City=Berlin.
- "Company Name - Low-Code Developer" (2023-08 - 2023-10, flagged Requires Attention) - dates match Tractionboard; fixed Company=Tractionboard, Job Title=Developer, City=Utrecht.
Education parsed 4 rows: Microsoft - Introduction to building AI agents (cert, correct), Microsoft Copilot Studio Agent Academy - blank Degree (set to "Certificate", no fabrication), Tray.AI Build Practitioner (cert, correct), Ca' Foscari University of Venice - Bachelor's (Oct 2020 - Jun 2024, correct, no edit needed).

## Contact/address (step 1 and step 3)
First/Last name pre-filled by Talemetry account memory (Prabhavit/Gupta). Email prabhavitg@gmail.com, Mobile +39 351 610 7807 (Italy +39 country code), base compensation 45000, top location preference Madrid, country of residence Italy. Address: Via Zanetti, 10 / Venice / Venezia (Italy province) / 30175 (matches the established convention used across other applications in answers/*.md).

## Job-related questions (step 4)
Legally eligible to work in Spain = No, I require a work permit / visa sponsorship. Will require sponsorship = Yes. Able to work in office = Yes. Travel frequency = Weekly. Ever employed by A&M = No. Family at A&M = No. Non-compete = No. Outside activity/conflict = No. Aware of A&M services to prior employer = No. Government official = No. Free-text follow-ups answered N/A.

## Submission
Additional Documents step: uploaded CoverLetter_AlvarezMarsalSr.pdf in the "E.g., Cover Letter" slot (11 KB, confirmed attached). Final page: Submit implies terms consent per the page's own wording, no separate checkbox. Clicked Submit -> landed on https://careers.alvarezandmarsal.com/pages/thank-you: "Thank You! Application Confirmation - Thank you for your application. You will soon receive an email confirmation, which will allow you to check the status of your application." SUBMITTED.
