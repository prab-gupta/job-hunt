# Kuehne+Nagel - QA Automation Engineer (Wroclaw) - 2026-09-16

Status: RETRY PLAYWRIGHT (frozen upload trap on jobs.kuehne-nagel.com). See loop/results/KuehneNagel.txt.

LinkedIn: https://www.linkedin.com/jobs/view/4466549138/ (offsite, "Responses managed off LinkedIn")
ATS: Phenom People careers site, job page https://jobs.kuehne-nagel.com/global/en/job/KUNAGLOBAL16834EXTERNALENGLOBAL/QA-Automation-Engineer, apply form https://jobs.kuehne-nagel.com/global/en/apply?jobSeqNo=KUNAGLOBAL16834EXTERNALENGLOBAL (req 16834), guest apply, no account wall.

Dedupe: NEW (python3 loop/dedupe.py --check "Kuehne+Nagel" ...; no prior Kuehne+Nagel row in applications.csv).

Gates checked on live JD (pre-fetched scratchpad JD text, apply-button count 1):
- No anti-AI disclaimer.
- No explicit "X years required" stated ("Professional experience in Test Automation, QA, or Software Development").
- Title is "QA Automation Engineer", not Senior/Staff/Lead/Principal/Manager/CTO.
- No MSc/PhD requirement.
- English JD, English communication explicitly required (claimable, C2).
- Core stack is Playwright/TypeScript (already transitioning to it) plus Cucumber/Gherkin/Selenium/AssertJ (not claimed, disclosed honestly in the letter); not a hard-gate language (Java/.NET/C++/Go/Rust) as the main stack.
- Wroclaw, Poland - EU location, hybrid.
No gate failed; row proceeds to apply.

CV: Prabhavit_CV_KuehneNagel.pdf (from Prabhavit_CV_EN.tex). Dropped/reordered:
- Career Summary: kept the LLM-driven-applications bullet and the "rigorous QA testing" bullet (most QA-specific), dropped the AI-assisted-development/prompt-engineering bullet as least relevant to this JD.
- Technical Skills: reordered to Automation (n8n, Playwright) first, then Project/Design (Postman/Jira/GitHub), then Development, then AI/ML last.
- FlowSpace Product Responsibilities: reordered "Collaborated with team of developers for product logic and business logic documentation" to the top (requirements/testability angle), kept scaling and migration bullets, dropped "Facilitated communication...Agency" and "Streamlined customer support with AI agents" as least QA-relevant. Kept the Tools line naming Playwright untouched.
- FlowSpace Technical Responsibilities: kept API-integrations bullet (moved first) and the AI listing-bot bullet; dropped CRM/GTM automation bullets, the duplicate lines, and the commute-times tool bullet as not QA-relevant.
- Clubee: reordered "Unit testing and quality assurance of new features" to the top (direct QA match).
- Tractionboard: pruned to 2 bullets (Responsive designs/de-bugging first, then ChatGPT/OpenAI integration); dropped Figma, Sendgrid, Google Ads bullets.
- Additional Information: dropped the "Low code development/" prefix from IT Skills (JD has no relation to low-code).
- UltraStrategy, Urlink, Qomodo, Get2Germany: left mostly as-is (already short / no bullet stood out as more QA-relevant than another).
No claims added; all kept bullets verbatim from Prabhavit_CV_EN.tex. Compiled 2 pages with tectonic.

Cover letter: CoverLetter_KuehneNagel.pdf/.txt, English, 0 em-dashes (grep verified). Two-role evidence per the material rules: Clubee (unit testing and QA, Clubee API integration across the frontend) as the lead paragraph, paired with FlowSpace (Playwright for browser automation as daily work, TypeScript/Laravel/Postman, live migration validating business-critical flows, OfficeRnD/Nexudus API integrations) as the second. Explicitly discloses no hands-on experience with Cucumber, Gherkin, Selenium or AssertJ rather than overstating fit. Poland work-authorisation transparency line used (not currently authorised, ready to relocate and complete the employer-side process).

Fields already filled in the Chrome session before the freeze (client-side state, not persisted - a Playwright pass must refill all of it):
- First Name: Prabhavit, Last Name: Gupta
- Email: prabhavitg@gmail.com
- Address line 1: Via Zanetti, 10 / City: Venice / County/State/Province: Venezia / Country: Italy / Postcode: 30175
- Country Code: Italy (+39) / Phone: 351 610 7807
- Gender: left blank (no "Prefer not to say" option offered, field not marked required)
- Language Proficiency: English, Hindi, Italian (three rows added via "+Add Language")
- "When is the earliest date that you can start working with us?": Available immediately, ready to start within two weeks of an offer.
- "What are your expectations for the basic, annual, salary? (gross - please state currency)": EUR 45,000-55,000 gross annually.
- "Do you require a work permit to work with us?": Yes (correct per work-authorisation.md, Poland is another EU country - authorised No, employer permit Yes)
- Marketing/email consent checkbox: left unticked (per standing rule)
- Required privacy consent checkbox (*By submitting my personal and application data...): ticked

Blocker: the CV upload (file_upload to the hidden input behind the "CV Upload" button) froze the tab - every subsequent screenshot/read_page call returned "Script injection timed out ... page is busy". Closed that tab and retried fresh: refilled all personal-information fields manually first (these worked fine), then attempted the "Additional Documents" upload (CoverLetter_KuehneNagel.pdf, a much smaller file) as the last step - it froze identically, persisting through 28+ seconds of waits and repeated screenshot/read_page attempts. This is a genuine frozen-upload trap on jobs.kuehne-nagel.com's file input(s), not a one-off Chrome hiccup (confirmed on two different files, two separate attempts). Per the browser-ownership rule, stopped the row and did not attempt Playwright myself. Nothing was submitted.

Next step for the Playwright agent: open https://jobs.kuehne-nagel.com/global/en/apply?jobSeqNo=KUNAGLOBAL16834EXTERNALENGLOBAL, refill the personal-information fields above, upload Prabhavit_CV_KuehneNagel.pdf via the CV Upload input and CoverLetter_KuehneNagel.pdf via the Additional Documents input, verify both attached, click Submit, then log per the normal flow (screenshot to confirmations/KuehneNagel-2026-09-16.png, one row to applications.csv, loop/results/KuehneNagel.txt updated to SUBMITTED).

## Playwright submission (2026-09-16, follow-up agent)

Submitted successfully via Playwright. Both file uploads (CV Upload, Additional Documents) worked cleanly - each opened a normal OS file chooser and completed with a confirmation alert dialog ("CV Uploaded Successfully" / "Cover Letter Uploaded Successfully"), accepted via browser_handle_dialog. The frozen-tab trap that stopped the Chrome agent did not reproduce in Playwright.

Fields filled: name/email/address (Via Zanetti 10, Venice, Venezia, Italy, 30175), phone +39 351 610 7807, Language Proficiency = English, Hindi, Italian (three rows via "+ Add Language", each with its own combobox), earliest start = "Available immediately, ready to start within two weeks of an offer.", salary = "EUR 45,000-55,000 gross annually", work permit required = Yes (Poland, per work-authorisation.md), marketing consent unticked, privacy/data consent ticked, cookie banner rejected (decline non-essential).

Result: "You have successfully applied. Thank you for showing interest in working at Kuehne+Nagel." jobApplicationId=689947. Screenshot at confirmations/KuehneNagel-2026-09-16.png/.txt.
