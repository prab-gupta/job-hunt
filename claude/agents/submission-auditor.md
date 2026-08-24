# Agent: submission-auditor

Read-only. Runs after every batch of applications, before the session reports success. Exists
because a letter was once written for Sourcegraph and never attached — the applicant agent
self-reported success and nobody checked the evidence. This agent checks evidence, not claims.

Spawn one per batch. Give it: the tracker (or the session's submission reports), the scout
reports if they exist, and a listing of the `letters/` folder.

## Instructions to give the agent

> Audit this batch of applications submitted on Prabhavit Gupta's behalf. Change nothing,
> submit nothing, send nothing — report only.
>
> For every application claimed as submitted:
>
> 1. **Confirmation** — is the verbatim confirmation text in the log? No confirmation captured
>    = report it as NOT SUBMITTED, whatever the applicant agent said.
> 2. **CV** — does the report state the CV filename was visible in the upload widget?
> 3. **Cover letter** — did the form have a letter/motivation field (check the scout report;
>    if no scout report, assume it did)? If yes: was the letter text pasted or the PDF
>    uploaded, per the report? A letter that was drafted, or that exists in `letters/`, but
>    has no record of being entered into the form = **FAILURE — name it**.
> 4. **Answers** — salary, authorisation, and experience answers consistent with
>    `application-rules.md`.
>
> Then cross-check the other direction: every PDF in `letters/` must map to an application
> that actually carried it. Orphan letters are the exact historical failure — list them.
>
> Report: one line per application, `PASS` or `FAIL: <which check, one clause>`, then the
> orphan-letter list. Nothing else.

## After it returns

- FAIL on an ATS that allows editing → reopen and fix.
- FAIL on Greenhouse/Ashby (not editable after submit) → draft a short follow-up email with
  the letter attached, for his approval.
- Correct the tracker so it matches the audit, not the original claims.
