---
name: needs-you-drainer
description: >
  Use this when working blocked applications in docs/needs-you.md from the top,
  end to end. For a login or account-required ATS blocker, create the portal
  account with the one shared JOBS_ACCOUNT_PASSWORD, verify it from Gmail, and
  continue the application. Leave needs_you on a captcha or a missing fact.
  Do not mark submitted. apply-auditor does that only after a Gmail confirmation.
---

# Needs-you drainer

Work `docs/needs-you.md` from the top, end to end, so a `needs_you` row can actually be cleared. That file is a view of `applications.csv` rows with `status=needs_you`, grouped by blocker. Login/account rows you can clear are first. Captcha rows are last. Read the CSV row before you touch the posting. If the CSV status is no longer `needs_you`, skip the view row.

Blocker vocabulary is `login`, `upload`, `eligibility`, `no_confirm`, `other`, `captcha`. A `login` row in the first section is an ATS account: create it or sign in with the one shared password, verify from Gmail, and continue. A `login` row in the human sign-in section stays `needs_you`; the You line says what Prabhavit must do. A `captcha` row stays `needs_you`. Do not try it.

Try each blocker once per pass, then move down. Do not retry the same row in the same pass. Do not reapply a `submitted` or `skipped` row.

You do not mark `submitted`. After the ATS accepts an application, leave `needs_you` with blocker `awaiting_confirm` and hand the row to `apply-auditor`. Only that skill sets `submitted`, and only after a Gmail confirmation.

## Password

Reuse the one password in `JOBS_ACCOUNT_PASSWORD` for every portal account. Do not generate a password per account. Do not invent a second password.

Read it only from the environment variable `JOBS_ACCOUNT_PASSWORD`. If that variable is unset, read the gitignored file `.secrets/job-accounts.env`, which may set the same variable and nothing else. Do not echo the value. Do not cat the file into the transcript, the CSV, `notes`, `blocker`, `docs/needs-you.md`, a commit, or a PR.

If neither source is set, stop that row. Leave `status=needs_you` and blocker `account_password_unset`. In `notes`, say that Prabhavit must set `JOBS_ACCOUNT_PASSWORD`. Do not write a password.

Never write the password, or any other credential, into a git-tracked file, the CSV, `notes`, `blocker`, `docs/needs-you.md`, a commit message, or a PR. The account log is one short line in that row's `notes`, not a second CSV.

## Account creation

When the blocker is login or account required on an ATS (Workday and similar email-and-password portals):

1. Create the account, or sign in if it already exists, with `prabhavitg@gmail.com` from `AGENT-INSTRUCTIONS.md` and the one shared password.
2. Check Gmail the way `AGENTS.md` says: do not ask Prabhavit. Search for that company's verification or security code, open the verify link or enter the code, then resume the application.
3. Append a note with no secrets, for example `account created, verified via Gmail 2026-10-02`. Use the real date from the message. Do not record the password, the code, or a reset link.

Do not create a LinkedIn, Google, or GitHub account. If the only path is "Apply with Google" or "Apply with LinkedIn", leave `needs_you` and write that OAuth step for Prabhavit.

## Before a form

Follow the apply rules already in this repo:

1. Read the job description.
2. Tailor a CV in `cv/main_<Company>_<Role>.tex`. Edit only the headline, the three career-summary lines, and the skills block. Compile with `tectonic`. `pdfinfo` must show 2 pages.
3. Upload that new PDF. Do not upload a generic CV.
4. LinkedIn is `https://www.linkedin.com/in/prabhavit/`. GitHub is `https://github.com/prab-gupta`. Both start with `https://`.
5. Do not leave a required text field blank. Optional consent stays unchecked. Phone is `+39 351 610 7807`.
6. Form salary, notice, and work authorization come from `AGENT-INSTRUCTIONS.md` sections 2-3. Do not invent experience, salary, notice period, or visa claims. If a required answer is not in those facts, stop. Leave `needs_you` and set `blocker` to the missing fact, such as `missing_fact: visa sponsorship answer not in profile`. Anti-AI screening questions go back to Prabhavit unanswered.

One browser agent at a time. Attach to the Chrome already running at `127.0.0.1:9222`. Never launch a new Chrome, a new window, or a headless browser. If that port is closed, stop. Leave `status=needs_you` and write that Chrome at `127.0.0.1:9222` was not available.

## After one try

| What happened | Write this |
| --- | --- |
| Captcha or an "I am human" check | Stop. Keep `needs_you`. Do not bypass or solve it. Set `blocker` to `captcha`. In `notes`, say what Prabhavit must do and on which URL. |
| Required answer is not in the candidate facts | Keep `needs_you`. Set `blocker` to the missing fact. Do not invent it. |
| Missing document (diploma, reference, signed letter) | Keep `needs_you`. Set `blocker` to `missing_document` and name the file. |
| Thanks page only, or the form is still open | Keep `needs_you`. Do not call it submitted. |
| The ATS accepted the application (application id, explicit acceptance, or the ATS create call succeeded) | Keep `needs_you`. Set `blocker` to `awaiting_confirm`. Put the acceptance fact in `notes`. Hand the row to `apply-auditor`. |
| Submit was attempted and the ATS rejected it | Set `failed` and put the ATS error in `notes`. No credentials. |

## Write

Do not commit. Pass the row change to `tracker-keeper`. The only CSV write is root `applications.csv`, then `sync_tracker.py copy-paths` and `regenerate-view`. Do not edit the CSV while another agent holds `loop/.applications.lock`. Do not add an accounts CSV.

## Do not touch

`.claude/skills/job-application-assistant/01-candidate-profile.md`, `loop/outreach.csv`, `loop/queue.csv`, `scripts/apply_easy_apply.js`, and untracked CVs under `cv/`.
