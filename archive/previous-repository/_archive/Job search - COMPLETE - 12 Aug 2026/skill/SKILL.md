---
name: job-hunt
description: >-
  Find, verify and rank live job and contract openings that fit Prabhavit's CV — AI/automation
  engineering, forward-deployed and solutions engineering, full-stack product engineering,
  technical PM — remote-first from Italy but worldwide in scope, delivered as a ranked .xlsx
  shortlist. Use this skill whenever the conversation turns to looking for work — "find me some
  jobs", "any new roles this week", "who's hiring for X", "check openings at a named company", "any
  freelance or contract gigs going", "is this posting worth applying to" — or when asked to
  compare or re-rank roles already found. Trigger even when the request is vague ("anything
  interesting out there?"), names no job board, or mentions only a company or a technology
  rather than a role.
---

# Job hunt

Prabhavit is looking for work right now — his FlowSpace contract ended in July 2026. What
helps him is a short list of openings that are **real, currently open, and genuinely open to
him**, each with an honest reason it's worth an application. What hurts him is volume: a dead
link, a role that turns out to be US-payroll-only, or a staff-level posting he has no chance at
costs him more time than a missed opportunity does. Bias the whole process towards precision.

Two references do the heavy lifting:

- `references/candidate-profile.md` — what "good fit" means. **Read it before every sweep.** It holds his eligibility, target titles, seniority band, hard gates and preferences.
- `references/sources.md` — the tested search playbook: which domains and URL patterns actually return live postings, which are dead ends, and the specific ways postings lie. **Read it before your first search in a session.**

Don't interview him before starting. He's already told the skill what he wants; ask at most one
question, and only when the answer would change the entire sweep (for example, if he names a
company that has no public board). Otherwise run the default sweep and note your assumptions in
the reply.

## Step 1 — frame the sweep

Set five parameters before searching. Anything the request specifies overrides these defaults:

| Parameter | Default |
|---|---|
| Tracks | All four from the profile, weighted A (AI/automation) > B (forward-deployed/solutions) > C (full-stack/product) > D (technical PM) |
| Geography | Worldwide, prioritised by the eligibility tiers in the profile — mostly Tier 1, a minority of Tier 3 |
| Work basis | Employment **and** contract/freelance, in the same sheet, flagged so he can compare a day rate against a salary |
| Freshness | Posted within 30 days; prefer the last 7 |
| Size | 12–20 verified roles. Expect roughly **one in three candidates to survive verification** — dead postings, board-index degradation, false "Remote" labels — so plan on fetching 3–4× the target. If the first pass lands short, run a second discovery pass with different vocabulary rather than shipping four rows. |

A narrow request ("just contract work", "only n8n stuff", "anything at ElevenLabs") narrows the
sweep — don't pad it back out with unrelated roles to hit a count.

## Step 2 — sweep wide before filtering

Cast a much wider net than the final sheet, because most candidates die at verification. Aim for
**50+ raw candidates**; fewer than ~30 means the sweep was too narrow, and the fix is almost
always vocabulary — the same job is posted as "AI Automation Engineer", "Applied AI Engineer",
"Solutions Engineer" and "Automation Consultant" at four different companies.

Verification is what caps the size of the sheet, so spend the discovery budget in ways that make
verification cheap. **Board APIs verify a whole company in one call** (§5 of `sources.md`), so
when several candidates come from the same org, check the org once instead of fetching each
posting. Where subagents are available, give each one a source family *and* have it return
already-verified rows — parallel verification is what turns a 6-row sheet into a 15-row one.

Run these in parallel in a single message (see `sources.md` for exact syntax and templates):

1. Two or three `WebSearch` calls with `allowed_domains` on the ATS hosts — one per track.
2. One contract-vocabulary query using the literal words that work: `"contract"`, `"6-month contract"`, `freelance`, `B2B`, `part time`, `fractional`.
3. One stack-keyword query — `n8n`, `low-code`, `AI agents`, `Bubble.io`. These postings are much less crowded and are his sharpest edge.
4. Two or three board fetches — euremotejobs region paths, remoterocketship with `sort=DateAdded`, himalayas (serialize these, it rate-limits).

If subagents are available, fan the sweep out: give each agent one source family and a fixed
return shape (title, company, url, location wording, comp, posted date, basis). Verification is
fetch-heavy, so parallelising the discovery leaves budget for it. Tell each agent to use only
WebSearch/WebFetch — curl and python fetching are prohibited in this environment.

## Step 3 — filter against the profile

Apply the hard gates from `candidate-profile.md` — language requirements he can't meet, deep ML
specialisation, agencies and aggregator reposts with no named end client, unpaid or
talent-pool listings. Being outside the EU is **not** a gate any more; it moves a role to
eligibility Tier 3 with a `Relocation` or `Sponsorship` flag.

Keep a short list of notable drops and why. When the sheet comes back with 14 roles instead of
40, he should be able to see that the filter did the work rather than wondering whether the
search was lazy.

## Step 4 — verify every survivor by fetching it

He will click every link in the sheet, so every row must come from a page you actually loaded.
Never list a role from a search snippet alone, and never reconstruct a URL that looks plausible.

For each candidate:

- Normalise the URL first (strip Ashby's `?embed=js`, `/application`, `?utm_data=…`; add `?language=en` on Personio).
- Fetch it, and pull: exact title, company, the **eligibility sentence** (not the word "Remote" in the title), comp or rate if disclosed, posted date, seniority requirement, and whether it's employment or contract.
- **If a single-posting fetch comes back describing many different jobs, the posting is closed** — Greenhouse silently serves the board index for dead roles and nothing else signals it. Drop it.
- Drop anything you can't confirm is live. A quiet omission is better than a broken row.
- When a posting looks strong but the fetch is ambiguous, check the company's JSON board API (`sources.md` §5) rather than guessing.

## Step 5 — score honestly

```
Fit = role & track match        30
    + eligibility & work basis  25
    + stack overlap             20
    + seniority realism         15
    + signal quality            10
```

- **Role & track match** — how close the actual responsibilities are to what he's done, not how good the title sounds.
- **Eligibility & work basis** — Tier 1 (workable from Italy today) scores full marks; Tier 2 (non-EU Europe, remote) most of them; Tier 3 (relocation or sponsorship) a fraction. A company willing to engage a contractor abroad scores as Tier 1 even if it's US-based.
- **Stack overlap** — named tools he has shipped with beat adjacent ones. `n8n` in a JD is worth more than a generic "Python required".
- **Seniority realism** — will they actually interview someone with ~3 years and no CS degree?
- **Signal quality** — freshness, disclosed comp, company type, clear scope.

Use the range. If every role scores 82–88 the scores carry no information and he can't triage;
a real sweep produces a spread. Bands: **80+** apply this week · **65–79** solid, worth an
application · **50–64** worth a look if the top of the list dries up. Below 50, leave it out and
say why in chat if it was interesting.

## Step 6 — build the spreadsheet

Write the roles to JSON and run the bundled script — it owns the column layout, tier colours,
fit colour-scale, filters and the "Search notes" sheet, so week-to-week shortlists stay
comparable and no run has to reinvent openpyxl:

```bash
python3 <skill-dir>/scripts/build_shortlist.py --in roles.json --out "Role shortlist — 5 Aug 2026.xlsx"
```

Use the absolute path to the skill directory — the working directory during a sweep is rarely
the skill folder.

The JSON shape is documented in the script's docstring. Fill `sweep_notes` — sources swept,
queries run, raw/gated/verified counts, notable drops — because that sheet is how he judges
whether the search covered the ground. Then deliver the file with `SendUserFile`.

## Step 7 — report briefly in chat

Short and useful; the spreadsheet holds the detail. Roughly:

- One line on what was swept and what came back (`19 verified from ~60 candidates`).
- The top three, one line each: role, company, and the specific reason it fits.
- What to do first — which one or two to apply to today, and why those.
- **A market read** — the part a bare list can't give him. What the roles you saw are paying (bands, or rates for contract work), which title framings are getting posted and which have dried up, and anything about his own profile that is visibly costing him applications. The most useful example so far: the Bubble.io/no-code weighting on his CV reads as "no-code contractor" to code-first teams, which is a fixable presentation problem rather than a skills gap. Say that kind of thing plainly — a shortlist plus one true observation beats a longer shortlist.
- Where a role would be a contract engagement with a non-EU company, note anything he'd need to handle on his side (invoicing as a Partita IVA, W-8BEN for US clients, Deel/Wise rails) — briefly, and only when it's actually load-bearing for that role.

Don't re-tabulate the sheet in chat, and don't pad with encouragement.

## Applying, not just finding

When he asks you to apply — and he does — the search is only the first half. Applying has its own
rules file, and it is not optional reading: **`references/application-rules.md`** holds his
details, his salary number, the standard answers to the questions every ATS asks, the writing
rules, and the list of things you must never do on his behalf. Read it before you touch a form.
Two things in it were learned the hard way: **the CV goes on every single application**, and
**his stated salary range is his, not yours to improve on**.

The workflow that works, per role:

1. **Scout the form** (`agents/form-scout.md`) — one cheap read-only agent per role, in parallel. It reports LIVE / CLOSED / GATED, every required question verbatim, and whether the form is basic or needs writing. This is where most rows die: postings that look live in search are frequently closed, and a real browser is a much stricter test than a fetch or an API read.
2. **Split by what the form wants.** Basic forms — name, email, phone, location, CV, links, dropdowns — get submitted straight away. Forms with written questions need drafted answers first.
3. **Write the material** (`agents/letter-writer.md` + `assets/motivation-letter.md`). Never leave a cover-letter field blank; adapt his real letter to the role. `scripts/make_letter.py` renders it as a PDF in his own layout when the form wants a file.
4. **Submit one at a time** (`agents/applicant.md`). Browser automation doesn't parallelise — concurrent agents fight over tabs. Screenshot the confirmation; if you didn't see one, it didn't happen.
5. **Log it.** Company, role, what went in the judgement-call fields, the verbatim confirmation, the link. Then tell him in chat what you decided for him, so he can correct it before the next batch.

Expect attrition and report it plainly. A sweep of twelve top rows will typically yield a handful
of live basic forms, several that need writing, and several that turn out closed or gated on
work authorisation. That's the market, not a failure of the search — but say so rather than
letting a short list look like laziness.

## Judgment calls

- **"Is this posting any good for me?"** with a single link — skip the sweep entirely. Fetch it, score it against the profile, answer in chat with the honest verdict and what to emphasise if he applies. No spreadsheet unless he asks.
- **A named company** — fetch its board directly (`job-boards.greenhouse.io/<company>`, or an `allowed_domains` search on the company name) instead of running a generic sweep.
- **A repeat run** — if an earlier shortlist exists in this session or in the project, dedupe against it and mark what's new, so he isn't re-reading last week's list. Say how many were carried over.
- **A thin sweep** — if verification leaves only a handful, deliver the handful and say plainly what you'd change next time (different vocabulary, wider geography, contract-only pass). Don't inflate the sheet.
- **He corrects a preference** — a rate expectation, a company he'd never join, a city he would move to — write it into `references/candidate-profile.md` so the next run inherits it.
- **Something in the sweep is worth acting on beyond applying** (a company hiring three roles he fits, a recruiter contact in the posting) — mention it in the chat reply; it's often more valuable than one more row.

## Files in this skill

```
job-hunt/
├── SKILL.md
├── references/
│   ├── candidate-profile.md   — what "good fit" means; keep it current
│   └── sources.md             — tested search playbook, dead ends, verification traps
└── scripts/
    └── build_shortlist.py     — roles JSON → formatted .xlsx shortlist
```
