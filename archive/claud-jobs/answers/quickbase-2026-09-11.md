# Quickbase - Software Engineer 1 (Sofia, Bulgaria) - 2026-09-11

LinkedIn: https://www.linkedin.com/jobs/view/4453477700/
ATS: Workday, job page https://quickbase.wd504.myworkdayjobs.com/External/job/Sofia/Software-Engineer-1_R26_00162-1?source=LinkedIn
Apply-manually direct URL: https://quickbase.wd504.myworkdayjobs.com/en-US/External/job/Sofia/Software-Engineer-1_R26_00162-1/apply/applyManually?source=LinkedIn
Requisition: R26_00162

## Dedupe
`python3 loop/dedupe.py --check "Quickbase" "https://www.linkedin.com/jobs/view/4453477700/"` -> NEW. `grep -i quickbase applications.csv` -> no prior rows. Not a duplicate.

## Hard gates (all pass, no kill)
- Years: none stated, "early in your career" role. Title: Software Engineer I (not Senior/Staff/Lead/Principal/Manager). No MSc/PhD requirement. JD in English. Core stack: JavaScript/TypeScript + React, claimable. Location: on-site Sofia, Bulgaria (EU), "Unlimited remote work policy" listed as a benefit. No anti-AI disclaimer (`grep -iE "AI-generated|AI assistance|without any AI|no AI"` on the saved JD = clean); the JD explicitly wants AI-tool users (Claude Code, Copilot).

## Blocker
Workday tenant (quickbase.wd504.myworkdayjobs.com). Clicked Apply -> "Choose your application journey: Apply Manually / Use My Last Application" -> Apply Manually -> step 1 of 6 is "Create Account/Sign In" with an email + password + "Verify New Password" form and no guest/continue-without-account path. Per brief, account creation is user-only: stopped before any account was created.

## Materials prepared (ready for you or for me once you are signed in)
- CV: Prabhavit_CV_Quickbase.pdf (built from Prabhavit_CV_EN.tex, 2 pages, tectonic-compiled, bullet-for-bullet parity checked against the original .tex). Career Summary trimmed to 2 bullets (AI-assisted development + LLM-driven apps). Technical Skills reordered: Development (Claude Code/Laravel/Typescript) first. Professional Experience: 5 FlowSpace bullets (migration to Next.js/Laravel, OfficeRnD/Nexudus API integration, AI listing bot, AI support agents, team collaboration on documentation), 2 UltraStrategy, 2 Urlink, 2 Get2Germany, 2 Clubee, 1 Qomodo, 2 Tractionboard (API-integrations trigger from the brief applied since the JD requires REST/GraphQL API work, so UltraStrategy and Get2Germany both carry 2 bullets, not just FlowSpace). Dropped "Low code development" wording from Additional Information (JD has no low-code/Bubble relation); the FlowSpace migration bullet that names Bubble.io was kept because it evidences the Next.js/Laravel stack the JD wants.
- Letter: CoverLetter_Quickbase.txt and .pdf, 272 words. Lead paragraph FlowSpace (migration off legacy stack to Next.js/Laravel, AI listing bot, OfficeRnD/Nexudus API integrations, Claude Code daily use). Second paragraph Get2Germany (Google API integrations, AI tools for courses/internships/jobs) chosen over UltraStrategy because the JD's core ask is REST/GraphQL API work, not CV parsing/document AI. No em-dashes (`grep -c` em-dash = 0). No "no-code"/"low-code"/"Bubble" in the letter text.

## Answers ready for the Workday form once past the account wall
- Years of experience: 3
- Salary: EUR 45,000-55,000
- Work authorisation: authorised to work in Bulgaria = No; employer-side permit/sponsorship = Yes. Transparency line used in the letter: "I hold Italian EU long-term resident status. I am not currently authorised to work in Bulgaria and would need the applicable employer-side permit or sponsorship process. I am ready to relocate and complete that process."
- Relocation: Yes, to Sofia.
- Languages: English professional (C1), Hindi native, Italian beginner.
- How did you hear: LinkedIn.
