---
name: needs-you-drainer
description: >
  Use this when working blocked applications in docs/needs-you.md from the top.
  Try each blocker once. Leave needs_you when a human must act. Set submitted
  only after a real submit, with date_applied and a confirmation note.
---

# Needs-you drainer

Work `docs/needs-you.md` from the top. That file is a view of `applications.csv` rows with `status=needs_you`, in CSV order. Read the CSV row before you touch the posting. If the CSV status is no longer `needs_you`, skip the view row.

Try each blocker once per pass, then move down. Do not retry the same row in the same pass. Do not reapply a `submitted` or `skipped` row.

## Before a form

Follow the apply rules already in this repo:

1. Read the job description.
2. Tailor a CV in `cv/main_<Company>_<Role>.tex`. Edit only the headline, the three career-summary lines, and the skills block. Compile with `tectonic`. `pdfinfo` must show 2 pages.
3. Upload that new PDF. Do not upload a generic CV.
4. LinkedIn is `https://www.linkedin.com/in/prabhavit/`. GitHub is `https://github.com/prab-gupta`. Both start with `https://`.
5. Do not leave a required text field blank. Optional consent stays unchecked. Phone is `+39 351 610 7807`.
6. Form salary, notice, and work authorization come from `AGENT-INSTRUCTIONS.md` sections 2-3. Do not invent a different notice period, visa, or salary. Anti-AI screening questions go back to Prabhavit unanswered.

One browser agent at a time. Attach to the Chrome already running at `127.0.0.1:9222`. Never launch a new Chrome, a new window, or a headless browser. If that port is closed, stop. Leave `status=needs_you` and write that Chrome at `127.0.0.1:9222` was not available.

## After one try

| What happened | Write this |
| --- | --- |
| Captcha, login wall, or a missing document | Keep `needs_you`. Set `blocker` to the gate (`captcha`, `login`, `missing_document`). In `notes`, say what Prabhavit must do, on which URL, and which file is missing. Do not submit. |
| Thanks page only, or the form is still open | Keep `needs_you`. Do not call it submitted. |
| The ATS accepted the application (application id, explicit acceptance, or the ATS create call succeeded) | Set `submitted`, set `date_applied` to that UTC date, and put the acceptance fact in `notes`. Then stop and hand the row to `apply-auditor`. |
| Submit was attempted and the ATS rejected it | Set `failed` and put the ATS error in `notes`. |

A captcha stops the pass on that row. Hand it to Prabhavit. Do not solve it.

## Write

Do not commit. Pass the row change to `tracker-keeper`. The only CSV write is root `applications.csv`, then `sync_tracker.py copy-paths` and `regenerate-view`. Do not edit the CSV while another agent holds `loop/.applications.lock`.

## Do not touch

`.claude/skills/job-application-assistant/01-candidate-profile.md`, `loop/outreach.csv`, `loop/queue.csv`, `scripts/apply_easy_apply.js`, and untracked CVs under `cv/`.
