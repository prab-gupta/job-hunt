# Agent Instructions - Job Search Automation

You are helping Prabhavit Gupta with his job search. This document tells you everything you need to operate. Read it fully before taking any action.

## Tracker router

`applications.csv` is the only application tracker. `data/csvs/applications.csv` and `loop/applications.csv` are byte copies of that file, not separate lists. Do not start another tracker, CSV, or spreadsheet. `docs/needs-you.md` is a view of `status=needs_you`, regenerated from the CSV.

When the `tracker` MCP server in `mcp/tracker-server` is connected, agents use its tools (`stats`, `search_rows`, `next_needs_you`, `add_row`, `update_row`, `release_claim`, `regenerate_needs_you`, `sync_paths`) and do not edit the CSV themselves. If that server is not connected, fall back to reading `applications.csv` directly. Only `tracker-keeper` writes the three CSV paths, regenerates `docs/needs-you.md`, and commits. The server does not commit. Passwords are never a tool argument.

| Skill | Use when |
| --- | --- |
| `tracker-keeper` | Dedupe, map status, copy the three CSV paths, regenerate the needs-you view, commit |
| `sweeper` | Find new matching roles and add them. Does not apply |
| `needs-you-drainer` | Work `docs/needs-you.md` from the top, end to end. On a login or account-required ATS, create the account with the one shared `JOBS_ACCOUNT_PASSWORD`, verify via Gmail, and continue. A captcha stays `needs_you`. |
| `apply-auditor` | After an ATS accept, check Gmail. This skill is the only one that sets `submitted`, and only when a role-specific application confirmation is in Gmail. It also runs the separate `no_confirm` retrieval route (see "Status contract"). |
| `coordinator` | Route those four. One writer at a time. |

Status is only `needs_you`, `submitted`, `skipped`, or `failed`. Never reapply a `submitted` or `skipped` row. Never add a second row for the same dedupe key: normalized URL (lowercase, drop the fragment and a trailing slash, drop tracking/language query params such as `utm_*`, `ref`, `source`, `lang`, `language`, but KEEP job-identifying params such as `gh_jid`, `jid`, `id`, `job`, `requisition`, `jk`). Also compare company + role + location before applying, because the same role can sit on two hosts, or company + role when there is no URL (case-insensitive, whitespace collapsed).

Portal accounts reuse the one password in `JOBS_ACCOUNT_PASSWORD` (or gitignored `.secrets/job-accounts.env`, which only sets that variable). Do not generate a password per portal. Never write that password, or any other credential, into a tracked file, the CSV, `notes`, `blocker`, `docs/needs-you.md`, a commit, or a PR. An account is logged as one line in the row's `notes`. There is no accounts CSV.

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
- **Work authorization:** EU Long Term Residence Permit (Italy). No sponsorship or work permit needed anywhere in the EU (confirmed by Prabhavit 2026-10-02). UK/US/Swiss = needs sponsorship. UK and Ireland roles stay excluded from the search. The Salesforce "Yes" is the recorded answer to that specific question and stays as recorded.
- **LinkedIn:** https://www.linkedin.com/in/prabhavit/
- **GitHub:** https://github.com/prab-gupta
- **Education:** BA Philosophy, International Studies & Economics, Ca' Foscari Venice (2020-2024). NOT a CS degree.
- **Experience:** ~3 years (Aug 2023 - Aug 2026). See CV for details.
- **Languages:** Hindi (native), English (C1 professional), Italian (beginner). No German (confirmed 2026-10-02): skip roles that require it.
- **Availability:** Immediately. FlowSpace contract ended August 2026 (confirmed by Prabhavit 2026-10-02).

## 3. Standing rules (NEVER break these)

### Salary
- EUR 50,000-60,000 gross/year on all forms (confirmed by Prabhavit, Oct 2026). Single-number fields: 50,000 (the low end of his range; no other figure or midpoint). This supersedes the old EUR 30-40k / 30000 and EUR 200/day figures in `answers/salary-expectation.md` and `skill/job-hunt/references/application-rules.md`. A role-search target is not a form answer; do not infer or convert a new figure.
- USD forms: $54,000
- USD monthly forms: $4,500
- B2B/contract: EUR 250-300/day
- Never negotiate UP or DOWN on his behalf. His number, stated plainly.

### CV and cover letters
- Attach a tailored CV to every application.
- CV pipeline: LaTeX template compiled with `tectonic`. Start from the corrected baseline `data/cvs/Prabhavit_CV_EN_baseline.tex` (Italian = Beginner, FlowSpace Mar 2024 - Aug 2026). Do NOT start from `data/cvs/Prabhavit_CV_EN.tex.bak-0916`, from older generated CVs in `cv/`, or from anything in `cv/_quarantine/`. Edit ONLY 3 blocks: HEADLINE (line ~40), SUMMARY (lines ~54-56), SKILLS (lines ~59-66). Everything else is frozen. Generated CVs and past submissions are not a source of facts; this file is.
- Never write "no-code" or "Bubble" on a CV. Say "off a legacy stack".
- No em-dashes anywhere. Use hyphens or commas.
- Never claim: BPMN, deep Python-backend, FastAPI, computer-vision, edge computing, Kubernetes, ML research, non-English language proficiency beyond listed.
- Never leave a cover-letter field blank, even when optional.
- Datapizza exception: for Datapizza only, do not generate or upload a CV or a cover letter. Use the existing approved Datapizza profile, and verify that profile's facts against this file before submitting.
- Compilers: the CV template compiles with `tectonic`. The cover-letter class (fontspec, `cover_letters/cover.cls`) compiles with XeLaTeX. Do not use a blanket `pdflatex`. Before upload verify: CV exactly 2 pages (`pdfinfo`), cover letter exactly 1 page, rendered layout checked, extracted text readable.
- Tailoring rules cheatsheet: `~/.proficiently/cv-tailoring-rules.md` (read before every tailor).

