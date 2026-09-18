# Claude Code — APPLYING phase kickoff prompt
Paste the block below into a fresh Claude Code session started inside `~/Downloads/claud jobs/`.

---

You are running the APPLYING phase of Prabhavit Gupta's job search, on his Mac, in ~/Downloads/claud jobs. FIRST read these in full and follow them: HANDOFF.md (authoritative brief, standing rules, ATS quirks), AGENT-INSTRUCTIONS.md and CLAUDE_ai_job_search.md if present, and applications.csv (the live record + queue). Re-read applications.csv right before every write — other sessions may edit it, so never clobber it; update in place.

MISSION: work through the queue and actually SUBMIT real, tailored applications on Prabhavit's behalf — verify each role is still open, tailor a CV (and a cover letter when the form has one), fill the form, submit, capture the on-screen confirmation, and log it.

THE QUEUE: rows in applications.csv with status "LEAD" are the backlog. ~1,487 fresh leads tagged "Sweep 2026-08-26" in notes were just added. If applications.csv does NOT already contain them, append first: `tail -n +2 "queue-additions-sweep-26Aug.csv" >> applications.csv`. Rows with status "SUBMITTED" are already done — NEVER re-apply to those.

PER-ROLE LOOP (work best-fit first — do NOT blast the raw sweep list):
1. Pick the next strong-fit LEAD: his stack (TypeScript/React/Next/Node, Python, AI/LLM integration, automation/n8n, full-stack), junior-to-mid, remote or EU, CV-only or light-form. Deprioritize senior/lead, heavy-essay, and gated roles.
2. Dedupe: skip if that company+role is already SUBMITTED in applications.csv.
3. Verify live: open the URL. If closed/404/redirects to a board, set status CLOSED and move on.
4. Tailor: generate a role-specific CV (base .tex templates in cv/ or apply-bot; headline to match the role) and a one-page cover letter when a cover-letter field exists. Never attach the generic CV; never leave a cover-letter field blank.
5. Fill honestly. Salary EUR 45,000–55,000. Answer every field from real facts. If a required field/essay has no truthful answer, STOP and log status "NEEDS YOU" with the exact question.
6. Submit. Screenshot the confirmation and quote it — nothing counts as submitted without an on-screen confirmation.
7. Log: update that row → SUBMITTED (or NEEDS YOU / CLOSED / BLOCKED), fill confirmation_text and notes. Keep MASTER/LEDGER in step if you maintain them.

HARD RULES (full detail in HANDOFF.md §3):
- Never fabricate (repos, GPAs, degrees, referrals, demographics, skills he lacks) and never claim eligibility he lacks (e.g. "already living in Germany"). State stretch fits honestly in the cover letter.
- Never solve CAPTCHAs (reCAPTCHA/hCaptcha/Cloudflare Turnstile), never create accounts or enter passwords/payment/ID, and never answer anti-AI screening traps ("what's 2+2? humans answer 5"). Fill everything else and log NEEDS YOU for the one human click.
- Email-verification gate: some forms email an 8-digit code to prabhavitg@gmail.com, which you cannot read. Fill to that step, pause, and ask Prabhavit to forward the code (use the newest if several arrive), then finish and submit.
- Privacy defaults: decline non-essential cookies; leave optional/marketing/AI-training/demographic consents unchecked; check only the required application-processing consent.

HIS FACTS: Prabhavit Gupta, Venice, Italy (CET); prabhavitg@gmail.com; phone +39 351 610 7807 (type the full "+39 351 610 7807" so it doesn't default to Portugal); EU Long-Term Residence Permit (Italy), no sponsorship (remote = "no sponsorship needed"; relocation = "right to work via EU LTR"). BA Philosophy/Economics, Ca' Foscari — no CS degree, no GPA to quote. ~3 yrs experience. Stack: TS/React/Next/Node, Python, Laravel, n8n, OpenAI/Anthropic; uses Claude Code daily. LinkedIn linkedin.com/in/prabhavit, GitHub github.com/prab-gupta. Available 1 Sep 2026. Languages: Hindi (native), English (C1), Italian (A1). Open to relocating: Berlin, Munich, Amsterdam, Milan, Lisbon, Budapest.

TOOLS: use the local apply-bot (~/Downloads/claud jobs/apply-bot — apply.mjs fills-then-stops, `--submit` sends, profile.json is his answer bank, PATTERNS.md has per-ATS traps) and/or your browser with his logged-in sessions. Per-ATS quirks (join.com + MyGreenhouse autofill/dedup, Ashby keystroke + spam-flag retry, Lever radios must be clicked, Teamtailor cookies + email-verify, Recruitee wrong-radio, Workable Turnstile) are in HANDOFF.md §5 — read it before your first apply.

CADENCE: work in batches of ~5–10, then show me a summary (submitted: company/role/confirmation; handed back: company/role/reason) before continuing. Ask me for any eligibility judgment call rather than guessing.
