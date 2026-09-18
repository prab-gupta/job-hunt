# Working rules — the operating manual

Consolidated from rules_out.md, form-quirks.md and everything learned through 12 August 2026. **These are his instructions, not suggestions.** Several exist because they were got wrong once already. If a rule here conflicts with your judgement about what would "look better" to an employer, the rule wins.

## 1. The non-negotiables

**1.1 The CV goes on every single application.** Use Prabhavit_CV.pdf, the exact file, unmodified. Never regenerate, reformat or substitute. sha256 e18579bb...; validate.py checks it.
*Why it's fixed:* an earlier version's Font Awesome contact icons extracted as the words Phone, Envelope, LINKEDIN and Map-marker-alt, and Lever autofilled http://Map-marker-alt into the website field.

**1.2 Salary — EUR 40,000-50,000 baseline.**
- Single-number fields: 45000 (or 50000 where the scope is clearly bigger)
- Monthly: EUR 3,300-4,200. Contract/day rate: EUR 250-300/day, ~EUR 35/hour. PLN roughly 100-120/hour net.
- **Where a posting discloses a band, align to their number rather than quoting below it** (his instruction, 12 Aug). *This reverses an earlier 6 Aug rule that said not to anchor on their band. The 12 August instruction is current.*
- Write it plainly. Do not write a paragraph where a number was asked for.

**1.3 Write bespoke material ONLY for weak-match roles.** Strong matches go out CV-only — **he writes those cover letters himself**. If a strong-match form makes a cover letter required, submit nothing and hand it to him with the link and the questions listed.

**1.4 Every answer stays on the question asked.** Work-authorisation, relocation and availability notes belong in the cover letter or a dedicated eligibility field, **never appended to a technical question**. *This exists because it happened at Lleverage: a "describe a project" answer had a paragraph about the Dutch work permit tacked on the end. It could not be edited after submitting.*

**1.5 Never invent anything.** No GitHub link, portfolio URL, referral name, demographic data, or biographical colour. Work-specific technical questions answered **only** from the CV, his own letter, or facts he has stated.
*Near-miss:* a draft at Duvo claimed he "moved to Venice from India at eighteen" and "studied in a language I had to learn". Neither established; the second contradicts his beginner Italian. Caught before submitting. **Inferring biographical detail is the most likely way to put a lie in front of an employer.**

**1.6 Nothing counts as submitted without an on-screen confirmation.** Screenshot it, quote it verbatim in the log.

**1.7 Say the gaps plainly.** His explicit preference, and it produced the best writing in every application. Claiming competence he doesn't have works exactly until someone checks.

## 2. Never do

- Never create an account or set a password. (join.com is the exception only because he is already signed in.)
- **Never solve a CAPTCHA.** Hand it to him.
- Never enter payment details, government ID or passport numbers.
- Never guess demographic data — pick the decline option.

## 3. His standing instructions, in his words

| Instruction | Date |
|---|---|
| "don't stop applying until you finish all CV only" | 6 Aug |
| "dont skip on stack apply there too" | — |
| "dont make up details about any work specific question let those be" | — |
| "SAY NO TO UK AUTHORISED WHO CARES / I WANT TO CHANCE ANYWAY" | 12 Aug |
| "make baseline 40-50k otherwise adjust with the number quoted" | 12 Aug |
| "only write answers and cover letters for jobs which are low match" + "others i will write the cover letter" | 12 Aug |
| "make sure you dont repeat" | 12 Aug |

Use prabhavitg@gmail.com, never spaces@flowspace.co. No em dashes anywhere.

## 4. Standard answers

| Question | Answer |
|---|---|
| Legally eligible to work where you'll work from? | Yes |
| Which status? | Citizen / permanent resident (the EU long-term permit) |
| Require sponsorship? | No for EU and remote-from-Italy. Yes for UK/Swiss/US — answer truthfully and flag it. |
| Based in Europe? | Yes |
| Location for city pickers | Venice, Venezia, Italy |
| LinkedIn | https://www.linkedin.com/in/prabhavit/ |
| GitHub / portfolio | None. Leave blank rather than inventing one. |
| Availability / notice | Immediately, 1 Sept 2026 or sooner. No notice period. |
| Native English? | No, C2. On dropdowns pick **Professional**, not Native/Bilingual. |
| Previously customer-facing? | Yes — FlowSpace (internal team / agency / members), Urlink (PM on client requirements) |
| Production at a 1,000+ enterprise? | "Only shipped in smaller companies or startups" — don't inflate |
| AI agents / agentic workflows? | "Built and operated agentic systems in production, including testing for non-determinism and failure recovery" — his strongest answer on any form |
| BPMN specifically? | n8n in production but NO BPMN. Never claim BPMN production experience. |
| Demographics | Blank or "prefer not to say" |
| How did you hear about us? | "Job Board" or "Other" |
| Cookie banners | Always the privacy-preserving option |

