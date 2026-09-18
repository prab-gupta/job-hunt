# GitKraken - Software Engineer (Full Stack Product Engineer, Insights) - 2026-09-09

ATS: BambooHR, https://gitkraken.bamboohr.com/careers/180
Status: NEEDS YOU (reCAPTCHA "I'm not a robot" checkbox on submit, form otherwise fully filled and left as-is)

Live JD facts confirmed before filling:
- Title: Software Engineer. Minimum Experience: Mid-level. Not Senior/Staff/Lead/Principal - hard gate not tripped.
- Location: "This is a hybrid position based in Alicante, Spain. This role combines the flexibility of remote work with the benefits of meaningful in-person collaboration." EU country (Spain), so the "location outside the EU with no remote-from-Italy" kill gate does not apply. Not remote-from-Italy though - a relocation role.
- Stack: React, Go, PostgreSQL, AWS. JD explicitly asks for "Backend engineering experience, ideally with Go or the ability to ramp quickly in Go" - Go is not required as an already-claimed core language, consistent with the queue note.
- JD is in English. No MSc/PhD requirement.

## Fields filled
- First Name: Prabhavit
- Last Name: Gupta
- Email: prabhavitg@gmail.com
- Phone: +39 351 610 7807
- Resume: Prabhavit_CV_Original_EN.pdf (uploaded, confirmed attached)
- Desired Pay: EUR 50,000 (standing salary answer, no band posted)
- Website, Blog or Portfolio: github.com/prab-gupta
- LinkedIn URL: linkedin.com/in/prabhavit
- "Where do you currently reside/intend to perform this role?" (optional): Venice, Italy. Open to relocating to Alicante, Spain for this role.
- Honeypot field "Please leave this field blank": left blank, not touched.

No cover letter upload or paste field exists on this BambooHR form - CoverLetter_GitKraken.pdf/.txt could not be attached because the ATS gives no slot for it. The letter itself was re-checked against the live JD and Master Experience.md before this run and needed no changes (already used "Alicante" relocation framing and Spain sponsorship framing correctly).

## Required essay answers written

**Why do you want to join GitKraken?**
GitKraken already reaches millions of developers, and Insights is a genuinely new problem inside that: turning PR flow, DORA metrics, and agent adoption data into something engineering leaders can act on. At FlowSpace I have spent the last two years building product features end to end in TypeScript and Laravel, wiring up third party APIs, and shipping AI assisted workflows that turn messy source data into structured, reviewable output. That is close to the shape of Insights, taking data most teams find hard to read and building an interface people trust. I also like that this role is explicit about using AI coding tools day to day rather than treating them as a side experiment, which matches how I already work.

**In an AI-assisted engineering environment, what do you believe the software engineer is still uniquely responsible for?**
The engineer is responsible for the judgment calls an AI tool cannot make on its own, deciding what the feature should actually do, whether a shortcut is safe for this specific system, and when generated code silently assumes something false about the data or the user. AI can produce a plausible implementation quickly, but it does not know the history of the codebase, the edge cases that broke last time, or which parts of the system are load bearing. I see my job as owning the specification, the review, and the accountability for what ships, using AI to move faster through the parts that are mechanical rather than the parts that require context.

**Describe how you would use AI to take a feature from vague idea to production-ready implementation. What would you delegate to AI, and what would you personally own?**
I start by writing down the actual requirement myself, who the user is, what they are trying to do, and what done looks like, because that framing is the part AI does worst when the idea starts vague. From there I delegate to AI the parts that are mechanical or exploratory, scaffolding a component, drafting a first pass at an API handler, writing repetitive tests, or summarizing an unfamiliar part of the codebase before I touch it. I personally own the technical plan, the data model and API contract decisions, the edge cases and error handling, and the final review of every diff before it merges. In practice this looks like using a tool such as Claude Code to produce a working draft quickly, then reading it line by line, tightening the parts that are too generic, and adding the validation and tests the draft usually skips.

**Imagine an AI agent produces a large pull request that appears to work. How would you decide whether it is safe to ship?**
First I shrink the surface, reading the diff fully rather than trusting a passing test suite, since a large AI generated PR is exactly where a plausible looking but wrong assumption hides. I check that the tests it added actually exercise the risky paths, not just the happy path, and I look specifically for silent behavior changes, altered function signatures, changed defaults, removed error handling, or a migration that is not reversible. For anything touching production data, payments, or authentication, I want a human who knows that part of the system to review it regardless of how confident the tests look. If I cannot explain why every part of the diff exists, I do not ship it, and I ask for the change to be made smaller and easier to verify instead.

## Blocker
Below the essay questions, before Submit, the form embeds a Google reCAPTCHA v2 "I'm not a robot" checkbox (iframe). This is a user-only blocker per the brief and per the standing safety rule against bypassing bot detection. Not clicked, not solved. Submit was NOT pressed. All fields above remain filled in the live tab.

Screenshot: confirmations/handback-gitkraken-recaptcha-2026-09-09.png
