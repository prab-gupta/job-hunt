---
name: coordinator
description: >
  Use this to route a job-search pass end to end. Sweeper adds rows,
  needs-you-drainer clears blockers (including ATS account creation with the
  one shared JOBS_ACCOUNT_PASSWORD), apply-auditor checks Gmail before any
  row is submitted, and tracker-keeper is the only writer that commits.
---

# Coordinator

`applications.csv` is the only application tracker. Route work to the other four skills. Do not scrape, apply, or audit in this skill. Do not keep a second list of accounts or applications.

## Access

When the `tracker` MCP server is connected, every read and write goes through it. `next_needs_you` is the claim that stops two drainers taking the same row. The server owns its own per-operation lock: it creates `loop/.applications.lock` for the length of one `next_needs_you`, `add_row`, `update_row` or `release_claim` and removes it again. The coordinator must NOT create that file around a pass, because the server would then refuse every operation with "tracker lock held". Agents do not edit the CSV while that lock is held. `tracker-keeper` is still the only skill that commits git. Passwords are not tool arguments.

If the server is not connected, fall back to the CSV procedure in each skill. The three paths stay byte-identical.

| Step | Skill | Does |
| --- | --- | --- |
| 1 | `sweeper` | Finds roles, rejects existing keys, hands new `needs_you` or `skipped` rows onward. Does not apply. |
| 2 | `needs-you-drainer` | Works `docs/needs-you.md` from the top, end to end. Creates or signs into an ATS account when the blocker is login or account required, then continues the application. |
| 3 | `apply-auditor` | Runs after an ATS accept. Sets `submitted` only when Gmail has the confirmation. |
| 4 | `tracker-keeper` | Dedupes, maps status, writes the three CSV paths, regenerates `docs/needs-you.md`, commits. |

`tracker-keeper` is the only writer that commits. The other skills use the `tracker` MCP server first and do not keep a side list. They read `applications.csv` only when that server is down.

## One writer (direct-CSV fallback only)

This manual lock applies only when the `tracker` MCP server is NOT connected and agents write the CSV directly. With the server connected, skip this section and the acquire/delete steps in the pass order: the server locks each operation itself. Never delete a lock you did not create.

Before any direct CSV write, create `loop/.applications.lock` with exclusive create. The file contents are the agent name, the UTC time, and the pid. If the lock already exists, stop. Do not delete it and do not write the CSV. A lock older than two hours is stale: report it and stop. Prabhavit removes a stale lock.

Release the lock only after `tracker-keeper` has copied the three paths and regenerated the view. Never commit `loop/.applications.lock` or anything under `.secrets/`.

No agent edits the CSV while another holds the lock. Browser work is one agent at a time, attached to Chrome at `127.0.0.1:9222`. Never launch a new Chrome.

## Pass order

1. MCP connected: no outer lock, start at step 2. Direct-CSV fallback: acquire `loop/.applications.lock`.
2. Sweeper proposes rows. Drop any key already in the CSV. Do not reopen `submitted` or `skipped`.
3. Tracker-keeper appends the survivors, copies the three paths, regenerates `docs/needs-you.md`.
4. Drainer claims with `next_needs_you`, one try per row, and releases the claim. Parked-question rows are not in that queue. On a login or account-required ATS blocker, it creates or reuses the portal account with the one password in `JOBS_ACCOUNT_PASSWORD`, verifies via Gmail, and continues. It does not generate a password per portal.
5. Drainer does not set `submitted`. After a real ATS accept it keeps `needs_you` with blocker `no_confirm` and the acceptance evidence in `notes`.
6. After each batch, the auditor runs its own retrieval route: `search_rows` with `status=needs_you` and `blocker=no_confirm`, then Gmail for a role-specific confirmation. A confirmation sets `submitted`, `date_applied`, and `gmail: <subject> @ <time>` in `notes`. No confirmation leaves `needs_you` / `no_confirm`. A thanks page is not enough. Do not resubmit a role just because its email is missing. There is no `confirmed` status.
7. Tracker-keeper commits. On a cloud checkout that commit stays on the working branch and opens a pull request against `main`. Never force-push. Never push `main` from a cloud agent.
8. Direct-CSV fallback only: delete the lock you created. With the server connected, call `sync_paths` and `regenerate_needs_you` once as the batch proof.

## Standing limits

Read `AGENT-INSTRUCTIONS.md` sections 2-5 before a form. Do not invent experience, salary, notice period, or visa claims. If a required answer is not in those facts, the drainer leaves `needs_you` with blocker `eligibility` or `other` and writes the exact missing fact in `notes`. Blockers are only `login`, `upload`, `eligibility`, `no_confirm`, `other`, `captcha`. LinkedIn and GitHub URLs start with `https://`. Required text fields stay filled.

On a captcha or an "I am human" check, stop and hand it to Prabhavit. Do not bypass or solve it.

The password is only the name `JOBS_ACCOUNT_PASSWORD` (or the gitignored file `.secrets/job-accounts.env` that sets it). The same value is reused for every portal. Never write it into the CSV, `notes`, `blocker`, `docs/needs-you.md`, a commit, or a PR.

## Do not touch

`.claude/skills/job-application-assistant/01-candidate-profile.md`, `loop/outreach.csv`, `loop/queue.csv`, `scripts/apply_easy_apply.js`, and untracked CVs under `cv/`.
