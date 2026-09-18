# Drees & Sommer Espana -- Experienced AI Engineer -- 2026-09-10

Source: `Prabhavit_CV_EN.tex` -> `Prabhavit_CV_DreesSommer.tex` -> `Prabhavit_CV_DreesSommer.pdf` (2 pages, compiled with tectonic, no errors).

JD focus (live LinkedIn posting, English, seniority level shown as "Entry level" despite the "Experienced" title): design, develop and deploy AI solutions end to end (RAG pipelines, agents, tools, skills, MCP connections); front-end and back-end components (Python, TypeScript, React, FastAPI, Docker, CI/CD); documentation, knowledge transfer and adoption/scaling support; degree in CS/Data Science/Math/Physics or a comparable field; practical AI engineering experience via professional work, internships, research or personal projects; English C1.

## Gates checked on live JD
- No years-of-experience number stated (role is framed by practical experience, not a threshold) -- pass.
- Title "Experienced Artificial Intelligence Engineer (AI Engineer)", LinkedIn seniority tag "Entry level" -- not Senior/Staff/Lead/Principal/Manager/CTO -- pass.
- Degree requirement: "comparable field" explicitly accepted, not a strict MSc/PhD -- pass.
- Language: JD entirely in English, only English C1 required, no Spanish or German requirement -- pass.
- Core stack: Python, TypeScript, React, FastAPI, Docker, CI/CD -- all on the claimable list (FastAPI/Docker as working knowledge) -- pass.
- No anti-AI disclaimer found (grepped JD text for "AI-generated", "without any AI", "no AI", none present).
- Not closed: LinkedIn guest API apply-button count = 1; live page showed "3 people clicked apply", Apply button active, "Responses managed off LinkedIn" (offsite).
- Dedupe: `python3 loop/dedupe.py --check` returned NEW; `grep -i "drees" applications.csv` returned no prior rows.

## Career Summary
Kept (2 of 3):
- "AI Solutions & Automation Engineer with hands-on experience building LLM-driven applications and intelligent workflows across European tech projects."
- "Transformed business requirements into production-ready features, delivering AI agents, LLM-powered data parsing, rapid prototypes, and rigorous QA testing."

Dropped: "Skilled in AI-assisted development, prompt engineering, and orchestrating complex API integrations." (weakest against RAG/agents/production-deploy keywords).

