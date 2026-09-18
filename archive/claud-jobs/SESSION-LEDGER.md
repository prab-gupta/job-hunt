# SESSION LEDGER - 19 Aug 2026 (Cowork cloud continuation)

Ran from the Cowork cloud session (device bridge + Claude-in-Chrome), not local Claude Code. NOTE: `claude plugin install proficiently` and the `/proficiently:*` commands are local-Claude-Code actions and cannot run from the cloud session; the underlying work was done manually instead.

Done:
- Re-read COWORK-START.md + AGENT-PROMPTS.md. Device bridge online; one browser connected (Browser 1, macOS).
- Relaunched the 2 unfinished sweeps as general-purpose subagents (candidate block + hard rule + dedupe).
  - Sweep 1 (FlowSpace competitors) -> "LinkedIn Connect Tracker" tab, +9 net-new EU-priority: Woolkye (IT), Wezoo (NL), Officely (UK), Worklib (FR), Kactus/Bird Office (FR), Flexspace AI (US-remote), MatchOffice (DK), Othership (UK VERIFY), Comet Meetings (FR, acquired). Dups caught: Zapfloor, Tribeloo, deskbird, Spacebring, Cobot, Nexudus, OfficeRnD, Optix, Archie, Habu, Deskimo, Morning.
  - Sweep 2 (EU AI consultancies + fintech/legal AI) -> "Outreach - AI Agent Cos" tab, +10, several with VERIFIED his-lane openings: dataroots (AI Solution Engineer, BE) [A], ML6 (Senior AI Engineer Advisory&Delivery, BE) [A], Liablix (founding eng, IT Bologna) [A], modefinance (Full Stack, IT Trieste/Milan) [A], Xomnia (NL), Artefact (FR), Radix (BE), Alexander Thamm (DE), Jus Mundi (FR legaltech), Doctrine (FR legaltech). Dups caught: Agile Lab, Datrix, Lexroom, Cleafy, Taktile.
  - Sweep 2 is the standout - real applied-AI/consultancy + Italian vertical-AI roles in his exact FDE/solutions lane. Best immediate applies: dataroots AI Solution Engineer, ML6, modefinance (Italy), Agile Lab Data Engineer III Remote (Italy remote), Jus Mundi/Doctrine.
- Built owed deliverables: Prabhavit_CV_GTM.md (Forward-Deployed/Solutions framing, agents+code, no-code scrubbed) and DM-templates.md (founder cold / recruiter / warm-hook Eden AI).

Still to do (browser-dependent, next): hiring.cafe verify sweeps; Gmail Jobs/Action + Jobs/Opportunity check; LinkedIn manual connects + warm-recruiter/founder DMs; apply-fill (STOP before submit) to the verified-live openings (Hostaway, Nebuly, DigitalGenius, Albatross, J.D. Power). Requires him logged into Gmail (prabhavitg@gmail.com) / LinkedIn / hiring.cafe in the controlled browser. Browser flaky this session (disconnected twice); if it drops these move to his local session.

---

# SESSION LEDGER — 18 Aug 2026

Everything done this session, so any next session picks up cold. Ledger folder = `~/Downloads/claud jobs/`.

## 1. COLD-OUTREACH LIST — ✅ COMPLETE
- Files: `Outreach - people to contact.xlsx` (standalone) + tab `Outreach - people to contact` in `Role shortlist - 8 Aug 2026.xlsx` (pos 5, START HERE points to it). KEEP BOTH IN SYNC.
- **96 rows: 89 with real contact, 0 pending, 7 dropped.** All 22 previously-pending persons filled this session.
- Categories: FlowSpace competitors (~25), coworking software vendors (~15, OfficeRnD/Nexudus = A API hook), Italian automation consultancies (9), automation products (~23), proptech-automation (~16).
- HARD RULE held: no fabricated names/emails/URLs; `not found` over guess; amber = VERIFY before send.
- Standout new contacts: Pipedream (Dylan Sather, co-founder DevRel), Workato (Zayne Turner, Dir Dev Communities), Glide (Andy Claremont), Bardeen (Cory Cofran SE), Cloudbeds (Sébastien Leitner VP Partnerships), RoomRaccoon (Stevie Reffin Head of Partnerships).
- Dropped: Spacery, Gowork, Relay.app (shutting down), andcards (=Spacebring), Wishbox (=Duve), Bubble.io + Apaleo (already applied).
- Full detail + colour code in `OUTREACH-PICKUP.md`. Remaining human work = actually reach out, fill Contacted?/Date columns.

