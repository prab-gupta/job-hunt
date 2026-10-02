---
name: sweeper
description: >
  Use this when finding new roles that match Prabhavit's profile. Read
  applications.csv first, reject anything already tracked, and add survivors
  as needs_you or skipped with a real blocker or reason. Do not apply.
---

# Sweeper

Find new roles. Do not open an application form and do not submit.

## Read first

1. Read `applications.csv` and build the dedupe set with `.claude/skills/tracker-keeper/sync_tracker.py` (`dedupe_key`).
2. Read `AGENT-INSTRUCTIONS.md` sections 2-5 for identity, salary-for-forms, target tracks, and hard gates. Do not invent experience, salary, notice period, or visa claims.
3. `docs/needs-you.md` is a view. Do not add rows there yourself.

## Search

Use the portal skills already in the repo (`.claude/skills/job-scraper` and `.agents/skills/*-search`). A hit is a company, a role, a URL, and a source. Skip a hit you cannot name.

## Accept or reject

For each hit, compute the dedupe key: normalized URL (lowercase, strip query string and trailing slash), or company + role when there is no URL (case-insensitive, whitespace collapsed).

- If the key is already in `applications.csv`, reject it. Do not update that row and do not add a second one. Never reapply a `submitted` or `skipped` row.
- Hard gate from section 4 (degree wall, 5+ years, missing language, unnamed aggregator, ML research, unpaid or talent pool): add `status=skipped` with a real blocker such as `not_a_fit: 5+ years` or `not_a_fit: unnamed aggregator`. The reason must be a fact from the posting.
- Posting closed or gone: `status=skipped`, blocker `closed`, and the page fact in `notes`.
- A posting that matches the profile and is still open: `status=needs_you`, blocker `needs_apply`. `notes` may quote a requirement from the JD. Do not claim he has a skill the profile does not list.

Fill every column. `date_added` is the day you add the row. Leave `date_applied` empty. Leave `salary_or_rate` empty unless the posting states a figure. `fit_score` stays empty unless you scored the JD against the written profile.

## Write

Do not commit. Pass the new rows to `tracker-keeper`, which is the only writer that updates the three CSV paths, regenerates `docs/needs-you.md`, and commits.

Do not edit the CSV while another agent holds `loop/.applications.lock`. If you must write before the keeper runs, write root `applications.csv` and then run `sync_tracker.py copy-paths` and `regenerate-view`. No other tracker file.

## Do not touch

`.claude/skills/job-application-assistant/01-candidate-profile.md`, `loop/outreach.csv`, `loop/queue.csv`, `scripts/apply_easy_apply.js`, and untracked CVs under `cv/`.
