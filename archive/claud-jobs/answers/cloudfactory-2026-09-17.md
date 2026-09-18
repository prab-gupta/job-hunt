# CloudFactory - Forward Deployed Engineer - 2026-09-17 (retry)

URL: https://www.linkedin.com/jobs/view/4461778895/
Retry of the 2026-09-16 NEEDS YOU row (see answers/cloudfactory-2026-09-16.md for the original dedupe/hard-gate work). Only blocker yesterday was LinkedIn's daily Easy Apply cap, which cleared overnight. Job page showed "Saved" today; re-checked apply-button availability, still open, no "not accepting applications" banner.

## Materials
Reused Prabhavit_CV_CloudFactory.pdf and CoverLetter_CloudFactory.txt built and verified 2026-09-16 (no changes needed).

## Form (Workable, 4 pages)
1. Contact info: Prabhavit Gupta, Italy +39 351 610 7807, mobile 3516107807, email prabhavitg@gmail.com, Location Venice, Veneto, Italy.
2. Resume: uploaded Prabhavit_CV_CloudFactory.pdf via Upload resume -> injected file input, confirmed selected and checked at the top of the resume list.
3. Additional Questions (discovered on first pass to be longer than expected, scrolled to see all fields):
   - Earliest Start Date: 10/1/2026 (two weeks from today per the standing notice-period rule)
   - Expected Annual Gross Salary: EUR 50000
   - Right to Work in Job Location (Germany): No
   - What is your most significant and comparable accomplishment related to this role: the FlowSpace AI listing bot (brochure in any format to drafted listing with a human in the loop, 900+ drafts, part of the 2,000 to 4,500+ user scale-up)
   - Why are you applying for a role at CloudFactory: three years building AI automation and agentic workflows with clients (FlowSpace AI listing bot, UltraStrategy CV-parsing pipeline on n8n/Eden AI), matched to CloudFactory's proof-of-concept-to-production FDE work
   - Are you currently working as a CloudWorker: No
   - Which country are you currently based in: Italy
   - Personal data consent: ticked (required)
4. Review page revealed a "Cover letter" section reading "Be sure to include an updated cover letter" with an Edit link; clicking Edit returned to page 2/3 territory and surfaced a dedicated cover-letter textbox (separate from the resume file upload) that had not appeared on the first pass through in the same visual scroll position. Pasted the full CoverLetter_CloudFactory.txt text into it via form_input, then re-advanced through Next -> Next -> Review and confirmed the Review page now showed the full cover letter text under "Cover letter".

## Trap encountered
The `computer` `type` action silently dropped characters on both free-text boxes ("Why are you applying" and the sponsorship-style long answers on other rows today) - e.g. "automation" became "automaion", "brochure" became "bochure". Caught this by re-reading the field on the review/edit screen before submitting, and fixed both fields with `form_input` (sets the DOM value directly, no dropped keystrokes) instead of retyping. Verified the final values via a JS read of all visible text inputs/textareas before proceeding to Review.

## Result
SUBMITTED. Confirmation: "Your application was sent to CloudFactory!" / "Application submitted - now". Saved to confirmations/CloudFactory-2026-09-17.txt.
