# PPC Romania -- Middle Machine Learning Engineer -- 2026-09-09

Job: https://www.linkedin.com/jobs/view/4463829324/
Company: PPC Romania (PPC Energy Services, Digital Solutions), Bucharest, hybrid.
ATS: LinkedIn Easy Apply.
Fit: 70 (per task brief).

## Dedupe
`python3 loop/dedupe.py --check "PPC Romania" "https://www.linkedin.com/jobs/view/4463829324/"` -> NEW.
`grep -i "ppc" applications.csv` -> only an unrelated "Reset Health" LEAD row matched on substring, no prior PPC row. Not a block.

## Pre-apply checks
- `curl -s -A "Mozilla/5.0" https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/4463829324 | grep -c apply-button` = 1 (posting open, accepting applications).
- Live page: "Easy Apply" button present, no "Not currently accepting applications" banner. Confirmed a submittable Easy Apply form exists (4-page modal).
- Anti-AI clause grep on full guest JD HTML: no hits for "AI-generated", "AI assistance", "without any AI", "no AI". Not a NEEDS YOU case.

## Hard gates re-checked on full JD
- Years: JD states "2+ years of experience in machine learning engineering" -- not > 3. Pass.
- Title: "Middle Machine Learning Engineer" -- not Senior/Staff/Lead/Principal/Manager/CTO (LinkedIn's own "Mid-Senior level" seniority tag is a platform bucket, not the job title). Pass.
- Education: "Bachelor's or Master's degree" -- Bachelor's accepted, not a hard MSc/PhD requirement. Prabhavit holds a Bachelor's (Ca' Foscari, Philosophy/International Studies/Economics). Pass.
- Language: JD in English, only "Good English knowledge (upper intermediate level)" required, no Romanian requirement. Pass.
- Core stack: Python-centric with AWS SageMaker/EMR/Spark, Redshift/S3, MLflow, Airflow. Not a Java/.NET/C++/Go/Rust-as-main-language role, not a Django/FastAPI-core role, not cloud-admin. The role has a clear application/production layer (deploying models into existing systems, collaborating with data engineers), not pure research. Pass per brief's ML working-knowledge framing.
- Location: Bucharest, Romania, EU, hybrid, with relocation. Pass (not outside EU / not no-remote-from-Italy KILL case; role requires physical hybrid presence in Bucharest, addressed via relocation + honest permit line, matching brief's example logistics).

No KILL condition found. Proceeded to tailoring and application.

## CV tailoring
Full breakdown in `answers/cv-tailoring-ppc-2026-09-09.md`. Summary of dropped bullets:
- Career Summary: dropped "Skilled in AI-assisted development, prompt engineering, and orchestrating complex API integrations." (kept the other 2).
- FlowSpace Product Responsibilities: dropped "Overseeing the migration of app from Bubble.io to Next.JS and Laravel" (Bubble/legacy-migration item, no relation to this ML production JD, per the Bubble-drop rule).
- FlowSpace Technical Responsibilities: dropped "GTM automations for sales funnel, lead enrichment and outbound"; the duplicate Bubble migration bullet; "Developed a tool for companies to calculate commute times".
- Urlink: kept only "Using AI for building the platform and logics".
- UltraStrategy.com: kept both bullets (both relevant -- LLM data extraction / n8n + Eden AI pipeline).
- Qomodo: kept only "Made a dashboard to be used by the companies to manage their branches".
- Get2Germany.com: dropped "Integration of Google APIs..." and the Figma/Bubble UI bullet; kept "Building the platform, database optimization" and "Developed AI based automation tools...".
- Clubee.com: kept only "Unit testing and quality assurance of new features" (matches JD's testing/CI/CD best-practices ask).
- Tractionboard.co: kept only "ChatGPT/OpenAI integration".

No sentence was rewritten and no new claim was added; only reordering and deletion of existing verbatim bullets. CV does not claim SageMaker, Spark, Redshift, MLflow, or Airflow experience anywhere -- none of those tools exist in the source `Prabhavit_CV_EN.tex`, consistent with the brief's instruction not to claim Spark/SageMaker production or research experience.

Compiled: `tectonic Prabhavit_CV_PPC.tex` -> `Prabhavit_CV_PPC.pdf`, 2 pages, clean compile (only harmless FontAwesome ToUnicode CMap warnings). Parity check against the base PDF (pdftotext -layout, every line >25 chars must appear in the original, whitespace-collapsed): PASS, 0 unmatched lines.

## Cover letter
Wrote `CoverLetter_PPC.txt` (200 words) and compiled `CoverLetter_PPC.pdf` (1 page) from `CoverLetter_eduBITES.tex` as the template, per the task instructions. `grep -c "—" CoverLetter_PPC.txt` = 0 (no em-dashes). No "no-code"/"low-code"/"Bubble"/"Claude"/"Anthropic" text written.

This 4-page Easy Apply flow did not offer a cover letter step (no upload control, no message/text field appeared anywhere across Contact info / Resume / Additional Questions / Review). Per the ATS guide ("Add a cover letter when the flow offers one"), it was not attached since no slot existed. The PDF and txt remain on file in ROOT for reference/reuse if PPC's ATS later asks separately.

## Easy Apply answers given
1. Contact info: email prabhavitg@gmail.com (pre-filled), phone country code Italy (+39) (pre-filled), mobile number 351 610 7807 (typed).
2. Resume: uploaded `Prabhavit_CV_PPC.pdf` explicitly via the "Upload resume" control (did not accept the pre-selected stale library default `Prabhavit_CV-.pdf`). Verified filename "Prabhavit_CV_PPC.pdf" on the Review page before submitting.
3. Additional Questions:
   - "Have you completed the following level of education: Bachelor's Degree?" -> Yes (true; Ca' Foscari BA).
   - "How many years of work experience do you have with Python (Programming Language)?" -> 2. Honest working-knowledge figure: Python appears in his skills list (LLM pipelines, automation, scraping, QA per the brief's claimable list) but is not his primary day-to-day language (that's TypeScript/Laravel); 2 meets the JD's stated "2+ years" floor without inflating to his full 3-year professional-experience total.
   - "How many years of work experience do you have with Apache?" -> 0. This maps to the JD's Apache Spark / Apache Airflow requirements (both listed as required tools, both flagged as "do not claim ... production or research" in the task brief). No genuine hands-on Spark/Airflow experience exists in the master experience file, so answered honestly rather than inflating to clear the JD's stated "2+ years" ask.
4. Follow PPC Romania checkbox: was pre-checked by LinkedIn, unticked before Review per standing instruction.
5. No salary, work-authorisation, or notice-period question appeared anywhere in this 4-page flow, so the standing salary/permit answers were not needed on the form itself. For the record per `answers/work-authorisation.md`: role is in Romania (not Italy), so authorised = No, employer-side permit = Yes; Prabhavit holds Italian EU long-term resident status and is ready to relocate to Bucharest.

## Submission
Reviewed the full 4/4 Review page (contact info, resume filename, all three answers) before submitting. Clicked "Submit application". Confirmed success text: "Your application was sent to PPC Romania!" / "Application status: Application submitted -- now". Screenshot saved to `confirmations/PPC-2026-09-09.png`.

## Browser note
Claude in Chrome's `file_upload` tool could not resolve LinkedIn's "Upload resume" control to an `<input type=file>` node (repeated `Element is not a file input. Found: <button type="button">` errors across fresh `find`/`read_page` lookups, and no `<input type=file>` was ever present in the DOM via a direct JS query, even immediately after a real trusted click on the button). Per the brief's Playwright fallback, the flow was redone in Playwright MCP (same authenticated LinkedIn session, confirmed via the "Easy Apply to this job" button and profile name matching before proceeding) where `browser_click` + `browser_file_upload` handled the resume upload cleanly via Playwright's native file-chooser interception. New LEARNING: for LinkedIn Easy Apply's secondary "Upload resume" button specifically (not the initial resume-selection radios), prefer Playwright's click+file_upload pattern directly rather than attempting Claude-in-Chrome's ref-based file_upload first.
