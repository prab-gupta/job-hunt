# SupportYourApp — (fluent English) AI Solutions Specialist (Global, remote)

Job (LinkedIn): https://www.linkedin.com/jobs/view/4442587582/
ATS (Workable) link LinkedIn redirects to: https://apply.workable.com/j/401F0266AC/ (via LinkedIn safety redirect)
Date: 2026-09-11

## Gate check
- Cheap check: `curl ... jobPosting/4442587582 | grep -c apply-button` = 1 (pass, LinkedIn side only).
- LinkedIn page showed "Apply on company website" (a "Saved" job, not "Application submitted"), no not-currently-accepting banner on LinkedIn itself.
- Clicked Apply -> LinkedIn opened a new tab to `apply.workable.com/j/401F0266AC/...` which resolved to Workable's generic 404 page ("Page not found. It seems we cannot find this page.").
- Re-tried the bare Workable job URL directly (same 404) and the company's Workable careers root (`apply.workable.com/supportyourapp/`), which loaded with a `This job is no longer available.` banner and `?not_found=true` in the URL.
- Cleared all location/workplace filters on the company's live Workable job list and read every posting title present: none is an AI Solutions Specialist or AI-flavoured role (only Customer Support Consultant variants, T3 Support Engineer, Administration & Operations Specialist).
- Verdict: hard gate "posting closed/404" triggered on the actual employer ATS, even though LinkedIn's own listing still displays as open and lets people click Apply. Stopped before drafting a CV or letter (gate check happens before materials are built).

## Note on "started as a Draft on LinkedIn"
The task said the user had started this application as a Draft on LinkedIn. No LinkedIn Easy Apply flow exists for this posting (it is LinkedIn-offsite only, "Responses managed off LinkedIn"), and the offsite target is gone, so there is nothing left to resume or finish. If a LinkedIn-side draft state exists for this job, it cannot be completed because the destination requisition has been pulled from Workable.

## Outcome
KILLED - closed/404 on the real ATS. No CV, letter or answers were drafted (correctly, per the gate-before-materials rule). Nothing for the user to do; if SupportYourApp reposts an equivalent AI role it would need a fresh LinkedIn/Workable URL.
