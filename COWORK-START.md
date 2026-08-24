# COWORK — START HERE (job search handoff)

Everything for Prabhavit's job search lives in THIS folder (`~/Downloads/claud jobs/`). Read this top to bottom, then continue.

## Who / positioning (use this framing everywhere)
Prabhavit Gupta — **AI engineer who builds AI agents and ships real code** (Python, TypeScript, Laravel, Next.js, LLM/RAG, n8n). Strongest lane = **Forward-Deployed / Solutions / Implementation / GTM / Applied-AI engineer**. Venice, Italy; wants **remote / EU / Italy**; mid-level (~3 yrs). Salary €40–50k (contract €250–300/day).
- **Do NOT frame him as a "no-code developer."** No-code (Bubble) is origin only — it's scrubbed from all materials on purpose. Lead with agents + coding + the FlowSpace migration.
- Email on applications: prabhavitg@gmail.com. LinkedIn: linkedin.com/in/prabhavit. GitHub: github.com/prab-gupta (profile + llm-doc-parser demo live). No CS degree, no MSc (hard-blocks those). No Polish.

## Enable the proficiently job-search plugin (the "close to it" config)
The plugin's data is bundled here at `./.proficiently/` (resume, preferences, profile, linkedin-contacts.csv, job-history, jobs/). The plugin reads `.proficiently` from the CURRENT WORKING DIR first, so:
1. Run Claude Code from inside `~/Downloads/claud jobs/` (or the coworker's copy of it).
2. Install the plugin: `claude plugin marketplace add proficientlyjobs/proficiently-claude-skills` then `claude plugin install proficiently@proficiently`. (`.claude/settings.json` here already declares the marketplace + enables the plugin, so a session started in this folder auto-loads it.)
3. If plugin clone fails on SSH: `git config --global url."https://github.com/".insteadOf "git@github.com:"`.
4. Now `/proficiently:job-search`, `:network-scan`, `:tailor-resume`, `:cover-letter`, `:apply` work against `./.proficiently`.
Note: can't perfectly replicate the original ~/.proficiently location, but cwd-resolution makes it work anywhere the folder goes.

## The files (what's what)
- **`LinkedIn Connect Tracker.xlsx`** — MASTER outreach workbook, 5 tabs: (1) Connect Tracker (73 cold company contacts) (2) Warm Network (57 people he already knows — 15 recruiters) (3) Blindspot Targets (27 FDE/agent people) (4) Recruiters (21 EU/AI recruiters + DeepRec agency) (5) Outreach - AI Agent Cos (84 AI/agent/GTM/vertical companies + named contacts). ~260 targets total.
- **`Job Leads (API).xlsx`** — 13 jobs from free job APIs (Remotive/Jobicy/Arbeitnow).
- **`~/Downloads/claud jobs/.proficiently/jobs/`** — saved postings for VERIFIED-LIVE openings (below).
- **`FUNNEL-STATS-aug.md`** — the diagnosis of why Aug had ~0 offers (targeting + channel, not ability).
- **`OUTREACH-TRACKER.md`** / **`OUTREACH-PICKUP.md`** — cold-outreach worklist + follow-up dates.
- **`JOB-LEADS-LEDGER.md`**, **`SESSION-LEDGER.md`** — running logs.
- **CVs:** `Prabhavit_CV_v2.tex/.md` (master), `Prabhavit_CV_ORCA.tex`, `Prabhavit_CV_TastyDose.tex`. Original untouched: `Prabhavit_CV.pdf`. (Bubble scrubbed from all; company names hyperlinked.)
- **`.claude/settings.json`** — commit this so any teammate cloning the folder auto-gets the plugin.

## VERIFIED-LIVE job openings to apply to (all opened + confirmed)
1. **Hostaway — Lead AI GTM Engineer** (remote EU) — TOP fit. hiringcafe.com/job/lead-ai-gtm-engineer-100-remote-europe-hostaway-europe-4cxm0yy0a470mw2m (NOTE: Hostaway auto-rejected a different role Aug 13 — separate team; contact Darcy Kurtz, GTM leader.)
2. **Nebuly — AI Engineer** (Turin, Italy, €50-60k, 1-3yr) — best local. hiringcafe.com/job/ai-engineer-nebuly-turin-piedmont-1wyd5q7y5puqw7jz
3. **DigitalGenius — Implementation Engineer** (Croatia/EU, 2+yr, AI agents).
4. **Klarkode — No-Code Developer (Make.com)** — warm (knows both co-founders); NOTE: lower-priority given the no-code steer, but a real verified opening.
5. **Albatross AI** (Zug) — actively hiring Forward-Deployed Engineers.
6. **J.D. Power — AI Engineer** (remote EU) · **Cohere — Applied AI Eng (agents)** · **ORCA — AI Automation Eng** · **ElevenLabs — FDE Italy** · **Uncapped — GTM Engineer** · **Brave — Sr Solutions Engineer** · **Blueocean — FDE (Berlin)** · **ecosio — Integration Engineer (EU)**.

## OPEN THREADS (do next)
1. **Warm outreach (highest ROI):** DM the 15 recruiters he already knows (Warm Network tab) + top AI-agent founders. Warm-hook standout: **Eden AI** (he built the CV parser on Eden AI). Italian/regional: **Aindo (Trieste), Equixly (Verona), indigo.ai (Milan)**.
2. **Send the drafted messages** (not yet sent): Ethos + Jet HR follow-ups; DM Beatrice Piazza (Arsenalia); the recruiter connect-note template.
3. **Apply** to the verified-live list above, tailored to the **GTM/Solutions-Engineer** framing.
4. **Finish the interrupted sweeps** (died on the session limit — re-run after limit resets):
   - Early-stage FlowSpace competitors + open roles. PARTIAL names found, UNVERIFIED (get real contacts before use): Wezoo, Deskimo, HQ.com, Flexspace.ai, Morning (FR, founder Clément Alteresco / also Ubiq), Spacebase, Kactus/Bird Office, WorkInSync, Smarten Spaces.
   - EU AI consultancies (Faculty/Peak/Fractal/Data Reply/Bitrock/Bip xTech type) + fintech/legaltech-AI startups.
5. **Build (still owed):** GTM/Solutions master CV; 3 reusable DM templates (founder cold / recruiter / warm-hook); Loom demo of the listing bot.

## Hard rules
- NO fabrication of names/emails/URLs — "not found" over a guess. Verify any agent-found job URL by opening it before trusting (an agent hallucinated a fake Qonto listing once).
- LinkedIn connects: do them manually (2 clicks), ~15-20/day max — automating them risks account restriction and mis-targets.
- Gmail: application replies go to prabhavitg@gmail.com (filters set up under Jobs / Jobs/Action / Jobs/Opportunity labels). Check **Jobs/Action** + **Jobs/Opportunity** daily.

## BROWSER PLAYBOOK (for the browser-driven work)
Log into these in the controlled browser first: **Gmail = prabhavitg@gmail.com** (his applications inbox, NOT flowspace.co), **LinkedIn** (his account), **hiring.cafe**. Try Claude-in-Chrome first (`list_connected_browsers`); if none connected (it was dead this whole session — OAuth mismatch), use **Playwright MCP** and say so.

**hiring.cafe (job sweeps):**
- Navigate a searchState URL: `https://hiringcafe.com/?searchState={"jobTitleQuery":"(\"forward deployed\" OR \"solutions engineer\" OR \"gtm engineer\" OR \"ai engineer\" OR \"implementation engineer\") AND NOT intern","workplaceTypes":["Remote"]}` (URL-encode it). Vary titles/omit workplaceTypes for Italy on-site/hybrid.
- Extract with `browser_evaluate` DOM scraping of listing cards — NEVER get_page_text (blows context). API is auth-gated (401/405), don't use it.
- VERIFY every promising job by opening its detail URL (an agent hallucinated a fake Qonto listing; always open-check before saving/showing).
- Save postings to ./.proficiently/jobs/<slug>/posting.md; log to SESSION-LEDGER.md.

**Gmail:**
- Search via `https://mail.google.com/mail/u/0/#search/<query>`. Funnel check: `(interview OR "next steps" OR assessment OR screening) after:2026/07/25` (incl Spam/Promotions). Scrape rows via evaluate on `tr.zA`.
- Filters already set: label **Jobs** (all ATS mail), **Jobs/Action** (interviews/tasks, starred), **Jobs/Opportunity** (inbound/leads, starred), **Jobs/Rejected** + **Jobs/LowPriority** (archived). Check Jobs/Action + Jobs/Opportunity daily.
- To track replies, ask him to connect prabhavitg@gmail.com as a Gmail integration (the connected one is his flowspace.co WORK inbox — different account).

**LinkedIn:**
- Connect requests: do them MANUALLY (open profile → Connect → Send without a note), ~15-20/day MAX. Automating them mis-targets (grabs sidebar suggestions) and risks account restriction — don't script bulk connects.
- Scrape his connections: connections page, scroll to load, `evaluate` over `a[href*="/in/"]` cards → name/headline/url. (Already done → ./.proficiently/linkedin-contacts.csv, 533.)
- Profile edits: intro/headline via `/in/prabhavit/edit/intro/`; About via `/in/prabhavit/edit/forms/summary/new/`. Headline + About + Skills already rewritten to the agents/coding/FDE framing (see COWORK-START positioning). Set Open-to-Work titles = AI Automation/Solutions/FDE, Remote+EU+Italy.

**Application forms (e.g. Google Forms):**
- Fill fields via native value setter + dispatch input/change events (React). ALWAYS STOP before final submit — hand back to him to review + submit. Never solve CAPTCHAs, never submit anti-AI-screening questions.

**GitHub:** edit via web editor — paste content into CodeMirror (`.cm-content`) with a synthetic ClipboardEvent, then Commit changes (x2 clicks). Profile README + llm-doc-parser already live, Bubble-free.
