# Workday runbook

Status: baseline. Workday varies heavily by employer tenant. Treat each tenant as unknown until verified.

## Safe baseline

1. Verify the named role on the employer's own Workday tenant.
2. If account creation or login is mandatory, hand back. Never create an account or enter a password.
3. If guest application is available, create job-specific materials and upload the tailored CV.
4. Attach or enter the cover letter whenever offered.
5. Review every parsed profile field; resume parsing can create incorrect values.
6. Complete each page truthfully using canonical profile facts only.
7. Use visible UI interactions for dropdowns and autocomplete controls.
8. Before the final page, verify contact data, work authorisation, employment history, education, salary, consent, and uploaded filename.
9. Hand back CAPTCHA, anti-AI questions, and unknown personal facts.
10. Submit after required action-time confirmation. Capture visible confirmation and screenshot before updating the tracker.

## Learning checklist

For each tenant, record: guest-vs-account requirement, resume parsing errors, page count, autosave behavior, duplicate-candidate warning, validation behavior, CAPTCHA, and confirmation signature.

