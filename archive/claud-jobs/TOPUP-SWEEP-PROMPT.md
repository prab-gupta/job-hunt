# Fresh-session prompt — blind-spot sweep TOP-UP (toward 2,000)
Start a NEW Cowork session (fresh WebSearch budget) with the desktop app connected, then paste the block below.
PREP: make sure `role-sweep-blindspot-26Aug.csv` is saved in `~/Downloads/claud jobs/` first (the other 3 dedupe files are already there).

---

CONTEXT: You're continuing a blind-spot job-role sweep for Prabhavit Gupta in a FRESH session (fresh WebSearch budget). A prior session already found 1,175 net-new "blind-spot" roles; the target is 2,000, so you need ~825 MORE net-new roles in the same lanes. His job folder is on his Mac at /Users/prab/Downloads/claud jobs (device bridge).

STEP 0 — build the dedupe corpus. If the device is connected, stage these four files from /Users/prab/Downloads/claud jobs and build an exclusion set from ALL of them (by URL AND by normalized company+role): applications.csv, role-sweep-1000-21Aug.csv, role-sweep-remote-500-21Aug.csv, role-sweep-blindspot-26Aug.csv. If any is missing or the device isn't connected, ask me to attach them. EVERY role you output must be NET-NEW versus all four.

PROFILE (for relevance): Prabhavit — ~3 yrs, Venice Italy, remote or open to EU relocation. Stack: TypeScript/React/Next/Node, Python, Laravel, n8n, OpenAI/Anthropic; uses Claude Code daily; comfortable customer-facing. Include strong-but-adjacent fits, junior-to-mid. Location filter: remote (worldwide/Europe/EMEA) OR located in EU/EEA/UK.

BLIND-SPOT LANES — prioritize the two that got starved last run FIRST:
1) Automation & AI-ops: growth/martech engineer, marketing automation, RPA/no-code (n8n/Zapier/Make/Retool), applied-AI / AI-ops / AI implementation, prompt/GenAI, conversational-AI/chatbot engineer.
2) Product & quality: founding engineer, product manager / technical PM / AI PM, QA/SDET/test-automation (Playwright/Cypress), developer experience, technical writer, community engineer.
Then top up:
3) Domain/vertical: proptech / real-estate / marketplace (his FlowSpace domain), fintech/insurtech/legaltech/healthtech, web3/crypto.
4) Customer-facing: DevRel/advocate, sales/solutions engineer, implementation/onboarding, TAM, L2/L3 support, forward-deployed.

METHOD — avoid last run's mistake: run sweeper agents SEQUENTIALLY, one lane cluster at a time — do NOT launch 4 at once (concurrent agents drained the shared 200-call WebSearch budget and starved each other). Each agent: use WebSearch to discover ATS boards (Ashby/Greenhouse/Lever/SmartRecruiters/Workday/Personio/Teamtailor/Recruitee) with its lane terms, PLUS WebFetch on JSON APIs (jobs.workable.com/api/v1/jobs?query=<term> — never pass location=Remote, it geocodes to Oregon; also remotive/jobicy/arbeitnow). Dedupe each agent's output against the corpus and within. Keep a running net-new tally; stop when combined new >= 825 (or sources are genuinely exhausted — then report the true number, never fabricate).

OUTPUT: merge all top-up agent files, dedupe, and write role-sweep-blindspot-topup-<date>.csv (schema: Company, Role Title, Location, Remote/Hybrid/Onsite, Lane, Source, URL, Posted). Sync it to /Users/prab/Downloads/claud jobs. Report: combined net-new count, running grand total toward 2,000, lane breakdown, sources, and any caveats.

RULES: only REAL roles you actually retrieved — never fabricate a company/title/URL, never reuse a corpus URL. Discovery only — do NOT apply to anything.
