# etalytics - QA Engineer (m/f/d) Test Automation - 2026-09-09

Job: https://www.linkedin.com/jobs/view/4464470633/
Applied via (external ATS, Recruitee-style, LinkedIn "Apply on company website"): https://join.etalytics.com/o/qa-engineer-mfd-test-automation/c/new?source=LinkedIn+Basic+Jobs

## Form answers given

- Full name: Prabhavit Gupta
- Email address: prabhavitg@gmail.com
- CV or resume: uploaded Prabhavit_CV_Original_EN.pdf
- Cover letter (written in the "Write it here instead" textarea, no PDF field offered):

  Dear etalytics team,

  I would like to apply for the QA Engineer (m/f/d) Test Automation role. At FlowSpace, a workspace marketplace platform, I spent the past two years owning quality on a live, fast-moving product: writing Playwright end-to-end tests and API-level checks across a Next.js frontend, Laravel backend and Supabase data layer, while the platform scaled from 2,000 to 4,500+ users. I also built and operated AI agents in production, which meant testing for non-determinism and failure recovery rather than simple pass or fail assertions, work that maps directly onto validating an AI-driven platform like etaONE.

  I liked the framing in your posting: quality as something measurable, not a gut feeling. That is how I approached FlowSpace's migration off its legacy stack, mapping data models per entity and driving the cutover while the product stayed live. I am comfortable with TypeScript, Git and CI/CD, and I am self-driven about finding gaps before a ticket is assigned.

  I am based in Venice, Italy, and hold an Italian EU long-term residence permit. I am not currently authorised to work in Germany and would need the applicable employer-side permit or sponsorship process. I am ready to relocate and complete that process.

  Prabhavit Gupta

- "Do you require a visa or work permit to be employed in Germany?": **Yes, I will apply for it** (role is in Germany, not Italy/remote-from-Italy; standard answer = not authorised now, employer-side permit needed).
- "Annual salary expectation in EUR?": 50000
- "What is the earliest possible date you could start with us?": 23/09/2026 (two weeks from application date 2026-09-09, standing rule).
- Legal agreement: ticked "I hereby confirm my acceptance of the etalytics GmbH privacy policy."
- Cookie banner: clicked "Agree to necessary" (decline non-essential).

## Notes / traps hit
- LinkedIn listing showed "Responses managed off LinkedIn" and a plain "Apply" (not Easy Apply) -> "Apply on company website", landing on join.etalytics.com, a Recruitee-style ATS (same `/o/<slug>/c/new` pattern as documented in apply-bot/PATTERNS.md for Recruitee).
- The GDPR consent checkbox: setting it via the form_input tool's boolean value did NOT register with the form's validation (submit failed with "This field is required and can not be left empty." even though the box visually looked checked and then reverted to unchecked on submit). Fix: a real mouse click on the checkbox element (not a programmatic value-set) registered correctly and the submit then succeeded. This matches the general React-state-wipe class of trap already documented for other ATSs; worth adding to PATTERNS.md for Recruitee/join.etalytics.com specifically.
