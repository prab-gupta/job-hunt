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

## Access

Use the `tracker` MCP server when it is connected. Call `sync_paths` and `regenerate_needs_you` instead of copying files by hand. `add_row` and `update_row` already sync the three paths. You are still the only agent that commits git. The server does not commit. Do not pass a password into any tool.

If the server is not connected, follow the CSV procedure below: edit the root file, then `sync_tracker.py copy-paths` and `regenerate-view`.

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
| `submitted` | `apply-auditor` found the application confirmation in Gmail |
| `needs_you` | Blocked on a human: captcha, missing fact, eligibility, or no confirmation. A login or account-required ATS row is cleared by `needs-you-drainer`, not left here after a successful account create |
| `skipped` | Closed, dropped, or not a fit |
| `failed` | A submit was attempted and failed |

Map any other incoming status before it is written:

- `sent`, `confirmed`, `applied`, `application_sent` → `needs_you` with blocker `no_confirm` (an incoming label is a claim, not a Gmail confirmation; there is no `confirmed` status, and only `apply-auditor` writes `submitted`)
- `needs_human`, `blocked`, `blocked_by_company`, `held`, `action_required`, `captcha` → `needs_you`
- `skip`, `closed`, `dropped`, `dead`, `dead_link`, `not_a_fit`, `duplicate`, `do_not_apply` → `skipped`
- `submit_failed`, `error` → `failed`

An unknown status becomes `needs_you`. Append `unmapped_status:<original>` to `notes`. Do not map an unknown status to `submitted`. A `needs_you` row needs a blocker from the six-value vocabulary. If the incoming row has none, use `no_confirm` for the unconfirmed labels above and `other` otherwise, and keep the original token in `notes`.

## Dedupe

Key: if `url` is non-empty, lowercase it, drop the fragment, strip the trailing slash, and drop tracking/language query parameters (`utm_*`, `ref`, `source`, `lang`, `language`, `locale`, `gclid`, `fbclid` and the like). KEEP job-identifying parameters (`gh_jid`, `jid`, `id`, `job`, `jobid`, `requisition`, `reqid`, `jk`, `ashby_jid` and the like): `jobs?gh_jid=1` and `jobs?gh_jid=2` are different jobs. The Greenhouse embed form keeps `for` and `token`. If `url` is empty, use company + role, case-insensitive, with whitespace collapsed. `dedupe_key` in `sync_tracker.py` is the proof. `check` reports any remaining duplicate keys.

Never add a second row for an existing key. Before saving, merge rows that share a key. Keep the most advanced status: `submitted`, then `needs_you`, then `failed`, then `skipped`. Combine `notes`. Keep a non-empty `date_applied`, `fit_score`, and `salary_or_rate` from the other row when the winner's cell is empty. Put the other raw URL in `notes` as `also_url:` when it differs. Never reapply a `submitted` or `skipped` row. An existing `needs_you` or `failed` row may be updated in place.

`needs_you` blockers use this vocabulary only: `login`, `upload`, `eligibility`, `no_confirm`, `other`, `captcha`. `login` covers an ATS account or sign-in. Keep the old blocker text, and the exact missing fact or condition, in `notes` when you replace it. An ATS-accepted application awaiting email is `needs_you` + `no_confirm`. Do not mark a row `skipped` as closed or expired unless that row's own `notes` or `blocker` says the posting is closed, not accepting, or gives a deadline that has passed. Do not guess. A login or account-creation gate is `needs_you` / `login`, not `skipped`.

On a live apply, only `apply-auditor` sets `submitted`, and only after a Gmail application confirmation (`audit_confirm`). A thanks page stays `needs_you`. If that mail is missing, the auditor sets `needs_you` with blocker `no_confirm` (`audit_missing`). The status map above is for incoming labels on a new row. It does not promote a `needs_you` row to `submitted`.

Never write `JOBS_ACCOUNT_PASSWORD`, any other password, a verification code, or a reset link into the CSV, `notes`, `blocker`, or `docs/needs-you.md`. Account creation is logged as one fact line in `notes`, such as `account created, verified via Gmail 2026-10-02`. Do not add an accounts CSV. The same environment variable is reused for every portal. Do not store a generated per-account password.

Leave `salary_or_rate` blank unless the posting or the submitted form stated a figure. The form amounts in `AGENT-INSTRUCTIONS.md` section 3 are for forms, not invented CSV salary claims.

## Write

With the MCP server connected, the server owns its per-operation lock; do not create `loop/.applications.lock` yourself. Only in the direct-CSV fallback, hold `loop/.applications.lock` (see `coordinator`) before writing. No other agent edits the CSV during the write.

1. Edit root `applications.csv` only, with the `csv` module, UTF-8, the header above.
2. Run `python3 .claude/skills/tracker-keeper/sync_tracker.py copy-paths`.
3. Run `python3 .claude/skills/tracker-keeper/sync_tracker.py regenerate-view`.
4. Run `check` again. Report row counts per status.

`docs/needs-you.md` is a view of `status=needs_you`, grouped by blocker type. Login/account rows the drainer can clear are first. Captcha rows are last. The You column is one line for Prabhavit only where a human must act. Do not edit the view by hand. Do not treat it as a database. Regenerate it with `sync_tracker.py regenerate-view` after every CSV write. `streamline` merges duplicate keys, reclassifies blockers, copies the three CSV paths, and regenerates the view.

## Proof pass

When asked to prove the tracker, run `check`. It does not add or remove rows. A duplicate key, including two URLs that differ only by `?language=` or any other query string, is a failure until `streamline` merges them. `streamline` is the edit that merges keys, reclassifies `needs_you` blockers, and reopens a skip whose own text says the only gate was account creation.

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
