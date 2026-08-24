# Agent Instructions - Job Search Automation

You are helping Prabhavit Gupta with his job search. This document tells you everything you need to operate. Read it fully before taking any action.

## 1. Start here

Read these files in order:
1. `HANDOFF.md` - full operational state, standing rules, where things stand
2. `README.md` - folder structure, what each file does
3. `LEDGER.md` - chronological session log, newest first (read top entry)
4. `SESSION-LEDGER.md` - per-session detail log

## 2. Who is Prabhavit

- **Name:** Prabhavit Gupta
- **Email (applications):** prabhavitg@gmail.com
- **Phone:** +39 351 610 7807
- **Location:** Venice, Italy (Via Zanetti 10, 30175)
- **Work authorization:** EU Long Term Residence Permit (Italy). No sponsorship needed in EU. UK/US/Swiss = needs sponsorship.
- **LinkedIn:** https://www.linkedin.com/in/prabhavit/
- **GitHub:** https://github.com/prab-gupta
- **Education:** BA Philosophy, International Studies & Economics, Ca' Foscari Venice (2020-2024). NOT a CS degree.
- **Experience:** ~3 years (Aug 2023 - Aug 2026). See CV for details.
- **Languages:** Hindi (native), English (C1 professional), Italian (beginner).
- **Availability:** Immediately. FlowSpace contract ended July 2026.

## 3. Standing rules (NEVER break these)

### Salary
- EUR 45,000-55,000 on all forms. Midpoint: 50,000.
- USD forms: $54,000
- USD monthly forms: $4,500
- B2B/contract: EUR 250-300/day
- Never negotiate UP or DOWN on his behalf. His number, stated plainly.

### CV and cover letters
- Attach a tailored CV to every application.
- CV pipeline: LaTeX template compiled with `tectonic`. Edit ONLY 3 blocks: HEADLINE (line ~40), SUMMARY (lines ~54-56), SKILLS (lines ~59-66). Everything else is frozen.
- Never write "no-code" or "Bubble" on a CV. Say "off a legacy stack".
- No em-dashes anywhere. Use hyphens or commas.
- Never claim: BPMN, deep Python-backend, FastAPI, computer-vision, edge computing, Kubernetes, ML research, non-English language proficiency beyond listed.
- Never leave a cover-letter field blank, even when optional.
- Tailoring rules cheatsheet: `~/.proficiently/cv-tailoring-rules.md` (read before every tailor).

### Forms and applications
- When a form demands 3+ years experience, write 3.
- Anti-AI screening questions = ALWAYS hand back to him. Never answer on his behalf.
- Never create accounts, solve CAPTCHAs, enter payment/ID details, or invent biographical details.
- Answer every question from his CV, his letter, or facts he has stated. Never fabricate.
- Privacy defaults: decline non-essential cookies, leave optional consents unchecked.
- Phone: type full "+39 351 610 7807" to avoid country auto-detect issues.

### Git and attribution
- No Claude/Anthropic/AI attribution in any git output. No Co-Authored-By trailers. No "Generated with Claude Code" anywhere.

### Deduplication
- Check EVERY new lead against the combined list: applications.csv + MASTER xlsx + any "Do not repeat" tabs. The combined set is ~800+ companies as of Aug 2026.
- Never apply to a company already covered.

## 4. Target roles (priority order)

**Track A - AI/Automation (highest priority)**
AI Engineer, AI Automation Engineer, Applied AI Engineer, Automation Consultant, AI Solutions Engineer

**Track B - Forward Deployed / Solutions**
Forward Deployed Engineer, Solutions Engineer, Implementation Consultant, Implementation Engineer, Technical Solutions Engineer

**Track C - Full Stack / Product**
Full Stack Engineer, Product Engineer, AI Product Engineer (TypeScript/Next.js/React preferred)

**Track D - Technical PM**
Technical Project Manager, AI Operations Manager, Digital Transformation PM

### Hard gates (auto-reject)
- Requires MSc or CS degree with no equivalence clause
- Requires 5+ years (his max honest answer is 3)
- Requires a language he doesn't speak (Polish, German fluent, French, etc.)
- Staffing agencies / aggregator reposts with no named end client
- ML research / model training roles (he integrates LLMs, does not train them)
- Unpaid or talent-pool listings

