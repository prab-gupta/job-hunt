# Blindspot top-up sweep: physical rows 38-73

Screened 28 Aug 2026. Exact URL comparison was performed first against `applications.csv` using the CSV `url` field with a trailing slash removed. The 36 physical rows contain 35 exact URL duplicates and one new URL. Existing application records were not discarded based on fit, location, or seniority; their recorded outcomes are reproduced below.

## Outcome by physical row

| Row | Company / role | Exact-URL result | Screened outcome and evidence |
|---:|---|---|---|
| 38 | Remote - Senior Forward Deployed Engineer | Duplicate | `applications.csv`: SKIP, seniority too high (Senior) for ~3 years experience. |
| 39 | Stacklok - Staff Forward Deployed Engineer - Kubernetes | Duplicate | `applications.csv`: SKIP, Staff seniority too high for ~3 years experience. |
| 40 | Redapt - Forward Deployed Engineer, Agentic AI | Duplicate | `applications.csv`: SKIPPED, US-Remote only. |
| 41 | GWI - Growth Marketing Automation Engineer | Duplicate | `applications.csv`: SUBMITTED; confirmation: “Thank you for applying, you've taken your first step towards a future at GWI.” Record says London hybrid, 2 days/week; no cover-letter field or essay. |
| 42 | Automattic - Growth Engineer, MarTech | Duplicate | `applications.csv`: DEAD; “Page not found - board no longer active”; entire board inactive. |
| 43 | Material Bank - Lead MarTech Engineer | Duplicate | `applications.csv`: SKIP, Lead seniority too high for ~3 years experience. |
| 44 | Twin Health - Senior Marketing Automation Engineer | Duplicate | `applications.csv`: SKIP, Senior seniority too high for ~3 years experience. |
| 45 | ZOE - MarTech Engineer | Duplicate | `applications.csv`: SKIP, marketing-domain role. |
| 46 | Owner.com - Senior Martech Engineer | Duplicate | `applications.csv`: SKIP, Senior seniority too high for ~3 years experience. |
| 47 | Encord - Growth Engineer | Duplicate | `applications.csv`: DEAD, 404 error / dead posting. |
| 48 | Outsourced Staff - Prompt Engineer - Conversational AI | Duplicate | `applications.csv`: DEAD_LINK; Lever posting, 100% attrition rate in this CSV batch. |
| 49 | Known - Conversational AI Engineer, System Prompt | **New** | **CLOSED / not live.** Direct Ashby navigation rendered heading “Job not found”, paragraph “The job you requested was not found.” and link “View all open positions”. No application form was available, so no form fields/options, essay, account, anti-AI question, or CAPTCHA could be assessed. |
| 50 | Farther - Senior Conversational AI Engineer | Duplicate | `applications.csv`: SKIP, Senior seniority too high for ~3 years experience. |
| 51 | ZenBusiness - Conversational AI & Prompt Engineer | Duplicate | `applications.csv`: DEAD; “Job no longer open”. |
| 52 | Jobgether - Remote ChatBot Engineer | Duplicate | `applications.csv`: SKIP, Jobgether aggregator repost, no real employer. |
| 53 | Jobgether - Chatbot Developer (WhatsApp, Telegram, Discord) | Duplicate | `applications.csv`: SKIP, Jobgether aggregator repost, no real employer. |
| 54 | Jobgether - Senior Engineer, Applied AI | Duplicate | `applications.csv`: SKIP, Jobgether aggregator repost, no real employer. |
| 55 | Nearform - Prompt Engineer (FTC, UK, Remote) | Duplicate | `applications.csv`: DEAD; posting no longer open. |
| 56 | Oowlish Technology - SDET - Regression Automation Engineer | Duplicate | `applications.csv`: DEAD_LINK; Lever posting, 100% attrition rate in this CSV batch. |
| 57 | Jobgether - QA Automation Engineer (SDET, Playwright & API) | Duplicate | `applications.csv`: SKIP, Jobgether aggregator repost, no real employer. |
| 58 | Smart Working Solutions - QA Automation Engineer (Remote, Full-Time) | Duplicate | `applications.csv`: DEAD_LINK; Lever posting, 100% attrition rate in this CSV batch. |
| 59 | Jobgether - SDET/QA Automation Lead | Duplicate | `applications.csv`: SKIP, Jobgether aggregator repost, no real employer. |
| 60 | Remote People - QA Automation Engineer | Duplicate | `applications.csv`: SKIP, QA/SDET specialist role. |
| 61 | Dashlane - Web QA Automation Specialist - SDET (Remote Eligible - Portugal) | Duplicate | `applications.csv`: SKIP, QA/SDET specialist role. |
| 62 | Jobgether - Senior Automation QA Engineer (SDET) | Duplicate | `applications.csv`: SKIP, Jobgether aggregator repost, no real employer. |
| 63 | EverAI - Senior AI Product Manager (Remote - Europe) | Duplicate | `applications.csv`: SKIP, Senior seniority too high for ~3 years experience. |
| 64 | Aledade - Senior Technical Product Manager - AI Innovation | Duplicate | `applications.csv`: DEAD_LINK; Lever posting, 100% attrition rate in this CSV batch. |
| 65 | LeoLabs - Technical Product Manager | Duplicate | `applications.csv`: SKIP, management/leadership role, wrong track. |
| 66 | Actian - Staff Product Manager, AI [gn] Europe | Duplicate | `applications.csv`: SKIPPED; Staff-level PM, 5+ years PM required, wrong track. |
| 67 | Yuno - Technical Product Manager - Money and Risk | Duplicate | `applications.csv`: DEAD_LINK; Lever posting, 100% attrition rate in this CSV batch. |
| 68 | Aledade - Senior Technical Product Manager (AI Data Platform) | Duplicate | `applications.csv`: DEAD_LINK; Lever posting, 100% attrition rate in this CSV batch. |
| 69 | Yuno - Technical Product Manager - RAILS | Duplicate | `applications.csv`: DEAD_LINK; Lever posting, 100% attrition rate in this CSV batch. |
| 70 | Aledade - Technical Product Manager (AI/ML Research) | Duplicate | `applications.csv`: DEAD_LINK; Lever posting, 100% attrition rate in this CSV batch. |
| 71 | Yuno - Technical Product Manager - Client Experience | Duplicate | `applications.csv`: DEAD_LINK; Lever posting, 100% attrition rate in this CSV batch. |
| 72 | Fireworks AI - Head of Developer Relations | Duplicate | `applications.csv`: SKIP, management/leadership role, wrong track. |
| 73 | Runpod - Senior Developer Advocate | Duplicate | `applications.csv`: SKIP, Senior seniority too high for ~3 years experience. |

