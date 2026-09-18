# Standing rules for submitting applications on Prabhavit's behalf

> **HIS STANDING INSTRUCTION, 6 August 2026, in his words: "don't stop applying until you finish all
> CV only."**
>
> Read that as: work the lead tabs until every role whose form needs only the CV plus standard
> details has been applied to. Do not stop at a round number, do not stop to summarise, and do not
> wait to be told to continue. Stop only for the four reasons below, and log the reason on the row:
>
> 1. The form has a cover letter field proper (rule 4).
> 2. It needs words, a video or a fact only he can supply (rule "things you must not do").
> 3. The posting is dead, already on file, or offers no truthful option.
> 4. The CV genuinely cannot be attached, for example SmartRecruiters' shadow-DOM upload.
>
> When a session ends with work left, the next session picks up from the lead tabs of the workbook
> and keeps going. The queue is finished when the lead tabs hold nothing with a direct application
> form left on it.

These are his instructions, not suggestions, and several of them exist because they were got
wrong once already. Read this file before touching a single form. If a rule here conflicts with
your own judgement about what would "look better" to an employer, the rule wins. It's his
career and his call.

## The non-negotiables

1. **Attach the CV to every application. Never submit one without it.** Use only the CV file he
   most recently supplied, the exact PDF, unmodified. Do not regenerate it, reformat it, or
   substitute a version you made. If the file isn't available in this session, stop and ask;
   don't proceed with a CV-less application.

   As of 6 August 2026 the current file is the edited CV: clickable blue underlined links on all
   eleven company and project headers, AliCreates removed from the text layer rather than covered
   over, spacing under the company rows normalised, and the Font Awesome contact icons remapped so
   they no longer extract as the words Phone, Envelope, LINKEDIN and Map-marker-alt. That last one
   was breaking resume parsers: Lever autofilled `http://Map-marker-alt` into the website field
   before it was fixed. sha256 e18579bb9bcffee3db28. `validate.py` in the folder checks this hash.

2. **Salary expectation, settled by him on 6 August 2026: normally EUR 40,000 to 50,000, stretching to
   EUR 60,000 where the role warrants it.** This replaces the earlier EUR 30,000 to 40,000, which was
   leaving money on the table. Write it plainly, "EUR 40,000-50,000" or "EUR 40,000-50,000, negotiable"
   at most. Do not write a paragraph where a number was asked for.

   - Default range: **EUR 40,000 to 50,000.**
   - Senior titles, or roles where the scope is clearly bigger: go to **EUR 50,000 to 60,000.**
   - Single-number fields get **45000**, or **55000** on the stretch cases.
   - A monthly field gets **EUR 3,300 to 4,200**, the same range divided by twelve.
   - Contract or day rate: **EUR 250 to 300 a day, about EUR 35 an hour.**
   - **Do NOT anchor on the posting's own published band**, his explicit instruction. Quote his number,
     not theirs, even where they advertise far more. Naming their figure back at them is not the goal.
   - Other currencies convert at the rate of the day: roughly USD 47,000 to 58,000, GBP 35,000 to 43,000.
   - Applications sent before this change quoted 30,000 to 40,000. Not worth correcting retrospectively,
     but expect the gap to come up in a first call on those, and he should hold the new number there.

3. **A generic message box is NOT a cover letter field.** Added by him on 6 August 2026. Where a form
   has only an open box like "Message to the Hiring Team, let the company know about your interest
   working there" and no cover letter field as such, **write a small line in his voice from the
   motivation-letter guidance below and submit with the CV.** Three or four sentences, factual, drawn
   from his real work, no salesmanship. This covers the SmartRecruiters and Ashby generic boxes.

4. **Do not apply at all where the form has a cover letter field proper, whether it is optional or
   required.** Corrected 6 August 2026, and this reverses the original rule. Open the form, look for a
   cover letter field by any name (Cover letter, Motivation letter, Why do you want to work here,
   Tell us about yourself, or a letter upload slot). If one exists, close the form, submit nothing,
   and record the role on the 'Has a cover letter field' tab of the workbook with the field's exact
   label. Only forms with no letter field anywhere get applied to. The single exception is when he
   asks for a letter on a named role, as he did for Sporty Group on 6 August; then adapt his
   motivation letter (`claude/motivation-letter.md`) to that role and nothing else.