### Geography
- Tier 1 (best): Fully remote from EU, or Italy-based
- Tier 2: Any EU country (on-site/hybrid OK - he's open to relocate)
- Tier 3: Non-EU requiring relocation/sponsorship (apply but flag)

## 5. His technical profile (for matching and writing)

### What he's actually built
- **AI listing pipeline** (Python): web scraping + Claude/OpenAI API extraction + human review + API push. 900+ records.
- **CRM integrations** (TypeScript/PHP): OfficeRnD + Nexudus end-to-end (OAuth2, webhooks, location sync, booking automation).
- **Platform migration**: Bubble.io to Next.js + Laravel. 2,000 to 4,500+ users. Data model mapping, live cutover.
- **Workflow automations** (n8n/Make): lead routing, data sync, support queries, AI agents against live data.
- **SEO Crawler** (Python): Streamlit app, Scrapy/Playwright crawling, Pandas, SQLite, 11-tab analysis tool.
- **Listing sync system** (Python): daily pipeline across 9 operators, rapidfuzz matching, staged approval, DRY_RUN safety.

### Stack
- **Primary:** TypeScript, Next.js, React, Node.js, PHP, Laravel
- **Python:** scripting, automation, AI APIs, web scraping (BeautifulSoup, trafilatura, Streamlit, Pandas, openpyxl)
- **Automation:** n8n, Make (Integromat), Zapier, Tray.ai, Microsoft Power Automate
- **AI:** Claude API, OpenAI API, prompt engineering, structured outputs, function calling, MCP, agent orchestration
- **Data:** PostgreSQL, Supabase, MySQL, SQLite
- **Certs:** Microsoft Copilot Studio Agent Academy, MS AI Agents, Power Automate, Tray.ai Build Practitioner

### What NOT to claim for him
- No Django/Flask/FastAPI
- No async Python (asyncio)
- No ML/model training (PyTorch, JAX, TensorFlow)
- No Kubernetes/Docker in production
- No deep cloud infra (AWS/GCP/Azure admin)
- No BPMN production experience

## 6. Files in this repo

### Core records
| File | Purpose |
|------|---------|
| `applications.csv` | Dedupe source of truth. One row per application. 784 rows as of 21 Aug. |
| `MASTER - every application - 13 Aug 2026.xlsx` | Authoritative tracker. Needs 21 Aug backfill (26 rows). |
| `HANDOFF.md` | Operational state. Read first every session. |
| `LEDGER.md` | Chronological session log. |
| `SESSION-LEDGER.md` | Detailed per-session notes. |
| `README.md` | Folder structure guide. |

### Shortlists and leads
| File | Purpose |
|------|---------|
| `Role shortlist - Sweep 10 - 21 Aug 2026.xlsx` | Latest sweep results. |
| `Role shortlist - 8 Aug 2026.xlsx` | Main leads workbook with multiple sweep tabs. |
| `Board sweep - 19 Aug 2026.xlsx` | Board-specific sweep results. |

### Application materials
| File | Purpose |
|------|---------|
| `Prabhavit_CV.pdf` | Canonical base CV (attach to non-tailored applications). |
| `Prabhavit_CV_Tapnote.pdf/.tex` | Example tailored CV. |
| `answers/` | Reusable answer library per recurring question. |
| `letters/` | Per-role motivation letters (PDF). |
| `drafts/` | Written but unsent material. |
| `confirmations/` | Screenshots of submission confirmations. |

### Automation
| File | Purpose |
|------|---------|
| `apply-bot/apply.mjs` | Playwright form-filler. `node apply.mjs <url>` fills, `--submit` sends. |
| `apply-bot/profile.json` | Answer bank for form automation. |
| `apply-bot/PATTERNS.md` | Per-ATS quirks and traps reference. |
| `validate.py` | Self-consistency check script. |
| `skill/` | Unzipped job-hunt.skill (search playbook, agent briefs, scripts). |

### Strategy and outreach
| File | Purpose |
|------|---------|
| `AGENT-PROMPTS.md` | Agent prompt templates. |
| `COWORK-START.md` | Cloud session startup instructions. |
| `DM-templates.md` | Cold outreach message templates. |
| `LINKEDIN-CONNECT-LIST.md` | LinkedIn networking targets. |
| `OUTREACH-PICKUP.md` | Cold outreach state and relaunch block. |

## 7. Workflow for a new session

1. Read `HANDOFF.md` top to bottom.
2. Read top entry of `LEDGER.md` for latest state.
3. Check `applications.csv` row count and last entry.
4. Ask what's needed: sweep (find new roles), apply (submit to known roles), or both.
5. For sweeps: dedupe against combined list before presenting.
6. For applications: read `apply-bot/PATTERNS.md` for ATS-specific traps.
7. Log every action: update `applications.csv` + `LEDGER.md` after each submit.
8. At session end: update `HANDOFF.md` section 4 with current counts and state.

## 8. Open items (as of 21 Aug 2026)

### CVs ready, forms not yet opened
- Swans Applied AI Specialist - `~/.proficiently/jobs/swans-applied-ai-specialist-2026-08-21/resume-swans-ai.pdf`
- Swans Forward Deployed Engineer - `~/.proficiently/jobs/swans-fde-2026-08-21/resume-swans-fde.pdf`
- Tiens/VMOMENT AI Ops PM - `~/.proficiently/jobs/tiens-ai-ops-pm-2026-08-21/resume-tiens.pdf`

### Blocked (needs human)
- fireup.pro - reCAPTCHA tick only
- GoReel - Cloudflare Turnstile
- Flosum - Cloudflare Turnstile
- Kestra - partially filled, location field outstanding
- Leadtech - email verification gate
- EssilorLuxottica - cheat sheet at `~/.proficiently/jobs/essilorluxottica-ai-intern-2026-08-21/form-cheatsheet.md`
- Paperpile - needs his cover letter + project story
- ElevenLabs - 90-day cooldown until ~3 Nov 2026

### MASTER backfill needed
26 applications from 21 Aug are in `applications.csv` but NOT in the MASTER xlsx. Next session should backfill.

## 9. Loom videos (for roles that ask for a walkthrough)
- Primary: https://www.loom.com/share/d0f6bf69fd3f4db2a429ae6948a098f4
- Continuation: https://www.loom.com/share/d711fd7971ed4385a2ee7e3e948c8e73

## 10. Reference letter
Draft at `~/.proficiently/reference-letter-draft-hayri.md` - for Hayri (FlowSpace CEO) to sign on letterhead.

## 11. Proficiently plugin data (local machine only)
The proficiently job-search plugin stores data at `~/.proficiently/` on his local machine:
- `jobs/` - per-company folders with posting.md, resume.tex/pdf, cover-letter.md, applied.md
- `cv-tailoring-rules.md` - anti-context-rot cheatsheet for CV tailoring
- `preferences.md` - job preferences
- `profile.md` - work history profile
- `job-history.md` - search history log
- `resume/Prabhavit_CV.pdf` - base CV

This data is NOT in the repo. If you need it, ask Prabhavit to share the relevant files.
