# BambooHR (<tenant>.bamboohr.com/careers/<id>)

Observed 2026-09-09 (GitKraken).

- Apply button opens a single-page form: First/Last name, Email, Phone, Desired Pay, Website, LinkedIn, residence question, custom essay questions, Resume upload.
- Only ONE file input (Resume). No cover-letter upload or paste field. Put letter content into a fitting essay answer if one exists, otherwise skip the letter and say so in the CSV notes.
- Honeypot text field "Please leave this field blank": never fill.
- Google reCAPTCHA v2 checkbox directly above "Submit Application": user-only. Pre-fill the form in the user's Chrome tab, stop before the checkbox, log NEEDS YOU with the tab id, and give the user the answers file path so they can re-enter if the tab resets.
- form_input by ref works for all text fields; essays are plain textareas.

- 2026-09-09 (Comply365, tenant vistairhr): some tenants DO have a Cover Letter upload field next to Resume; check before assuming none. reCAPTCHA above Submit confirmed again.

- 2026-09-11 (Tickmill, tenant tickmill.bamboohr.com): single resume-only file input again (no cover letter slot), reCAPTCHA directly above Submit confirmed again. New trap: the Country dropdown defaults to the job posting's own country (Estonia here), not blank or the visitor's locale — must be explicitly changed to the candidate's actual country. Changing Country silently clears the Province field, which then needs to be refilled.
