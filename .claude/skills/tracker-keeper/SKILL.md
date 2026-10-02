---
name: tracker-keeper
description: >
  Use this when deduping applications, mapping a row into needs_you, submitted,
  skipped, or failed, copying the tracker to its three paths, regenerating
  docs/needs-you.md, or committing tracker changes. applications.csv is the
  only application tracker. This skill is the only writer that commits.
---

# Tracker keeper

You own `applications.csv` and the generated view `docs/needs-you.md`. No other file is an application list. Do not start a second tracker, CSV, or spreadsheet.

`data/csvs/applications.csv` and `loop/applications.csv` are byte copies of the root file. Write the root file, then copy those bytes onto the other two. Use `.claude/skills/tracker-keeper/sync_tracker.py`.

## Read first

1. Read `applications.csv` before any edit.
2. Run `python3 .claude/skills/tracker-keeper/sync_tracker.py check`.
3. If the three paths are not byte-identical, stop and report the three sha256 values. Do not pick a winner and do not copy one over the others.
4. Candidate facts, salary figures for forms, and hard gates are in `AGENT-INSTRUCTIONS.md` sections 2-5. Do not invent experience, salary, notice period, or visa claims. Facts in a row belong in `notes` and `blocker` only.

## Columns

Keep this header, in order:

`company, role, url, source, status, fit_score, date_added, date_applied, salary_or_rate, notes, blocker`

`status` may only be `needs_you`, `submitted`, `skipped`, or `failed`.

| Status | Meaning |
| --- | --- |
| `submitted` | The application was sent or a confirmation email was found |
| `needs_you` | Blocked on a human: captcha, login, upload, eligibility, or no confirmation |
| `skipped` | Closed, dropped, or not a fit |
| `failed` | A submit was attempted and failed |

Map any other incoming status before it is written:

- `sent`, `confirmed`, `applied`, `application_sent` → `submitted`
- `needs_human`, `blocked`, `blocked_by_company`, `held`, `action_required`, `captcha` → `needs_you`
- `skip`, `closed`, `dropped`, `dead`, `dead_link`, `not_a_fit`, `duplicate`, `do_not_apply` → `skipped`
- `submit_failed`, `error` → `failed`

An unknown status becomes `needs_you`. Append `unmapped_status:<original>` to `notes`. Do not map an unknown status to `submitted`. A `needs_you` row needs a blocker. If the incoming row has none, use the original status token, or `needs_human` when that token is empty.

## Dedupe

Key: if `url` is non-empty, lowercase it, drop the query string and the fragment, and strip the trailing slash. If `url` is empty, use company + role, case-insensitive, with whitespace collapsed.

Never add a second row for an existing key. Never reapply a `submitted` or `skipped` row. An existing `needs_you` or `failed` row may be updated in place. `apply-auditor` may add a Gmail subject and time to a `submitted` row, or set that row back to `needs_you` with blocker `no_confirm`.

Leave `salary_or_rate` blank unless the posting or the submitted form stated a figure. The form amounts in `AGENT-INSTRUCTIONS.md` section 3 are for forms, not invented CSV salary claims.

## Write

Hold `loop/.applications.lock` (see `coordinator`) before writing. No other agent edits the CSV during the write.

1. Edit root `applications.csv` only, with the `csv` module, UTF-8, the header above.
2. Run `python3 .claude/skills/tracker-keeper/sync_tracker.py copy-paths`.
3. Run `python3 .claude/skills/tracker-keeper/sync_tracker.py regenerate-view`.
4. Run `check` again. Report row counts per status.

`docs/needs-you.md` is a view of `status=needs_you` in CSV order. Do not edit it by hand. Do not treat it as a database.

## Proof pass

When asked to prove the tracker, run `check` only. Do not add, remove, or change application rows. If the check finds a bad header, a bad status, a hash mismatch, or a duplicate key, report it and stop. Do not silent-fix those rows.

If the only problem is that `docs/needs-you.md` is out of date relative to the CSV, run `regenerate-view`, run `check` again, and say so. Then report the row counts per status.

## Commit

You are the only agent that commits tracker changes. No AI attribution and no `Co-Authored-By` trailer.

On Prabhavit's machine, commit and push `main` with a normal push. Never force-push.

In a cloud checkout, do not push `main`. Commit the working branch and open a pull request against `main` so his local checkout and GitHub `main` can stay in sync.

## Do not touch

These are local uncommitted edits on Prabhavit's machine when they appear:

- `.claude/skills/job-application-assistant/01-candidate-profile.md`
- `loop/outreach.csv`
- `loop/queue.csv`
- `scripts/apply_easy_apply.js`
- untracked CVs under `cv/`
