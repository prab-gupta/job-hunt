# Ashby runbook

Canonical mechanics: [`../form-quirks.md`](../form-quirks.md) and [`../apply-bot/PATTERNS.md`](../apply-bot/PATTERNS.md).

## Fast path

1. Normalize the role URL to `jobs.ashbyhq.com/<org>/<uuid>` and use `/application` for the form.
2. Verify the named role renders. A JavaScript-shell message is a render failure, not proof the role is closed.
3. Upload the tailored CV, then attach or enter the cover letter when offered.
4. Fill fields with real keystrokes. Do not rely on programmatic value assignment.
5. For location, type a partial term, inspect tenant-specific options, and click the truthful city or country result.
6. Fill every truthful field you can answer, even if its HTML does not mark it required.
7. Review all fields before submit.
8. If Ashby reports a missing visible field, select all, delete, and retype that field with real keystrokes. Recheck the full form after rerender.
9. If submission is flagged as possible spam and the page explicitly permits retry, retry once only.
10. Hand back CAPTCHA and anti-AI questions.
11. Capture confirmation text and screenshot, then update the tracker.

## Known traps

- Error rerenders can reset previously completed fields.
- Location granularity varies by employer: country, city, or plain text.
- Requiredness in the page markup is not reliable.
- Essay-looking fields may be optional; inspect required state before spending time drafting.


- 2026-09-09 (Teero): custom Yes/No segmented toggle can render selected yet fail "Missing entry" on Submit; click the other option then back to force onChange, re-verify, resubmit.
- 2026-09-16 (Thought Machine): a numeric (`type=number`) salary field silently discards its value if the typed text contains a stray letter a JS number input reads as exponent notation, e.g. typing "EUR 55,000" renders as "E55000", an invalid number that vanishes on the next re-render (CV upload, any other field's click-away). The field looks filled right after typing, so this is easy to miss. Type digits only ("55000") into any Ashby number-type field.
