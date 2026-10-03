> **SUPERSEDED for autonomous runs.** For autonomous application runs, `AGENT-INSTRUCTIONS.md` and the `needs-you-drainer` skill (`.claude/skills/needs-you-drainer/SKILL.md`) are the authority. Where this file conflicts with them, they win. In particular, ignore here: per-application approval prompts, "Best guess" or any guessed factual answer (park the row instead with the exact missing fact), the ban on ATS account creation (authorized with the one shared `JOBS_ACCOUNT_PASSWORD`), the old salary figure and "unmodified base CV" rule (see `AGENT-INSTRUCTIONS.md` section 3), and any parallel, headless or newly launched browser or "form scout" (browser work is strictly sequential, one existing tab, existing Chrome at `127.0.0.1:9222`). This file remains valid only for manual, interactive sessions where Prabhavit is present.

# Session runbook — every job-hunt session, in this order

Deterministic order so nothing falls through. Skip a step only when its input is empty.

0. **Read `application-rules.md`.** Non-negotiable, every session, before any form.
1. **Follow-up sweep** (`agents/follow-up.md`) — inbox against the Submitted list. Interview
   invites jump the queue: run `agents/interview-prep.md` for each, everything else waits.
2. **Anything unblocked?** If he has signed in to join.com, run the five blocked roles first.
   If the auditor left FAILs or orphan letters last session, fix those before anything new.
3. **Next batch** — take the top unopened rows from the shortlist workbook. If the shortlist
   is exhausted or older than ~7 days, run the job-hunt search skill for a fresh sweep first
   (postings die in days; the workbook is a snapshot, not a source).
4. **Per role:** `form-scout` (parallel, cheap) → `letter-writer` for anything NEEDS-WRITING →
   `applicant` (strictly one at a time). BASIC forms go straight to applicant.
5. **Audit** (`agents/submission-auditor.md`) — before anything is reported as submitted.
   The applicant's own success claim is not evidence.
6. **Log** — tracker rows with verbatim confirmation text; update the counts in `README.md`
   (state of play) so the next session starts true.
7. **Report to him:** interview invites first, then submitted, then blocked, then needs-him.

Standing rules of the loop: one company, one best role. No new applications while an audit
FAIL is unfixed. Never report success the auditor hasn't passed.
