# CV tailoring -- PagerDuty

Source: `Prabhavit_CV_EN.tex` -> `Prabhavit_CV_PagerDuty.tex` -> `Prabhavit_CV_PagerDuty.pdf` (2 pages, compiled with tectonic, no errors).

JD focus: AI/ML Engineer (explicitly early-career), PagerDuty, Lisbon, Portugal, hybrid, Greenhouse job 6147470004. Required: 2+ years software engineering shipping production software; CS degree or equivalent practical experience; hands-on experience with LLMs, prompting, retrieval, or agent frameworks; comfort moving between application code and AI/model code; some exposure to distributed systems. Nice to have: cloud infrastructure (AWS/GCP/Azure), LangChain/LlamaIndex, vector databases, Kafka/Airflow, agentic systems, evaluation/guardrails for LLMs.

## Career Summary
Kept (2 of 3), reordered to lead with the production/agents bullet:
1. "Transformed business requirements into production-ready features, delivering AI agents, LLM-powered data parsing, rapid prototypes, and rigorous QA testing." (matches "help build and ship AI systems that run in production... Incident Management AI Agents")
2. "Skilled in AI-assisted development, prompt engineering, and orchestrating complex API integrations." (matches "prompt and agent orchestration... tool/API integrations")

Dropped: "AI Solutions & Automation Engineer with hands-on experience building LLM-driven applications and intelligent workflows across European tech projects." (more generic than the other two against this JD's specific asks).

## Technical Skills
Reordered within lines only, nothing deleted:
- AI/ML: "AI Agents, RAG, API integration, OpenAI/ChatGPT integration, Chatbot development, Eden AI" (agents/RAG/API/LLM-API led, chatbot/Eden AI moved last as least relevant to a backend AI/ML infra role).
- Development: "Typescript, Claude Code, Laravel" (Typescript led as the closest existing item to "application code"; Laravel moved last).
- Project/Design: "GitHub, Jira, Postman, Figma, Trello" (GitHub led as most engineering-relevant).
- Automation line unchanged ("n8n, Playwright").

**Note on Python/cloud infra:** the task instruction to bring "Python... first" could not be done literally -- Python is not a skill-list item anywhere in the base `Prabhavit_CV_EN.tex` (confirmed by grep), though it is claimable per the Master Experience file's claim ladder. Per brief rule 4 ("reorder... delete nothing else") and rule 1 ("do not add claims"), reordered existing items toward that intent instead (Typescript led in Development, AI/ML led overall) rather than inserting a new "Python" token. Same precedent as the VitaminWell and Integer CV tailoring notes. AWS/GCP/Azure are never claimed per the Master Experience guardrail (cloud admin not claimable) and are absent from the base CV, so nothing added there either.

## Additional Information
- IT Skills: dropped the "Low code development/" prefix (JD is a backend AI/ML engineering role with no low-code/no-code relation): "Low code development/AI based development, AI (RAG, Chatbot) and API integration, ..." -> "AI (RAG, Chatbot) and API integration, AI based development, Automation (n8n), Project Management, Communication".
- Tools: reordered "Claude Code, Laravel, Typescript, n8n, Supabase, Jira, Slack" -> "Claude Code, Typescript, n8n, Supabase, Laravel, Jira, Slack" (Typescript moved up, Laravel down).

## Professional Experience -- moves and drops

### FlowSpace.co (kept: 4 bullets across both sub-lists, min 3 required)
Product Responsibilities -- kept 2, reordered:
1. Streamlined customer support with AI agents (directly maps to Incident Management AI Agents theme)
2. Scaled platform from 2000 to 4500+ users through iterative product development (production-at-scale theme)
Dropped: "Overseeing the migration of app from Bubble.io to Next.JS and Laravel" (JD has no migration/legacy-stack relation for this early-career AI/ML role); "Collaborated with team of developers for product logic and business logic documentation"; "Facilitated communication between internal team and Agency" (both internal-process bullets, no AI/ML signal).

Technical Responsibilities -- kept 2, reordered:
1. AI tool for processing and scraping of data and increasing listings on platform
2. Integration of external APIs (Office Rnd and Nexudus) for automated bookings
Dropped: duplicate "AI tool for processing of data and increasing listings on platform"; duplicate migration bullet; "Consolidated leads in CRM..."; "GTM automations for sales funnel..."; "Developed a tool for companies to calculate commute times" (all sales/ops-ops themed, not AI/ML infra).

### Urlink (kept 2 of 3)
1. Using AI for building the platform and logics
2. Implementing automations in regards to client requirements
Dropped: "Implementing UIs made with AI" (UI/design task, least relevant to backend AI/ML).

### UltraStrategy.com (kept both of 2, satisfies the AI-role minimum of 2)
1. Made a CV parsing tool using n8n and Eden AI
2. Developed platform for different user profiles
Nothing dropped -- base only had 2 bullets and the AI/automation JD rule requires keeping both.

### Get2Germany.com (kept 2 of 4, satisfies the AI-role minimum of 2)
1. Developed AI based automation tools for finding courses, internships and jobs
2. Integration of Google APIs for effective tracking of the platform
Dropped: "UI/UX work, design from Figma to Bubble"; "Building the platform, database optimization" (neither has AI/API-integration signal).

### Qomodo (kept 1 of 2)
1. Made a dashboard to be used by the companies to manage their branches
Dropped: "Implementation of Figma designs" (design task, no relevance).

### Clubee.com (kept 1 of 3)
1. Integration of Clubee API for all of frontend
Dropped: "Unit testing and quality assurance of new features"; "Developed tools for: domain integration, shop, federation dashboard" (kept the single strongest API-integration bullet to save space for the AI-heavy roles).

### Tractionboard.co (kept 1 of 5)
1. ChatGPT/OpenAI integration
Dropped: "Implementation of designs from Figma to Bubble"; "Responsive designs, de-bugging"; "Google Ads 4 implementation" (none match LLM/AI keywords).

## Result
- Page count: 2 (photo included), compiled clean with tectonic (only harmless FontAwesome ToUnicode CMap warnings).
- Every role, date and location preserved; all kept bullets are verbatim from the original; no new sentences or claims added.
- Parity check (every pdftotext line >25 chars must appear, ligature/dash/quote/bullet/LaTeX-command-normalized, in `Prabhavit_CV_EN.tex`'s text): 51 of 56 long lines matched exactly; the 5 remaining mismatches are all reordered comma-separated skill/tool lists (same tokens, resequenced, plus the allowed "Low code development/" prefix drop) -- same pattern as the Leadbay and Integer CV tailoring precedents. Effective PASS.
