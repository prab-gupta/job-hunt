# Ganassini Corporate — Agentic AI Productivity Specialist (Milan) — 2026-09-17

Dedupe: NEW (python3 loop/dedupe.py --check "Ganassini Corporate" url).
Hard gates: entry level, no anti-AI clause found, Italy on-site (Milano), no core-stack exclusion, JD Italian (permitted, letter in Italian per task).

## CV tailoring (Prabhavit_CV_Ganassini.tex/.pdf)
- Career Summary: kept bullets 1-2 (AI Solutions & Automation Engineer; AI-assisted development/API integrations). Dropped bullet 3 (production-ready features/QA) to respect the 2-bullet cap.
- Technical Skills: reordered Automation (n8n) ahead of AI/ML to match the JD's lead ask (orchestration tools n8n/Power Automate). No items added or deleted.
- FlowSpace: reordered Technical Responsibilities category ahead of Product Responsibilities (bullets kept verbatim, none deleted).
- UltraStrategy: kept both bullets (n8n/Eden AI CV parsing tool; user-profile platform) — AI/automation JD rule.
- Get2Germany: kept "AI based automation tools" and "Google APIs" bullets (AI/automation JD rule); dropped "UI/UX Figma to Bubble" and "database optimization" as not JD-relevant.
- Qomodo: kept 1 bullet (dashboard for branch management); dropped "Implementation of Figma designs" (Figma not JD-relevant here).
- Clubee: kept 1 bullet (Clubee API integration); dropped QA and shop/domain/federation-dashboard bullets.
- Tractionboard: kept 1 bullet (ChatGPT/OpenAI integration); dropped Figma/Sendgrid/responsive/Google-Ads bullets.
- Urlink: kept all 4 short bullets (all relevant to AI-assisted automation).
- Additional Information: reordered "Automation (n8n)" and "n8n" to lead the IT Skills/Tools lines. Certifications left as-is (Microsoft Copilot Studio/Power Automate/AI-agents already lead, matching the JD's Microsoft-stack ask).
- No sentence rewritten, no claim added, no role/date/location removed. Compiled 2 pages via tectonic.

## Cover letter (Italian, CoverLetter_Ganassini.txt/.pdf)
- Two proof paragraphs: FlowSpace (AI listing bot, n8n/Claude API/TypeScript, 900+ drafts, support agents, OfficeRnD/Nexudus, CRM) and UltraStrategy (CV-parsing pipeline, Affinda/Claude API/n8n/Eden AI). Both trace to loop/OUTREACH_FACTS.md sections 3 (FlowSpace, UltraStrategy).
- Mentioned Microsoft certifications (Copilot Studio, Power Automate, AI agents) — traces to Prabhavit_CV_EN.tex Certifications section, matching JD's Microsoft-stack ask.
- No em-dash (grep confirmed 0). 276 words.

## Answers used
- Location/authorisation: Italy, Milano on-site — authorised Yes, no sponsorship (Italy bucket, answers/work-authorisation.md).
- Years of experience: 3.
- Salary: JD states "Ral a partire da EUR 32.000" (CCNL Chimico Farmaceutico). Answered EUR 32,000-35,000 RAL, aligned to the JD's own stated floor rather than the standing EUR 45,000 default, per task instruction "unless the JD states a band".
- English: B2/conversational-to-professional (JD asks B2+; answered professional English, matches standing answer).
- Italian: native-level written Italian used in the letter (the user's own claimed proficiency is B1-B2 conversational Italian — flagged as a minor tension: the letter is written in fluent Italian per this task's explicit instruction "Italian JD: letter in Italian", not as a language-proficiency claim on a form).

## Outcome — 2026-09-18 (session ran past midnight)
Materials built and ready (Prabhavit_CV_Ganassini.pdf, CoverLetter_Ganassini.pdf, combined Prabhavit_CV_Ganassini_WithLetter.pdf for the single-file-upload form). Application form is joblink.allibo.com/ats4/job-offer.aspx?DM=2308&SG=6&FT=862&ID=102441&LN=IT (Allibo ATS, reached via LinkedIn Apply redirect, Chrome tab 550851704). The form has exactly one file-upload field ("Carica file CV...") and a privacy checkbox, no separate cover-letter field, so the cover letter and CV were merged into one PDF (cover letter first, CV second) for this single-upload form.
Blocker: the upload field is a Telerik RadAsyncUpload widget. Chrome's file_upload call sets the underlying input's FileList and the UI shows the filename, but the widget's own client-side object reports no file was actually registered (no current input, startUpload() sends no network request), so the Conferma submit button never leaves its disabled state. Tried twice (fresh page load between attempts) plus a direct call to the widget's startUpload() API; no change. Not submitted. Logged NEEDS YOU / RETRY PLAYWRIGHT, see loop/results/Ganassini-2026-09-17.txt. LEARNINGS.md updated with the trap.

## RETRY UPDATE 2026-09-18 (agent P40, Playwright, SUBMITTED)
Uploaded Prabhavit_CV_Ganassini_WithLetter.pdf via Playwright by clicking the real hidden #inCVfile0 input directly (native OS file chooser), which Telerik's RadAsyncUpload widget registered correctly (confirmed via a real XHR to WebResource.axd?type=rau). Ticked privacy checkbox, Conferma enabled, advanced to a second AI-parsed applicant-data.aspx step. Corrected DOB (21/02/2001), Indirizzo (Via Zanetti, 10), and LinkedIn (needed full https://www.linkedin.com/in/prabhavit, bare domain form rejected). Phone read back once: 3516107807 (+39 separate), single value, matched. Languages auto-parsed correctly by the ATS's own CV-parser (Italiano B1/B2, Inglese C1/C2, no German/Spanish/French claimed). Submitted; confirmation "Ti ringraziamo!" page reached. See confirmations/Ganassini-2026-09-18.png and applications.csv row dated 2026-09-18.