## Correction and first qualifying role

The initial pass incorrectly treated every exact duplicate as excluded. Per the corrected instruction, tracker rows with non-submitted statuses were re-opened in physical order and fit/location/seniority were not used as exclusion criteria.

- Row 38 (Remote) is live but has required essay fields: “Why are you interested in the Forward Deployed Engineer role, and what about Remote's platform and use cases excites you?” and “Describe your most complex customer-facing project. What made it complex, and how did you solve it?” Excluded under the required-essay rule.
- Row 39 (Stacklok) is not live: the Greenhouse board/API returns “Job not found.”
- Row 40 (Redapt) is the first qualifying live CV-upload form. It is listed as US - Remote and has a required US-work-authorization question, but this was retained for the user's decision rather than filtered out. The form has no required essay, no anti-AI question, no account/password requirement, and no visible CAPTCHA widget. Greenhouse has an invisible reCAPTCHA configuration, which is not a visible CAPTCHA.

### Redapt exact form fields and options

Required fields shown by the live Greenhouse form:

- First Name
- Last Name
- Email
- Phone
- Candidate Location
- Resume/CV (PDF, DOC, DOCX, TXT, or RTF upload; manual text alternative also offered)
- LinkedIn Profile
- “Will you now or in the future require Visa sponsorship?” Options: Yes; No
- “Are you currently authorized to work for any employer in the United States?” Options: Yes; No
- Location

