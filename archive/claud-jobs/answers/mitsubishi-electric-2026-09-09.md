# Mitsubishi Electric Iconics Digital Solutions - Software Development Engineer - 2026-09-09

Job: https://www.linkedin.com/jobs/view/4464637146/ (LinkedIn "Apply" -> external redirect,
"Responses managed off LinkedIn")
Real ATS: SaaSHR, https://secure7.saashr.com/ta/6207547.careers?ShowJob=604475218
Fit: 72. Greater Genoa Metropolitan Area, hybrid, base pay disclosed EUR 30,000-60,000/yr.

STATUS: NEEDS YOU. The application was filled to 100% (all 6 steps) but blocked at the final
"Sign & submit application" step by a Consent/Acknowledgement modal requiring a password for
"(Prabhavit Gupta)" to confirm. No account was ever explicitly created and no password exists
for it; entering or setting one is out of scope for autonomous action. Tab left open
(tabId 550849764) on the completed review page for manual completion. See
confirmations/MitsubishiElectric-2026-09-09.txt for the exact blocker text.

## Hard gates re-checked on the live JD (LinkedIn jobPosting API + the SaaSHR posting page)
- Years: "1-2 years of professional software development experience (internships
  considered)" - not a >3 requirement. Pass.
- Title: "Software Development Engineer" - not Senior/Staff/Lead/Principal/Manager/CTO
  (LinkedIn's own "Mid-Senior" seniority label does not match the JD text). Pass.
- Degree: "Bachelor's degree ... preferred (or equivalent practical experience)" - has the
  equivalent-experience escape valve, not a hard MSc/PhD requirement. Note: the SaaSHR
  structured metadata field separately shows "Required Degree: Masters", which conflicts
  with the actual JD body text; treated the written requirement (with escape valve) as
  authoritative per the PATTERNS.md rule that an equivalent-experience clause is not a kill.
- Language: JD in English; no Italian requirement of any kind stated. Pass.
- Core stack: "experience with at least one programming language (e.g., Python, JavaScript,
  C#, Java, or similar)" plus REST APIs, web dev, Git, GEN AI tools, containerization/CI-CD
  awareness - all directly claimable (Python, JavaScript, REST APIs, Docker/CI-CD working
  knowledge, GEN AI/Claude Code). Not a narrow Java/.NET/C++/Go/Rust-only or cloud-admin
  role. Pass.
- Location: Genoa, Italy, hybrid - inside the EU, authorised. Pass.
- Posting live: 34 people clicked apply, posted 15 hours before this run. Pass.
No hard gate triggered.

## Dedupe
`python3 loop/dedupe.py --check "Mitsubishi Electric Iconics Digital Solutions" "https://www.linkedin.com/jobs/view/4464637146/"` returned NEW.
`grep -i "mitsubishi" applications.csv` returned no prior rows.

## What was uploaded
- Resume: Prabhavit_CV_Original_EN.pdf (verified filename on the Resume & Cover Letter step)
- Cover letter: CoverLetter_MitsubishiElectric.pdf (built from CoverLetter_MitsubishiElectric.txt
  via CoverLetter_MitsubishiElectric.tex + tectonic; 175 words, 0 em-dashes), uploaded via the
  "Choose" file control on the same step.

## Step 1 - Contact Information
- Name: Prabhavit Gupta, prabhavitg@gmail.com (from resume parse, correct)
- Address: resume parse defaulted to "Venice, USA" - corrected to Country=Italy,
  Street="Via Zanetti, 10", City="Venice", Postal Code="30175"
- Phone: +39-351-610-7807 (Home, Primary) - correct from resume parse, left as is
- Security Question (Optional): left blank

## Step 2 - Resume & Cover Letter
- Available Start Date: 09/23/2026 (two weeks from today, per standing rule)
- Referral: LinkedIn
- Required salary: 45,000.00 / year (EUR; the form's currency symbol displays as "$" but no
  separate currency selector exists - entered the numeric standing target of EUR 45,000,
  which sits inside the disclosed EUR 30,000-60,000 band)
- If referred by employee: left blank
- Objective Summary: left the resume-parsed text as is ("AI Solutions & Automation Engineer
  with hands-on experience building LLM-driven applications and intelligent workflows across
  European tech projects. Skilled in AI-assisted development, prompt engineering, and
  orchestrating complex API integrations.") - accurate and matches the claim ladder.

## Step 3 - EEO Information
- Gender: left as parsed default "Undefined" (equivalent to prefer not to say)
- Full time student?: No
- Citizenship: left BLANK - the dropdown only offers US and UK/GBR citizenship/visa
  categories (U.S. Citizen, Permanent Resident - USA, British citizen, Non British Citizen
  with valid work permit - GBR, etc.), none of which is truthful for an Indian citizen with
  Italian EU long-term residence. No accurate option existed, so it was left unanswered
  rather than picking a false one (same rule as the Greenhouse US-states-only trap).
- Ethnicity: left blank (prefer not to say)
- Primary language: English
- Secondary language: left blank
- Are you a protected veteran?: "No, I Am Not a Protected Veteran" (factual, not a
  demographic guess)
- Visa type: left blank - only Australian/US visa categories offered, not applicable
- Are you eligible to work in the country you are applying for? *: Yes (authorised in Italy)

## Step 4 - Professional References
All three reference slots left blank - optional (no asterisk), and no reference contact data
exists in the facts file to enter truthfully.

## Step 5 - Job Related Questions (all 10 required, all answered)
1. Why are you looking for a new role? - "My freelance engagement at FlowSpace, a workspace
   marketplace where I was lead developer, ended in August 2026 after we finished migrating
   the platform to Next.js and Laravel and scaling it to 4,500+ users. I am now looking for a
   role where I can keep shipping production software, ideally with more variety across
   problem domains, which is what drew me to this role."
2. What is your total salary expectation for this role? (base + variable pay) - "EUR 45,000
   total (base plus variable), in line with the posted range for this role."
3. Do you have employment authorization to work in the country where the job is located? -
   Yes
4. Do you now or in the future require employment sponsorship/visa? - No
5. Are you comfortable with a Hybrid work environment? (3 days in office may be required) -
   "Yes. I am currently based in Venice and would relocate closer to Genoa for this role so I
   can reliably be in the office for the required in-person days."
6. Do you have reliable transportation to your work location? - "Yes, once relocated to the
   Genoa area I will have reliable transportation to the office."
7. When are you available to start? - "I am available to start two weeks after an offer,
   around 23 September 2026."
8. Can you please share why you left your previous role? - "My previous role was a freelance
   engagement at FlowSpace that was scoped around the platform migration and growth phase I
   was hired for. That phase wrapped up in August 2026 once the platform was fully migrated
   to Next.js and Laravel and had scaled past 4,500 users, so the engagement ended on its own
   timeline rather than me leaving mid-project."
9. Explain, in as much detail as you can, exactly what happens from the moment you press
   Enter on a prompt to an AI coding assistant until code appears in your editor - detailed
   technical answer covering context assembly, the HTTPS request to the model provider,
   token-by-token streaming generation, the agent tool-call loop (read/edit/bash execution
   fed back into context), the diff/file-write the harness applies, and the editor's
   filesystem watcher picking up the change. Written from direct experience using Claude Code
   daily. Full text is in the submitted form (see screenshot/field content).
10. Pick a small, concrete feature... write the specification you would hand an AI agent -
    chose a "Copy API key" button next to a masked key field; specified exact behavior,
    accessibility, security constraint (never copy the masked string, never log the raw key),
    a definition of "correct," a Playwright verification plan (stubbed clipboard, keyboard
    path, failure path), and named failure modes an agent could hit (copying the masked
    display text instead of the real key, skipping the permission-denied path, using a legacy
    execCommand fallback without an HTTPS check).

Questionnaire modal confirmed "Completed - Questionnaire successfully submitted" after these
were entered.

## Step 6 - Review (100% complete, all 6 sections shown correctly)
Reviewed every section on the summary page before attempting to submit; all fields matched
what was entered above. No signature field or additional consent checkboxes existed beyond
the password modal that blocked the final click.
