# RULES.md - standing rules for the job loop (read fresh every tick; never act from chat memory)
Updated 2026-09-06. Merged from HANDOFF-SWEEP.md, AGENT-INSTRUCTIONS.md, approved plan. Lessons: append at bottom with date.

## Scope
- ANY relevant role, Python included. Tracks: A AI/automation eng, B FDE/solutions/implementation/customer eng, C full-stack/product eng, D technical PM; plus support/customer engineer, GTM engineer, DevRel, QA automation.
- Python roles in when Python = AI/LLM pipelines, automation, scraping, data tooling, QA. Skip when Django/FastAPI/asyncio backend is THE core requirement.
- Gates: <=3 yrs required (write 3 when asked), no MSc/CS-degree clause, no Polish/German/French required, no unnamed agencies or reposters, no unpaid/talent-pool, no ML research/model-training-core roles.
- Skip titles: Senior, Staff, Principal, Lead, Head, Director. Manager only if project/product/automation manager.
- Skip agencies: Scale Army, Remote Recruitment, ISTA, Teamified, Activate Talent, Pavago, Jobgether, Oowlish, W3Global. Reposters: Hire Feed, Quik Hire Staffing, Crossing Hurdles, FetchJobs.co.
- Geography: fully remote (EU/EMEA/worldwide) or any EU country on-site/hybrid. UK/US/CH need sponsorship: apply only if remote-friendly, answer authorisation honestly.
- Dedupe: `python3 loop/dedupe.py --check "<Company>" "<url>"` before touching any form. HIT = do not apply.
- Cooldowns: n8n eligible Sep 12 2026; ElevenLabs eligible ~Nov 3 2026.

## Facts (never go beyond)
Prabhavit Gupta · prabhavitg@gmail.com · +39 351 610 7807 (type full with +39) · Venice, Italy 30175 · linkedin.com/in/prabhavit · github.com/prab-gupta · DOB 21/02/2001
Italian EU Long Term Residence Permit: Italy or remote work performed from Italy = authorised Yes, sponsorship No. Any role performed outside Italy = authorised No, sponsorship or employer-side permit Yes, with the transparency line in answers/work-authorisation.md. Ireland and Denmark are outside Directive 2003/109/EC mobility. Available immediately. ~3 yrs experience (Aug 2023 - Aug 2026). BA Philosophy/Intl Studies/Economics, Ca' Foscari (not CS).
Salary: EUR 45,000-55,000 (single number 50000). USD 54,000. USD monthly 4,500. B2B EUR 250-300/day. Align up to a disclosed band.
Languages: Hindi native, English C2, Italian conversational (B1-B2, user 2026-09-11). How did you hear: Job board. EEO: decline to self-identify.
Facts source: `Prabhavit - Master Experience.md`. Canned answers: `answers/*.md`. Loom demos: https://www.loom.com/share/d0f6bf69fd3f4db2a429ae6948a098f4 and https://www.loom.com/share/d711fd7971ed4385a2ee7e3e948c8e73

## Claim ladder (2026-09-06)
FastAPI/Flask, Docker/Kubernetes, ML (fine-tuning, embeddings, evals, PyTorch) = claimable as working knowledge. "Production" wording only with a concrete example from Prabhavit (ask once, one line, when a JD centres it). Never: BPMN, cloud admin, computer vision, edge, ML research, extra languages.

## Materials
- CV: copy `Prabhavit_CV_Base.tex` (concise base, 2026-09-06; user: description text was too wordy), edit ONLY HEADLINE, SUMMARY, SKILLS. Summary 35 to 45 words max (3 sentences), bullets 14 to 22 words, no adjectives, one concrete outcome per bullet. `tectonic <file>.tex` with photo.jpg in the same folder. Save `Prabhavit_CV_<Co>.tex/.pdf` in ROOT. Never write "no-code" or "Bubble" (say "off a legacy stack"). No em-dashes. One page.
- Cover letter ALWAYS (even when optional): ~250 words, structure = role, FlowSpace proof, link to their product, logistics (Venice/CET, EU LTR, immediate). Save `CoverLetter_<Co>.txt`; pdf via .tex when an upload is required. Re-read the JD fresh; reuse the skeleton, never the claims.
- Essays: I write them from Master Experience + answers/. 150-300 words unless capped. Save to `answers/<company>-<slug>.md`. Vary, never resend verbatim.
- User-only (by rule): CAPTCHAs, account creation, anti-AI screening questions or "no AI" attestations, video answers. Leave the form filled, log NEEDS YOU with the exact question + tab id.

