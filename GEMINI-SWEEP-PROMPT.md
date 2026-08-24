# Gemini job-sweep prompt (reusable)

How to use: open Gemini, turn on **Deep Research** (or grounding with Google Search). ATTACH `LinkedIn Connect Tracker.xlsx` and `applications.csv` from this folder so it dedupes against what you already have. Paste everything below the line. Paste its two tables back to me (or into the tracker) and I will verify + file them.

---

You are my job-search research analyst. Use Google Search grounding / Deep Research. Today is 19 August 2026. Return only current, verified results.

DEDUPE: I have attached "LinkedIn Connect Tracker.xlsx" (5 tabs) and "applications.csv". Treat every company and person in those files as ALREADY COVERED and do NOT return any of them. Also use the EXCLUDE list at the bottom. Return NET-NEW only.

CANDIDATE (Prabhavit Gupta):
- AI engineer who builds AI agents and ships real code: Python, TypeScript, Laravel, Next.js, LLM/RAG, n8n. He integrates LLMs and builds the harness around them; he does not train/fine-tune models.
- Lane: Forward-Deployed / Solutions / Implementation / GTM / Applied-AI engineer. Do NOT frame him as a "no-code developer".
- Based Venice, Italy. Wants: remote, or anywhere in the EU (on-site/hybrid fine), or Italy. Mid-level, about 3 years. Salary EUR 40-50k employee, or EUR 250-300/day contract.
- Hard blocks: no CS degree and no Master's, so skip roles that REQUIRE either; no Polish, so skip Polish-language-required roles; he needs no visa sponsorship inside the EU (Italian long-term residence permit) but is NOT authorized for UK / US / Switzerland without sponsorship, so flag those.
- Links: github.com/prab-gupta, email prabhavitg@gmail.com.

FIND TWO THINGS, both net-new:

A) TARGET COMPANIES to reach out to, in priority order:
   1. EU applied-AI / ML consultancies and services firms that embed forward-deployed / solutions / delivery / implementation engineers on client projects (the ML6 / dataroots / Xomnia / Faculty / Peak / Fractal type, plus Italian AI boutiques and system integrators with a real AI/automation practice).
   2. Vertical-AI startups (fintech, insurtech, legaltech, health, logistics, proptech), EU or Italy, pre-seed to Series B, where a founder or engineering lead is reachable.
   3. AI-agent / applied-AI product startups and GTM-engineering / RevOps-automation tool companies (EU-first, small enough that a founder DM lands).
   Prioritize: early-stage; EU/Italy; a reachable NAMED human (founder, eng lead, or recruiter) with a real LinkedIn URL.

B) LIVE JOB OPENINGS in his lane: AI / Applied-AI Engineer, Forward-Deployed Engineer, Solutions / Implementation Engineer, GTM Engineer, AI Automation Engineer, Integration Engineer. EU or remote, mid-level. Open each posting to confirm it is live, and give the direct apply URL on the employer ATS (Greenhouse / Lever / Ashby / Workable / Teamtailor / Personio) or LinkedIn.

HARD RULES:
- NO FABRICATION. Only give a company, person, LinkedIn URL, email, or job URL you actually found on a real page or search result. Never invent or guess a URL or email. If you do not have it, write "not found". Write "VERIFY" if you could not confirm the person or role on a page.
- Open-check that every job URL is live and current (postings go stale fast). Prefer employer ATS pages and hiring.cafe over stale aggregator mirrors (Indeed / Glassdoor / ZipRecruiter).
- Exclude everything in my attached files and the EXCLUDE list below. Exclude WeWork / IWG / Regus and mega-corps. Net-new only.
- Skip roles that require a CS/ML degree or Master's, that are 5+ years / senior / staff / principal level, that require Polish, or that need US/UK/CH work authorization (or flag the last clearly as "needs sponsorship").