No cover-letter field was present, so no `cover_letter.txt` was created. Optional demographic questions were not part of the application materials and were left untouched. The visible form had a “Submit application” button, but it was not clicked.

### Prepared materials

- Tailored one-page CV source: `redapt-fde-2026-08-28/Prabhavit_CV_Redapt.tex`
- Compiled one-page PDF: `redapt-fde-2026-08-28/resume-redapt-fde.pdf`
- Copied photo: `redapt-fde-2026-08-28/photo.jpg`
- Compile verification: Tectonic exit code 0; PDF has 1 page, A4 size.
- Only headline, summary, and skills were changed from the base tailored template. No other CV sections were altered.

No data was entered into the browser, no CV/photo was uploaded, no account was created, and no application was submitted.

### Continuation screen, rows 41-73

- Row 41 GWI: confirmed already `SUBMITTED` in `applications.csv`; excluded by exact URL rule.
- Row 42 Automattic: confirmed dead board / page not found.
- Row 43 Material Bank: **qualifying live Greenhouse CV-upload form**. It has required identity/contact, candidate location, CV, US work authorization/sponsorship, prior-employment, restrictive-covenant, and current-brand-partner questions. It has an optional Cover Letter upload/text field. No required essay, anti-AI question, account/password, or visible CAPTCHA was found. Prepared materials are in `material-bank-lead-martech-2026-08-28/`.
- Rows 44 Twin Health, 45 ZOE, 46 Owner.com, and 49 Known: no live application form was available (current-openings/dead Ashby states); excluded.
- Row 47 Encord: confirmed 404/dead posting.
- Row 48 Outsourced Staff: confirmed dead Lever link.
- Row 50 Farther: current openings page, no live application form for this URL.
- Row 51 ZenBusiness: confirmed job no longer open.
- Rows 52-54, 57, 59, and 62 Jobgether: confirmed 404 aggregator reposts, no real employer form.
- Row 55 Nearform: confirmed posting no longer open.
- Row 56 Oowlish: confirmed dead Lever link.
- Row 58 Smart Working Solutions: confirmed dead Lever link.
- Rows 60 Remote People, 61 Dashlane, and 65 LeoLabs: employer board pages are live but the exact job URLs have no application form/job detail, so excluded under no application form.
- Row 63 EverAI: no live application form available at the Ashby URL.
- Row 64 Aledade: confirmed dead Lever link.
- Row 66 Actian: live posting page but no CV-upload application form was available at the exact URL; excluded under no application form.
- Rows 67-71 Yuno/Aledade: confirmed dead Lever links.
- Row 72 Fireworks AI: confirmed board no longer active / page not found.
- Row 73 Runpod: posting metadata says “Remote - USA”; no qualifying application form was exposed at the exact Ashby URL, so excluded under no application form.

### Additional prepared role

- Tailored one-page CV source: `material-bank-lead-martech-2026-08-28/Prabhavit_CV_Material_Bank.tex`
- Compiled one-page PDF: `material-bank-lead-martech-2026-08-28/resume-material-bank.pdf`
- Copied photo: `material-bank-lead-martech-2026-08-28/photo.jpg`
- Optional cover letter: `material-bank-lead-martech-2026-08-28/cover_letter.txt`
- Compile verification: Tectonic exit code 0; PDF has 1 page, A4 size.
- Only headline, summary, and skills were changed in the CV template.

## Exact URL checked

`https://jobs.ashbyhq.com/known/032dee42-0fd3-47fd-9ca7-90632a4c59f8`

## Confirmation data

No submission occurred; there is no confirmation text, confirmation ID, or screenshot. The exact Redapt form can be opened at `https://job-boards.greenhouse.io/redapt/jobs/5396488008` for the user to review and decide whether to proceed with its US-only/work-authorization constraints.
