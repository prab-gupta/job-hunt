# Personio and Factorial runbook

Canonical mechanics: [`../apply-bot/PATTERNS.md`](../apply-bot/PATTERNS.md).

## Fast path

1. Verify the role and location on the employer's own posting.
2. Open the application form and upload the tailored CV through the visible upload trigger or supported file chooser.
3. Confirm the submit button becomes enabled after upload.
4. Attach or enter the cover letter when offered.
5. Complete text, dropdown, work-authorisation, relocation, salary, and privacy fields truthfully.
6. Review all values and uploaded filename.
7. Submit and wait for a visible success page or message.
8. If the server returns an error, do not log submission. Preserve the filled-state evidence and retry only when safe.
9. Hand back CAPTCHA, account creation, passwords, and anti-AI questions.
10. Screenshot confirmation and update the tracker.

## Known traps

- File inputs are commonly hidden behind styled controls.
- Disabled Submit is useful evidence that upload or a required field has not landed.
- Personio can return a server error after a fully valid form. A request attempt is not a submission.

