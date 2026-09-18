# AGENT PROMPTS — copy/paste to relaunch the exact sweeps

Launch each as a `general-purpose` subagent (Task tool / Agent tool). All share the same **candidate block** + the same **HARD RULE**. Dedupe every sweep against the ~260 targets already in `LinkedIn Connect Tracker.xlsx` (5 tabs) + `Outreach - people to contact.xlsx`.

## CANDIDATE BLOCK (prepend to any sweep)
Prabhavit Gupta — AI engineer who builds AI agents + ships real code (Python, TypeScript, Laravel, Next.js, LLM/RAG, n8n). Lane: Forward-Deployed / Solutions / Implementation / GTM / Applied-AI engineer. Venice, Italy; remote/EU/Italy; mid-level (~3 yrs). Salary €40–50k. NOT a no-code developer (no-code = origin only). No CS degree, no Polish.

## HARD RULE (append to any sweep)
NO FABRICATION: only record a LinkedIn URL / email / job URL you actually SAW in a search result or on a page. Never construct or guess a URL/email. If none, write "not found". Mark VERIFY if the person/role isn't confirmed. Fewer real entries beat a padded list. Return a markdown table only — data, not a message.

---

## 1. FlowSpace competitors (early-stage + open roles + people)  [UNFINISHED — re-run]
Find 20-30 NET-NEW flex-office / coworking / workspace-booking companies (marketplaces, brokerages, booking platforms, desk/room-booking, coworking-operator groups with tech). PRIORITIZE: (1) early-stage pre-seed/seed/Series A (founder DM lands); (2) EU/Italy; (3) note any OPEN ROLE he'd fit (software/AI/automation/GTM/solutions/FDE/product eng) — check careers pages. Partial names already spotted (verify, get real contacts): Wezoo, Deskimo, HQ.com, Flexspace.ai, Morning (FR — founder Clément Alteresco, also Ubiq), Spacebase, Kactus/Bird Office, WorkInSync, Smarten Spaces. Columns: company | what | stage | website | prime person | LinkedIn/email | OPEN ROLE (title+link or "none") | region. EXCLUDE the ~25 competitors already on his list (Anchor, Tally, Hubble, Kitt, Workthere, Instant, Rubberdesk, Desana, Officeguru, Upflex, Coworker, LiquidSpace, Office Freedom, Flexas, Deskeo, Kontoret, BASE, Adapt, eOffice, shareDnC, CoworkingSpain, Rete Cowo, Cofoundry + all software vendors + proptech already listed).

## 2. EU AI consultancies + vertical fintech/legal AI  [UNFINISHED — re-run]
Two veins: (1) EU applied-AI/ML consultancies & services firms that embed forward-deployed/solutions/delivery engineers (Faculty/Peak/Fractal/Data Reply/Bitrock/Bip xTech type + Italian boutiques); (2) vertical-AI startups (fintech/insurtech/legaltech) EU/Italy, seed–Series B, founder/eng-lead reachable. Columns: company | what | website | prime person | LinkedIn/email | why | region.

## 3. AI-agent / GTM-tool companies (DONE — 32 found, in tab 5)
Buckets: EU AI-agent/applied-AI startups; GTM-engineering/RevOps-automation tools (Clay-style, AI SDR); automation/integration + AI dev-tool cos with FDE/SE motions; Italian AI cos. Skew small/startup where a founder DM lands.

## 4. Italy + EU seed AI cos (DONE — 42 found, in tab 5)
Deep Italian AI/automation/SaaS (VC portfolios: United Ventures, P101, 360 Capital, CDP; incubators: H-FARM, PoliHub, LVenture, Talent Garden) + EU AI-agent seed/pre-seed from recent YC (W24–S25) + AI dev-tool/LLM-infra with FDE/SE motions.

## 5. Vertical-AI (health/support/logistics/proptech) (DONE — 10 found, in tab 5)

## 6. Blindspot: FDE + AI-agent company people (DONE — 27, tab 3)
Recruiters/talent at AI-agent cos (ElevenLabs, Cognition, Sierra, Decagon, Dust, Mistral, Baseten...); FDE/Applied-AI engineer peers; founders of EU/Italian AI-agent startups. EU-first.

## 7. HR / recruiter sweep (DONE — 21, tab 4)
In-house recruiters at AI companies (EU/remote) + EU/Italy tech-recruitment agencies (DeepRec.ai, European Tech Recruit) named consultants + freelance AI recruiters.

## 8. network-scan warm companies (DONE — see network-scan-history.md)
Given his linkedin-contacts.csv, for companies where he knows someone: check careers pages for matching roles + name his contact for a warm intro. (Or run `/proficiently:network-scan`.)

## 9. contact-finder for the 10 job-leads (DONE — JOB-LEADS-LEDGER.md)
For each hiring company, find the best reachable human (hiring mgr/eng lead/recruiter > founder) + real contact.

---
After any sweep: append results to the right tab of `LinkedIn Connect Tracker.xlsx` (openpyxl), tier A/B, hyperlink verified /in/ URLs, flag VERIFY/not-found. Log to `SESSION-LEDGER.md`.
