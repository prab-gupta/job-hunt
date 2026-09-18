# Navigraph — Fullstack Developer — 2026-09-09

Job: https://www.linkedin.com/jobs/view/4464996019/ (LinkedIn Apply is external, "Responses managed off LinkedIn") -> redirected to careers.navigraph.com (Teamtailor) -> https://careers.navigraph.com/jobs/8342827-fullstack-developer

## Dedupe
`python3 loop/dedupe.py --check "Navigraph" "https://www.linkedin.com/jobs/view/4464996019/"` returned NEW. No prior Navigraph row in applications.csv.

## Cheap check / apply-button gate
`curl -s -A "Mozilla/5.0" https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/4464996019 | grep -c apply-button` = 1. Live page confirmed an "Apply" control (external, not Easy Apply) and the Teamtailor job page confirmed "Apply for this job".

## Hard-gate re-check on full JD (fetched via jobs-guest API + live careers.navigraph.com posting)
- Seniority level tag: Entry level.
- No years-of-experience number stated anywhere in the JD.
- Title is "Fullstack Developer", not Senior/Staff/Lead/Principal/Manager/CTO.
- No MSc/PhD requirement.
- JD fully in English; no Swedish language requirement (only "Swedish-born company" language, not a language requirement).
- Core stack: TypeScript, Node.js, NestJS, React, React Native — all claimable. Required skills include "managing cloud and infrastructure, AWS Docker and CI/CD" as one bullet among several (not the core/primary stack, which is TypeScript/Node/React); judged not a hard-gate core-stack kill given the brief's pre-screen (fit 85) and that TypeScript/Node/React/API work is the dominant ask.
- No anti-AI clause: grepped JD text for "AI-generated", "AI assistance", "without any AI", "no AI" — zero hits.
- Location: Stockholm, Sweden, hybrid — EU, standard non-Italy work-authorisation rule applies.
All gates pass.

## Pre-screen question
"This position is based in our Stockholm office. Will you be able to work in Stockholm a couple of days/week?" — answered **Yes** (relocation: yes anywhere in EU; hybrid/on-site: yes per standing answers). Did not disable the form.

## Form fields (careers.navigraph.com, Teamtailor)
- First name: Prabhavit
- Last name: Gupta
- Email: prabhavitg@gmail.com
- Phone: +39 351 610 7807 (selected Italy +39 from country dropdown, overriding the Sweden default)
- Upload CV: Prabhavit_CV_Navigraph.pdf (verified filename shown in the dropzone after upload)
- Additional files: none uploaded (cover letter text field was available, used that instead)
- Cover letter (free-text box): pasted the full CoverLetter_Navigraph.txt body (199 words), ending "Regards, Prabhavit Gupta" — verified in the textarea after typing.
- Consent checkbox ("I agree that I have read the Privacy Policy and confirm that Navigraph store my personal details..."): ticked (required).
- "Yes, Navigraph can contact me directly about specific future job opportunities": left unticked (marketing/future-opportunities checkbox, per standing rule).
- No salary, years-of-experience, or notice-period fields were present on this form.
- Did not use "Apply with LinkedIn" (avoids an OAuth/account-link action); filled manually instead.

## CV tailoring (Prabhavit_CV_Navigraph.tex/.pdf, built from Prabhavit_CV_EN.tex)
- Career Summary: kept 2 bullets ("Skilled in AI-assisted development... orchestrating complex API integrations" and "Transformed business requirements into production-ready features... rigorous QA testing"); dropped the "AI Solutions & Automation Engineer... LLM-driven applications" bullet as the JD has no AI/LLM ask.
- Technical Skills: reordered categories, Development (Claude Code, Laravel, Typescript) moved to top.
- Professional Experience:
  - FlowSpace: trimmed Product Responsibilities to 3 bullets (Scaled platform 2000->4500+ users; Collaborated with team on product/business logic; Streamlined customer support with AI agents) and Technical Responsibilities to 3 bullets (Integration of external APIs Office Rnd/Nexudus; Developed commute-time calculator tool; Consolidated CRM lead integration). Dropped: "Facilitated communication between internal team and Agency" (weak relevance); both AI-tool-for-listings duplicate bullets; GTM automations bullet (marketing-specific); and "Overseeing the migration of app from Bubble.io to Next.JS and Laravel" (appeared twice in the original) — dropped per the standing "never write Bubble" material rule, since the sentence cannot be edited and must stay verbatim if kept. This was the single most JD-relevant bullet in the original CV (Next.js/Laravel full-stack migration) and its removal is the main tradeoff of this rule.
  - Urlink, UltraStrategy, Get2Germany, Clubee, Tractionboard: kept all non-Bubble bullets, reordered for relevance; dropped "UI/UX work, design from Figma to Bubble" (Get2Germany) and "Implementation of designs from Figma to Bubble" (Tractionboard) for the same Bubble-mention reason. Role titles de-Bubbled: "AI and Low-Code Developer" -> "AI Developer" (Qomodo), "Low Code Developer and Quality Assurance" -> "Developer and Quality Assurance" (Clubee), "Low-Code Developer" -> "Developer" (Tractionboard). Tools lines had "Bubble.io" removed (Technical Responsibilities/FlowSpace, Get2Germany, Clubee, Tractionboard); Qomodo's Tools line (which was only "Bubble") dropped entirely.
- Additional Information: dropped "Low code development/AI based development" phrase from IT Skills; reordered Tools to put Typescript/Laravel first.
- Compiled with tectonic, 2 pages including photo (pdfinfo confirmed Pages: 2).

## Cover letter (CoverLetter_Navigraph.txt/.tex/.pdf, 199 words)
Built from CoverLetter_eduBITES.tex template. Content: FlowSpace full-stack proof (Next.js/TypeScript frontend, Node.js/Laravel backend, Supabase/PostgreSQL, OfficeRnD/Nexudus API integrations, Playwright, 900+ listing LLM pipeline, 2,000->4,500+ user scale, legacy-stack migration to Next.js/Laravel); why Navigraph (1.7M-user consumer SaaS, matching TypeScript/Node/React stack); logistics (Venice-based, Italian EU long-term resident, not authorised in Sweden, needs employer-side permit, ready to relocate to Stockholm). No em-dashes (`grep -c "—"` = 0). No "Bubble"/"low-code"/"no-code" (grepped, zero hits). PDF compiled with tectonic, 1 page confirmed via pdfinfo.

## Salary / years / notice
Not asked on this form.

## Result
SUBMITTED. Confirmation page text: "Thanks for applying / We have received your application and we will be reviewing it shortly." Progress indicator showed "Applied" step complete. Screenshot captured (Chrome save-to-disk did not resolve to a locally readable path in this session; per the brief's Chrome-section note that PNG saving is not available in Chrome, the confirmation text file is the record: confirmations/Navigraph-2026-09-09.txt).
