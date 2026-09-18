# ATS application runbooks

Use this folder as the platform router. It is an execution aid, not a second policy source.

## Canonical rules

- Applicant facts, tailoring rules, salary, consent, CAPTCHA and submission rules: [`../HANDOFF.md`](../HANDOFF.md)
- Cross-platform mechanics and known quirks: [`../form-quirks.md`](../form-quirks.md)
- Detailed failure evidence: [`../apply-bot/PATTERNS.md`](../apply-bot/PATTERNS.md)
- Application tracker: [`../applications.csv`](../applications.csv)

If a guide conflicts with a canonical file, the canonical file wins. Add newly verified quirks to `form-quirks.md` first, then update the relevant guide.

## Router

| Platform | Guide | Confidence |
|---|---|---|
| Greenhouse | [`greenhouse.md`](greenhouse.md) | Verified on real applications |
| Ashby | [`ashby.md`](ashby.md) | Verified on real applications |
| Workable | [`workable.md`](workable.md) | Verified on real applications |
| Recruitee | [`recruitee.md`](recruitee.md) | Verified on real applications |
| Personio / Factorial | [`personio-factorial.md`](personio-factorial.md) | Partly verified |
| LinkedIn Easy Apply | [`linkedin-easy-apply.md`](linkedin-easy-apply.md) | Verified on real applications |
| Teamtailor | [`teamtailor.md`](teamtailor.md) | Verified on real applications |
| Traffit / JustJoin | [`traffit-justjoin.md`](traffit-justjoin.md) | Verified on real applications |
| Lever | [`lever.md`](lever.md) | Baseline only; expand after first verified run |
| Workday | [`workday.md`](workday.md) | Baseline only; expand after first verified run |

## Universal application loop

1. Read the matching `applications.csv` row and verify the posting is live.
2. Read `HANDOFF.md`; do not infer missing personal facts.
3. Create a job folder and tailor the CV. Never upload the generic CV.
4. Prepare a cover letter whenever the form offers a cover-letter field.
5. Open the ATS guide, then fill the form using real UI interactions where required.
6. Stop for account creation, passwords, CAPTCHA, anti-AI questions, or facts only Prabhavit can provide.
7. Before final submission, verify every field, uploaded filename, privacy choice, and truthful work-authorisation answer.
8. Submit only with action-time confirmation when the browser safety layer requires it.
9. Capture visible confirmation text and a screenshot. No confirmation means not submitted.
10. Update the exact tracker row. Do not add a duplicate row.

