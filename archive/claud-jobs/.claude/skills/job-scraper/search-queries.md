# Search Queries for Job Scraper

## Installed portal CLIs (primary for `/scrape`)

## Search Sites

Primary (your market's job boards - scaffold one with `/add-portal`):
- **linkedin.com/jobs**
- **justjoin.it**
- **himalayas.app**

## Source of Truth

Load these before every sweep, in this order:

1. `.proficiently/preferences.md`
2. `AGENT-INSTRUCTIONS.md`, especially Target roles and Hard gates
3. `applications.csv`, the application dedupe source

## Query Categories

Run the first three categories by default. Run each title as a separate CLI query for precision.

### Priority 1: Forward Deployed and AI Solutions

- Forward Deployed Engineer
- Forward-Deployed AI Engineer
- AI Solutions Engineer
- Technical Solutions Engineer AI
- Implementation Engineer AI
- Solutions Engineer AI

Fallback web query:
`site:linkedin.com/jobs ("Forward Deployed Engineer" OR "Forward-Deployed AI Engineer" OR "AI Solutions Engineer" OR "Implementation Engineer") (Italy OR Europe OR Remote)`

### Priority 2: Applied AI and Agentic Products

- Applied AI Engineer
- AI Engineer agents
- AI Engineer LLM
- AI Product Engineer agents
- Agentic AI Engineer

Only keep AI Engineer results centered on agents, LLM applications, Generative AI integration, or production AI products. Exclude model-training and ML-research roles.

Fallback web query:
`site:linkedin.com/jobs ("Applied AI Engineer" OR "Agentic AI Engineer" OR "AI Product Engineer" OR "AI Engineer") (agents OR LLM OR "Generative AI") (Italy OR Europe OR Remote)`

### Priority 3: AI Automation

- AI Automation Engineer
- Automation Consultant AI
- Automation Engineer n8n
- Automation Engineer Make
- AI Implementation Engineer

Fallback web query:
`site:linkedin.com/jobs ("AI Automation Engineer" OR "Automation Consultant" OR "AI Implementation Engineer") (n8n OR Make OR agents OR LLM) (Italy OR Europe OR Remote)`

### Priority 4: Adjacent Technical Go-to-Market

Run only for a broad sweep:

- Sales Engineer AI
- Developer Advocate AI
- Developer Relations automation
- GTM Engineer AI

## Role Exclusions

- Do not target generic frontend, backend, full-stack, QA, SDET, data science, ML research, or technical PM roles.
- A generic engineering role survives only when the posting is explicitly shaped around FDE, AI agents, LLM applications, AI solutions, or AI automation.
- Do not target No-Code Developer as a primary lane.

## Hard Gates

- Requires an MSc or a CS or technical degree with no equivalence clause
- Requires 5 or more years of experience
- Requires a language beyond English or beginner Italian
- Unnamed staffing agency or aggregator repost
- Requires ML research, model training, or fine-tuning as core work
- Unpaid role or talent-pool listing

## Location Filter

- Best: fully remote from Italy or Europe, or Italy-based
- Allowed: on-site or hybrid in an EU country, candidate is open to relocate
- Outside the EU: remote-friendly only

## Language Filter

- English: professional
- Italian: beginner
- Exclude roles requiring fluent or native Italian or another undeclared language

## Date Filter

Only include jobs posted within the last 14 days. Apply the client-side date filter when a portal lacks a recency flag.
