---
name: apply-auditor
description: >
  Use this only after an ATS accept. Check Gmail for that company's application
  confirmation. You are the only skill that sets submitted, and only when that
  mail is present. If it is not, set needs_you with blocker no_confirm. Never
  mark submitted from a thanks page.
---

# Apply auditor

## Access

Use the `tracker` MCP server when it is connected. You are the only caller that may set `submitted`. Call `update_row` with `actor` `apply-auditor`, `notes` containing `gmail: <subject> @ <time>`, and `date_applied` set from that message. If the mail is missing, set `needs_you` and blocker `no_confirm` with the same actor. Do not pass a password into a tool.

If the server is not connected, find the row in `applications.csv` and hand the same change to `tracker-keeper`.

## Retrieval route for `no_confirm` rows

`next_needs_you` never returns `no_confirm` rows, so the drainer will not hand them to you. After each application batch, fetch them yourself: `search_rows` with `status=needs_you` and `blocker=no_confirm`. Read the ATS-acceptance evidence in each row's `notes`. Then run the Gmail check below for each row. Do not resubmit a role merely because its email is missing. Match account-verification mail and application-confirmation mail separately, using the role or requisition and a time window that starts at the acceptance time.

Run only for rows that `needs-you-drainer` left at `needs_you` / `no_confirm` after an ATS accept, or a row that is already `submitted` and needs the confirmation checked. A thanks page, a redirect, or an agent saying "submitted" is not a confirmation.

Read the tracker first and find the row by dedupe key (normalized URL, or company + role when there is no URL).

If the row is `skipped`, stop. Do not reapply it. Do not promote a `needs_you` row that is still a captcha, a login, or a missing fact. Those stay with the drainer.

You are the only skill that sets `submitted`. Set it only when the Gmail confirmation is present.

## Gmail

Search the connected Gmail account (`prabhavitg@gmail.com`) with `search_threads`. This is the application confirmation, not the account-verification mail the drainer already used. Query the company name plus application words. Example shape:

`to:prabhavitg@gmail.com newer_than:14d "<company>" (application OR applied OR thank OR received OR candidature)`

Read the matching message. A confirmation is role-specific mail: its subject or body is about this application, this role, or this requisition. An unrelated message that merely contains the company name is not a confirmation. An account-verification mail is not an application confirmation. If the match is ambiguous, treat it as missing.

## Result

| Mail | CSV |
| --- | --- |
| Application confirmation present | Set `status=submitted`. Set `date_applied` from the message date. Append `gmail: <subject> @ <message time>` to `notes`. Copy the subject and time from the message. Clear `blocker`. |
| Not present, or ambiguous | Set `status=needs_you` and `blocker=no_confirm`. In `notes`, say that Gmail had no application confirmation for this company. |

Do not invent a subject, a timestamp, or a salary. Do not mark `submitted` because a thanks page was visible. Do not write a password or a verification code into `notes`.

## Write

Do not commit. Pass the row to `tracker-keeper` with operation `audit_confirm` or `audit_missing`. The keeper writes root `applications.csv`, copies it to `data/csvs/applications.csv` and `loop/applications.csv`, regenerates `docs/needs-you.md`, and commits. With the MCP server connected it owns the lock; do not touch `loop/.applications.lock`. Only in the direct-CSV fallback, do not edit the CSV while another agent holds it.

## Do not touch

`.claude/skills/job-application-assistant/01-candidate-profile.md`, `loop/outreach.csv`, `loop/queue.csv`, `scripts/apply_easy_apply.js`, and untracked CVs under `cv/`.
