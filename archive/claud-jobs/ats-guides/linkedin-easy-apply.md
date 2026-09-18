# LinkedIn Easy Apply runbook

Canonical mechanics: [`../apply-bot/PATTERNS.md`](../apply-bot/PATTERNS.md).

## Fast path

1. Confirm this is **Easy Apply**, not an external redirect.
2. Start the modal and inspect every step; expect several pages.
3. At the resume step, explicitly upload or select the tailored CV. Never accept the default resume without verifying its filename.
4. Add a cover letter when the flow offers one.
5. Complete each page truthfully, then review the full application summary.
6. Hand back anti-AI questions, account/security prompts, or facts not present in canonical profile files.
7. Before final Submit, verify resume filename, phone, location, work authorisation, years, and salary.
8. Submit after required action-time confirmation.
9. Require the visible text **Application status: Application submitted** or equivalent.
10. Screenshot it and update the exact tracker row.

## Known traps

- LinkedIn's resume library contains stale generic CVs.
- `Next` is not submission. Continue through Review and Submit.
- External redirects follow the destination ATS guide instead.


- 2026-09-09: to upload a tailored CV (instead of the library resume), use Playwright MCP: browser_click on "Upload resume", then browser_file_upload with the PDF path. Claude in Chrome file_upload cannot reach this control.
