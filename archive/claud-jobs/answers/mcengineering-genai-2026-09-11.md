# MC Engineering - Gen AI Engineer (Turin, remote) - 2026-09-11

LinkedIn: https://www.linkedin.com/jobs/view/4443978264/
ATS (Inrecruiting/intervieweb.it, guest form): https://mcengineering.intervieweb.it/jobs/gen-ai-engineer-243429/it/?src=LinkedIn (req slug gen-ai-engineer-243429)

## Dedupe
- `python3 loop/dedupe.py --check "MC Engineering" "<ats url>"` -> HIT COMPANY (not HIT URL).
- `grep -i "MC Engineering" applications.csv` returned 5 prior rows, none for this requisition (Gen AI Engineer, Turin): AI Automation Engineer (LEAD), Power Platform Agentic Developer (LEAD), AI Integration Engineer (NEEDS YOU / saved), AI Integration Engineer again (GATED - password reset sent), Software Engineer - Test Automation (QUEUED NOT CV ONLY), AI Platform Engineer (NEEDS_YOU - same intervieweb.it gate). No SUBMITTED/NEEDS YOU/INTERVIEW/REJECTED row for this exact requisition or same-level role in the last 60 days blocks this one, so proceeded per task instructions.
- Confirmed via tabs_context that another agent's tab (550850564 / 550850561) was on a different MC Engineering requisition, "Claude Code Specialist" (slug claude-code-specialist-243423) - never touched those tabs.

## CV decision
`Prabhavit_CV_MCEngineering.pdf`/`.tex` already existed (touched 2026-09-11 15:47, evidently just built by the concurrent agent for the Claude Code Specialist requisition): its Technical Skills section had been reordered to put "Development -- Claude Code, Laravel, Typescript" ahead of "AI/ML -- AI Agents, RAG...", which fits a Claude-Code-titled role but not this LLM/RAG/microservices-focused Gen AI Engineer JD, and reusing a file another concurrent agent might still be writing to risked a race. Built a fresh `Prabhavit_CV_MCEngineering_GenAI.tex/.pdf` instead, per the task's fallback instruction.

