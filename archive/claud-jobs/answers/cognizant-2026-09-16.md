# Cognizant — DevOps & Automation Engineer (Stockholm, hybrid) — 2026-09-16

LinkedIn: https://www.linkedin.com/jobs/view/4466529325/ (OFFSITE, "Responses managed off LinkedIn")
ATS: Cognizant careers page -> Taleo
Status: NEEDS YOU (account wall)

## Dedupe
`python3 loop/dedupe.py --check "Cognizant" "https://www.linkedin.com/jobs/view/4466529325/"` -> NEW
`grep -i cognizant applications.csv` -> no prior rows.

## Hard gates re-checked on the live JD
- Anti-AI disclaimer: none found (grepped the prefetched JD text for "AI-generated", "AI assistance",
  "without any AI", "no AI").
- Years: JD headline says "3+ years... required" but then explicitly softens it: "candidates with
  approximately 2 years of highly relevant experience are also encouraged to apply." Matches the task's
  own note ("the JD welcomes about 2 years of experience"). Three years stated honestly, above the
  welcomed floor. Not a hard gate kill.
- Seniority: "Not Applicable" on LinkedIn criteria; no Senior/Staff/Lead/Principal/Manager/CTO title.
- Degree: Bachelor's listed under "will help you stand out", not a hard requirement. No MSc/PhD gate.
- Language: English JD, no other language required.
- Core stack: Jenkins/Terraform/Ansible/cloud provisioning across AWS/Azure/GCP are the JD's core tools
  and are NOT claimable per the Master Experience claim ladder (cloud admin is explicitly on the never
  claim list). Per this task's explicit instruction, applied anyway with fully honest 0/No answers on
  Jenkins/Terraform/Ansible, leaning on CI/CD fundamentals, GitHub workflow discipline, n8n and Python
  automation scripting instead. This is a known stretch, flagged plainly in the cover letter itself
  rather than glossed over.
- Location: Stockholm/Goteborg/Malmo, Sweden, hybrid. Inside the EU, no remote-from-Italy claimed.

## Apply flow and blocker
LinkedIn Apply -> https://careers.cognizant.com/global-en/jobs/00068910034/devops-automation-engineer/
-> "Apply now" -> Taleo Privacy Notice page -> "I Confirm" -> Taleo login page
(https://cognizant.taleo.net/careersection/iam/accessmanagement/login.jsf?...) offering only:
Username + Password login, or "New User" registration. No guest-apply path, no autofill-from-resume
bypass. Direct application URL (the redirect target, useful once signed in):
https://cognizant.taleo.net/careersection/Lateral/jobapply.ftl?job=00068910034&lang=en&source=JB-11500&src=JB-11500

Per task instruction ("Cognizant's ATS may demand an account: if so, save CV + letter, log NEEDS YOU
with the exact URL, do not create an account"), stopped here. No account created.

## CV tailoring — Prabhavit_CV_Cognizant.tex/.pdf (2 pages, tectonic compiled clean, verified via pdfinfo)
- Career Summary: kept bullets 1 and 2 from Prabhavit_CV_EN.tex (Automation Engineer framing + "API
  integrations"). Dropped bullet 3 (CV-parsing/AI-agent specific, least relevant to a CI/CD role).
- Technical Skills: reordered Automation (n8n, Playwright) to the top; added "Python (automation
  scripting)" to Automation and "Docker (working knowledge)" to Development, both justified by the
  Master Experience claim ladder (2026-09-06: Python is a listed language skill; Docker/Kubernetes are
  claimable as working knowledge in Skills) - same precedent as the Docker addition on
  Prabhavit_CV_moveax.tex. Moved GitHub to the front of Development (JD asks for GitHub PR/branching
  administration). AI/ML and Project/Design sections moved down, nothing deleted from them.
- Professional Experience: FlowSpace kept all 8 bullets (well above the 3-bullet minimum), reordered so
  Technical Responsibilities (API integrations, CRM/GTM automation, data tooling) lead before Product
  Responsibilities. Since the JD title itself is "Automation Engineer" and centres on workflow/pipeline
  automation, treated it as an AI-or-automation JD per the tailoring rule and kept 2 bullets under
  UltraStrategy (already at 2, unchanged) and 3 under Get2Germany (reordered automation + Google API
  bullets to the top; dropped the "UI/UX work, design from Figma to Bubble" bullet as clearly irrelevant
  to a DevOps JD and unrelated to any Bubble/low-code claim worth keeping). Urlink, Qomodo, Clubee kept
  with existing minimums (Clubee reordered to put the API-integration bullet first). Tractionboard
  trimmed from 5 bullets to 1 (ChatGPT/OpenAI integration only), dropping four clearly irrelevant
  UI/design/ads bullets, min-1 still satisfied. No role, date or location deleted; no bullet text
  rewritten.
- Additional Information: IT Skills reordered to "Automation (n8n), API integration, AI-based
  development, Project Management, Communication" (dropped the "Low code development/" prefix only,
  following the same precedent used on the Sonova CV, since this JD has zero relation to low-code).
  Tools reordered with n8n first.
- Parity check: every bullet present in Prabhavit_CV_Cognizant.tex traces to an existing bullet in
  Prabhavit_CV_EN.tex verbatim, except the two explicitly-justified skill additions (Python, Docker
  working knowledge) and the GitHub reorder.

## Cover letter — CoverLetter_Cognizant.pdf/.txt
`grep -c` for U+2014 = 0 (no em-dashes). Two-role evidence per brief, FlowSpace is not the only proof
paragraph:
1. FlowSpace: n8n CRM/GTM automation, OfficeRnD/Nexudus API integrations, Python/TypeScript AI listing
   tool, all versioned through GitHub; plus the automated live migration off the legacy stack onto
   Next.js and Laravel (2,000 to 4,500+ users).
2. Get2Germany: n8n automation tools integrated against Google APIs, database optimisation.
Explicit, honest paragraph stating no production experience with Jenkins, Terraform or Ansible, and
naming what is actually held instead (CI/CD fundamentals, GitHub workflow discipline, Python automation
scripting). Sweden work-authorisation transparency line (not authorised, would need employer-side
permit/sponsorship, ready to relocate).

## Standing answers on file for whoever finishes this row
- Years: 3. Salary if asked: EUR 45,000-55,000, aligned to band bottom (JD states no explicit salary).
- Start: available immediately, two weeks after offer.
- Sweden work authorisation: authorised No, sponsorship/employer permit Yes (per
  answers/work-authorisation.md standard table).
- Languages: English C2, Italian conversational (not relevant to this JD).
- Jenkins / Terraform / Ansible experience: honest No / 0 years each if asked directly.
- How did you hear: LinkedIn.

## Files ready
Prabhavit_CV_Cognizant.tex/.pdf, CoverLetter_Cognizant.tex/.txt/.pdf. No confirmations file (nothing
submitted). Logged in applications.csv (status NEEDS YOU) and NEEDS_YOU.md section C, row 17r.
