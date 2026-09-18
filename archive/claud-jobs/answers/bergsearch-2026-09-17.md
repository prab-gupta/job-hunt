# Berg Search - Forward Deployed Engineer (Athens) - 2026-09-17

URL: https://www.linkedin.com/jobs/view/4456705662/
ATS: LinkedIn Easy Apply
Task: FDE-ALL rule row (agent C61). Athens/Greece line; kill only if Greek is explicitly required.

## Dedupe
`python3 loop/dedupe.py --check "Berg Search" "https://www.linkedin.com/jobs/view/4456705662/"` -> HIT COMPANY~ (fuzzy)
`grep -i "berg" applications.csv`: two matches, but both are location substrings inside unrelated companies' notes ("Prenzlauer Berg" in a Skyflow row, "Kronberg DE" in an Accenture DACH row) - no actual Berg Search row exists anywhere in applications.csv. Fuzzy hit does not block per the brief (a company-name substring match on an unrelated company never blocks). Proceeding as NEW.

## Hard gates
Cheap check + live page: Easy Apply present, on-site Athens, no closed banner, no prior application-submitted state.
JD (recruiter posting on behalf of a confidential fast-growing AI platform company): no Greek-language requirement anywhere in the JD body. The Easy Apply flow turned out to be a single page (contact info + resume + submit, no Additional Questions page at all), so there was no possibility of a Greek screening question appearing - this differs from the two other Athens postings referenced in LEARNINGS (2026-09-16/17), which evidently had a longer flow with a language question. Requirements: 3+ years technical problem-solving (fits honest 3), no hard degree requirement, Python/Go/TypeScript stack (Go is a stack ask, not a kill under the FDE-ALL rule), no anti-AI disclaimer. Passed all gates.

## CV
Prabhavit_CV_BergSearch.tex/.pdf built from Prabhavit_CV_EN.tex, same FDE tailoring pattern as Cresta/Devoteam (parity-diffed: reorder/delete only). 2 pages.

## Cover letter
CoverLetter_BergSearch.pdf/.txt/.tex (0 em-dashes grep-verified). FlowSpace lead paragraph (live migration, support AI agent, AI listing bot 900+ drafts, OfficeRnD/Nexudus integrations) paired with UltraStrategy (CV-parsing pipeline, Affinda + Claude API, n8n/Eden AI). Honest 3 years. Greece work-authorisation transparency line: Italian EU LTR status, not currently authorised in Greece, needs employer-side permit/sponsorship, ready to relocate to Athens.
No cover letter upload field on this Easy Apply flow; PDF/txt kept on file only.

## Standing answers given
- Contact info was pre-filled from the LinkedIn profile (email prabhavitg@gmail.com, phone country code Italy +39, phone 3516107807) - no edits needed.
- No Additional Questions page existed on this form (contact info + resume + submit only), so no work-authorisation, salary, or language questions were asked directly on the form itself.
- Follow Berg Search checkbox: unchecked (default was ticked).

## File-upload note (compare with SoTalent row, RETRY PLAYWRIGHT)
On the SoTalent Easy Apply form, clicking "Upload resume" never exposed an accessible file input to Claude in Chrome (the underlying `input[type=file]` stayed `display:none` even after the click, confirmed via JS, so no read_page/find ref could target it for the file_upload tool). On this Berg Search form, the same button DID expose a usable file-input ref on the first re-run of `find` after clicking Upload resume, and the upload succeeded cleanly. Likely a per-posting or per-load rendering difference in LinkedIn's Easy Apply widget rather than a systemic block; worth retrying find 1-2 times before falling back to RETRY PLAYWRIGHT.

## Submission
Verified Prabhavit_CV_BergSearch.pdf selected (green radio, top of list) before submitting. Clicked Submit application; job page's own Application status panel showed "Application submitted" immediately after.