## 5. ATS mechanics — learned the hard way

**Greenhouse**
- **The stale-CV trap.** Autofills an older Prabhavit_CV-.pdf from MyGreenhouse. **Click the X and re-upload the canonical file every single time.** Bit at Ophelos, Scale AI, The Quality Group.
- **A posting URL that serves the board index means the role is CLOSED.** Often with ?error=true. Nothing else flags it.
- Comboboxes ignore programmatic input — click open, click the option.
- Phone-country and city pickers silently blank themselves. Click, type 2-3 letters, click the option.
- Optional cover-letter blocks still count as being asked.

**Ashby**
- **The location-combobox overwrite.** After selecting an option, typing again re-opens the dropdown and silently overwrites it. Set "Venice, Florida, United States" at SolveAI and "Itasy, Madagascar" at Hexa. **Fix: triple-click, retype, click the exact option, verify by screenshot.**
- Often a JS shell to a fetcher — but NOT uniformly. n8n's FDE posting and Vapi's rendered fine while board indexes didn't.
- URL: jobs.ashbyhq.com/<org>/<uuid>, add /application. Strip ?embed=js, ?utm_data=.
- Discloses salary bands more reliably than any other ATS.
- ElevenLabs embeds Ashby in an iframe — go direct to jobs.ashbyhq.com/elevenlabs/<id>/application.

**join.com**
- He is signed in, so applications take ~2 minutes.
- **Shows "You've applied on <date>" on roles already sent — free dedupe.** Caught Tangible and CityZ.
- "Use this CV as my default" is ticked, so the canonical CV carries automatically.
- **Its metadata lies about freshness.** Novosafe said "updated 12 August", live page said archived 6 months ago. SERA said "updated within the last minute", archived a month. Always open the page.
- Returns HTTP 410 for dead postings.

**Recruitee / Teamtailor / Personio / Lever**
- All render server-side and verify cleanly.
- Recruitee phone fields default to the company's country — switch the country selector FIRST, then type the bare number.
- Teamtailor often hides gating questions ABOVE the personal-information block; scroll up before filling.
- Lever returns a clean 404 for dead postings.

**Workable** — always a JS shell, needs a browser. Long forms: address, citizenship, sanctions declarations.

**All ATSs**
- **The file input is the element typed `file`, not the visible "Attach" button.** Clicking the button opens a native OS dialog no agent can see.
- Phone fields already showing a country prefix: **type the bare number.** "+39 351..." into a field showing "+39" produces "+39003516107807". Happened at Lightning AI.
- Greenhouse and Ashby submissions cannot be edited afterwards.

## 6. Verification rules for sweeps

**Aggregator mirrors are not verification.** Roles verified only via RemoteRocketship, Himalayas, Jobgether, Built In, Remotive or euremotejobs were dead on the real ATS repeatedly (Space Inch, Action1, Quadrivia, Airtable, Keyrus, Convera, Workato, ClickHouse, Bitpanda). **Every Built In listing checked carried a "this job was removed" stamp.** Always fetch the real ATS page.

**~50% attrition is normal.** Half of what a sweep returns is dead, gated or hard-blocked when opened in a browser.

## 7. Company rate limits

| Company | Limit |
|---|---|
| **n8n** | 1 application per 15 days; no re-apply to the same role within 90 days. Applied 5 Aug -> **clear 20 Aug**. |
| Camunda | Max 2 per 30 days |
| Siena AI | Max 3 per 60 days across all roles; no re-apply within 30 days, 90 for the same job |
| Scale AI | 90-day wait for the same role |
| ElevenLabs | Hard throttle refusing submission outright |

## 8. Practical

- **Use the in-app browser, not headless.** His join.com login lives there, Greenhouse autofill behaves, headless-from-datacentre trips Cloudflare, and he can watch — he caught the Reflection application mid-flow that way.
- **Bash `cd` does not persist between calls.** Prefix every command with `cd <working dir> &&`.
- Letters: `python3 make_letter.py --in x.json --out "X_Motivation_Letter.pdf"` with keys role, location, date, opening, role_specific, closing.
