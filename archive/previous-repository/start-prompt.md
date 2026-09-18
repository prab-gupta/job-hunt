# Session start prompt — paste this to begin an application session

Start a job application session. I'm Prabhavit Gupta and I authorise you to fill and submit
applications on my behalf, within my standing rules.

Read first, in this order:
1. `README.md` in the "claud jobs" folder — state of play
2. `claude/application-rules.md` — follow it exactly; run its pre-submit checklist before every single submit
3. `claude/session-runbook.md` — the session order
4. `profile-gaps.md` and `form-quirks.md`
5. Run `python3 validate.py` — must pass now and again at session end

Then work the runbook:
- Follow-up sweep against `applications.csv` (use Gmail if connected; if not, say so and skip)
- Draft the Sourcegraph follow-up email attaching `letters/Sourcegraph_Motivation_Letter.pdf` — show me, do NOT send
- If I've signed in to join.com: run the 5 blocked roles first. If not, remind me once and move on
- Next batch: take the top unopened rows from `role-shortlist-2026-08-05.xlsx`. Verify each posting is live in the browser before spending time (search indexes run ~a month stale). Scout the form, write, apply — one application at a time, target 5–10 this session
- CV = `Prabhavit_CV.pdf`, unmodified, attached to every application. Letters adapted from `claude/motivation-letter.md` — never a blank cover-letter field, even optional ones
- Facts current as of 5 Aug evening (authoritative in `profile-gaps.md`): FlowSpace ongoing with ~2 weeks' notice, contract rate €200/day, LinkedIn URL in portfolio/GitHub fields, Italian beginner actively studying
- Audit every submission per `claude/agents/submission-auditor.md` before counting it
- Log each one in `applications.csv` and `follow-ups.md`, then update the counts in `README.md`

Stop and ask me only when you hit: an account wall or CAPTCHA, a payment/ID request, a claim
about my experience the files don't cover, or a UK/Swiss/US sponsorship question.

End-of-session report: submitted (with verbatim confirmation text), blocked, needs-me — in
that order. Nothing counts as submitted without a confirmation seen on screen.
