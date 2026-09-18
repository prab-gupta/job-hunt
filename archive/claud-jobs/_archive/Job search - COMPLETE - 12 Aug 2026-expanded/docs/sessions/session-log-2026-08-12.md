# Session log — 12 August 2026

What was asked, what was done, in order. Kept so a future session can see how the work actually ran, not just its output.

---

## What he asked for, in his words

1. Finish the Otherworldly application and keep applying down the FDE queue
2. "keep going with cv only my g"
3. "make sure you put the latest cv in join.com applications"
4. "for these roles make a tab in the sheet and say need follow up and attach the company applied's linkedin"
5. "i just submitted reflection's applicqation dont ignore uk based roles"
6. "APPLY FOR REASONABLE AI NOW" / "SAY NO TO UK AUTHORISED WHO CARES" / "I WANT TO CHANCE ANYWAY"
7. "go on keep applying if you run out then research and start applying"
8. "can you use the in app browser? it would be faster and efficient no?"
9. "do a deep dive to find new relevant roles for me"
10. **"make baseline 40-50k otherwise adjust with the number quoted"** — rule change
11. **"describe a project, you answered wrong"** — correction
12. **"only write answers and cover letters for jobs which are low match pls"** + **"others i will write the cover letter"** — rule change
13. "continue apply only-cv roles until you exhaust the list"
14. "from my profile and cv what are my blindspots that i have not aimed for?"
15. "run a sweep using everything" → "do a even deeper sweep, look for more sources" → "and from all the sheets you have generated make sure you dont repeat"
16. "document all our convo and your research, cv, applications, mode of working, everything"

---

## What happened

**42 applications submitted** during this session, on top of 38 from earlier sessions. Full list in `master-application-log.md`.

**Three rule changes he made mid-session**, all now in `working-rules.md`:

- Salary baseline 30–40k → **40–50k, aligning up to a disclosed band**
- Cover letters and long answers **only for weak-match roles**; he writes the strong-match ones
- Every answer **stays on the question asked** (added after the Lleverage error)

**One mistake I made and he caught:** at Lleverage I answered "describe a project that best demonstrates your technical abilities" with the FlowSpace migration and then appended a paragraph about the Dutch work permit. It reads as though the answer to a technical question is visa admin. Recruitee applications can't be edited, so it stands. Rule 1.4 exists because of it.

**One mistake I caught myself before submitting:** a draft answer at Duvo claimed he "moved to Venice from India at eighteen" and "studied in a language I had to learn". Neither is established anywhere, and the second contradicts his Italian being beginner level. Rewritten from known facts only. Worth flagging as a pattern: **inferring biographical colour is the most likely way to put a lie in front of an employer.**

**The blindspot analysis** (his question 14) produced eight categories from his own CV that he had never aimed at, and the sweep that followed immediately found Miaplaza (€51–90k, Playwright + TypeScript, 2+ years) and Avenga (his Microsoft certs restated as a job spec). Details in `blindspot-sweep-2026-08-12.md`.

**The session's web search budget hit 200/200**, so two agents — VC portfolio boards and national/Italian job boards — could not run a single search. That slice is untouched, not empty.

---

## How the work ran, practically

- **Browser over headless.** His join.com login lives in his own browser, Greenhouse autofill behaves there, headless-from-datacentre trips Cloudflare, and he can watch. He caught the Reflection application mid-flow that way and told me he'd already sent it.
- **Research fanned out to parallel subagents; applications done one at a time.** Browser automation doesn't parallelise — concurrent agents fight over tabs.
- **Every application logged as JSON immediately** with the verbatim confirmation, the answers given, and the judgement calls made. That log is what every sheet and doc is built from.
- **Screenshot-verify after every combobox and file upload.** Both Ashby location overwrites were caught this way, and both would otherwise have submitted silently wrong.

---

## Standing observation for whoever picks this up

He responds well to being told plainly what was decided on his behalf and what was refused. Twice this session he corrected a rule immediately after seeing a judgement call written out — the salary baseline and the cover-letter policy both changed that way. **Surfacing the decision is what lets him steer.** Don't bury it.
