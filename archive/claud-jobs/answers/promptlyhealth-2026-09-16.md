# Promptly Health (Portugal) - Forward Deployed Engineer - 2026-09-16

URL: https://www.linkedin.com/jobs/view/4446732955/

USER RULE 2026-09-16: apply to every FDE posting on LinkedIn in Italy/EU, no kill for fit/years/seniority/agency/stack. Portugal line, offsite, honest about no healthcare background (task note).

## Dedupe
`dedupe.py --check "Promptly Health" <url>` returned NEW. No prior row. Proceeded.

## Hard gates
JD's primary requirement is "demonstrable blended healthcare domain knowledge" and trust built inside healthcare organisations - Prabhavit has neither. Per the standing FDE-blanket rule this is a fit gap, not one of the three listed kill reasons (closed, duplicate submission, missing language), so the row proceeds with the gap stated plainly in the letter rather than invented. No required language beyond English; JD is English throughout, Portugal is the listed location but no Portuguese requirement appears. No anti-AI clause in the JD text (the "How We Build With AI" section in fact expects AI-assisted development).

## CV tailoring (Prabhavit_CV_PromptlyHealth.tex/.pdf, from the verified Prabhavit_CV_Harmattan.tex base)
- Career Summary: default 2 bullets unchanged.
- Technical Skills reordered: AI/ML first, then Development (Claude Code, Laravel, Typescript - the "modern application stack" the JD says it will accept in place of a software-engineer title), then Automation, then Project/Design.
- FlowSpace, UltraStrategy, Urlink, Get2Germany, Qomodo, Clubee, Tractionboard bullet sets unchanged from the Harmattan base (verbatim from Prabhavit_CV_EN.tex). No healthcare-specific claim added anywhere - none exists on file to add.
- Compiled 2 pages via tectonic.

## Cover letter
CoverLetter_PromptlyHealth.pdf/.txt. Lead FlowSpace (AI listing bot with human-in-the-loop and confidence-based escalation - the closest evidence to "build in the sandbox, ship to production, own the outcome"), paired with UltraStrategy (CV-parsing pipeline: Affinda + Claude API, data extraction and scoring delivered to a live frontend - evidence of the "data work" and "own evaluation" themes the JD stresses). States plainly and early that he has no healthcare-domain background or track record inside clinical/health organisations, so the letter does not claim the JD's primary requirement; it frames the application as the Python/SQL/AI-product technical layer the JD says it will accept without the software-engineer title, while being explicit the domain-trust requirement is unmet. 0 em-dashes.

## Standing answers
Years: 3. Salary: EUR 45,000-55,000 (no band in JD). Work authorisation: Portugal = No/Yes sponsorship, transparency line added. Italian: conversational. Driver's license: No.

## Form fill attempt (RETRY PLAYWRIGHT)
Reached the real application form at https://people-jobs.com/promptlyhealth/apply/2ccaed54-a839-4f4b-b703-38499c6e6fd1?utm_source=linkedin&utm_campaign=revolut_people (Revolut People ATS, via LinkedIn Apply redirect). The entire form renders with NO elements visible to Claude in Chrome's accessibility tree - `find` and `read_page` both return empty/no-match for every field (Full name, Email, even generic "input field"), and `get_page_text` reports "canvas-based content". This matches the brief's shadow-DOM/unreachable-widget case exactly; nothing on this form can be filled or clicked from Chrome.

Full field map read visually via screenshots, for a Playwright agent to fill:
- CV / Resume upload (drag & drop dropzone, "Apply with CV" tab already selected vs "LinkedIn Profile" tab) -> Prabhavit_CV_PromptlyHealth.pdf
- Additional link field (optional) -> can add https://www.linkedin.com/in/prabhavit/ and/or https://github.com/prab-gupta/llm-doc-parser
- General information: Full name = Prabhavit Gupta; Email = prabhavitg@gmail.com; Phone (optional) = +39 351 610 7807; Current company = FlowSpace; Current country = change from default "United States" to Italy; Preferred work locations = Portugal / Remote Europe
- Education: Add -> Ca' Foscari University of Venice, Bachelor's, Philosophy/International Studies & Economics (per Prabhavit_CV_EN.tex)
- Expected package: Q1 expected base salary range (EUR gross/year) = 45000-55000; Q2 expected variable component = 0 / not applicable
- English Proficiency: C2 - Proficient/Native (honest, per standing answers)
- Years of work experience: 2-3 years (closest bucket to 3; if a "3-5" style bucket existed it would be preferred, but this form's buckets are 0-1/2-3/4-6/7-9/10+, so 2-3 is the honest closest fit for "3 years")
- Other relevant skills & experience:
  Q1 healthcare organisations experience -> "I have no professional experience working with healthcare organisations." (honest, matches the letter's disclosure)
  Q2 programming experience (Python/SQL) -> closest honest pick is "I have professional experience with Python or SQL, but not both" (Python used for automation/scraping, SQL via Supabase/Postgres queries, not "regularly develop production-quality applications using Python and SQL" as his main stack is TypeScript/Laravel) - use judgement, do not pick the top option, it overstates
  Q3 built solutions used by clinicians/healthcare ops/patients in live healthcare -> "No."
  Q4 willing to travel regularly to client sites across Europe and UK -> "Yes"
- Interview transcripts AI consent (optional, does not affect prospects) -> "Yes, I consent" is a reasonable neutral pick, or leave as the user prefers
- "I agree that my data will be used to assess my suitability for other roles" checkbox -> leave UNTICKED (standing rule: talent-pool/other-roles checkboxes stay unticked)
- Applicant declaration is informational text above Submit application, no separate checkbox to tick
- Click "Submit application" only after uploading the CV and confirming all of the above

No separate cover letter upload field exists on this form; CoverLetter_PromptlyHealth.pdf/.txt is built and on file but cannot be attached here.

## RETRY RESULT (2026-09-17, Playwright)
Reopened the same URL in Playwright: the whole form was fully visible/fillable (unlike Claude in Chrome, which reported a canvas-based, no-elements page). Uploaded Prabhavit_CV_PromptlyHealth.pdf, filled General information (Full name, Email, Phone, Current company=FlowSpace, Current country=Italy changed from default United States), Preferred work locations=Europe, added an Education entry (University of Venice / International Relations / Bachelor's degree or equivalent / Oct 2020 - Jun 2024, the closest catalogue values to Ca' Foscari University of Venice's Philosophy, International Studies & Economics degree), Expected package (45000-55000 base, 0 variable), English C2, Years of experience=2-3 (closest bucket to 3), the four Other-relevant-skills checkboxes exactly as documented in the original answers above, Interview-transcript AI consent=Yes, left the other-roles marketing checkbox unticked. First Submit click surfaced a validation error: the "Add additional link" field (LinkedIn/Github/portfolio) was in fact REQUIRED despite no visible asterisk; added https://www.linkedin.com/in/prabhavit/ and resubmitted. Success dialog: "Thank you for your application! We will be in touch with you shortly." SUBMITTED. See applications.csv row 2026-09-17 and confirmations/PromptlyHealth-2026-09-17.png/.txt.