## Forms and browser
- Chrome MCP bug: coordinate actions hit the FOREGROUND tab. Use ref-based only: find, form_input, read_page, computer with ref=, javascript_tool.
- Read `ats-guides/<ats>.md` (and apply-bot/PATTERNS.md) before a new ATS. Ashby: real keystrokes after failed submit, location autocomplete must be CLICKED. Workable: refill address after CV upload. Recruitee: apply page is /c/new.
- Decline non-essential cookies, leave optional consents unchecked. Anti-AI screen = stop, hand back.
- Nothing is SUBMITTED without the on-screen confirmation. Screenshot to `confirmations/<co>-<date>.png`, then append the applications.csv row (exactly 10 fields: date,company,role,ats,url,status,confirmation_text,salary_stated,cover_letter_attached,notes).
- LinkedIn: Easy Apply = apply. Not Easy Apply = Save the listing and list it in STATE.md. Keep LinkedIn actions modest.
- Status vocabulary: SUBMITTED, NEEDS YOU, TO APPLY, BLOCKED, DROPPED, CLOSED, DEAD, SKIP - <reason>, REPLIED, REJECTED, INTERVIEW.

## Outreach (standing authorization 2026-09-06)
- Email-first, sent autonomously from prabhavitg@gmail.com via the Gmail connector. Only to addresses published on the company's own site (careers@, jobs@, named founder/recruiter). One per company. Cap 10/day. One follow-up at +7 days. CV attached (Prabhavit_CV_Original_EN.pdf, the user's original 3-page CV; the concise Base is retired per user 2026-09-06). Log every send in loop/outreach.csv with source_url of the address.
- LinkedIn = daily ready-to-send batch `outreach/linkedin-<date>.md`, 15-20 rows, note <300 chars. User clicks.
- Templates: DM-templates.md. Demo link: github.com/prab-gupta/llm-doc-parser. Never open with "passionate". Never mention Bubble/no-code.

## Loop hygiene
- One bounded unit per tick. Write results to disk before ending. Rewrite STATE.md (<=60 lines) at the end of every tick.
- No Claude/Anthropic ATTRIBUTION anywhere (no "generated by", no Co-Authored-By). Naming Claude Code and the Claude API as tools he uses is correct and encouraged. No em-dashes anywhere.
- Page count: use `pdfinfo file.pdf | grep Pages` (the /Type /Page regex fails on tectonic output). Trim the Summary to ~70 words to hold one page.

## Lessons (append, dated)
- 2026-09-06: applications.csv has 211 malformed rows; dedupe scans all cells, do not repair in place.
- 2026-09-06: Never resubmit to a company with a REJECT or interview-feedback thread in gmail_threads.jsonl on a matching-seniority req. Nearform rejected on senior+Python Aug 12 and got a Senior Python & AI submit Sep 2; its 11 Senior/Lead LEAD rows are SKIP.
- 2026-09-06: URL dedup before logging SUBMITTED. 14 URLs already have 2+ SUBMITTED rows (Mastra Customer Engineer 3x, Sep 3-5). dedupe.py --check on the exact url; any SUBMITTED row = do not apply.
- 2026-09-06: VERIFY / ACTION_REQUIRED / NEEDS YOU rows are same-day tasks and open every tick before any sweep. Leadtech (exact-title match) died at 31 days unactioned; Axmed continuation link and Huzzle Luna chat are open now.
- 2026-09-06: Gmail is the funnel's source of truth, not applications.csv. 7 of 11 interview-class companies (TOPdesk, Mayerfeld, rembrandtadvantage, Ethos...) have no CSV row; scorecard.py must flag Gmail ACK/REJECT/INTERVIEW companies with zero well-formed CSV row.
- 2026-09-06: One company = max 2 on-lane titles (FDE / Solutions / AI Automation / Support), never every open req (n8n: 21 URLs, 2 on-lane). Status must come from the fixed vocabulary; 703 distinct strings and 87 conflicting URLs exist today.
- Send window: outreach emails go out Mon-Fri 08:00-19:00 Europe/Rome only. Research and drafting can run any time.

