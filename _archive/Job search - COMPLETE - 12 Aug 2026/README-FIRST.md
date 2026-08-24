# Job search — complete archive, 12 August 2026

Everything from the job search, in one folder.

## What's here

```
Prabhavit_CV.pdf              THE canonical CV. Attach to every application, unmodified.
                              sha256 e18579bb… — scripts/validate.py checks it.
                              This is the ONLY CV in the folder. The skill shipped an older
                              copy with different bytes; it has been deleted (see
                              skill/assets/NOTE-cv-removed.txt) so there is nothing to confuse.

sheets/
  MASTER - every application - 12 Aug 2026.xlsx   All 114 rows. THE source of truth.
  Role shortlist - 8 Aug 2026.xlsx                Working workbook, 9 tabs (see below).
  Blocked - needs you - 7 Aug 2026.xlsx           Historical.
  Prabhavit_job_leads_2026-08-06.xlsx             Historical.
  Working workbook - 6 Aug 2026.xlsx              Historical (Summary, New leads,
                                                  FlowSpace-like platforms, Submitted,
                                                  Needs you or blocked, Outreach targets).

docs/
  00-START-HERE.md            Index + the prompt for a new session.
  working-rules.md            THE OPERATING MANUAL. Read before touching a form.
  candidate-dossier.md        CV verbatim, eligibility, evidence, hard gates, blindspots.
  market-intelligence.md      Pay bands, live vs dead titles, which sources lie.
  master-application-log.md   All 80 applications + the 11 open items.
  do-not-repeat.md            The 348-company dedupe list.
  project-docs-index.md       Every doc in the Claude project, and where each one landed here.
  rules_out.md                Earlier rules file (6 Aug) — superseded, kept for provenance.
  form-quirks.md              Earlier ATS quirks file — folded into working-rules.md.
  follow-ups.md               Earlier follow-up tracking.
  README.md, run-sheet-2026-08-06.md, claude-lead-run-2026-08-06.md  Earlier working notes.
  sessions/                   The four 12 August write-ups: handover, deep-dive,
                              blindspot-sweep, session-log.

skill/                        The whole job-hunt skill, verbatim:
                              SKILL.md (the sweep method), references/sources.md
                              (tested search playbook + verification traps),
                              references/application-rules.md, references/candidate-profile.md,
                              assets/motivation-letter.md, agents/ (form-scout, letter-writer,
                              applicant briefs), scripts/build_shortlist.py.

letters/                      All 28 generated motivation letters (PDF).
role-inputs/                  The JSON each letter was generated from — role, opening,
                              role-specific paragraph, closing. Re-render with
                              scripts/make_letter.py.

transcript/                   THE SESSION RECORD. Start with transcript/README.md.
  research-agent-reports.md   **76 research agents' full reports** — every role found,
                              including the ones rejected and why. This is where the
                              shortlists came from.
  subagents/                  106 raw agent transcripts (~33 MB): every search query
                              run and every page fetched.
  session-transcript.md/.jsonl  The main conversation (final stretch — see the README
                              for the compaction caveat).
  tool-results/               PDF page renders opened during the session.

sweeps/                       Raw lead data before filtering: allleads.json, the queue
                              files, roles_aug8.json, applications.csv (~600 rows),
                              APPS_TABLE.md, dedupe-doc.md.

cv-versions/                  cv_original.pdf and the prefix backup, plus the render
                              previews used to check layout. NOT for sending — the one
                              to send is Prabhavit_CV.pdf at the top level.

earlier-sessions/             5–6 August outputs: the first shortlist, "Application
                              answers — ready to paste.md", the original claud-jobs
                              README, job-hunt.skill, work/ (profile-gaps.md,
                              materials-index.md, new-leads CSV), and
                              sweep-2026-08-05/ (the raw rows-A…J sweep files).
raw-logs/                     under75_run.jsonl (12 Aug, 76 rows)
                              applied.jsonl (5–8 Aug, 38 rows)
                              blocked_today.jsonl, coverletter.jsonl, needswords.jsonl
                              DEDUPE.txt — the raw 348-name list
scripts/                      make_letter.py (letter generator), validate.py (CV hash
                              check), build_cv.py, finalize_cv.py, and the 16 sheet-
                              building scripts that produced every tab in the workbooks.
```

## The tabs in `Role shortlist - 8 Aug 2026.xlsx`

| Tab | What |
|---|---|
| **Deep sweep queue** | **16 verified-live roles not yet applied to.** Green = CV-only, can go straight out. Amber = needs you. |
| **Do not repeat** | 348 companies already seen. Check before applying to anything. |
| Applications sent | Colour-coded log with verbatim confirmations |
| Follow up | Every application sent, with company LinkedIn and a suggested angle |
| CV-only queue, FDE focus, Search notes, Shortlist, Raw leads | Working tabs |

## The numbers

- **80 applications submitted** — 38 across 5–8 August, 42 on 12 August
- **11 open**, waiting on something only he can supply
- **16 verified live** and queued, not yet applied to
- **348 companies** on the do-not-repeat list
- **76 research agents** ran; their full reports are in `transcript/research-agent-reports.md`

## Time-sensitive

- **n8n — Forward Deployed Engineer EMEA** unlocks **20 August** (their one-application-per-15-days limit; applied 5 Aug). Possibly the best-fitting role found in any sweep.
- **ElevenLabs** — retry around **19 August** (their own throttle refused submission).

## Note on where the documentation lives

The narrative docs are **also in the Claude project "Job Search"**, which is their live home — they load automatically into any new session, so a new conversation already knows the rules without being told. The copies in `docs/` are for reading offline.

`docs/project-docs-index.md` lists all 27 project docs and says where each one landed in this folder, so nothing in the project is invisible from here. The twenty dated shortlists and run logs from 5–8 August are the only ones not duplicated: every role they name is already a row in the MASTER workbook and every company is already on the "Do not repeat" list.

## Prompt to start a new session

> I'm Prabhavit, continuing my job search. Everything you need is in this project — **read `claude/00-START-HERE.md` first**, then `claude/working-rules.md` before you touch any application form.
>
> - 80 applications are already submitted. Full record in **`MASTER - every application - 12 Aug 2026.xlsx`**.
> - **Never apply to a company on the "Do not repeat" tab** of `Role shortlist - 8 Aug 2026.xlsx` (348 entries). Check every candidate against it first.
> - **16 verified-live roles are already queued** on the "Deep sweep queue" tab — ten are CV-only and can go straight out.
> - My CV is `Prabhavit_CV.pdf`. Attach it to every application, unmodified.
> - Salary: **EUR 40,000–50,000 baseline**, and where a posting discloses a band, align to their number rather than quoting below it.
> - **Only write cover letters and long answers for weak-match roles.** Strong matches go out CV-only — I write those letters myself. If a strong-match form requires a cover letter, hand it to me with the link and the questions.
> - Answer everything from my CV, my own letter, or facts I've told you. **Never invent** a GitHub link, portfolio, referral, demographic answer or biographical detail. State the gap plainly instead.
> - Never create an account, never solve a CAPTCHA, never enter payment or ID details.
> - Nothing counts as submitted without an on-screen confirmation — screenshot it and quote it in the log.
> - UK roles: answer work authorisation honestly as No and apply anyway.
> - Use the in-app browser, not headless — my join.com login lives there.
> - No em dashes.
>
> Time-sensitive: **n8n's FDE EMEA unlocks 20 August**; **ElevenLabs retry ~19 August**.
>
> Today I'd like you to: **[what you want]**
>
> Keep the workbook and project docs updated, and tell me plainly what you decided on my behalf.