Tailoring from `Prabhavit_CV_EN.tex` (no sentences rewritten, no claims added):
- Career Summary: kept bullets 1+2 (LLM-driven applications/intelligent workflows; AI-assisted development/prompt engineering/API integrations) - both name JD-matching themes verbatim. Dropped bullet 3 (generic "production-ready features").
- Technical Skills: kept EN.tex's existing order (AI/ML first) - already JD-relevant-first for this LLM/RAG role, no change needed.
- FlowSpace (min 3): kept "Streamlined customer support with AI agents" (top) + "Scaled platform 2000->4500+ users" under Product; "AI tool for processing and scraping of data" (top) + "Integration of external APIs (Office Rnd and Nexudus)" under Technical = 4 bullets. Dropped the Bubble.io migration bullet (duplicated + legacy-platform mention, JD has no migration/legacy angle), CRM/GTM automation bullet, business-logic-documentation bullet, Agency-communication bullet, commute-time-tool bullet (none clearly relevant to a GenAI/LLM/microservices JD).
- Urlink (AI-assisted dev role, close to JD theme): kept all 3 original bullets, none clearly irrelevant.
- UltraStrategy (AI JD, min 2): kept both existing bullets (CV parsing tool with n8n/Eden AI; platform for different user profiles).
- Get2Germany (AI JD, min 2): moved "Developed AI based automation tools for finding courses, internships and jobs" to top, kept "Integration of Google APIs for effective tracking of the platform". Dropped "UI/UX work, design from Figma to Bubble" (Bubble mention, unrelated to this JD) and "Building the platform, database optimization" (kept minimum satisfied without it).
- Qomodo (min 1): kept "Made a dashboard..." only, dropped "Implementation of Figma designs" (more generic).
- Clubee (min 1): kept "Integration of Clubee API for all of frontend" only (directly matches JD's "integrazione di servizi ... tramite API" ask), dropped unit-testing and domain/shop/federation-dashboard bullets.
- Tractionboard (min 1, one-line aside per Material rules): kept "ChatGPT/OpenAI integration" only.
- Additional Information: dropped the "Low code development/" prefix from IT Skills (JD has zero relation to low-code) - "AI based development, AI (RAG, Chatbot) and API integration, Automation (n8n), Project Management, Communication" retained.
- Compiled with tectonic: 2 pages confirmed via `pdfinfo`.

## Cover letter (Italian, per task instructions)
`CoverLetter_MCEngineering_GenAI.txt` (264 words) and matching `.tex`/`.pdf`. Natural plural "voi", no "Lei", 0 em-dashes (`grep -c` confirmed on both). Two lead-proof paragraphs as instructed: UltraStrategy CV-parsing pipeline (Affinda + Claude API for parsing/generation, n8n + Eden AI for the CV-data-extraction tool, standardised "Ultra CV" output) paired with FlowSpace (AI support agents grounded in live platform data with confidence-based escalation; AI listing bot from brochure to draft listing, 900+ produced) as the lead paragraph; Urlink (AI-assisted platform build, client automations) and Get2Germany (Google API integrations, AI tools for courses/internships/jobs) as the second-proof paragraph. Three years stated plainly ("tre anni di esperienza continuativa, da agosto 2023"). All claims trace to loop/OUTREACH_FACTS.md section 3 and its Italian glossary (section 5).

**No cover-letter field or second file-upload slot exists on this ATS form** (Inrecruiting guest form has only: Nome, Cognome, Email, Conferma Email, Data di nascita, Indirizzo di domicilio, Numero di cellulare, Cittadinanza, Livello di istruzione, Lingue (Inglese), File CV upload, Foto upload (optional), Video presentazione (optional), Privacy policy checkbox). The letter could not be attached or pasted anywhere; it is kept on file only.

## Form fields filled (guest form, no login)
- Nome: Prabhavit / Cognome: Gupta
- Email + Conferma Email: prabhavitg@gmail.com
- Data di nascita: 21-02-2001
- Indirizzo di domicilio: typed postcode 30175 in the "CAP o Città" sub-field, selected "30175 (Venezia)" -> auto-resolved Nazione=Italia, Provincia=Città Metropolitana di Venezia, Comune=Venezia, Frazione=Venezia -> final value "30175 Venezia VE, Italia"
- Numero di cellulare: +39 (pre-selected) 351 610 7807
- Cittadinanza: Indiana
- Livello di istruzione: Laurea 3 anni (closest match to the Bachelor's at Ca' Foscari)
- Inglese: C2
- File CV: Prabhavit_CV_MCEngineering_GenAI.pdf uploaded and confirmed attached (filename shown in the dropzone)
- Foto: left blank (optional)
- Video presentazione: left blank (optional, "Aggiungi Video presentazione" not clicked)
- Privacy policy checkbox: ticked ("Dichiaro di aver letto e compreso l'informativa")

## Blocker
Clicking "Invia" returned: "Errore! Utente già registrato! ... accedi alla tua area candidati ... qui / Hai dimenticato la password? ... qui". The email prabhavitg@gmail.com already exists as an Inrecruiting candidate profile on this MC Engineering tenant, carried over from two earlier stuck MC Engineering applications (applications.csv rows dated 2026-08-26 AI Integration Engineer and 2026-09-04 AI Platform Engineer, both already logged NEEDS_YOU/GATED on this same intervieweb.it wall). The only two paths offered are logging in or resetting the password - both require entering/setting a password, which is prohibited for me (account creation / credential handling). Nothing was submitted. Materials are ready for the user or a future session once logged in.

## Outcome
STATUS: NEEDS YOU. Logged to applications.csv, loop/results/MCEngineering-GenAI.txt, and NEEDS_YOU.md section C (row 17p).
