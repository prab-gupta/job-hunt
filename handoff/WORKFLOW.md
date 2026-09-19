# Operating workflow

## Scope first
Latest phase: applications, explicitly authorised by the user on 2026-09-18 after repository consolidation: “then continue applying use cheap agents”. Apply from the saved queue with honest answers and verified evidence. Earlier outreach authorisation remains recorded. A later explicit finding-only request would limit that task to research.

Standing application preference: prioritise Italy, junior roles and LinkedIn suggestions; all Italy/EU FDE postings were explicitly requested. Soft seniority filters were relaxed for LI-PICK/FDE-ALL. Still answer every qualification truthfully. Closed requisitions, confirmed duplicates and required languages the user lacks are exclusions. Account/CAPTCHA/assessment walls are blockers, not successes.

## Discovery
Rank A automation/AI, B FDE/solutions, C full-stack/product, D technical product. Employment and Partita IVA contracts both count. Tier 1 workable from Italy; tier 2 remote-across-Europe; tier 3 strong relocation/sponsorship matches, minority of results. Prefer <=30-day listings, especially <=7 days. Load the actual employer posting this run. Record eligibility wording, pay/rate or unknown, location, posted date or unknown, basis, fit and gaps. Never fabricate a URL or use a search snippet as verification. The archived original sweep brief has detailed source queries; apply PROFILE.md corrections first.

## Dedupe and evidence
1. Match exact canonical requisition/URL, employer and ATS aliases against `archive/claud-jobs/applications.csv`, `loop/queue.csv`, `loop/corpus.json`, confirmations and available Gmail evidence.
2. `loop/dedupe.py --check "Company" "URL"` is the historical helper. Inspect portability before execution. The CSV has malformed historical rows: scan all cells; do not repair in place. A company hit or LEAD alone does not prove this role was submitted.
3. Prior matching rejection/interview evidence must be reviewed before reapplying. Do not apply twice to the same requisition.
4. SUBMITTED requires actual confirmation text/screenshot or a reliable acknowledgement. Save it and log its path. Prepared form, attempted click and verification-email request are not submission evidence.

## Applications
Reopen the posting and review the form before submission. Use a checked, tailored CV; verify company, role, dates, contacts, language and permit answers. Do not invent numeric years or salary. Use current authorised tools; keep one owner per browser/tab. Stop at an actual platform limit; do not bypass it. Continue eligible company-site work when the requested phase permits it. Human-only challenges, self-attestations, assessments and accounts follow their actual requirements.

## Outreach
Prior user authorisation: email published company/recruiter contacts, review past sent messages and dedupe first. Italian companies get Italian emails. Personalise with at least two relevant experience examples, attach the checked CV, verify attachment presence, then log message/thread ID and source of address. At most one initial email per company and one in-thread follow-up after seven days. Saved cap is 20/day. Time-window notes conflict (19:00 versus 21:00); use the shared Mon–Fri 08:00–19:00 Europe/Rome window until clarified. Never resend an uncertain send without checking Sent. LinkedIn message drafts do not imply authorisation to send them automatically.

## Agents and continuity
Use cheaper available models for bounded discovery, dedupe and drafting; reserve the main model for ambiguity and final checks. Use Headroom where available/relevant, as requested. If unavailable, say so without claiming it ran. Do not restart rate-limited agents in a loop. Assign files/tabs explicitly; coordinator owns queue merge. Do not recreate overnight schedules from historical text.

Keep status, attempt and evidence separate. Preserve raw history. Update a short checkpoint after each bounded action. No invented success counts, credentials in Git, or AI attribution in commits.
