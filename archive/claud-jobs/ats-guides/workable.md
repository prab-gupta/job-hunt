# Workable runbook

Canonical mechanics: [`../apply-bot/PATTERNS.md`](../apply-bot/PATTERNS.md).

## Fast path

1. Treat a redirect containing `?not_found=true` as closed.
2. Upload the tailored CV using the real resume file input or its supported file chooser.
3. Refill city and country after upload; CV parsing can wipe address fields.
4. Attach or enter the cover letter when offered.
5. Complete one radio group at a time because rerenders can invalidate element references.
6. Review all values and uploaded filename.
7. Inspect the area immediately above Submit for Cloudflare Turnstile or another CAPTCHA.
8. If CAPTCHA exists, hand back before submission.
9. Submit and wait for the job header to change to **Applied**; Workable may not show a separate thank-you page.
10. Screenshot the applied state and update the tracker.

## Known traps

- Resume dropzone overlays can intercept clicks. Use the real file input/file chooser, not blind coordinate retries.
- A button stuck on `Submitting...` can mean hidden Turnstile, not a slow request.
- Generated radio IDs may become stale after each selection.

