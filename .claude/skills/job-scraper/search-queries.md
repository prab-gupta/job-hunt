# Search Queries for Job Scraper

## Installed portal CLIs (primary for `/scrape`)

## Search Sites

Primary (your market's job boards - scaffold one with `/add-portal`):
- **linkedin.com/jobs**
- **justjoin.it**
- **himalayas.app**

Tier-1 additions (full URL templates in `skill/job-hunt/references/sources.md` §4b; use as WebSearch/WebFetch fallbacks):
- **jobs-radar.com** (`/en/search?q=<query>&location=Europe&range=month`)
- **hiring.cafe** (needs the browser agent)
- **jobdex.io** (`/remote-from/Italy`, `/stack/n8n`, `/stack/LLM`)
- **deployaijobs.com** (`/jobs?location=Europe&remote=remote&seniority=junior`)
- **deployedjobs.com** (`/?location=Italy`)
- **community.n8n.io Jobs** (`/c/jobs/13.json?order=created`, keep `[HIRING]` titles)

## Query Categories

### Priority 1: Full-Stack & AI Engineer
site:linkedin.com/jobs "AI Engineer" OR "Full-Stack Engineer" OR "Next.js" Italy OR Remote
site:justjoin.it "AI Engineer" OR "TypeScript" Remote
site:himalayas.app "AI" OR "Next.js" Remote

### Priority 2: Applied AI & Solutions Engineering
site:linkedin.com/jobs "Solutions Engineer" OR "Implementation Engineer" Italy OR Remote
site:justjoin.it "Solutions Engineer" Remote

### Priority 3: Technical PM & Product Engineering
site:linkedin.com/jobs "Product Engineer" OR "Technical PM" Italy OR Remote

## Location Filter
- Italy (Remote)
- Europe (Remote - B2B/Contractor)

## Language Filter
- English (C2/Fluent)
- Italian (Beginner - exclude jobs requiring fluent Italian)

## Date Filter
Only include jobs posted within the last 14 days.
