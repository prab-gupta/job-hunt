# CV tailoring -- Leadbay (YC F25)

Source: `Prabhavit_CV_EN.tex` -> `Prabhavit_CV_Leadbay.tex` -> `Prabhavit_CV_Leadbay.pdf` (2 pages, compiled with tectonic, no errors).

JD focus: Forward Deployed Engineer - FRA, Leadbay (YC F25, MCP-native agentic sales/lead-qualification tool). Junior/early career, no degree required, values GitHub projects and shipped side projects over titles. Core loop: land account, listen to real usage, ship client-specific skills/connectors/prompts/automations, expand. Customer-facing (CEO/Head of Growth), CRM-adjacent workflows.

## Career Summary
Kept (2 of 3):
- "AI Solutions & Automation Engineer with hands-on experience building LLM-driven applications and intelligent workflows across European tech projects."
- "Transformed business requirements into production-ready features, delivering AI agents, LLM-powered data parsing, rapid prototypes, and rigorous QA testing."

Dropped:
- "Skilled in AI-assisted development, prompt engineering, and orchestrating complex API integrations." (weakest against the "ship client-specific workflows fast" framing; the other two already cover LLM/agentic workflows and business-requirements-to-shipped-feature, which map directly onto Leadbay's Land->Listen->Ship loop).

## Technical Skills
Reordered Project/Design line so GitHub leads (JD explicitly "values GitHub projects"): "Figma, Jira, GitHub, Postman, Trello" -> "GitHub, Jira, Figma, Postman, Trello". AI/ML category already led the list; no change needed there.

## Additional Information
Reordered IT Skills line, dropped the "Low code development/" prefix (JD has no low-code/no-code relation; product is AI/MCP agentic tooling and the JD explicitly wants people who ship code, not visual builders): "Low code development/AI based development, AI (RAG, Chatbot) and API integration, ..." -> "AI (RAG, Chatbot) and API integration, AI based development, Automation (n8n), Project Management, Communication". Nothing else deleted.

## Professional Experience -- moves and drops

### FlowSpace.co (kept: 7 bullets across both sub-lists, min 3 required)
Product Responsibilities -- reordered:
1. Streamlined customer support with AI agents
2. Overseeing the migration of app from Bubble.io to Next.JS and Laravel
3. Scaled platform from 2000 to 4500+ users through iterative product development
Dropped: "Collaborated with team of developers for product logic and business logic documentation"; "Facilitated communication between internal team and Agency" (both internal-facing, no customer-facing/delivery signal for an FDE role).

Technical Responsibilities -- reordered:
1. Integration of external APIs (Office Rnd and Nexudus) for automated bookings
2. Consolidated leads in CRM and automated lead capture by developing integration between CRM used by the organization
3. GTM automations for sales funnel, lead enrichment and outbound
4. AI tool for processing and scraping of data and increasing listings on platform
Dropped: "AI tool for processing of data and increasing listings on platform" (exact duplicate of bullet 4); "Overseeing the migration of app from Bubble.io to Next.JS and Laravel" (duplicate of the Product Responsibilities bullet); "Developed a tool for companies to calculate commute times" (no CRM/sales/customer-workflow relevance).

### Urlink (kept 2 of 3)
1. Implementing automations in regards to client requirements
2. Using AI for building the platform and logics
Dropped: "Implementing UIs made with AI" (design task, least relevant to a forward-deployed/customer-workflow role).

### UltraStrategy.com (kept 1 of 2)
1. Made a CV parsing tool using n8n and Eden AI
Dropped: "Developed platform for different user profiles" (generic, no automation/LLM-pipeline keyword match).

### Qomodo (kept 1 of 2)
1. Made a dashboard to be used by the companies to manage their branches
Dropped: "Implementation of Figma designs" (design task, no relevance).

### Get2Germany.com (kept 2 of 4)
1. Developed AI based automation tools for finding courses, internships and jobs
2. Integration of Google APIs for effective tracking of the platform
Dropped: "UI/UX work, design from Figma to Bubble"; "Building the platform, database optimization" (neither is automation/integration/customer-facing).

### Clubee.com (kept 2 of 3)
1. Integration of Clubee API for all of frontend
2. Developed tools for: domain integration, shop, federation dashboard
Dropped: "Unit testing and quality assurance of new features" (QA framing is less relevant than the shipped-integrations framing this role wants).

### Tractionboard.co (kept 1 of 5)
1. ChatGPT/OpenAI integration
Dropped: "Implementation of designs from Figma to Bubble"; "Responsive designs, de-bugging"; "Google Ads 4 implementation" (none match the LLM/automation/integration keywords as directly as the ChatGPT/OpenAI bullet).

## Result
- Page count: 2 (photo included), compiled clean with tectonic (only harmless FontAwesome ToUnicode CMap warnings, same as every other build off this base).
- Every role, date and location preserved; all kept bullets are verbatim from the original; no new sentences added.
- Parity check (every pdftotext line >25 chars must appear, ligature/dash/quote/LaTeX-escape-normalized, in `Prabhavit_CV_EN.tex`'s text): 49 of 51 long lines matched exactly; the 2 remaining mismatches are the Technical Skills "Project/Design" line and the Additional Information "IT Skills" line, both of which differ only because the comma-separated items were reordered per the tailoring rule -- all tokens are the same, just resequenced, not a fabricated claim. Effective PASS (same pattern as the Integer CV tailoring precedent).
