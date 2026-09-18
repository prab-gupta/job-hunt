# Job hunt — state of play

**Last updated: 6 August 2026.** Everything in this folder was produced across the 5 and 6 August sessions.
If you're a future Claude session reading this: start here, then read `application-rules.md`
inside `job-hunt.skill` (or the copy in the Job Search project) before touching any form.

## Where things stand

**30 applications submitted, all confirmed on the employer's own success page.** (15 on 5 Aug
daytime, +2 in the evening: Reedsy, Cohere, +6 late: Goldsky, n8n, ElevenLabs, Musixmatch,
MyEdSpace, Eneba, +4 from a second sweep: Reflow, Codex, Checkly, Supabase, +3 from a third:
Jimdo, Taxfix, Make.) Machine
answer to "have we applied here?": **`applications.csv`** — 249 rows covering submitted,
closed, gated, skipped, blocked and not-yet-opened, with URLs and confirmation text. Human detail — including what
was entered in every judgement-call field — is in `applications-2026-08-05.xlsx`, tab
"Submitted". Run `python3 validate.py` at session start and end; it checks confirmations,
letters-vs-applications, the CV hash, and duplicates.

EggAI · Nuitée · Arize AI (AI Sales Engineer, EMEA) · Arize AI (AI Solutions Manager, EMEA) ·
HiPeople · G2i (Senior/Staff TypeScript) · G2i (Senior Engineer) · G2i (AI Interaction Evaluator) ·
OpenHands · Camunda · Viktor · tem · Oh · Duvo · Sourcegraph · Reedsy · Cohere ·
**Goldsky** · **n8n** · **ElevenLabs** · **Musixmatch** · **MyEdSpace** · **Eneba**.

Batch 2: **Reflow** · **Codex** · **Checkly** · **Supabase**.
Batch 3: **Jimdo** · **Taxfix** · **Make (Celonis)**.

Three shortlists now live in the Job Search project: `role-shortlist-2026-08-05.md`,
`-batch2.md` and `-batch3.md`. Batch 3 is the one with unspent leads in it.

**Both shortlists are worked through.** The first queue is exhausted; the second (batch 2) has
four submitted, four next-pass candidates with no blocker (Shippeo, Parloa x2, Remote People,
Dash0), and the rest recorded as closed, gated or blocked. The new shortlist is
`claude/role-shortlist-2026-08-05-batch2.md` in the Job Search project.

**Two hard lessons from batch 2, worth reading before the next sweep.** First: the Ashby posting
API is not verification. Four of the highest-scoring finds (GRAI 86, Mercura 84, Quadrivia 79,
Glacis 66) were listed as live by `api.ashbyhq.com` and returned "Job not found" the moment a real
browser opened them. Only the browser counts. Second: the "GTM Engineer" market is large, live,
well paid and almost entirely gated on US or Canadian work authorisation. The EU-eligible yield
came from European-native hosts: SmartRecruiters, the EU Greenhouse board, join.com and
euremotejobs.

**Still blocked, needs Prabhavit:** five join.com roles (GTM Base, dexter health, Pinnipedia,
Arkipel, Jamie). join.com forces account sign-in before the form opens and Claude cannot create
accounts. If he signs in to join.com in Chrome first, they can all be done in one pass.

**Known gaps from that session, for honesty:** four Greenhouse forms had optional Cover Letter
fields that were left blank — EggAI, Nuitée and both Arize roles (before the letter existed) and
**Sourcegraph, where the letter had already been written**. Submitted applications can't be edited
on Greenhouse or Ashby. The Sourcegraph letter is in this folder if he wants to send it as a
follow-up. The rules file now carries a pre-submit checklist so it doesn't recur.

## 6 August 2026: the big sweep

**246 verified leads are now on `Prabhavit_job_leads_2026-08-06.xlsx`**, which supersedes the older
shortlist spreadsheets. He asked for 200 and this passed it. Five tabs:

| Tab | Rows | What it is |
|---|---|---|
| Summary | - | Formula-driven counts plus the legend, the tier rules, the fit rubric and the verification caveats. |
| New leads | 215 | Everything not applied to yet, sorted by fit, with the eligibility sentence verbatim and a live apply link. |
| FlowSpace-like platforms | 31 | The coworking, desk-booking, short-stay, hospitality and travel-booking roles, kept separate at his request. Extra column names the specific domain edge his Office RnD / Nexudus / Clubee work gives him on each one. |
| Submitted | 30 | All 30, with confirmation text seen on screen. |
| Needs you or blocked | 24 | Everything that stopped for a reason that needs him rather than more searching. |