## LinkedIn browse + Easy Apply unit (added 2026-09-06 on user request)
- LinkedIn unit runs EVERY day, every 3rd tick (user 2026-09-06: "keep applying on linkedin"). Weekdays 08:00-20:00: f_TPR=r86400 (past 24h). Weekends, nights and whenever a 24h pass returns 0: widen to f_TPR=r604800 (past week); dedupe.py removes anything already applied to.
- Every 3rd tick (or when queue.csv is empty and no outreach is due): open the logged-in LinkedIn in Chrome and browse fresh roles, do not rely only on the guest CLI. URL pattern: https://www.linkedin.com/jobs/search/?keywords=<q>&location=European%20Union&f_TPR=r86400&f_AL=true (relevance sort; sortBy=DD gives the 7 newest which on a weekend are all noise). Only the first ~7 cards hydrate in a background tab, so run more queries rather than scrolling. Queries: AI engineer, forward deployed engineer, solutions engineer AI, automation engineer AI, GTM engineer, product engineer AI, customer engineer, AI implementation engineer; locations European Union, Italy, Remote.
- Discovery: sweep.py's LinkedIn guest CLI already returns full result pages; the logged-in search list hydrates only ~7 cards while the tab is in the background (2026-09-06 test: scrolling the inner scroller to 2742px never rendered more), so use loop/linkedin_harvest.js only if the tab is foregrounded. The LinkedIn unit therefore = take LinkedIn leads from candidates.csv/queue.csv, open /jobs/view/<id>/ logged in, read the full JD, Easy Apply. Dedupe every id and company with dedupe.py before opening a card. Kill by title with the same regexes as sweep.py (senior/staff/lead/manager, German/French titles, m/w/d, US locations).
- Open the card (click by ref or navigate to /jobs/view/<id>/), read the JD with curl from https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/<id> (div show-more-less-html__markup; the logged-in page does not render the description in a background tab), apply the gates yourself for 1-3 leads, or batch 4+ to a haiku verifier.
- Easy Apply needs the LinkedIn tab VISIBLE (document.visibilityState === "visible"); in a background tab the modal never opens. Check visibility first; if hidden, prefer the company ATS named in the job URL (applicantTrackingSystemName=Recruitee/Greenhouse/Lever...) or add the job to NEEDS_YOU with "click the LinkedIn tab once, then say linkedin ready". When visible: click "Easy Apply" (ref), the modal has 3 to 6 steps: contact info (email/phone prefilled from profile, check the phone), resume (UPLOAD the tailored CV pdf via the hidden file input, never keep the stale library CV), additional questions (years of experience: integers; work authorisation: Yes/No only for Italy or remote work performed from Italy, No/Yes for every other country, then add the transparency line when possible; salary numeric per rules; languages: English only, never claim German/French), review, Submit application. Uncheck "Follow company" if present. Success = "Your application was sent to <company>" toast or "Application submitted" text; log 10 CSV fields with ats=LinkedIn Easy Apply.
- Not Easy Apply (external "Apply" button): treat like any ATS lead, queue it with the external URL.
- Cap 8 Easy Apply per day was a soft guideline; user 2026-09-06 said "apply to everything": apply to every lead that survives the hard gates (years > 3, senior/CTO/Executive title, hard MSc/PhD, non-English JD or required language, unclaimable core stack, closed). Agencies, contract/hourly roles and Mid-Senior labels are no longer kills for Easy Apply. 12 submits on 2026-09-06 drew no throttle warning; stop for the day only if LinkedIn shows a limit banner. Save on listing anything in-lane you cannot finish.
- 2026-09-06 21:18 USER RULE: the concise Prabhavit_CV_Base.pdf is "bad". Base CV = the original ~/Downloads/Prabhavit_CV.pdf (3 pages, Aug 6; copy kept as Prabhavit_CV_Original_EN.pdf). For Indeed Italia use Prabhavit_CV_IT.pdf = word-by-word Italian translation of that CV (Prabhavit_CV_IT.tex, 2 pages). Do not shorten or rewrite it; the user wants the same content.

- 2026-09-09 (user): CV per application = the original CV trimmed, not rewritten. Build Prabhavit_CV_<Co>.tex from Prabhavit_CV_EN.tex: summary max 2 existing bullets, experience bullets verbatim but relevant-first and pruned (min 3 FlowSpace, 1 per other role), skills relevant-first, 2 pages max, photo kept, no new sentences. The untouched original stays the fallback and the outreach attachment.

