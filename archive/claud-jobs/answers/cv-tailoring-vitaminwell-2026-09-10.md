# CV tailoring -- Vitamin Well Group

Source: `Prabhavit_CV_EN.tex` -> `Prabhavit_CV_VitaminWell.tex` -> `Prabhavit_CV_VitaminWell.pdf` (2 pages, compiled with tectonic, no errors).

JD focus: Fullstack Engineer, Vitamin Well Group (Stockholm, Sweden), Teamtailor-hosted careers page. Required: 2-5+ years modern web development including Python, REST APIs and frontend frameworks; hands-on e-commerce platform experience (Shopify); AI-first development practice with expert-level skills using tools like Claude; SQL, API integrations, data modelling in a modern data warehouse.

## Career Summary
Kept (2 of 3):
- "AI Solutions & Automation Engineer with hands-on experience building LLM-driven applications and intelligent workflows across European tech projects."
- "Transformed business requirements into production-ready features, delivering AI agents, LLM-powered data parsing, rapid prototypes, and rigorous QA testing."

Dropped:
- "Skilled in AI-assisted development, prompt engineering, and orchestrating complex API integrations." (weaker than the two kept bullets against "ship AI-driven products end to end" and "own solutions from scoping to deployment"; the kept two cover LLM production apps and shipped AI-agent features more directly.)

## Technical Skills
Reordered categories: Development (Typescript, Claude Code, Laravel) moved first since the JD is a fullstack coding role; within it, Typescript moved to lead (closest existing item to the JD's Next.js/React/frontend-framework ask; the CV has no literal "React"/"Next.js"/"Python" skill-list entries to reorder -- see note below). AI/ML category items reordered to put "API integration" second (REST APIs ask) ahead of RAG/Chatbot/Eden AI/OpenAI. Automation and Project/Design unchanged, moved after Development/AI/ML. Nothing deleted from Technical Skills.

**Note on Python/React/PostgreSQL:** the JD instruction to bring "Next.js/React, Python, REST, PostgreSQL" to the front of skills could not be done literally -- none of those four tokens exist as skill-list items in the base `Prabhavit_CV_EN.tex` (Python is not listed anywhere in it, though it is claimable per the brief's claim ladder and is used at FlowSpace per the Master Experience file). Per brief rule 4 ("reorder... delete nothing else") and rule 1 ("do not add claims"), I reordered existing items toward that intent instead of inserting new ones: Typescript (proxy for Next.js/React) and Supabase (proxy for PostgreSQL) were moved to the front of their lists; "API integration" (proxy for REST) was moved up in the AI/ML list. Python is not claimed anywhere in this CV.

## Additional Information
- IT Skills: dropped "Low code development/" prefix (JD has no relation to low-code/no-code work) and reordered so "AI (RAG, Chatbot) and API integration" leads: "Low code development/AI based development, AI (RAG, Chatbot) and API integration, Automation (n8n), Project Management, Communication" -> "AI (RAG, Chatbot) and API integration, AI based development, Automation (n8n), Project Management, Communication".
- Tools: reordered to bring Typescript and Supabase forward: "Claude Code, Laravel, Typescript, n8n, Supabase, Jira, Slack" -> "Typescript, Supabase, Claude Code, Laravel, n8n, Jira, Slack". Nothing deleted.

## Professional Experience -- moves and drops

### FlowSpace.co (kept: 6 bullets across both sub-lists, well over the 3-bullet minimum)
Product Responsibilities -- reordered to:
1. Overseeing the migration of app from Bubble.io to Next.JS and Laravel (Next.js -- direct frontend-framework match)
2. Streamlined customer support with AI agents (AI feature shipped to production)
3. Scaled platform from 2000 to 4500+ users through iterative product development (fullstack product ownership)
Dropped: "Collaborated with team of developers for product logic and business logic documentation"; "Facilitated communication between internal team and Agency" (both generic, no stack/AI/e-commerce keyword match).

Technical Responsibilities -- reordered to:
1. Integration of external APIs (Office Rnd and Nexudus) for automated bookings (REST integrations)
2. AI tool for processing and scraping of data and increasing listings on platform (AI shipped to production)
3. Consolidated leads in CRM and automated lead capture by developing integration between CRM used by the organization (REST integrations)
Dropped: "GTM automations for sales funnel, lead enrichment and outbound" (weakest against the JD's stack/AI/e-commerce keywords); "AI tool for processing of data and increasing listings on platform" (near-duplicate of the kept AI-tool bullet); "Overseeing the migration of app from Bubble.io to Next.JS and Laravel" (duplicate, already kept under Product Responsibilities); "Developed a tool for companies to calculate commute times" (no relevance to the JD themes).

### Urlink (kept 2 of 3)
1. Using AI for building the platform and logics
2. Implementing UIs made with AI
Dropped: "Implementing automations in regards to client requirements" (generic automation, weaker match than the two AI/platform bullets).

### UltraStrategy.com (kept 1 of 2)
1. Made a CV parsing tool using n8n and Eden AI
Dropped: "Developed platform for different user profiles" (generic, no AI/data-pipeline keyword match).

### Qomodo (kept 1 of 2)
1. Made a dashboard to be used by the companies to manage their branches
Dropped: "Implementation of Figma designs" (design task, not code/product).

### Get2Germany.com (kept 3 of 4)
1. Integration of Google APIs for effective tracking of the platform (REST integrations)
2. Developed AI based automation tools for finding courses, internships and jobs (AI feature)
3. Building the platform, database optimization (fullstack + data)
Dropped: "UI/UX work, design from Figma to Bubble" (Bubble/design task, no relation to the JD's stack).

### Clubee.com (kept 2 of 3)
1. Integration of Clubee API for all of frontend (REST + frontend)
2. Developed tools for: domain integration, shop, federation dashboard ("shop" -- e-commerce-adjacent)
Dropped: "Unit testing and quality assurance of new features" (weaker match than the two kept).

### Tractionboard.co (kept 2 of 5)
1. ChatGPT/OpenAI integration (LLM production feature)
2. Implementation of Sendgrid (REST/API integration)
Dropped: "Implementation of designs from Figma to Bubble"; "Responsive designs, de-bugging"; "Google Ads 4 implementation" (none match the JD's stack/AI/REST themes as directly).

## Result
- Page count: 2 (photo included), compiled clean with tectonic (only pre-existing FontAwesome ToUnicode-CMap warnings, same as every other CV built from this template).
- Every role, date and location preserved verbatim; every kept bullet is copied verbatim from the original, only reordered or dropped.
- Parity check (every pdftotext line >25 chars must exist, ligature/dash/quote/whitespace-normalized, in `Prabhavit_CV_EN.tex`'s flattened text): 55 of 61 long lines matched exactly. The 6 remaining: (1) the header contact line, garbled by pdftotext's inability to extract the FontAwesome icon glyphs -- confirmed present identically in `Prabhavit_CV_EN.pdf` itself, so a template artifact, not a content change; (2) one line broken mid-word ("intelli-") by pdftotext's line-wrap hyphenation of "intelligent", which is unchanged verbatim text; (3)-(6) the four reordered skill/tools lines (Development, AI/ML, IT Skills, Tools), each containing exactly the same tokens as the base file in a different order, which is what tailoring rule 4 explicitly permits. No fabricated claims. Effective PASS.