## 2. PROFICIENTLY PLUGIN — ✅ INSTALLED + ONBOARDED
- Claude Code plugin `proficiently@proficiently` (marketplace `proficientlyjobs/proficiently-claude-skills`). Enabled user-scope in `~/.claude/settings.json` + committable copy at `~/Downloads/claud jobs/.claude/settings.json` for coworkers.
- Skills live: `/proficiently:job-search`, `:apply`, `:tailor-resume`, `:cover-letter`, `:network-scan`, `:setup`, `:jobsearch-telegram`.
- Data store seeded at `~/.proficiently/`: resume (Prabhavit_CV.pdf), `preferences.md` (€40–50k, EU/remote, dealbreakers: no-MSc/no-Polish/hand-back-required-cover-letters/anti-AI-Qs), `profile.md` (reconciled 1:1 against the actual CV — 8 roles Aug2023→ongoing, all freelance/collaborator).
- Permissions added to settings: Read/Write/Edit `~/.proficiently/**`.
- Fix applied: git `url."https://github.com/".insteadOf "git@github.com:"` (plugin clone was failing on SSH).

## 3. WEBSEARCH CAP — raised
- `~/.claude/settings.json` env `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION = 10000` (was hitting silent ~200/session shared cap). Took effect after restart — searches worked this session.

## 4. JOB-SEARCH RUN — IN PROGRESS (interrupted by limit)
- Claude in Chrome = NOT connected (dead, as HANDOFF warned) → used Playwright fallback on hiring.cafe (hiringcafe.com).
- Filter applied. Live URL with his role query:
  `https://hiringcafe.com/?searchState=%7B%22jobTitleQuery%22%3A%22%28%5C%22automation+engineer%5C%22+OR+%5C%22solutions+engineer%5C%22+OR+%5C%22forward+deployed%5C%22+OR+%5C%22developer+advocate%5C%22+OR+%5C%22support+engineer%5C%22+OR+%5C%22AI+engineer%5C%22+OR+%5C%22integration+engineer%5C%22%29+AND+NOT+intern%22%7D`
- Boolean query used: `("automation engineer" OR "solutions engineer" OR "forward deployed" OR "developer advocate" OR "support engineer" OR "AI engineer" OR "integration engineer") AND NOT intern`.
- **NEXT:** open that URL, extract cards via `browser_evaluate` (DOM innerText of listing cards — the API is auth-gated 401/405, do NOT use it; do NOT use get_page_text), score vs `~/.proficiently/profile.md` + `preferences.md`, save to `~/.proficiently/job-history.md`, resolve employer URLs for High fits into `~/.proficiently/jobs/<slug>/posting.md`. Then `/proficiently:apply <url>` per role.
- Extraction proven working (pulled 30 cards; default feed was unfiltered Italy — hence the keyword filter).

## 5. LINKEDIN CONTACTS (for network-scan) — ✅ DONE
- EU account: no direct "Connections" checkbox. Correct path = Settings → Data privacy → Download my data → pick the TOP radio **"Download larger data archive, including connections…"** → Request archive → wait for email (larger archive up to ~24h) → `Connections.csv` inside the ZIP → give path or drop in `~/.proficiently/linkedin-contacts.csv`. (Member Data Portability API = unnecessary, same result.)

## 6. MEMORY updated
- `project_job_search.md`: salary corrected to €40–50k; added outreach-list + WebSearch-cap + plugin pointers.

## KEY FACTS (confirmed this session)
- Salary €40–50k (contract €250–300/day). Venice/Veneto, Italian LTR permit (EU/remote, no sponsorship for Italy). Email prabhavitg@gmail.com. LinkedIn linkedin.com/in/prabhavit, GitHub prab-gupta. BA (no CS degree, no MSc). No Polish.

