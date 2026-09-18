# EnduroSat — Technical Support Engineer — 2026-09-09

URL: https://www.linkedin.com/jobs/view/4464617541/
Channel: LinkedIn Easy Apply (JazzHR-powered, 2-page flow)

## Gate re-check on live JD
- Seniority: "Not Applicable" (LinkedIn field) / no years-of-experience minimum stated anywhere in the JD text. Pass.
- Title: Technical Support Engineer. Not Senior/Staff/Lead/Principal/Manager/CTO. Pass.
- Degree: no MSc/PhD requirement mentioned. Pass.
- Language: JD is entirely in English. Pass.
- Core stack kill check: JD explicitly says "Familiarity with Python and/or C programming languages ... this is not a code-heavy role but an understanding of concepts and tools will allow you to excel during communication with engineering teams" — listed only under "How to Stand Out", not a requirement, and the role itself is customer support (email/chat/video), not engineering. No Java/.NET/C++/Go/Rust/Django/FastAPI/cloud-admin core requirement. Pass.
- Location: Sofia, Bulgaria, on-site, full-time. EU country; task instructions marked this role as ready-to-relocate, remote-if-offered (remote was not offered — on-site only). Pass.
- Posting live: "15 hours ago", "7 applicants", Easy Apply active. Pass.

No gate failed. Fit 42 applied under the hard-gates-only rule.

## Dedupe
`python3 loop/dedupe.py --check "EnduroSat" "https://www.linkedin.com/jobs/view/4464617541/"` → `NEW`
`grep -i endurosat applications.csv` (before this run) → no rows. Clean NEW, no prior EnduroSat history.

## Form fields (contact info page)
- First name: Prabhavit / Last name: Gupta (pre-filled from LinkedIn profile)
- Phone country code: Italy (+39) (pre-filled)
- Mobile phone number: 351 610 7807
- Email: prabhavitg@gmail.com (pre-filled)
- Address: Via Zanetti, 10
- City: Venice
- State: Veneto
- Postal: 30175

## Resume
Selected from LinkedIn's resume library: "Prabhavit_CV-.pdf" (9/7/2026) — matches the brief's named library file and is the user's original CV. Did not use the newer "Prabhavit_CV.pdf" (9/8/2026) that was pre-selected by default, since it does not match the brief's specified filename.

## Cover letter
No cover letter field of any kind (upload or paste) appeared in this Easy Apply flow — it is a short 2-step JazzHR flow (contact info -> resume -> review/submit), no free-text or file questions beyond resume. Prepared both `ROOT/CoverLetter_EnduroSat.txt` (204 words) and `ROOT/CoverLetter_EnduroSat.pdf` (built via tectonic from `CoverLetter_EnduroSat.tex`, confirmed 1 page) per the brief, but there was nowhere to attach or paste either. Kept on file in case of future direct-ATS follow-up.

Cover letter content traced to `Prabhavit - Master Experience.md`:
- RAG-backed support agents with confidence-based escalation → "Support AI agents that answer customer queries against live platform data and escalate to a human on low confidence."
- OfficeRnD/Nexudus integration support for live operators → "OfficeRnD and Nexudus API integrations for automated bookings."
- Debugging production booking flows → "maintaining the platform... understanding and resolving customer issues as they come up" + FlowSpace day-to-day description.
- Python automation → Skills: "LLM integration & pipelines... n8n, Make" and Python listed under Languages & frameworks.
- Eight companies in three years → "Eight European companies in ~3 years... ramps up fast."
- Checked `grep -c "—" CoverLetter_EnduroSat.txt` = 0. No "no-code"/"low-code"/"Bubble"/"Anthropic" strings present.

## Work authorisation / relocation (recorded for consistency; no field asked for it on this short form)
Per `answers/work-authorisation.md`: role performed in Bulgaria (Sofia) = authorised now: No; sponsorship/employer-side permit needed: Yes. Transparency line used in the cover letter: "I hold an Italian EU long-term residence permit, which does not itself authorise me to work in Bulgaria, so I would need an employer-side permit or sponsorship; I am ready to start that process." Ready to relocate to Sofia, per task instructions.

## Other
- Unticked "Follow EnduroSat to stay up to date with their page" before submitting (checked by default).
- No years-of-experience numeric field, no notice-period field, no consent/EEO checkboxes appeared on this form — the flow was limited to contact info + resume + follow-checkbox + submit.
- Confirmation seen: "Your application was sent to EnduroSat! You can keep track of your application in the 'Applied' tab of My Jobs" plus page-level "Application status: Application submitted".