OUTPUT: two markdown tables, data only, no preamble or commentary.
- Table A (Companies): Company | What they do | Stage | Website | Prime person (name + title) | LinkedIn or email (only if seen) | Open role for him (title + link, or "none") | Region | Why he fits (1 line)
- Table B (Jobs): Company | Role | Location / remote | Direct apply URL (verified live) | Seniority / years | Salary (if shown) | CV-only or essay-required | Fit note
Aim for about 20-30 rows across both tables. Fewer real, verified rows beat a padded list.

EXCLUDE (already covered - non-exhaustive; also dedupe against my attached files):
- Flex-office / coworking: Anchor Offices, Tally Workspace, Hubble, Kitt, Workthere, Instant Group, Rubberdesk, Desana, Officeguru, Upflex, Coworker, LiquidSpace, Office Freedom, Flexas, Deskeo, Kontoret, BASE, Adapt Workspace, eOffice, shareDnC, CoworkingSpain, Rete Cowo, Cofoundry, Nibol, Talent Garden, Copernico, Ubiq, Newton Offices, Workero, SKEPP, Seats2meet, Chainels, Spacebase, Flexopus, Seatti, Aticco, IDEA Spaces, Spaceflow, Flowscape, Runway East, Kadence, Skedda, Gable, Codi, Deskpass, Hotdesk, Letswork, GoFloaters, myHQ, Woolkye, Wezoo, Officely, Worklib, Kactus/Bird Office, Flexspace AI, MatchOffice, Othership, Comet Meetings, OfficeRnD, Nexudus, Cobot, Optix, Spacebring, Archie, Yardi Kube, Essensys, Habu, Zapfloor, Tribeloo, deskbird, Robin, OfficeSpace.com, Envoy, Morning, Deskimo, Smarten Spaces, WorkInSync, Flexday.
- Automation / no-code / dev-tools: Make, Zapier, Retool, Pipedream, Workato, Activepieces, Gumloop, Glide, Tray.ai, Xano, Latenode, Parabola, Windmill, Softr, WeWeb, Bubble, Airtable, ManyChat, Pabbly, Relay.app, Lindy.ai, Bardeen, Albato, SendPulse, Respond.io, n8n.
- Hospitality / PMS: Mews, Cloudbeds, Lodgify, Smoobu, Hostaway, Duve, Operto, RoomRaccoon, Zeevou, Apaleo, Beyond Pricing, PriceLabs, Sweeply, Cohost, Enso Connect, Charge Automation.
- AI brands already applied to or rejected: Cohere, Scale AI, Mistral, ElevenLabs, Dust, Synthesia, Hugging Face, Wayve, Photoroom, PolyAI, Celonis, Contentful, Aircall, Doctolib, Helsing, Multiverse, Parloa, Contentsquare, Corti, Lovable, Poolside, Translated, indigo.ai, Vedrai, Musixmatch, Aindo, Clearbox, Axyon, Cardo AI, Aptus.AI, QuestIT, Userbot, Glickon, Tines, Satispay, Casavo, Bending Spoons, Nebuly, Camunda, Kestra, Vapi, Deepnote, Tavily, Lago, Arize.
- Consultancies / vertical-AI already found: ML6, dataroots, Xomnia, Artefact, Radix, Alexander Thamm, Agile Lab, Datrix, Lexroom, Jus Mundi, Doctrine, Liablix, modefinance, Taktile, Reply, Lutech, Var Group, Engineering Ingegneria Informatica, Eurofins.
- Employers already in my pipeline: Hostaway, ORCA, Peratera, Software Mind, BCD Travel, AI Digital, PRINOTH, Quvia, Nearform, Freedom24, Capital.com, NineTwoThree, Huzzle, Ethos, Jet HR, Leadtech, Kirey, Miaplaza, Veepee, fireup.pro, GoReel, Flosum, Paperpile, N-iX, Intel 471, UNGUESS, DigitalGenius, Albatross AI, J.D. Power, Uncapped, Brave, Blueocean, ecosio, Klarkode.
