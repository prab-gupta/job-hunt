# Greenhouse runbook

Canonical mechanics: [`../form-quirks.md`](../form-quirks.md) and [`../apply-bot/PATTERNS.md`](../apply-bot/PATTERNS.md).

## Fast path

1. Confirm the posting URL still renders the named role. A redirect to a board index or `?error=true` means closed.
2. Click **Apply** if the form is not already visible.
3. Remove any MyGreenhouse/autofill CV and upload the tailored PDF.
4. Upload or manually enter the cover letter whenever offered, even if marked optional.
5. Fill text fields. For React Select dropdowns, click, type a short search term, then click a visible option.
6. Re-enter phone with full `+39` prefix. Verify city and phone-country controls did not silently clear.
7. Answer every required custom question truthfully. Hand back anti-AI questions.
8. Leave optional marketing consent unchecked; acknowledge required privacy/legal notices truthfully.
9. Review the uploaded filenames and all dropdown values.
10. Submit. If email verification appears, request the fresh code immediately. Never retrieve or guess it.
11. If reCAPTCHA appears or cannot connect, hand back. Never bypass it.
12. Save the success screenshot and exact confirmation text before updating the tracker.

## Known traps

- Programmatic text values may not update React state. Prefer native fill/type or the browser's supported locator actions.
- JavaScript scrolling may not move the rendered form. Use browser scroll.
- Autocomplete values must be selected from the visible list; typed text alone can clear on blur.
- Stale verification codes expire quickly. Reloading may reset the form.
- A visible value is not proof Greenhouse accepted it. Submission confirmation is the only final proof.


## Embedded Greenhouse iframe on a company careers page (mongodb.com, 2026-09-09)
- The form lives in a cross-origin iframe. Claude in Chrome tools cannot interact with it (no focus, no value change, read_page empty for the iframe). Use Playwright MCP: browser_snapshot reads into the iframe; fill/click/select/file_upload work.
- Success text: 'Thanks for taking the time to apply to MongoDB!'. Decorative reCAPTCHA badge never challenges.

## Puck-built Greenhouse job boards (app.careerpuck.com, e.g. Domino Data Lab, 2026-09-16)
- Same cross-origin-iframe trap as mongodb.com above: the apply form sits inside an iframe (`id="grnhse_iframe"`, title "Greenhouse Job Board") that Claude in Chrome's read_page/find cannot reach at all.
- The bare `job-boards.greenhouse.io/<token>/jobs/<id>` URL does not help here: it 301-redirects straight back to the careerpuck.com wrapper, so there is no iframe-free entry point for this tenant. Use Playwright MCP for the whole form.
- Fields on this tenant: First Name, Last Name, Email, Country, Phone, Location (City) with a "Locate me" geolocation link, Resume/CV attach, Cover Letter attach, LinkedIn Profile, a work-authorisation dropdown, a GDPR "Point of Data Transfer" dropdown, and a "use my info to consider me for other roles" consent dropdown, all required except the cover letter.