4. **When a form asks for years of experience and wants 3 or more, write 3.** Don't skip an
   application because a year count is above his. Answer honestly with 3 and let the employer
   decide. Same principle for any "do you have N years of X" free-text field: give the true
   number and one clause of context, no more.

5. **Skip join.com** unless he has signed in on that browser. Their apply flow forces account
   creation or Google sign-in, and account creation is off-limits.

6. **Don't make the writing sound AI-generated.** Details in the writing section below.

7. **No em dashes anywhere**, in any file, letter or form field.

## His details

| Field | Value |
|---|---|
| Name | Prabhavit Gupta (preferred: Prabhavit) |
| Email | prabhavitg@gmail.com |
| Phone | +39 351 610 7807 (country: Italy, +39) |
| Address | Via Zanetti, 10, Venice, Veneto, 30175, Italy |
| Location for city pickers | Venice, Venezia, Italy |
| LinkedIn | https://www.linkedin.com/in/prabhavit/ |
| GitHub / portfolio | none supplied. Leave blank rather than inventing one |
| Work authorisation | Italian EU long-term residence permit. **Needs no sponsorship anywhere in the EU.** Not UK, Swiss or US authorisation. |
| Availability | Two weeks from an offer |
| Languages | English professional, Hindi native, Italian beginner |
| Current company / title on forms | FlowSpace, Lead Developer |

Standard answers to the questions that recur:

- *Legally eligible to work where you'll work from?* -> **Yes**
- *Which status allows you to work there?* -> **citizen / permanent resident** (the EU long-term permit)
- *Will you require sponsorship now or in future?* -> **No** for EU-based and remote-from-Italy roles. For a **UK, Swiss or US** role, the honest answer is **Yes**. Answer it truthfully and flag the role to him rather than fudging it.
- *Are you legally authorised to work in [EU country]?* -> **Yes**, on the Italian EU long-term residence permit, with no sponsorship. Worth him knowing this is the reading applied on his instruction: Article 14 mobility still means filing for a residence permit in the second country, so it is not sponsorship but it is not automatic either. Where a form instead offers a closed list of permit types and his is not on it, as capital.com's Cyprus form does, **stop** rather than pick the nearest option.
- *Able and willing to work remotely?* -> **Yes**
- *Based in Europe?* -> **Yes**
- *Previously worked in a customer-facing capacity?* -> **Yes** (FlowSpace: mediated between the internal team, an external agency and members; Urlink: project manager on client requirements)
- *Production experience at a large enterprise (1,000+)?* -> **"only shipped in smaller companies or startups"**. True, don't inflate it
- *AI agents / agentic workflows?* -> **"built and operated agentic systems in production, including testing for non-determinism and failure recovery"**. True, and his strongest answer on any form
- *BPMN specifically?* -> he has n8n workflow automation in production but no BPMN. Pick the middle option where one exists; never claim BPMN production experience
- *Native English speaker?* -> **No, fluent at C2 level**
- *Military obligations?* -> **Not applicable**
- *Pronouns, gender, ethnicity, disability, veteran status* -> he has given he/him and male; everything else is blank or "prefer not to say". Never guess demographic data.
- *How did you hear about us?* -> the honest answer is a job board; pick "Job Board" or "Other" and say "job board" if a follow-up field appears. Where the list has no job-board option, "elsewhere" or "other job websites" is the accurate pick, not LinkedIn.
- *Marketing newsletter consent* -> **decline**. It is separate from the application and declining has never blocked a submit.
- *May we keep your CV on file for future roles?* -> **yes**. Being contacted about other openings is the whole point.

## Writing that doesn't read as machine-written

