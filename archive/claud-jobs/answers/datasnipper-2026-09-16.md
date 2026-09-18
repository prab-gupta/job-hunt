# DataSnipper - Forward Deployed Engineer (Audit experience required) - 2026-09-16

URL: https://www.linkedin.com/jobs/view/4463391194/
Apply routes to: https://careers.datasnipper.com/job-listing?ashby_jid=743b4a63-bf1a-44c1-87e6-a9c963a2f74f
(Application tab; underlying ATS is Ashby, embedded as a cross-origin iframe on DataSnipper's own careers page)
Status: NEEDS YOU / RETRY PLAYWRIGHT

## Dedupe
`python3 loop/dedupe.py --check "DataSnipper" ""` -> HIT COMPANY on one unrelated row: 2026-08-14, DataSnipper,
GTM Engineer, Ashby, status "CLOSED - job not found". Different requisition and role, not blocking.

## Hard gates
No anti-AI disclaimer (JD explicitly welcomes "using a variety of AI tools like Claude in the build and test
loop"). English JD. No degree requirement. No language other than English required. Title says "Audit experience
required" but the JD's own "Must-Have" list reads "Domain expertise in audit and/or finance or strong interest
w/ ability to learn" - not an absolute requirement, so not an automatic kill. Applied honestly noting no audit
background, per the task's explicit instruction for this row.

## What happened
The "Application" tab on DataSnipper's careers page renders an Ashby form, but it is inside a cross-origin
iframe: Claude in Chrome's `find` and `read_page` tools return nothing for any field in it (confirmed: searching
for "Upload file button for resume" found no matching element even though it is visibly rendered on screen).
This is the same documented pattern as the Databricks/Greenhouse cross-origin-iframe case already in
NEEDS_YOU.md. Plain coordinate-based clicking and typing DOES work through the iframe (tested: clicked the Name
field by coordinate and typed "Prabhavit Gupta" successfully), but the file_upload tool requires a DOM `ref`
that cannot be obtained here, and clicking the "Upload File" control directly would only open a native OS file
picker that cannot be seen or driven. Per the brief, this is a RETRY PLAYWRIGHT case: stopped rather than
submitting without the required resume.

## Full field list observed (for whoever finishes this in Playwright)
- Name* -> Prabhavit Gupta (already typed in Chrome, not submitted)
- Email* -> prabhavitg@gmail.com
- Resume* (Upload File, required) -> Prabhavit_CV_DataSnipper.pdf (BLOCKED, could not upload)
- "Are you located in the Netherlands?*" (free text) -> "No, I am based in Venice, Italy and hold Italian EU
  long-term resident status. I am not currently authorised to work in the Netherlands and would need the
  applicable employer-side permit or sponsorship process. I am ready to relocate to Amsterdam."
- "Please insert your Linkedin url:*" -> https://www.linkedin.com/in/prabhavit/
- "What are your salary expectations:" (optional) -> EUR 50,000 (standing 45-55k target; JD only says
  "Excellent salary" with no number)
- "Are you comfortable commuting to our office in Amsterdam at least 3 days per week?*" (Yes/No toggle) -> Yes
- Consent checkbox "I have read and understood the Recruitment Privacy Policy and consent..." -> tick (I agree)
- Submit Application button

## Materials built
Prabhavit_CV_DataSnipper.pdf (2 pages, CloudFactory-pattern tailoring) and CoverLetter_DataSnipper.pdf/.txt
(UltraStrategy CV-parsing pipeline led, FlowSpace AI listing bot + support AI agents paired, honest about no
audit/finance background, 0 em-dashes grep-verified).

## Update - completed via Playwright
Status changed to SUBMITTED. Playwright's contentFrame()-based locators reached every field inside the
cross-origin Ashby iframe, including the Resume* file input (Chrome's find/read_page could not see any element
in it). Uploaded Prabhavit_CV_DataSnipper.pdf, filled all fields exactly as listed above, salary answered as
EUR 45,000 (this batch's stated target), clicked Yes on the Amsterdam commute question, ticked consent, and
submitted. Confirmation: "Your application was successfully submitted. Thank you! We will be in contact as soon
as possible." Screenshot at confirmations/DataSnipper-2026-09-16.png. New applications.csv row appended
(2026-09-16, SUBMITTED) below the earlier NEEDS YOU row for the same requisition, per instruction not to edit
the existing row.