## Technical Skills
Reordered per the job's explicit ask (Python, LLM/RAG, TypeScript/React, FastAPI/Flask first):
- `Development -- Python, Typescript, React, FastAPI/Flask (working knowledge), Docker (working knowledge), Claude Code, Laravel` (Python/React/FastAPI/Docker added as skill-list items; all four are on the brief's Claimable list and the Master Experience claim ladder explicitly allows FastAPI/Flask and Docker as working-knowledge skills items -- no production claim made for them anywhere else).
- `AI/ML -- RAG, AI Agents, Chatbot development, API integration, Eden AI, OpenAI/ChatGPT integration` (RAG moved first).
- Automation and Project/Design categories unchanged, moved after the two JD-relevant categories.

## Additional Information
- IT Skills line: dropped "Low code development" (JD has no low-code relation), reordered to lead with AI/API items: "AI (RAG, Chatbot) and API integration, AI based development, Automation (n8n), Project Management, Communication".
- Tools line: reordered to lead with Typescript: "Typescript, Claude Code, Laravel, Supabase, n8n, Jira, Slack".

## Professional Experience -- moves and drops

### FlowSpace.co (kept 8 bullets across both sub-lists, well above the 3-bullet minimum)
Product Responsibilities -- reordered:
1. Streamlined customer support with AI agents
2. Collaborated with team of developers for product logic and business logic documentation
3. Overseeing the migration of app from Bubble.io to Next.JS and Laravel
4. Scaled platform from 2000 to 4500+ users through iterative product development
Dropped: "Facilitated communication between internal team and Agency" (generic, no AI/dev-stack/documentation keyword match).

Technical Responsibilities -- reordered:
1. AI tool for processing and scraping of data and increasing listings on platform
2. Integration of external APIs (Office Rnd and Nexudus) for automated bookings
3. Consolidated leads in CRM and automated lead capture by developing integration between CRM used by the organization
4. GTM automations for sales funnel, lead enrichment and outbound
Dropped: "AI tool for processing of data and increasing listings on platform" (exact duplicate of bullet 1 in the base file); "Overseeing the migration of app from Bubble.io to Next.JS and Laravel" (duplicate of the Product Responsibilities bullet); "Developed a tool for companies to calculate commute times" (least relevant to RAG/agents/Python/TS/React/integrations/documentation themes).

### Urlink (kept 1 of 3, per this job's "1 per other role" instruction)
1. Using AI for building the platform and logics
Dropped: "Implementing UIs made with AI"; "Implementing automations in regards to client requirements".

### UltraStrategy.com (kept 1 of 2)
1. Made a CV parsing tool using n8n and Eden AI (LLM data-extraction pipeline, closest match to "LLM pipelines").
Dropped: "Developed platform for different user profiles".

### Qomodo (kept 1 of 2)
1. Made a dashboard to be used by the companies to manage their branches
Dropped: "Implementation of Figma designs" (design task, not code/AI).

### Get2Germany.com (kept 1 of 4)
1. Developed AI based automation tools for finding courses, internships and jobs
Dropped: "Integration of Google APIs for effective tracking of the platform"; "UI/UX work, design from Figma to Bubble"; "Building the platform, database optimization".

### Clubee.com (kept 1 of 3)
1. Integration of Clubee API for all of frontend (integrations + frontend, matches TypeScript/React theme).
Dropped: "Unit testing and quality assurance of new features"; "Developed tools for: domain integration, shop, federation dashboard".

### Tractionboard.co (kept 1 of 5)
1. ChatGPT/OpenAI integration (LLM API integration, most relevant).
Dropped: "Implementation of designs from Figma to Bubble"; "Implementation of Sendgrid"; "Responsive designs, de-bugging"; "Google Ads 4 implementation".

## Result
- Page count: 2 (photo included), compiled clean with tectonic.
- Every role, date and location preserved; all kept bullets are verbatim from the original.
- Parity check (pdftotext, no -layout, bullet markers stripped, LaTeX escaping/dash/ligature normalized): 46 long lines (>25 chars), 8 flagged as not found verbatim in the base .tex text -- of those, 4 (Development skills line, AI/ML skills line, IT Skills line, Tools line) are the intentional reorderings/additions documented above (same tokens, new order, four new claimable skill words); the other 4 (Automation, Project/Design, Language, Work Authorization lines) are unchanged text that only failed the check because the verification script does not strip the `\textbf{...}` LaTeX macro wrapper -- manually confirmed identical to the base file. No fabricated claims.

## Cover letter
`CoverLetter_DreesSommer.txt`, 250 words. Claims traced to `Prabhavit - Master Experience.md`: AI listing pipeline (brochure/website/spreadsheet -> LLM extraction -> drafted listing -> human review), "900+ listings drafted" proof point, support AI agents with confidence-based escalation, TypeScript/Next.js + Node.js/Laravel + Python stack, OfficeRnD/Nexudus integrations, platform migration + documentation/handover work. No em-dashes (`grep -c "—"` = 0). No no-code/low-code/Bubble wording. No Claude/Anthropic mention. No PDF built: the SmartRecruiters form has no separate cover-letter upload field, only a "Message to the Hiring Team" text box, which the letter text was pasted into.

## Answers given on the form
- Name: Prabhavit Gupta. Email/confirm email: prabhavitg@gmail.com.
- City: Venice, Veneto, Italy (selected from autocomplete).
- Phone: country code switched from the form's Spain default to Italy +39, number 351 610 7807.
- LinkedIn: https://www.linkedin.com/in/prabhavit. Website: https://github.com/prab-gupta.
- Message to the Hiring Team: full cover letter text (work-authorisation transparency line included in the closing paragraph: EU long-term resident, not currently authorised in Spain, would need employer-side permit, ready to relocate to Malaga).
- Salary: not asked on this form (no salary field present before the blocker).
- Resume: not uploaded -- see blocker below.

## Blocker (STATUS: NEEDS YOU)
The required "Resume *" field is a SmartRecruiters `spl-dropzone` custom element. Its real `<input type=file data-test="resume-upload">` lives inside a shadow root that Claude in Chrome's read_page/find tools cannot produce a ref into (confirmed by direct DOM walk finding the element via JS, then confirming `find` returns "no browse button as children" of the Resume section, and `file_upload` on the container ref errors "Element is not a file input"). Clicking the visible "Choose a file" text would open a native OS file picker outside tool control, which is against the browser rules. Left the form filled, did not submit. See `confirmations/DreesSommer-2026-09-10.txt` for the full note and tab id.

## Follow-up session (Playwright MCP, resolved the Resume blocker) -- STATUS: SUBMITTED

Resume uploaded successfully via Playwright: clicked the Resume * "Choose a file" button, Playwright intercepted the
native file-chooser (shadow DOM was not an obstacle for Playwright's locator engine, unlike Claude in Chrome), and
`browser_file_upload` attached `Prabhavit_CV_DreesSommer.pdf`. Filename confirmed rendered in the dropzone.

Page 2, "Preliminary questions" (not present/seen in the prior blocked session):
- Salary expectation (required, free text): "EUR 45,000 gross annual"
- Notice period / availability (required, free text): "Available immediately, can start within two weeks of an offer."
- Additional attachments (optional): left empty.
- "I agree that my application may also be considered for other positions in the Drees & Sommer group." (required radio): No.
- Required privacy-notice checkbox: ticked. Optional "join communities for future career opportunities" checkbox: left unticked.

Submitted. Success page text: "Application submitted! Your application for Experienced Artificial Intelligence
Engineer (AI Engineer) at Drees & Sommer Digital Services has been submitted successfully. You'll receive a
confirmation email shortly." Screenshot: confirmations/DreesSommer-2026-09-10.png.