His own motivation letter is the voice to match: direct, concrete, slightly formal, first person,
specific numbers, no salesmanship. Things to avoid because they are the tells:

- Openings like "I'm excited to apply" or "I am thrilled by the opportunity".
- Three-item lists everywhere, and sentences of identical length stacked together.
- "Leverage", "passionate about", "cutting-edge", "seamlessly", "robust solutions", "I thrive in".
- Restating the job description back at them instead of saying what he did.
- Perfect symmetry. Real writing has a short sentence after a long one, and occasionally starts with "But" or "So".

What to do instead: name the specific thing he built, the tool he built it in, and the number it
moved. Say plainly where he's weaker rather than papering over it. A sentence like "my agent work
has been in n8n rather than a Python harness, so I'd be learning your idioms early on" reads as
human and costs nothing.

## The facts worth reaching for

Use these rather than adjectives. They're all on his CV.

- FlowSpace: took over an existing system, grew the platform **2,000 to 4,500+ users**, led the migration from **Bubble.io to Next.js + Laravel** on a live product, built the support **AI agents**, lead capture and enrichment into the CRM, GTM and outbound automations, and a scraping/parsing tool that increased listings.
- Integrations shipped: **Office RnD, Nexudus** (automated bookings), Clubee API, Sendgrid, Google APIs, OpenAI/Anthropic, Eden AI.
- UltraStrategy: **CV-parsing tool in n8n + Eden AI**. Get2Germany: Google API tracking, AI tools for finding courses and jobs. Clubee: API integration, unit testing and QA.
- Urlink: built a platform largely with AI, acting as PM and developer.
- Eight European companies in about three years (UK, Spain, France, Italy, Germany, Luxembourg, Netherlands). The ramp-fast argument.
- Certifications: Microsoft Copilot Studio Agent Academy, Microsoft AI agents, Power Automate, Tray.ai Build Practitioner.
- Degree: BA Philosophy, International Studies & Economics, Ca' Foscari Venice. No CS degree. Don't hide it, don't apologise for it.

## Things you must not do

- Create an account, set a password, or sign in as him.
- Solve a CAPTCHA.
- Enter payment details, government ID numbers, or a date of birth he hasn't given.
- Invent a GitHub link, a portfolio URL, a referral name, or demographic data.
- Answer a question that asks for his own opinion, ambition or judgement. Those go to him. Real
  examples from 6 August: Distru's three opinion questions about LLMs, and Deliverect's
  "what is the one impossible achievement you want attached to your name".
- Claim experience he can't evidence, specifically BPMN, Python backend depth, ML research, or a language beyond English.
- Submit two applications to the same company for roles he clearly doesn't qualify for. One good application beats two scattershot ones.

When you hit one of these, stop that application, leave the form filled if you can, and tell him
exactly what's needed.

## Form mechanics learned the hard way

- **Ashby silently drops values set programmatically.** Fields look filled but submit empty. Type
  into them with real keystrokes and read the validation banner before trusting a submit. On a Mac
  the select-all is cmd+a, not ctrl+a, or you end up with "GuptaGupta".
- **Lever parses the CV on upload and overwrites fields.** Upload first, wait for "Analyzing
  resume" to finish, then set the fields, then re-read them before submitting.
- **A batch of browser actions stops at the first failure.** Put the file upload first so a
  rejected path doesn't silently discard the typing that came after it.
- **A dead Greenhouse posting redirects to the board index with `?error=true`.** A dead Lever
  posting 404s. A dead Ashby posting says "Job not found" but still serves the old page title, so
  a title match proves nothing.
- **Some Greenhouse links bounce to the company's own careers site**, where the form is
  unreachable. The working form is `boards.greenhouse.io/embed/job_app?for=<org>&token=<id>`.

## Log every submission

After each one, record: company, role, the ATS, what was entered in each non-obvious field, the
confirmation text you actually saw, and the link. If you didn't see a confirmation, it didn't
happen. Say so. He is tracking this in a spreadsheet and a silent failure is worse than a
visible one.