Nothing new was applied to on 6 August. His instruction was collect-and-list, not apply.
All 170 new rows are logged in `applications.csv` as `not-yet-opened`, so the dedupe source of
truth is still authoritative: **249 rows, 30 submitted**.

**Tier 1 is now 94 roles** he could work from Venice today with no move and no authorisation
question. That is the queue to spend the next session on.

**Where the new leads came from.** Eleven parallel search lanes: dedicated n8n and automation
tooling; forward-deployed, solutions and implementation engineering; GTM and revenue operations;
applied AI at EU startups; full-stack TypeScript and Laravel; internal AI enablement at non-tech
employers; proptech and booking platforms; contract and freelance day-rate work; developer support
and experience; Italy-specific English-working roles; and a geography sweep of the Netherlands,
Germany, Spain, Portugal, Poland and the Nordics and Baltics.

**Verification is honest, not uniform.** 79 rows were confirmed from a rendered posting body with a
working apply path, 67 from a rendered aggregator mirror, and 24 could only be confirmed at the
title or feed level. The Verification column on each row says which, in plain words. Ashby and
several employer ATS hosts stayed unreadable for this session, so those rows are flagged rather
than dropped.

**New market findings from this sweep:**

6. **Aggregator-hosted postings are now a real share of the EU market.** Himalayas, euremotejobs,
   arbeitnow, startup.jobs and remoterocketship carry roles whose employer ATS page is unreachable
   or does not exist as a public URL. Those are applyable through the aggregator, but the employer
   side cannot be independently checked. Treat the apply path as the aggregator, not the company.
7. **The "one role, N country reqs" pattern is common and worth exploiting.** Dorado Software Group
   posts the same Marketing AI and Automation Specialist for Portugal, Spain, Poland and Romania;
   TripleTen does the same for its CRM Systems and Automation Manager; Wing Assistant for Poland and
   Croatia. He should pick the one country he would actually move to and apply once, not four times.
8. **Country-list roles that omit Italy are the quiet killer.** Paires, Holtzbrinck, Intellectsoft
   and several others are fully remote and a good fit, but Italy is simply absent from the eligible
   list. Those are relocation decisions, not applications, and they are flagged as such.

## Next actions (needs him)

0. **Answers only he has.** **Kairos** and **Gensyn** — both require a free-response answer with
   the employer explicitly asking for no AI assistance. **YLD** — confirm whether he has an
   LTD/SRL; they engage limited companies only. **Supabase** — his passport country (not in any
   file) and a GitHub profile he doesn't have. **Fueled** — a required US work-authorisation
   dropdown. **Moneyfarm** and **Mindrift/Toloka** — apply.workable.com is blocked for the
   browser extension; he applies by hand or grants the domain.
1. **Sign in to join.com in Chrome — this now unblocks ELEVEN applications**, including the two
   best-paying roles found in either sweep: peopleIX (€65–80K, Cologne hybrid, workflow automation
   platform) and salesHAX (€60–110K, remote, whose named stack is Next.js, React, Node, PostgreSQL,
   Supabase, OpenAI, Claude, Make.com and n8n). This is the single highest-value thing he can do.
2. Sourcegraph: letter was written but never attached and the form can't be edited — approve a
   follow-up email with the letter attached.
3. Say "next batch" to continue down the shortlist (run order in `claude/session-runbook.md`).

## What's in this folder

Agent-readable layer (read these, not the xlsx):

| File | What it is |
|---|---|
| `applications.csv` | **Dedupe source of truth.** One row per application: status, URL, confirmation, salary stated, letter attached. |
| `answers/` | Reusable answer library, one file per recurring question, with what was actually sent to whom. |
| `form-quirks.md` | Per-ATS fill/submit mechanics learned the hard way. Append new ones. |
| `follow-ups.md` | Dated chase schedule for all 30 submitted + the join.com block + the Sourcegraph orphan letter. |
| `drafts/` | Written-but-unsent material: the Sourcegraph follow-up email, the n8n answer pack (now submitted). |
| `validate.py` | Self-consistency check: confirmations, letters↔applications, CV hash, duplicates. |
| `skill/` | `job-hunt.skill` unzipped, diffable. **Edit here, then repack:** `cd skill && zip -rFS ../job-hunt.skill job-hunt` |

Human layer:

