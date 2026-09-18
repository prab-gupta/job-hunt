# Agent: applicant

Fills and submits one application, end to end. Runs **one at a time** — several of these driving
the same browser will fight over tabs and produce half-filled forms.

Give it: the posting URL, the CV path, and the scout's field report if you have one.

## Instructions to give the agent

> Submit this application on Prabhavit Gupta's behalf. He has authorised submission.
>
> **Read `references/application-rules.md` first and follow it exactly** — his details, his
> salary number, the standard answers, and the list of things you must not do are all there.
>
> - Posting URL: `<…>`
> - CV to attach: `<absolute path>` — attach it to every application; never submit without it
> - Cover letter, if the form asks for one: `<path to the adapted PDF>` or paste the adapted text
>
> Mechanics that will otherwise cost you calls:
>
> - **Ashby forms ignore programmatic value-setting.** Click the field, then type. If a submit attempt says a field is missing while the value is visible on screen, select-all, delete, and retype that field by keystroke.
> - **Greenhouse phone-country and city pickers** need click → type two or three letters → click the option in the list. Typing the full word then moving on leaves the field unset and the form fails validation.
> - **File inputs**: the element that accepts an upload is the one reported as type `file`, not the visible "Attach" button. Never click a file button — it opens a native dialog you cannot see.
> - Fill everything, then screenshot before submitting and work through the pre-submit checklist in the rules file line by line. The one that gets missed is the **cover-letter field that isn't marked required** — scan the page text for "cover letter" or "motivation" before you decide the form doesn't have one, because a submitted application cannot be edited afterwards.
> - Submit, wait, and **screenshot the result**. Only a visible confirmation counts.
>
> Stop and report back without submitting if: the form wants an account or a CAPTCHA, it asks for
> payment or ID details, a required question needs a claim about his experience that the rules
> file doesn't cover, or it demands work authorisation he doesn't hold.
>
> Report: what you entered in every non-obvious field, the verbatim confirmation text, and
> anything you had to judge for yourself.

## After it returns

Add the row to the tracker with the confirmation text. If the agent reports a judgement call it
had to make, surface that to him in chat — those are the ones he'll want to correct.
