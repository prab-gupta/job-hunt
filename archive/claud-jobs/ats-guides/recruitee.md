# Recruitee runbook

Canonical mechanics: [`../apply-bot/PATTERNS.md`](../apply-bot/PATTERNS.md).

## Fast path

1. Open the application page ending in `/c/new` before filling anything.
2. Upload the tailored CV through the candidate CV file input.
3. Add the cover letter when offered.
4. Click custom-radio labels, not hidden inputs. Read each selected state back immediately.
5. Complete all truthful fields and required privacy consent.
6. Verify every radio group, checkbox, text value, and uploaded filename.
7. If hCaptcha appears or intercepts the submit area, hand back.
8. Submit only when no CAPTCHA blocks it.
9. Capture the visible confirmation and update the tracker.

## Known traps

- The job page's inline form is not always the final application page.
- Clicking hidden radios can select the wrong option or do nothing.
- hCaptcha may surface only as an intercepted click or permanently busy submit button.


- 2026-09-09: GDPR consent checkbox must be clicked with computer left_click (ref), not set via form_input; programmatic value does not register with validation.

- 2026-09-09 (cozycozy): phone widget ignores form_input for the local number (only the country prefix sticks); click the field and type real keystrokes. Country dropdown defaults to the job country (Hungary), reset to Italy +39.
