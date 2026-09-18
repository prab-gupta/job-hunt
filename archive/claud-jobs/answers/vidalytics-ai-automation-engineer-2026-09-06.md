# Vidalytics - AI Automation Engineer (ClickUp form) - answers written 2026-09-06
Form: https://forms.clickup.com/2375967/f/28g8z-68551/T6DCVAL6967ICXGO2M | CV: vidalytics-ai-automation-2026-09-05/Prabhavit_CV_Vidalytics.pdf | Comp: 60000 USD | Location: Venice, Italy

## Why new role / why this position
My FlowSpace contract wrapped up in August 2026 after two and a half years, and I want to spend the next stretch building AI automation full time inside one product team instead of across freelance clients. Vidalytics caught my attention because the role is exactly the shape of what I built at FlowSpace: n8n plus LLM pipelines plus GTM and ops automations that real people depend on daily, with Claude Code as the main build tool. A video marketing platform has a lot of repetitive, data-heavy workflows (onboarding, analytics reporting, support, lead routing) that are a strong fit for the agentic systems I have shipped.

## How I use AI now / how to leverage it more
Claude Code is my primary development tool: I use it for architecture, prototyping, refactors, tests and code review every day, with MCP servers for Supabase, the browser and internal APIs. In production I run LLM APIs inside pipelines: structured extraction from documents, classification and routing, and support agents that answer against live data with confidence scoring. What I would push further: a proper eval harness with regression sets for every prompt change, agentic QA that exercises the product end to end, and more internal MCP tooling so ops and GTM teams can trigger automations directly from where they work.

## Most impressive automation
The FlowSpace listing pipeline. Analysis: the ops team spent 30+ minutes per workspace listing, copying data by hand from brochures that arrived as PDFs, web pages, photos or spreadsheets, and could not get past a few listings a day. I mapped the fields that mattered, the formats that showed up most, and where errors came from. Solution: a pipeline that ingests any format, runs multi-step LLM extraction with structured outputs and validation, drafts the full listing with photos and descriptions, routes it to a human review UI, and pushes the approved result to the backend API. I built it with the ops lead and the CEO as the reviewers, iterating on the review flow weekly based on what they corrected. Impact: listing drafting went from 30+ minutes to under 5 minutes including review, 900+ records processed, and the platform grew from 2,000 to 4,500+ users while the ops team stayed the same size.

## How do you know an AI system works once live
Instrument the boundary between the model and the world. For the listing pipeline: reviewer acceptance rate, how much reviewers edit each draft, field-level error counts against the source document, and a weekly sample audit. For support agents: escalation rate, confidence-score distribution, thumbs feedback, and reading real transcripts rather than synthetic tests. Underneath that: logging every model call with inputs, outputs, cost and latency, retries and dead-letter handling for partial API failures, and alerts when acceptance drops or cost spikes. A prompt change ships only after it beats the current version on the saved regression set.

## Full-stack rating and stack
Overall 7/10. TypeScript 8, Next.js and React 8, Node.js 7, Laravel and PHP 7, Python 7 (AI pipelines, scraping, data tooling), SQL with PostgreSQL and Supabase 7, n8n 9, Tailwind 7, Playwright 7, REST and webhook integrations 8, Docker 5 (working knowledge), FastAPI 4 (working knowledge).

## Tools worked with / expert level
Expert: n8n, Make, Claude Code, MCP (I build and use MCP servers daily). Proficient: Zapier, Vercel (production deployments), Supabase with pgvector for RAG, Claude Cowork for long-running research and sweeps, bolt.new and v0 and Lovable for prototyping. Basic: LangChain. Not used in production: BigQuery and GCP (my stack is Supabase and Postgres), HubSpot and Intercom (my CRM work was Attio and Amplemarket), PostHog (I have used Microsoft Clarity and GA4 instead).

## Interviewing elsewhere
Yes, I have active applications for AI automation and forward-deployed roles in Europe. A few are in early screening, none at offer stage. I can decide within two weeks of an offer and can start immediately.

## Frontier models and how I choose; Claude Code and Cowork day to day
Claude (Sonnet and Opus) for agentic coding, long-context document extraction and anything where structured-output reliability matters most. Smaller and cheaper models (Haiku tier, GPT-4o-mini class) for high-volume classification, routing and first-pass extraction where cost per document dominates. I pick by the task: reliability of structured outputs, context length needed, cost per call at volume, latency for anything user-facing like support agents. Day to day Claude Code runs my plan, implement, review loop, with subagents for parallel research and MCP servers for the database and browser. Cowork handles long-running research and batch work so the terminal stays free for building.

## Hours (US Eastern)
Monday to Friday, 8:00am to 4:00pm US Eastern (14:00 to 22:00 CET), consistently.

## Portfolio
https://github.com/prab-gupta/llm-doc-parser
