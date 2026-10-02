---
name: apply-auditor
description: >
  Use this only after a submit. Check Gmail for that company's confirmation.
  Keep submitted and store the subject and time when the mail is there. If it
  is not, set needs_you with blocker no_confirm. Never mark submitted from a
  thanks page.
---

# Apply auditor

Run only after a submit. A thanks page, a redirect, or an agent saying "submitted" is not a confirmation. Read `applications.csv` first and find the row by dedupe key (normalized URL, or company + role when there is no URL).

If the row is `skipped`, stop. Do not reapply it. If the row is not `submitted`, do not promote it from a thanks page. Leave it for `needs-you-drainer`.

## Gmail

Search the connected Gmail account (`prabhavitg@gmail.com`) with `search_threads`. Query the company name plus application words, limited to mail after `date_applied` when that date is set. Example shape:

`to:prabhavitg@gmail.com newer_than:14d "<company>" (application OR applied OR thank OR received OR candidature)`

Read the matching message. A confirmation is mail whose subject or body is about this application or this role. An unrelated message that merely contains the company name is not a confirmation. If the match is ambiguous, treat it as missing.

## Result

| Mail | CSV |
| --- | --- |
| Confirmation present | Keep `status=submitted`. Append `gmail: <subject> @ <message time>` to `notes`. Copy the subject and time from the message. |
| Not present, or ambiguous | Set `status=needs_you` and `blocker=no_confirm`. In `notes`, say that Gmail had no confirmation for this company after the submit. |

Do not invent a subject, a timestamp, or a salary. Do not mark `submitted` because a thanks page was visible.

## Write

Do not commit. Pass the row to `tracker-keeper`, which writes root `applications.csv`, copies it to `data/csvs/applications.csv` and `loop/applications.csv`, regenerates `docs/needs-you.md`, and commits. Do not edit the CSV while another agent holds `loop/.applications.lock`.

## Do not touch

`.claude/skills/job-application-assistant/01-candidate-profile.md`, `loop/outreach.csv`, `loop/queue.csv`, `scripts/apply_easy_apply.js`, and untracked CVs under `cv/`.
