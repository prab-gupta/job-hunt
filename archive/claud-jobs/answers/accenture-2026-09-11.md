# Accenture Italia — AI Native Software Engineering Specialist

Job (LinkedIn): https://www.linkedin.com/jobs/view/4441357652/
Job page (accenture.com): https://www.accenture.com/it-it/careers/jobdetails?id=R00344641_it (job n. R00344641, Rome / Multiple Locations)
Apply URL (Workday): https://accenture.wd103.myworkdayjobs.com/AccentureCareers/job/Roma/AI-Native-Software-Engineering-Specialist_R00344641/apply
Date: 2026-09-11

## Gate check
- Cheap check: `curl ... jobPosting/4441357652 | grep -c apply-button` = 1 (pass).
- LinkedIn "Apply on company website" -> accenture.com job page (live text matches the saved JD exactly). Internal label "AI Native Software Engineering Team Lead/Consultant | Mid-Level | Full time" - "Team Lead/Consultant" here is Accenture's job-family name, not a seniority title, and the level tag is explicitly "Mid-Level", so the Senior/Staff/Lead/Principal/Manager/CTO title gate did not trigger.
- No explicit numeric years-of-experience floor (the JD's "three production systems in four years" line is a preference framing, not a hard requirement number). No MSc/PhD requirement. No German/Italian-only language requirement (the JD text itself is in English; the site chrome is localised Italian). Core stack is Python-led with Java "acceptable", both claimable per the brief. Location Rome, Italy, EU. No anti-AI disclaimer.
- Dedupe: `dedupe.py --check "Accenture Italia" <url>` = HIT COMPANY. `grep -i accenture applications.csv` showed many Accenture Greece LEAD rows (different company, not blocking), one existing Accenture Italia NEEDS YOU row ("AI Native Software Engineering Analyst", Milan, Workday req R00344568/R00344568-style URL) and one Accenture DACH NEEDS YOU row. This lead's Workday requisition (R00344641, Specialist, Rome) is confirmed different from the prior Analyst req (R00344568) by requisition id and URL, so it is a different requisition, not a duplicate. Proceeded.
- Verdict: gates pass, proceeded to the Workday apply flow.

## Apply flow result: account creation required (user-only)
On the Workday landing page ("Start Your Application") there are three options: Autofill with Resume, Apply Manually, Use My Last Application. Clicking "Apply Manually" advances the 6-step Application Progress bar to step 1, "Create Account/Sign In", and the page immediately redirects to a Workday Sign In screen (page title becomes "Sign In"). There is no guest-checkout or "continue without an account" path on any of the three buttons. Per the brief, account creation is user-only, so the flow was stopped here without creating an account.

## Materials prepared for the user to submit after they sign in
- CV: Prabhavit_CV_Accenture.tex/.pdf (2 pages, verified with `pdfinfo`).
  - Career Summary: kept bullets 1 and 3 (LLM-driven applications/intelligent workflows; production-ready features, AI agents, LLM data parsing, QA), dropped bullet 2 (prompt engineering/API integrations).
  - FlowSpace Product Responsibilities: "Streamlined customer support with AI agents" moved to top (closest to "production agentic architectures"); kept scale (2000->4500+) and migration bullets; dropped the two generic collaboration bullets.
  - FlowSpace Technical Responsibilities: deduped the repeated AI-tool and migration lines from the source .tex, dropped the one-off commute-time tool, kept the AI listing tool, OfficeRnD/Nexudus integration, CRM/lead-capture and GTM automation bullets (7 FlowSpace bullets total, minimum 3).
  - Urlink: dropped the UI-only bullet, kept the AI platform-build and client-automation bullets.
  - UltraStrategy: kept both bullets unchanged (AI/automation JD minimum of 2 - CV-parsing tool, multi-profile platform).
  - Qomodo: kept the dashboard bullet, dropped the Figma-implementation bullet.
  - Get2Germany: kept both AI-automation-tools and Google-API bullets (AI/automation JD minimum of 2), AI bullet moved to top; dropped the Figma/Bubble UI bullet and the generic platform/database bullet.
  - Clubee: kept both remaining bullets (Clubee API integration; unit testing and QA - the QA bullet ties to the JD's "eval harness"/quality-metrics theme); dropped the tools-list bullet.
  - Tractionboard: kept only "ChatGPT/OpenAI integration" (direct LLM-provider-integration match); dropped Figma/Sendgrid/responsive-design/Google-Ads bullets.
  - Additional Information / IT Skills: dropped the "Low code development/" prefix (JD has no low-code relation); order otherwise unchanged.
  - No sentences rewritten, no claims added.
- Cover letter: CoverLetter_Accenture.tex/.txt/.pdf (270 words). Two-role evidence per the letter rule: FlowSpace (AI listing bot 900+ listings, support AI agents with confidence-based escalation, live migration 2,000->4,500+ users) and UltraStrategy (CV-parsing pipeline: Affinda + Claude API for parsing/generation, n8n + Eden AI for the extraction tool), with a one-line Get2Germany aside (Google API integration, AI course/job-finder tools). No em-dashes (`grep -c` for U+2014 = 0), no "no-code"/"low-code"/"Bubble" (none present), legacy platform referred to only as "a legacy stack". Italy is the work location so no relocation transparency line was needed (standard Italy answer: authorised Yes, no sponsorship).

## What the user needs to do
1. Open https://accenture.wd103.myworkdayjobs.com/AccentureCareers/job/Roma/AI-Native-Software-Engineering-Specialist_R00344641/apply (or reuse the same Accenture Workday account already created for the other pending Accenture leads, items #15/17c/17d/17e in NEEDS_YOU.md).
2. Sign in / create the account (their own credentials, per the brief's prohibition on Claude creating accounts).
3. Say "accenture specialist ready" (or equivalent) so the rest of the 6-step form (My Information, My Experience, Application Questions, Voluntary Disclosures, Review) can be filled with Prabhavit_CV_Accenture.pdf + CoverLetter_Accenture.pdf and the standard Italy answers (authorised Yes, sponsorship No, salary EUR 45,000-55,000, years 3).

Logged in loop/results/Accenture.txt and appended as row 17f in NEEDS_YOU.md section C (Account creation).
