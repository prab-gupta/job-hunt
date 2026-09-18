# Teamtailor runbook

Canonical mechanics: [`../apply-bot/PATTERNS.md`](../apply-bot/PATTERNS.md).

## Fast path

1. Decline non-essential cookies so the application control remains clickable.
2. Click **Apply for this job** to reveal the full form.
3. Upload the tailored CV and attach or enter the cover letter when offered.
4. Complete the form and set required consent using the real visible checkbox, preferably by its unique ID.
5. Verify the resume filename using the dropzone and/or populated resume URL state.
6. Review all values before submit.
7. If validation fails, recheck and re-upload the CV before retrying.
8. Hand back CAPTCHA and anti-AI questions.
9. Capture success text and screenshot, then update the tracker.

## Known traps

- Consent can render as both a hidden input and a visible checkbox with the same name.
- Failed submission can silently drop the uploaded CV.
- Displayed resume filenames may be lowercased.