## 7. JOB LEADS (companies to reach out to) — NEW
- `JOB-LEADS-LEDGER.md` = 10 scored hiring companies from proficiently job-search, each with role + hiring.cafe link + a reachable-human contact (agent-sourced, no-fabrication).
- Full scored matches: `~/.proficiently/job-history.md`. Contacts patched in as the agent returns.
- Distinct from `OUTREACH-PICKUP.md` (that = competitors/vendors/consultancies to cold-approach; this = employers actively hiring).
- Profile enriched with FlowSpace listing-bot + Bubble→Next.js/Laravel migration narrative (in `~/.proficiently/profile.md`).


## 8. STATE AT LAST STOP (18 Aug, limit reset) — PICK UP HERE
- ✅ LinkedIn: 308 connections scraped from the Playwright window (user's own logged-in session, connections page) → `~/.proficiently/linkedin-contacts.csv` (cols: First/Last/URL/Email/Company/Position/Connected On; 88 have a parsed Company — headline-derived, approximate). network-scan can run.
- ⏳ Contact-finder agent for the 10 job leads DIED on the session limit before returning — **RELAUNCH IT**: general-purpose agent, find best reachable human (hiring mgr/eng lead/recruiter > founder) at ORCA Group, Peratera, ElevenLabs, Nearform, Cohere, Software Mind, BCD Travel, AI Digital, PRINOTH, Quvia; no-fabrication rule; patch results into `JOB-LEADS-LEDGER.md` contact column.
- Leads themselves already in `JOB-LEADS-LEDGER.md` (10 rows, roles + hiring.cafe links, scored).
- Browser state: Playwright tab 0 = filtered hiring.cafe (146 remote hits, 10 pulled — more pages available), tab 1 = LinkedIn connections.

## 9. GITHUB FIXED (18 Aug) — github.com/prab-gupta
- Profile README repo (prab-gupta/prab-gupta) — recruiter pitch, renders on profile. LIVE.
- Profile bio + location (Venice, Italy) + website (LinkedIn) set.
- Demo repo **llm-doc-parser** (public): README.md + parser.py + requirements.txt. Runnable Python LLM document→JSON extractor; mirrors the FlowSpace listing bot / CV parser; in Python ON PURPOSE to close the Python gap that was auto-filtering his automation apps.
- Fixes funnel pattern #5 (zero inbound / invisible builder). CV github link now backed by real content.
- TODO (optional next): pin llm-doc-parser; add a 2nd repo (n8n workflow export) + a sample brochure so the demo runs out-of-box; record a 2-min Loom.

## 10. GMAIL FILTERS (18 Aug) — inbox de-noised
Imported 3 filters to prabhavitg@gmail.com (applied to existing mail):
- `Jobs` — ATS senders (greenhouse/lever/ashby/workable/teamtailor/recruitee/workday/icims/personio/factorial/join/calendly) → label + important + never-spam.
- `Jobs/Action` — subject interview/next steps/assessment/screening/schedule/book a time/action required/offer/take-home → label + STAR + important.
- `Jobs/LowPriority` — micro1/remoteleverage/sparkhire/10x-hire → archive out of inbox.
Filter XML kept at ~/.playwright-mcp/gmail-jobfilters.xml (+ scratchpad copy). Daily habit: check Jobs/Action.

### Gmail filters v2 (added Rejected + Opportunity + content catch-all)
- `Jobs` also catches by content: "thank you for applying / your application / application received / your candidacy / application update" (employers on non-ATS domains).
- `Jobs/Rejected` — rejection phrases AND job-context → archive out of inbox, kept for record.
- `Jobs/Opportunity` — inbound/leads ("came across your profile", "we're hiring", "open role", "talent pool", recruiter reach-outs) → label + STAR + important.
- Full set now 6 filters. Daily check = Jobs/Action + Jobs/Opportunity (both starred). XML: ~/.playwright-mcp/gmail-jobfilters.xml + gmail-jobfilters2.xml.

---

# EMAIL OUTREACH SWEEP - 19 Aug 2026 (net-new, email-first)
Ask: "look for more reachouts email this time with company website."
Method: 4 parallel discovery subagents (Italian AI consultancies / EU AI consultancies / vertical-AI startups / AI-agent+GTM tools), strict NO-FABRICATION + must-cite-email-source. Then I independently WebFetch-verified every email on its source page.
Result: 42 companies found -> 8 already in tracker (dropped to enrichment) -> 34 NET-NEW. 33/34 have a published email verified on-page (only ReportAId has none on-site -> founder LinkedIn). Priority A=10, B=15, C=9.
Deliverables:
- NEW: "Email outreach - 19 Aug 2026.xlsx" (Tab1 = 34 net-new email+website; Tab2 = 8 verified emails for companies already in tracker).
- Appended the 34 to "Outreach - people to contact.xlsx" master (now 132 companies; email in col H, verify-note + person LinkedIn in col J).
Top A-tier (verified email + strong lane fit, several hiring now): Superlinear (BE, FDE API&Data role live, no degree - jobs@superlinear.eu), statworx (DE, AI Engineer live - info@statworx.com), DareData (PT remote - contact@daredata.ai), Computas (NO, AI Dev live - contact@computas.com), inovex (DE, ML Eng live - info@inovex.de), Boosha AI (IT, n8n+agents, CEO mario@boosha.it), Cato/get-cato.com (IT Milan, founder hiring AI - info@get-cato.com), ComplyDo (DE, YC agents - info@complydo.io), Martes AI (IT - contact@martes-ai.com), i3k (IT on-prem RAG - info@i3k.eu).
Flags: Trigify UK=sponsorship; SPS Fulfillment now US-based; Computas=Norway/EEA; Klaaryo & Captain Data publish only privacy/GDPR emails; deepset imprint anti-scrapes 'info at deepset.ai'.

---

# POWER PLATFORM PIVOT SWEEP - 19 Aug 2026
Ask: junior/entry Power Apps / Power Platform roles (career pivot). Note: he holds MS Power Automate + Copilot Studio certs -> credible ENTRY, not beginner.
Method: 3 subagents launched but ALL died on account session limit (resets 3pm UTC); finished SOLO via WebSearch/WebFetch. ~55 candidates seen, verified each.
Finding: junior + remote-EU + English + no-clearance Power Platform roles are SCARCE. Market splits into US-federal (clearance), DACH (German), senior 5+ yrs, India/LATAM, on-site consultancy.
Verified clean fit (1): Trueblue S.p.a. (Milano/Verona, Italy, hybrid, English B2 working lang, junior-friendly, Power Apps + D365 CE) -> https://truebluecorp.com/en/power-platform-developer  [fit 86]
Leads/channels (near-misses tab): Dev4Side (Milan MS Partner, English site - apply + pitch), Avanade (grad programme), Version 1 (Academy), Expleo (Spain-only, junior, Copilot Studio - watch for EU equiv), UBDS (UK), Ciellos (talent pool), IRIUM (Power BI Spain).
Dropped: Accenture Federal / DSA / ARSIEM / PingWind (US clearance); reemento / Macaw / LIONSCOUT (German); Smart Working (5+ yrs, RO/BG/HU/RS/PL not Italy); Heinsohn (LATAM); Capco/Temus/Unify (India/SG); Version1 + Macaw postings expired.
Pivot plan (tab in file): (1) Italian MS partners in English (Trueblue, Dev4Side, Reply/Lutech/Var Group/Engineering); (2) graduate/academy (Version 1 Academy, Avanade grad); (3) certify PL-900 then PL-400 to title himself 'Power Platform Developer Associate'; (4) do 1-2 Power Automate/Copilot freelance gigs for portfolio proof; (5) watch himalayas/remoterocketship for 'all levels, remote EU/Italy'.
File: "Power Platform pivot - 19 Aug 2026.xlsx" (Shortlist / Near misses / Search notes / Pivot plan). Delivered + synced. Save-only.