| File | What it is |
|---|---|
| `Prabhavit_job_leads_2026-08-06.xlsx` | **The current workbook.** 246 leads across five tabs, see the 6 August section above. Use this one. |
| `applications-2026-08-05.xlsx` | Superseded. The older application tracker. Tabs: Submitted / Needs you / Closed or gated / Not yet opened. |
| `role-shortlist-2026-08-05.xlsx` | 71 verified roles from 745 candidates, scored and tiered. Tabs: Shortlist / Near misses / Search notes. |
| `job-hunt.skill` | The packaged skill: search playbook, rules, six agent briefs, CV, letter, two scripts. Save it in Claude to load automatically. |
| `Prabhavit_CV.pdf` | **The only CV to send.** Attach to every application. sha256 recorded in `validate.py`. |
| `application-answers.md` | The original drafted answers for forms with written questions (now mirrored in `answers/`). |
| `letters/*_Motivation_Letter.pdf` | Letters adapted per role from his own Arsenalia letter. |
| `claude/application-rules.md` | The rules + pre-submit checklist, canonical text (same file lives inside the skill). |
| `claude/motivation-letter.md` | His Arsenalia letter as text — paragraph bank + what to change per role. |
| `claude/session-runbook.md` | The order every session runs: follow-up → unblocked → batch → audit → log. |
| `claude/agents/` | New agent briefs (also inside the skill): `submission-auditor` (verifies evidence, not claims — catches letters written but never attached), `follow-up` (inbox sweep, chases, orphan letters), `interview-prep` (one-page prep when an invite lands). `form-scout` / `letter-writer` / `applicant` live in the skill only. |
| `cowork-job-application-prompt.md` | Paste-able Cowork prompt: positioning, flagship project evidence, drafting rules. |
| `materials-index.md` | Map of the Cowork project docs + skill bundle. |

## The standing rules, in short

Full version lives in the skill. The ones that were learned the hard way:

- **The CV goes on every application.** Only the file he last supplied, unmodified.
- **Salary or rate: €30,000–40,000.** His number, stated plainly, no market-data commentary and no paragraph where a figure was asked for. ⚠️ **Worth revisiting with him:** Checkly publishes OTE €115–150K for a role he applied to, and the rule made the answer €30–40K. The rule stands until he changes it, but he should see the cases where it costs him.
- **No em dashes.** His instruction, 5 Aug 2026. Use a plain hyphen. `make_letter.py` and the letter paragraph bank were scrubbed.
- **Never leave a cover-letter field blank, even when it isn't marked required.**
- **When a form demands 3+ years, write 3.** Answer honestly rather than skipping the application.
- **Skip join.com** unless he's signed in.
- **Don't sound machine-written**: name the tool and the number, admit a limitation, no "excited to apply".
- Never create an account, solve a CAPTCHA, enter payment or ID details, or invent a GitHub link, referral or demographic answer.

## His details

Prabhavit Gupta · Via Zanetti, 10 · Venice · Veneto · 30175 · Italy
prabhavitg@gmail.com · +39 351 610 7807 · https://www.linkedin.com/in/prabhavit/
Italian EU long-term residence permit — no sponsorship needed anywhere in the EU. Not UK, Swiss or
US authorisation. Availability for NEW applications: currently at FlowSpace (per the CV on file),
~2 weeks' notice — his choice, 5 Aug 2026. The 15 daytime apps said "immediately"; keep
stories consistent per employer. **Nationality / passport country is not recorded anywhere** —
ask him rather than guessing; Supabase already stalled on it. Full detail in `profile-gaps.md` and the rules file.

## Two things worth knowing about the market

1. **"GTM Engineer" converts better than "AI Engineer"** for his profile. That vocabulary outperformed every AI-titled query in the sweep.
2. **Search indexes run about a month stale.** Nine in ten candidates were already closed when the real browser opened the form. Verify in a browser, not by fetching.
3. **The "GTM Engineer" market is large, live, well paid and almost entirely gated on US or Canadian work authorisation.** EU-eligible yield comes from European-native hosts: SmartRecruiters, the EU Greenhouse board, join.com and euremotejobs.
4. **His Microsoft Copilot Studio and Power Automate certifications are currently worth almost nothing to him**, and not for lack of demand. That market in the EU is Microsoft-partner consultancies serving domestic clients, so it gates on the local language nearly every time. Working Italian is the unlock, not more searching.
5. **Italy is reachable but language-gated.** Of ten Italian finds in the third sweep, six were Italian-language postings and only three carried an explicit English-only line. The most expensive single loss anywhere was Reverse's Deployment Strategist AI in Milan/Rome: €60–80K, asks 2–5 years which is exactly his band, no technology mandated, and requires fluent Italian.