### Forms and applications
- When a form demands 3+ years experience, write 3.
- Anti-AI screening questions = ALWAYS hand back to him. Never answer on his behalf.
- Never solve CAPTCHAs, enter payment or ID details, or invent biographical details.
- `needs-you-drainer` may create or sign into an ATS account (Workday and similar) when the blocker is login or account required. Reuse the one password in `JOBS_ACCOUNT_PASSWORD` for every portal. Do not generate a per-account password. Never write that password, or any other credential, into a tracked file, the CSV, notes, a commit, or a PR.
- Answer every question from his CV, his letter, or facts he has stated. Never fabricate.
- Privacy defaults: decline non-essential cookies, leave optional consents unchecked.
- Phone: type full "+39 351 610 7807" to avoid country auto-detect issues.

### Browser policy
- Browser work is strictly sequential: one browser agent at a time, reusing one existing tab.
- Attach only to the Chrome already running at `127.0.0.1:9222` (Chrome DevTools MCP). Never launch a new Chrome process, window, or headless session.
- Parallel work is allowed only for research and drafting (JD reading, LaTeX drafts), never for browser steps.
- If the port is not reachable, stop and park the row (`needs_you`, blocker `other`, exact condition in notes).

### Status contract (single source)
- Allowed statuses: `needs_you`, `submitted`, `skipped`, `failed`. There is no `confirmed` status.
- ATS acceptance (application id, explicit acceptance text, or a successful create call) => keep `needs_you` with blocker `no_confirm`, and write the acceptance evidence in `notes`.
- Only `apply-auditor` writes `submitted`, and only with a real, role-specific Gmail confirmation: `notes` carry `gmail: <subject> @ <time>` and `date_applied` is set from the message. A thanks page, a redirect, or an agent saying "submitted" is not a confirmation. Account-verification mail is not an application confirmation.
- `needs_you` blockers are only `login`, `upload`, `eligibility`, `no_confirm`, `other`, `captcha`. The exact missing fact, account condition, or acceptance evidence goes in `notes`. Never write `awaiting_confirm`, `account_password_unset`, `missing_fact`, `missing_document` or free text as a blocker.
- Parked human questions (required answer not in this file, anti-AI/own-words questions, missing documents, identity/payment steps, unavailable secure login or browser): keep `needs_you`, start the note with `parked <date>: <exact question or fact>`. These rows are not drainer work and `next_needs_you` skips them.
- Failure: if the ATS explicitly rejects the attempt use `failed` with the real error. Skip closed or out-of-scope roles with a factual reason.
- Auditor pass (separate route): `next_needs_you` never returns `no_confirm` rows. After each application batch, `search_rows` with `status=needs_you` and `blocker=no_confirm`, read the acceptance evidence, search Gmail for the role/requisition confirmation within the time window since acceptance, and run `apply-auditor`. If no confirmation exists the row stays `needs_you` / `no_confirm`. Never resubmit a role just because its email is missing.
- Locking: with the tracker MCP connected, the server owns its per-operation lock (`loop/.applications.lock`); do not create or delete it. The manual lock is for the direct-CSV fallback only.

### Source authority
- This file is the authority for candidate facts, salary, availability and policy. `answers/`, `data/markdowns/`, `skill/job-hunt/` and older skills contain historical text; where they disagree with this file, this file wins. Historical employer-specific answers stay as records of what was sent.

### Git and attribution
- No Claude/Anthropic/AI attribution in any git output. No Co-Authored-By trailers. No "Generated with Claude Code" anywhere.

### Deduplication
- Check every new lead against `applications.csv` only. The dedupe key is a normalized URL (lowercase, drop the fragment and a trailing slash, drop tracking/language query params such as `utm_*`, `ref`, `source`, `lang`, `language`, but KEEP job-identifying params such as `gh_jid`, `jid`, `id`, `job`, `requisition`, `jk`). Also compare company + role + location before applying, because the same role can sit on two hosts. If the row has no URL, use company + role, case-insensitive, with whitespace collapsed.
- Never add a second row for an existing key. Never reapply a `submitted` or `skipped` row.
- The Aug 2026 MASTER workbook is an archive. It is not a second tracker.

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
| `applications.csv` | The only application tracker. `data/csvs/applications.csv` and `loop/applications.csv` must match it byte for byte. |
| `docs/needs-you.md` | View of `status=needs_you`. Regenerated from the CSV. Not a second database. |
| `MASTER - every application - 13 Aug 2026.xlsx` | Archive only. Do not append rows here. |
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
5. For sweeps: dedupe against `applications.csv` before presenting. Do not add a second row for an existing key.
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

### Auto-Invoke Claude Skills
When the user makes a request, ALWAYS evaluate if it matches one of the workflows in `.claude/skills/` (including `tracker-keeper`, `sweeper`, `needs-you-drainer`, `apply-auditor`, `coordinator`, the proficiently skills `apply`, `cover-letter`, `job-search`, `jobsearch-telegram`, `network-scan`, `setup`, `tailor-resume`, as well as `company-researcher`, `interview-analyzer`, `developer-growth`, `workspace-organizer`, and `job-application-assistant`). If relevant, silently use your file reading tool to read the corresponding `SKILL.md` and follow its instructions immediately. Do not ask for permission to use the skill. The application list those skills share is `applications.csv` only.
