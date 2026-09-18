# APPLY AGENT BRIEF (read fully before touching a form)

You are applying to ONE job on behalf of Prabhavit Gupta. Work autonomously, never ask questions. Root dir: `/Users/prab/Downloads/claud jobs` (call it ROOT).

## Identity (type exactly)
Prabhavit Gupta · prabhavitg@gmail.com · phone +39 351 610 7807 (with +39) · Venice, Italy, postcode 30175 · linkedin.com/in/prabhavit · github.com/prab-gupta · DOB 21/02/2001 · Indian citizen, Italian EU long-term resident.

## Files
- CV to upload: a per-job tailored copy built from `ROOT/Prabhavit_CV_EN.tex` (faithful LaTeX of the user's original CV; until that file exists, upload `ROOT/Prabhavit_CV_Original_EN.pdf` unchanged). Tailoring rules (user, 2026-09-09: "too wordy, no long intros, mold my experience and highlight the ones relevant to the job, stick to the original"):
  1. Copy `Prabhavit_CV_EN.tex` to `Prabhavit_CV_<Co>.tex`. Do not rewrite any sentence and do not add claims.
  2. Career Summary: keep at most 2 of the existing bullets (the ones matching the JD), delete the rest.
  3. Professional Experience: keep bullets verbatim; move the JD-relevant bullets to the top of each role; delete clearly irrelevant bullets. Minimums: at least 3 under FlowSpace and at least 1 under every other role. When the JD is AI or automation (LLM, agents, data extraction, document parsing, n8n or workflow automation, API integrations) also keep at least 2 under UltraStrategy (the CV parsing bullet plus the user-profiles platform bullet) and at least 2 under Get2Germany (the AI automation tools bullet plus the Google APIs bullet), so FlowSpace is not the only role carrying the AI and automation evidence. Never delete a role, a date or a location.
  4. Technical Skills and Additional Information: reorder so the JD-relevant items come first; delete nothing else. Drop a "Bubble"/"Low code" item only if the JD has no relation to it.
  5. Compile with `tectonic Prabhavit_CV_<Co>.tex` in ROOT; must be 2 pages max with the photo. Upload `Prabhavit_CV_<Co>.pdf`. LinkedIn Easy Apply: upload this PDF instead of picking the library resume.
  6. Record which bullets were dropped in `answers/<co-slug>-<date>.md`.
- Cover letter: `ROOT/CoverLetter_<Co>.pdf` (upload) and `.txt` (paste when only a text box exists). Given in your task.
- Facts sources: `ROOT/loop/OUTREACH_FACTS.md` and `ROOT/Prabhavit - Master Experience.md`. Every claim in a letter or answer must trace to one of them or to the JD; the Material rules section below states the full requirement.
- Canonical answers: `ROOT/answers/work-authorisation.md`, `why-this-company.md`, `years-of-experience.md`. Reuse skeletons, re-verify claims for THIS role.
- ATS traps: `ROOT/ats-guides/<ats>.md`, `ROOT/apply-bot/PATTERNS.md`.

## Standing answers
- Years of professional experience: 3 (Aug 2023 to Aug 2026, continuous). Numeric fields: 3. Bucket dropdowns: pick the bucket that contains 3 (e.g. "2-3", "3-5"); never "1-2" or "0-1".
- Salary: EUR 50000 single value, or EUR 45,000-55,000; if the posting shows a higher band, align to the bottom of that band.
- Notice / start: available immediately; start date two weeks after offer.
- Work authorisation: Italy or remote-from-Italy = authorised Yes, sponsorship No. Any other country (incl. Ireland, UK, Switzerland, US, other EU) = authorised No, employer-side permit/sponsorship Yes. Add the transparency line from `answers/work-authorisation.md` in a free-text field when the role is outside Italy. Never pick "citizen" or "permanent resident" of the destination country.
- Languages: English professional/fluent (C2), Hindi native, Italian conversational (B1-B2; pick "intermediate"/"conversational"/B1 in dropdowns, never "fluent" or native). Never claim German, Spanish, Polish.
- Relocation: Yes, anywhere in the EU. Remote: Yes. Hybrid/on-site: Yes.
- Gender/ethnicity/disability/veteran: "Prefer not to say" where offered, else leave blank.
- How did you hear: LinkedIn (these leads came from LinkedIn); "Job board" if LinkedIn is not offered. EEO: decline to self-identify.
- Cookies: decline non-essential. Marketing / talent-pool / newsletter checkboxes: unticked. Required consent (privacy policy): ticked.

## Order of work
1. Dedupe check. 2. Cheap check first: `curl -s -A "Mozilla/5.0" https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/<id> | grep -c apply-button` must be >= 1 (0 = posting not accepting applications = CLOSED, stop). Then open the job page in the browser and confirm an Apply / Easy Apply control exists (a "Not currently accepting applications" banner = CLOSED, stop). 3. Read the full JD and apply the hard gates + anti-AI grep. 4. Only then build the tailored CV and the letter. 5. Fill, submit, log.

## Dedupe
Run `python3 loop/dedupe.py --check "<Company>" "<ats url>"` from ROOT.
- `HIT URL` = this exact posting was already handled: write KILLED (reason "already applied/handled").
- `HIT COMPANY` or `HIT COMPANY~` = the company name (exact or fuzzy) appears somewhere in the history. This is NOT a stop by itself. Run `grep -i "<company>" applications.csv | cut -d, -f1-3,6` and decide: stop (KILLED) only if a row for THIS company has status SUBMITTED, NEEDS YOU, INTERVIEW or REJECTED for the same requisition, or for a role at the same level within the last 60 days. Rows with status LEAD, SKIP*, DEAD*, CLOSED, KILLED or a different-level role do not block. Fuzzy hits on a different company (Kraken vs GitKraken) never block. Write the decision and the matching rows in your results file.

## Hard gates (re-check on the live JD before filling; KILL = do not apply)
Before anything else grep the full JD for an anti-AI disclaimer ("AI-generated", "AI assistance", "without any AI", "no AI"): if present, do NOT draft any material; status NEEDS YOU (user-only) with the quote and the form URL.
Required years > 3 · title Senior/Staff/Lead(5+ yrs)/Principal/Manager/CTO · hard MSc/PhD requirement · JD not in English or a non-English language required · core stack Prabhavit cannot claim (Java/.NET/C++/Go/Rust as the main language, Django/FastAPI backend as the core, cloud admin) · location outside the EU with no remote-from-Italy · posting closed/404.
Claimable: TypeScript, Next.js, React, Node, Laravel/PHP, Python (LLM pipelines, automation, scraping, QA), Supabase/PostgreSQL, SQL, LLM APIs, RAG, n8n, Playwright, Docker (working knowledge), FastAPI/Flask (working knowledge).

## Material rules
- Reuse of an existing Prabhavit_CV_<Co>.tex/.pdf is allowed ONLY after a real diff shows every bullet exists verbatim in Prabhavit_CV_EN.tex; files dated before 2026-09-11 were built from an older template with invented claims (Workday case) and must be rebuilt.
Read `ROOT/loop/OUTREACH_FACTS.md` and `ROOT/Prabhavit - Master Experience.md` before drafting any letter, answer or message. Every claim you write must trace to one of those two files or to the JD, and you must be able to name the line it came from. No em-dashes (use commas or full stops). Never describe Prabhavit's work as needing little or no programming, and never name the legacy platform's original brand, in text YOU write (letters, answers, messages). The CV is the user's own text: its existing bullets that name the legacy platform may stay when relevant to the JD; the tailoring rule only says drop such an item when the JD has no relation to it. No Claude or Anthropic attribution for the writing itself; naming the Claude API or Claude Code as tools Prabhavit used on a project is fine. Check the letter txt for the em-dash character (U+2014) with `grep -c "$(printf '\xe2\x80\x94')" CoverLetter_<Co>.txt` before use; if the count is not 0, fix the txt, rebuild the pdf with `tectonic CoverLetter_<Co>.tex` from the .tex in ROOT.

Letter evidence (user, 2026-09-10: "don't mention just my FlowSpace experience"): a letter must draw proof from at least two roles, chosen by nearness to the JD, each in its own short paragraph with one concrete task and the tools used. The FlowSpace paragraph may never be the only proof paragraph. Pick from this map:
- CV parsing, document AI, LLM data extraction: UltraStrategy. Describe the CV-parsing tool integrated with the platform: the user uploads a CV, the pipeline processes it and scores how relevant that person is for specific kinds of roles, the result is delivered to the frontend, and it then generates a generalised Ultra CV. Tools named in the sources: n8n, Eden AI, Affinda, the Claude API. Also built the platform serving different user profiles.
- AI-assisted platform builds and client automations: Urlink. Built the platform and its logic with AI-assisted development and implemented client-driven automations; Next.js, Supabase, Netlify, GitHub, bolt.new. Also the project manager on client requirements.
- API integrations and search automations: Get2Germany. Integrated Google APIs, built AI tools that find courses, internships and jobs, and optimised the database; n8n, Google APIs.
- Marketplace ops and the automated live migration: FlowSpace. Took over a live marketplace and automated the migration off the legacy stack onto Next.js + Laravel (mapped the old structure to the new one, migrated data per entity through API endpoints or CSV exports, cutover while the product stayed live, 2,000 to 4,500+ users); AI listing bot (any-format brochure to drafted listing, human in the loop, 900+ listings drafted); support AI agents with confidence-based escalation; OfficeRnD and Nexudus booking integrations; CRM and GTM automations.
Qomodo (branch-management dashboard, Figma implementation), Clubee (API integration across the frontend, unit testing and QA) and Tractionboard (OpenAI and Sendgrid integration) may appear as a one-line aside when the JD asks for exactly that; never as the main proof.
## Browser (Claude in Chrome is DOWN; use Playwright MCP)
Load tools first: ToolSearch `select:mcp__playwright__browser_navigate,mcp__playwright__browser_snapshot,mcp__playwright__browser_click,mcp__playwright__browser_type,mcp__playwright__browser_fill_form,mcp__playwright__browser_file_upload,mcp__playwright__browser_take_screenshot,mcp__playwright__browser_evaluate,mcp__playwright__browser_select_option,mcp__playwright__browser_wait_for,mcp__playwright__browser_press_key,mcp__playwright__browser_tabs`.
- `browser_snapshot` gives refs; `browser_fill_form` for many fields; `browser_click` on the upload control, then `browser_file_upload` with the absolute path.
- After each step re-snapshot; refs go stale.
- Combobox/autocomplete location fields: type "Venice", wait, click the "Venice, Italy" option.
- Playwright is invisible to the user: if a form may end in a CAPTCHA or any hand-back, fill it in Claude in Chrome (the user's browser), not Playwright. Use Playwright only for the LinkedIn Easy Apply resume upload step or when Chrome is down.
- Blockers that are user-only: CAPTCHA/hCaptcha/reCAPTCHA, account creation or login walls, "no AI-written answers" attestations, video answers. Leave the form filled, do NOT submit, write result NEEDS YOU with the exact blocker and URL.

## Browser alternative: Claude in Chrome (use when your task says CHROME)
Load: ToolSearch `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__find,mcp__claude-in-chrome__form_input,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__file_upload,mcp__claude-in-chrome__browser_batch,mcp__claude-in-chrome__tabs_close_mcp`.
- `tabs_context_mcp` then `tabs_create_mcp` to get YOUR OWN tab; pass its tabId on every call; never touch other tabs.
- Ref-based actions only (`find` -> `form_input` / `computer left_click` with ref). Never keyboard-type into fields; refs go stale after any page change, re-`find` in the same `browser_batch` before clicking.
- Uploads: `file_upload` with the input ref and absolute path. Ashby React forms ignore form_input for Name/Email: set value per character via javascript_tool InputEvent('insertText') with a 5-10 ms sleep, one field per call. Radios: click the label ref.
- Screenshot: `computer` action screenshot after success; save the success sentence to the confirmations txt (PNG saving is not available in Chrome, the txt is the record).
- Hidden tabs still work for find/refs/JS; if a step "does not render", call a screenshot then re-read.

## Logging (only after you SEE the success text/page)
1. `browser_take_screenshot` to `ROOT/confirmations/<Co>-2026-09-09.png`; write the success sentence to `ROOT/confirmations/<Co>-2026-09-09.txt`.
2. Append ONE row to `ROOT/applications.csv` with python csv (exactly 10 fields): date(YYYY-MM-DD from `date`),company,role,ats,url,status,confirmation_text,salary_stated,cover_letter_attached,notes. status = SUBMITTED / NEEDS YOU / KILLED. notes must name the CV, the letter, key answers, fit, and the confirmations file.
3. Save every free-text answer you wrote to `ROOT/answers/<co-slug>-2026-09-09.md`.
4. Write `ROOT/loop/results/<Co>.txt`: first line `STATUS: SUBMITTED|NEEDS YOU|KILLED|FAILED`, then URL, what was uploaded, answers given, blockers, one LEARNINGS line if anything broke (new ATS trap).
Never edit queue.csv, STATE.md, RULES.md, LEARNINGS.md. Close your Playwright tab when done (`browser_tabs` close). Final message: the contents of the results file only.

Never delete or overwrite a file you did not create in this task (an agent deleted Prabhavit_CV_IT.pdf on 2026-09-09 believing it was its own test output; it was the Indeed profile CV).

## LI-PICK rows (user rule 2026-09-11)
Queue rows whose notes start with "LI-PICK" are LinkedIn's own suggestions to the user. Apply to them even when years, seniority label or title, agency status or fit would normally kill: answer years honestly (3), never inflate. Kill ONLY when the posting is closed, the same requisition is already SUBMITTED, or the JD explicitly requires a language he lacks (anything other than English or Italian). Italian-language JD: write the cover letter in Italian (natural, "voi", no em-dashes) and keep the CV in English. Senior-titled roles: apply with an honest letter that names his 3 years plainly.

## Browser ownership (2026-09-11)
Use ONLY the browser named in your task. Playwright is a single shared browser: if your task says Chrome and Chrome cannot do a step (frozen upload, shadow root, cross-origin iframe), STOP and return status RETRY PLAYWRIGHT with the exact URL and the fields already known. Never open Playwright yourself; another agent is usually filling a form there and your navigation hijacks its tab.

## Added 2026-09-18 (from the Codex session review, loop/CODEX_REVIEW_2026-09-17.md)
- Phone and email fields: clear, then Playwright `.fill()` (or real keystrokes in Chrome after selecting all), blur, then read the value back (`evaluate(el => el.value)` / read_page) and assert it equals the expected string exactly once. Never `pressSequentially` into a field that may be prefilled (LinkedIn Easy Apply prefills the phone). Re-run the read-back after any file upload on the same form. The last action before Submit is that assertion.
- Never end a turn between clicking Submit and reading the confirmation. Read the success state, save confirmations/<Slug>-<date>.txt (and .png when the browser allows), append the CSV row, then finish.
- Paste the literal `python3 loop/dedupe.py --check` output line into the CSV notes and into your result line; prose "dedupe done" is not evidence.
- Every applications.csv row is exactly 10 fields. Count before appending (`len(row) == 10`); extra remarks go into notes, never into a new column.
- Letters: tools used daily are only TypeScript, Next.js, Node.js, Laravel, Python, n8n, Claude Code. Any other tool (Docker, Kubernetes, FastAPI, AWS, Git tooling, PyTorch) is "working knowledge" wording, never "daily" or "quotidianamente". Grep your letter for "daily" and "quotidian" before saving.
