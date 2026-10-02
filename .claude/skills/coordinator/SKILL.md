---
name: coordinator
description: >
  Use this to route a job-search pass. Sweeper adds rows, needs-you-drainer
  works blockers, apply-auditor checks mail, and tracker-keeper is the only
  writer that commits. No agent edits applications.csv while another is
  writing it.
---

# Coordinator

`applications.csv` is the only application tracker. Route work to the other four skills. Do not scrape, apply, or audit in this skill.

| Step | Skill | Does |
| --- | --- | --- |
| 1 | `sweeper` | Finds roles, rejects existing keys, hands new `needs_you` or `skipped` rows onward. Does not apply. |
| 2 | `needs-you-drainer` | Works `docs/needs-you.md` from the top, one try per blocker. |
| 3 | `apply-auditor` | Runs only after a real submit. Checks Gmail. |
| 4 | `tracker-keeper` | Dedupes, maps status, writes the three CSV paths, regenerates `docs/needs-you.md`, commits. |

`tracker-keeper` is the only writer that commits. The other skills read `applications.csv` first and do not keep a side list.

## One writer

Before any CSV write, create `loop/.applications.lock` with exclusive create. The file contents are the agent name, the UTC time, and the pid. If the lock already exists, stop. Do not delete it and do not write the CSV. A lock older than two hours is stale: report it and stop. Prabhavit removes a stale lock.

Release the lock only after `tracker-keeper` has copied the three paths and regenerated the view. Never commit `loop/.applications.lock`.

No agent edits the CSV while another holds the lock. Browser work is one agent at a time, attached to Chrome at `127.0.0.1:9222`. Never launch a new Chrome.

## Pass order

1. Acquire the lock.
2. Sweeper proposes rows. Drop any key already in the CSV. Do not reopen `submitted` or `skipped`.
3. Tracker-keeper appends the survivors, copies the three paths, regenerates `docs/needs-you.md`.
4. Drainer starts at the top of the view. One try per row.
5. After a real submit, auditor checks Gmail before the commit. No confirmation means `needs_you` / `no_confirm`, not `submitted`.
6. Tracker-keeper commits. On a cloud checkout that commit stays on the working branch and opens a pull request against `main`. Never force-push. Never push `main` from a cloud agent.
7. Delete the lock.

## Standing limits

Read `AGENT-INSTRUCTIONS.md` sections 2-5 before a form. Do not invent experience, salary, notice period, or visa claims. LinkedIn and GitHub URLs start with `https://`. Required text fields stay filled. On a captcha, stop and hand it to Prabhavit.

## Do not touch

`.claude/skills/job-application-assistant/01-candidate-profile.md`, `loop/outreach.csv`, `loop/queue.csv`, `scripts/apply_easy_apply.js`, and untracked CVs under `cv/`.
