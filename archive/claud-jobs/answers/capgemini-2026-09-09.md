# Capgemini Engineering - Software Engineer (Marcon, Veneto) - 2026-09-09

Status: NEEDS YOU. Blocked by mandatory account creation on Capgemini's SuccessFactors ATS
before any application field could be reached, so no free-text answers were submitted. This
file records the gate check, dedupe decision, and the material ready for the user to use.

## Hard gates re-checked on the live JD (Italian; JD text fetched via LinkedIn jobs-guest API
and cross-checked on the Capgemini careers page, identical text, req 436075-en_GB)

- Anti-AI disclaimer: none found.
- Language: JD is in Italian, role is on-site in Italy (Marcon, Veneto) - acceptable per the
  Italy-role precedent. No mandatory-Italian phrase present ("ottima conoscenza della lingua
  italiana", "madrelingua" do NOT appear). JD only asks for "Conoscenza dell'inglese tecnico"
  (technical English). Not a KILL.
- Years required: not specified as a number. Not a KILL.
- Title: "Software Engineer" - not Senior/Staff/Lead/Principal/Manager/CTO. Not a KILL.
- Degree: "Laurea Triennale o Magistrale ... o affini" (Bachelor's OR Master's OR related) -
  not a hard MSc/PhD requirement. Not a KILL.
- Core stack: generic areas (Application/Cloud/Mobile Software Engineering, Infrastructure &
  Tools, QA, XR/AR/VR) - not Java/.NET/C++/Go/Rust/Django/FastAPI as the sole stack, not cloud
  admin. Claimable via TypeScript/Next.js/Node/Laravel/Python/Playwright. Not a KILL.
- Location: Italy, on-site, within the claimed region. Not a KILL.
- Posting: live (fetched successfully both via LinkedIn and capgemini.com).

Verdict: gates pass, proceeded to apply.

## Dedupe

`python3 loop/dedupe.py --check "Capgemini Engineering" "https://www.linkedin.com/jobs/view/4462844208/"`
-> `HIT COMPANY~` (fuzzy company match only, not a URL hit).

`grep -i "capgemini" applications.csv`:
- 2026-08-06, Capgemini, Automation Engineer - NL, status LEAD (not applied; different company
  name, different role, different country, status does not block per the brief).

No prior SUBMITTED/NEEDS YOU/INTERVIEW/REJECTED row for Capgemini Engineering at any level.
Decision: proceed, not a duplicate.

## What blocked the application

LinkedIn's own Apply button is off-platform ("Responses managed off LinkedIn"), no Easy Apply
was offered. It opened Capgemini's own job page (capgemini.com/jobs/436075-en_GB_SAPBTP), which
matched the LinkedIn posting's JD text and requisition ID (Marcon VE is one of the listed
locations). Clicking "Apply for this job" there opened a SAP SuccessFactors career portal
(career5.successfactors.eu) whose very first screen requires creating an account: Email,
Retype Email, and "Choose Password" (8-18 chars, upper+lower case, number/punctuation) are
mandatory fields alongside the CV/cover-letter upload, before any application content can be
entered. "Already a registered user? Please sign in" confirms this is a login/account wall.

Per the brief this is a hand-back: no account was created, no email/password was entered, no
fields were filled beyond inspecting the page.

## Material prepared for the user

- CV to use: `Prabhavit_CV_Original_EN.pdf` (unchanged, canonical file).
- Cover letter (English, 170 words, no em-dashes) - `CoverLetter_Capgemini.txt`:

Dear Hiring Manager,

I am applying for the Software Engineer role at Capgemini Engineering in Marcon, Veneto.

At FlowSpace, a workspace marketplace, I worked across the stack areas this role spans. On
application software I built and shipped features end to end with Next.js, TypeScript and
Node.js, and helped migrate the platform's backend onto Laravel with Supabase and PostgreSQL.
On automation and tooling I built Python scripts and LLM pipelines that ingest documents in
any format and draft structured records with a human in the loop, and I integrated
third-party booking APIs, OfficeRnD and Nexudus, into the platform. On quality I used
Playwright for end to end testing so releases stayed reliable while the product kept shipping.
That range, product code, backend, automation and QA, matches how Capgemini Engineering's
Software Product Engineering team is organised.

I am based in Venice, authorised to work in Italy with no sponsorship needed, and can commute
to Marcon. My English is professional working level; my Italian is beginner and actively
improving.

Regards,
Prabhavit Gupta

- PDF built from `CoverLetter_Capgemini.tex` via `tectonic`, confirmed 1 page:
  `CoverLetter_Capgemini.pdf`.

## Standard answers ready if the user signs in and continues

- Legally entitled to work in Italy: Yes.
- Country of Application: Italy.
- Country of Residence: Italy.
- Employed by Capgemini before: No.
- Disability disclosure / gender disclosure consent checkboxes: leave unticked (optional,
  "prefer not to say" per standing rule); "How do you identify?" leave blank if it appears.
- WhatsApp contact consent: No (not required).
- Notification / recruitment-events marketing consent checkboxes: leave unticked.
- Privacy Notice acknowledgement: required, must be ticked to submit.
- Phone: +39 351 610 7807, Country/Region Code: Italy (+39).
- Name: Prabhavit Gupta (Legal First Name: Prabhavit, Legal Last Name: Gupta).
