# Form quirks — per-ATS mechanics learned the hard way

Fill-and-submit mechanics only. Discovery/verification traps (dead boards, postings that lie
about location, closed-posting signatures) live in `skill/job-hunt/references/sources.md` §6.

## Ashby (jobs.ashbyhq.com)

- **Ignores programmatic value-setting.** Click the field, then type real keystrokes.
- **Claims filled fields are missing.** If submit fails on a field whose value is visible on
  screen: select-all, delete, retype that field by keystroke.
- Canonical URL is `jobs.ashbyhq.com/<org>/<uuid>`; add `/application` to reach the form.
  Strip `?embed=js`, `?utm_data=…`, `?locationId=…`.
- Page sometimes loads as a JS shell ("You need to enable JavaScript") — that's a failed
  render, not a closed role. Retry or use the org's posting API.
- Discloses salary bands more reliably than any other ATS, often multi-currency.

## Greenhouse (job-boards.greenhouse.io / job-boards.eu.greenhouse.io)

- **Phone-country and city pickers silently blank themselves.** Click → type two or three
  letters → click the option in the dropdown list. Typing the full word and tabbing away
  leaves the field unset and validation fails.
- **A posting URL that serves the board index (many jobs on one page) means the role is
  closed.** Nothing else flags it.
- The form is on the posting page — click "Apply" if fields aren't rendered.
- **Optional cover-letter blocks ("Attach / Dropbox / Enter manually") still count as being
  asked** — rule 3. This is the exact reading that caused the Sourcegraph miss.

## All ATSs

- **The file input is the element typed `file`, not the visible "Attach" button.** Clicking
  the button opens a native OS dialog no agent can see. Set the file on the `file` input.
- Submitted applications on Greenhouse and Ashby **cannot be edited afterwards**.
- Only a visible success page counts as submitted — screenshot it, quote it in the log.
- join.com forces account sign-in before the form opens — skip unless he's signed in.

## Append below as new ones are learned

<!-- format: ## <ATS or site> — <one-line quirk> — <date> -->
