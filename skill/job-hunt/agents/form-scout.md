> **SUPERSEDED for autonomous runs.** For autonomous application runs, `AGENT-INSTRUCTIONS.md` and the `needs-you-drainer` skill (`.claude/skills/needs-you-drainer/SKILL.md`) are the authority. Where this file conflicts with them, they win. In particular, ignore here: per-application approval prompts, "Best guess" or any guessed factual answer (park the row instead with the exact missing fact), the ban on ATS account creation (authorized with the one shared `JOBS_ACCOUNT_PASSWORD`), the old salary figure and "unmodified base CV" rule (see `AGENT-INSTRUCTIONS.md` section 3), and any parallel, headless or newly launched browser or "form scout" (browser work is strictly sequential, one existing tab, existing Chrome at `127.0.0.1:9222`). This file remains valid only for manual, interactive sessions where Prabhavit is present.

# Agent: form-scout

Opens one application form and reports exactly what it demands. Cheap, read-only, and the step
that stops the expensive agent wasting its budget on a dead posting.

Spawn one per role, in parallel. Give it: the company, the role title, and the posting URL.

## Instructions to give the agent

> Open this application form and report what it requires. Do not fill anything in and do not
> submit anything.
>
> - Company / role / URL: `<…>`
> - For an Ashby URL, add `/application` to reach the form. Strip `?embed=js`, `/application/…`, `?utm_data=…` and `?locationId=…` first.
> - For Greenhouse, the form is on the posting page — click "Apply" if the fields aren't rendered.
>
> Read the whole form, then report:
>
> 1. **Status** — one of: `LIVE`, `CLOSED` (the URL serves a board index, a 404, "job not found", or "no longer active"), or `GATED` (needs an account, a CAPTCHA, or a work authorisation he doesn't have).
> 2. **Every required field, quoted verbatim.** Question wording matters — he answers these himself when they need judgement.
> 3. **Classification** — `BASIC` (name, email, phone, location, CV, links, plus yes/no or dropdown questions only) or `NEEDS-WRITING` (any free-text question, essay, or cover-letter field).
> 4. **Gates** — anything that rules him out: UK/US/Swiss work authorisation, a mandatory on-site commute, a language other than English, 7+ years or staff/principal level, an application deadline in the past.
> 5. **Disclosed compensation**, if shown.
> 6. **Which field is the file input for the CV**, and whether the form is Ashby-style (needs real keystrokes) or Greenhouse-style.
>
> Use the browser tools only — no curl or python fetching. Budget about 8 calls. If the page
> doesn't render, wait two seconds and retry once, then report what you saw.

## Why the classification matters

`BASIC` forms can be submitted immediately under the standing rules. `NEEDS-WRITING` forms need
either a drafted answer or his sign-off, and shipping a weak paragraph is worse than waiting a
day. Getting this split right is most of the value of the whole workflow.