- 2026-09-09 20:12 (user): more cold outreach by email; Italian companies get the email in Italian (natural, formal-friendly "Lei" avoided, "voi" plural to the team; tu only to a named founder of a small startup). Daily cap raised from 10 to 20; send window extended to 08:00-21:00 Europe/Rome. Same guardrails: address published on the company site, one email per company, CV attached, log outreach.csv.
- 2026-09-10 20:40 (user): cover letters, CV tailoring and outreach emails must NOT lean only on FlowSpace. Draw on the whole record: UltraStrategy (CV-parsing LLM pipeline integrated into the platform: user uploads a CV, the pipeline extracts the data and scores relevance for specific role types, returns it to the frontend, then generates a standardised "Ultra CV"; Affinda + Claude API, n8n/Eden AI), Urlink (built the platform and logic with AI-assisted development, client-driven automations), Get2Germany (Google API integrations, AI tools that find courses/internships/jobs, n8n, database optimisation), and the FlowSpace live migration off the legacy stack (automated per-entity data migration, API vs CSV, cutover while live). Facts block for agents: loop/OUTREACH_FACTS.md (written and verified 2026-09-10 21:20) and Prabhavit - Master Experience.md (patched the same evening).
- 2026-09-11 10:20 (user): "don't drop anything LinkedIn suggests, especially junior positions". For every LinkedIn-suggested posting (Top job picks, My Jobs, recommendations; queue rows tagged LI-PICK) the soft gates are OFF: no fit floor, no years-of-experience kill, no Senior-title kill, no agency kill, no "Mid-Senior" kill, Italian-language JDs get an Italian letter. Only drop when the posting is closed, already applied (same requisition), or the JD explicitly requires fluent German/French/Dutch/Spanish/Danish/Norwegian etc. that he does not have (list those in STATE for the user). Account walls, CAPTCHAs and assessments stay NEEDS YOU with materials prepared. Junior, intern, entry-level and associate postings go first.
- 2026-09-11 10:25 (planner, reversible): Italian-language JD gate LIFTED for Italy-located roles. Basis: user confirmed Italian is conversational (B1-B2) and asked to apply to every LinkedIn suggestion including Italian ones. Italian JDs get an Italian cover letter, English CV, honest language level. Say "keep the gate" to revert.

- 2026-09-14 (user): Do not use Astra for everything. Delegate routine dedupe, listing verification and application drafting to cheaper agents where useful; keep the main model for ambiguity, failures and final accuracy checks. Separate ownership of tabs/files.

- 2026-09-14 (user confirmed): Has an active Partita IVA and is open to roles engaged through it. Answer active Partita IVA Yes.

- 2026-09-16: Brand names hide the ATS org. LinkedIn "MAU / AI-LAB" = Leadtech (leadtech.teamtailor.com); --check "MAU" missed two Leadtech AI Automation Engineer rejections (Jul 28, Aug 11), now logged. dedupe.py maps known brands to the org in ALIASES (inside norm_co, so corpus and --check both resolve). When the queue company name differs from the ATS domain or the email sender org, run --check on BOTH names and add the pair to ALIASES.

- 2026-09-16 (user): Campari Group rows are applied regardless of the years requirement ("apply campari, ignore years"). Honest letter: 3 years against the ask.

- 2026-09-16 22:50 (user, twice): "clear all forward deployed engineer italy and eu linkedin" / "all FDE roles in italy on priority and eu, use linkedin". STANDING: every LinkedIn Forward Deployed Engineer posting in Italy (first) and the EU gets an application, LI-PICK treatment (kill only closed / already SUBMITTED / language he lacks). Re-harvest the FDE keyword daily via the guest API (Italy geo 103350119 first, then EU 91000000, pages to start=975) and dispatch new rows before anything else.
- 2026-09-17 07:50 (user): when LinkedIn Easy Apply is capped, keep applying on company websites (offsite rows first) and run an FDE sweep (LinkedIn re-harvest + local candidate mining) instead of idling.
- 2026-09-18 (Codex session review): letters carry one structural honesty block (daily tools = TypeScript, Next.js, Node.js, Laravel, Python, n8n, Claude Code; everything else = working knowledge; no CS degree stated plainly when asked). Browser reads are filtered by role/name and capped (no unfiltered accessibility-tree or DOM dumps). A SUBMITTED row needs a confirmations/ file and the dedupe stdout in notes. Pre-09-11 per-company CV files stay quarantined (46 of them claim AWS/Docker production).
