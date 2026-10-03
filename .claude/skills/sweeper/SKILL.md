---
name: sweeper
description: >
  Use this when finding new roles that match Prabhavit's profile. Read
  applications.csv first, reject anything already tracked, and add survivors
  as needs_you or skipped with a real blocker or reason. Do not apply.
---

# Sweeper

Find new roles. Do not open an application form and do not submit.

## Access

Use the `tracker` MCP server when it is connected. `search_rows` before you add anything. `add_row` rejects a duplicate normalized key. Do not pass a password into any tool.

If the server is not connected, read `applications.csv` and dedupe with `dedupe_key` as below, then hand new rows to `tracker-keeper`.

## Read first

1. Read the tracker (MCP `search_rows` / `stats`, or `applications.csv` if the server is down) and build the dedupe set with `dedupe_key`.
2. Read `AGENT-INSTRUCTIONS.md` sections 2-5 for identity, salary-for-forms, target tracks, and hard gates. Do not invent experience, salary, notice period, or visa claims.
3. `docs/needs-you.md` is a view. Do not add rows there yourself.

## Search

Use the portal skills already in the repo (`.claude/skills/job-scraper` and `.agents/skills/*-search`). A hit is a company, a role, a URL, and a source. Skip a hit you cannot name.

Also work the boards and ATS hosts in `skill/job-hunt/references/sources.md` §2, §4 and §4b. Run at least one query per Tier-1 board per sweep. hiring.cafe and EURES must go through the browser agent, never curl.

## Accept or reject

For each hit, compute the dedupe key with `dedupe_key`: normalized URL (lowercase, drop the fragment, strip the trailing slash, drop tracking/language params such as `?language=`/`utm_*`, but keep job-identifying params such as `gh_jid`, `jid`, `id`, `job`, `requisition`), or company + role when there is no URL (case-insensitive, whitespace collapsed).

- If the key is already in `applications.csv`, reject it. Do not update that row and do not add a second one. Never reapply a `submitted` or `skipped` row. A `?language=` twin is the same key.
- Hard gate from section 4 (degree wall, 5+ years, missing language, unnamed aggregator, ML research, unpaid or talent pool): add `status=skipped` with a real blocker such as `not_a_fit: 5+ years` or `not_a_fit: unnamed aggregator`. The reason must be a fact from the posting.
- Posting closed or gone: `status=skipped`, blocker `closed`, and the page fact in `notes`. Do not mark a posting closed unless the page says so.
- Login wall or account required on an ATS, and the posting is otherwise in scope: `status=needs_you`, blocker `login`. Do not skip it. The drainer can create that account.
- A posting that matches the profile and is still open, with no tighter gate: `status=needs_you`, blocker `other`. `notes` may quote a requirement from the JD. Do not claim he has a skill the profile does not list.

Fill every column. `date_added` is the day you add the row. Leave `date_applied` empty. Leave `salary_or_rate` empty unless the posting states a figure. `fit_score` stays empty unless you scored the JD against the written profile.

## Write

Do not commit. Pass the new rows to `tracker-keeper`, which is the only writer that updates the three CSV paths, regenerates `docs/needs-you.md`, and commits.

With the MCP server connected it owns its lock; do not touch `loop/.applications.lock`. In the direct-CSV fallback, do not edit the CSV while another agent holds it. If you must write before the keeper runs, write root `applications.csv` and then run `sync_tracker.py copy-paths` and `regenerate-view`. No other tracker file.

## Do not touch

`.claude/skills/job-application-assistant/01-candidate-profile.md`, `loop/outreach.csv`, `loop/queue.csv`, `scripts/apply_easy_apply.js`, and untracked CVs under `cv/`.
