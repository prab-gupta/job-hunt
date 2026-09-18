# Google - AI Outcome Customer Engineer, Forward Deployed Engineering - Madrid - 2026-09-17

LinkedIn URL: https://www.linkedin.com/jobs/view/4467197803/
Applied direct: https://www.google.com/about/careers/applications/apply/412c3e01-0453-49eb-9317-d7d2df100fb9/form
(also findable at https://www.google.com/about/careers/applications/jobs/results/124343651391152838-ai-outcome-customer-engineer-forward-deployed-engineering-google-cloud)

## Status: NEEDS YOU (profile filled and saved, final submit blocked by a site bug)

## Dedupe
`python3 loop/dedupe.py --check "Google" "https://www.linkedin.com/jobs/view/4467197803/"` returned HIT COMPANY~ (fuzzy). Checked every "google" hit in applications.csv: all were unrelated mentions (Google Sheets, Google Places autocomplete, a BIP "Google practice" role, etc.), no real prior Google application. Treated as NEW.

## CV tailoring (Prabhavit_CV_GoogleFDE.tex/.pdf)
Built from Prabhavit_CV_EN.tex, parity-diffed (only reordering/pruning, two sub-bullet-list reorderings, no new text). FlowSpace Technical Responsibilities led with the API-integration bullet (OfficeRnD/Nexudus) to match the JD's "Interfaces (APIs)" qualification. Get2Germany reordered to lead with the Google-APIs-integration bullet (direct relevance to the employer). UltraStrategy kept both bullets per the AI/automation minimum rule. 2 pages confirmed via pdfinfo.

## Cover letter (CoverLetter_GoogleFDE.txt/.pdf)
FlowSpace (API integrations, live Next.js/Laravel migration, support agent) as lead paragraph, paired with Get2Germany (Google APIs integration) and UltraStrategy (Affinda/Claude API CV-parsing pipeline) as the second proof paragraph. Honest that 3 years falls short of the 7 years asked. Spain work-authorisation transparency line verbatim from answers/work-authorisation.md. 0 em-dashes (grep-verified). 323 words.

## Sign-in
Chrome was already signed in as prabhavit (prabhavitg@gmail.com) per the task's instruction; that session was used throughout. No login page, no 2-step-verification prompt appeared at any point, so the "stop and log NEEDS YOU with the exact wall" login-wall condition from the task did not trigger.

## What was filled (Careers profile, step 1 of 4)
- Legal name: Prabhavit / Gupta
- Address: Italy, Venice, 30175
- Phone: Italy +39 351 610 7807
- Resume: Prabhavit_CV_GoogleFDE.pdf uploaded and auto-parsed by Google's own resume parser
- Higher education: Ca' Foscari University of Venice, Bachelor's Degree - Other, Graduated, "Philosophy, International Studies, Economics", Italy
- Alphabet-experience question: No
- Applying for first job: No
- Work experience: all 7 roles present and completed (the resume parser filled job titles, start/end months, and some countries automatically but left every Employer name blank and several Country/City fields blank; these were filled in and verified by direct DOM value inspection):
  1. FlowSpace, Lead Developer, Mar 2024-ongoing, London, United Kingdom
  2. Urlink, Project Manager, Apr-Jul 2025, Barcelona, Spain
  3. Qomodo, Low-Code Developer, Jan-Jun (parser-assigned months), Milan, Italy
  4. UltraStrategy.com, Automation Developer, Dec 2024-May 2025, France (no city given in the CV)
  5. Clubee.com, Low Code Developer, Sep 2023-Aug 2024, Foetz, Luxembourg
  6. Get2Germany.com, Lead Developer, Jan-May 2024, Berlin, Germany
  7. Tractionboard.co, Low-Code Developer, Aug-Oct 2023, Utrecht, Netherlands
- Personalize-profile question: No
- Both required consent checkboxes (privacy policy consent, information-accuracy certification): ticked
- Confirmed saved: the page's own "Last updated today at 12:12 AM" timestamp advanced as fields were edited, confirming server-side persistence under this application id.

## The blocker
Clicking "Submit profile & continue" (tried many times, both button instances on the page, and again after a full page reload) never advances past step 1. Chrome's network log shows, on every click:
- `POST .../HiringCportalFrontendUi/jserror?...&error=W_jd%20is%20not%20defined` (204)
- Two `POST .../HiringCportalFrontendUi/cspreport` calls fire at page load, before any interaction

This points to a genuine Content-Security-Policy conflict between Google's strict CSP on this page and the Claude-in-Chrome automation extension's own injected content scripts, leaving a variable ("W_jd") that Google's own submit-validation code depends on undefined, so every submit click fails with a generic "Missing response to a required question" toast. This was checked exhaustively for a real missing field first: every required radio group has an answer, all 7 job entries are complete (employer, title, dates, country, city), and no `mat-error`/`role=alert` element anywhere in the DOM is actually visible/populated. This is an automation-environment incompatibility with this specific ATS, not a data problem and not the login/2FA wall the task anticipated.

## What's needed
Open the same URL (https://www.google.com/about/careers/applications/apply/412c3e01-0453-49eb-9317-d7d2df100fb9/form) signed in as prabhavitg@gmail.com in a normal browser session (or via Playwright, which does not inject the same content scripts) and click "Submit profile & continue" to complete step 1, then finish steps 2-4 (Role Information, Voluntary self-identification, Review & apply). All data is already filled and saved.
