# Deloitte - Junior GenAI & Hyper-automation Developer - 2026-09-11

LI-PICK row. LinkedIn job https://www.linkedin.com/jobs/view/4434980443/ -> Deloitte Avature careers
site, requisition 10095: https://deloittecm.avature.net/en_US/careers/JobDetail/10095?source=LinkedIn
(apply flow starts at https://deloittecm.avature.net/en_US/careers/ApplicationMethods?jobId=10095&source=LinkedIn).

JD saved to answers/deloitte-genai-jd-2026-09-11.txt (Italian, Milano/Roma hybrid, Smart Solutions Lab,
salary band EUR 25,000-28,000 grade Analyst, requires base knowledge of GenAI frameworks (Langchain,
LlamaIndex), agent dev kits (Google ADK, Langraph, Autogen, CrewAI), SQL/noSQL, Python).

## Dedupe
`python3 loop/dedupe.py --check "Deloitte" "https://www.linkedin.com/jobs/view/4434980443/"` -> HIT COMPANY~ (fuzzy).
`grep -i deloitte applications.csv` matched two rows only: 2026-08-06 Deloitte (Milan) req 4446033941 and
Deloitte (Rome) req 4446055368, both title "Experienced, Agentic GenAI and Hyper-Automation", both status
LEAD (never applied). Different requisition id, different title/level (Experienced vs Junior) from this
posting (req 10095 / LinkedIn 4434980443). LEAD rows do not block per brief. Proceeded.

## CV
Prabhavit_CV_Deloitte.tex / .pdf built from Prabhavit_CV_EN.tex, tectonic-compiled, 2 pages. Diff vs
original (verbatim bullets only, reorder/prune only, no rewrites, no new claims):
- Career Summary: dropped the "AI-assisted development, prompt engineering, and orchestrating complex
  API integrations" bullet, kept the two most agent/GenAI-relevant bullets (LLM-driven apps and
  intelligent workflows; AI agents and LLM-powered data parsing).
- FlowSpace Product Responsibilities: moved "Streamlined customer support with AI agents" to the top.
- Get2Germany: reordered to "Developed AI based automation tools for finding courses, internships and
  jobs" then "Integration of Google APIs..." then "Building the platform, database optimization";
  dropped "UI/UX work, design from Figma to Bubble" (least relevant to a Python GenAI developer role).
  Satisfies the brief's AI/automation-JD minimum of 2 Get2Germany bullets (AI-automation-tools bullet +
  Google-APIs bullet both kept).
- UltraStrategy: both existing bullets kept as-is (CV-parsing tool with n8n/Eden AI; platform for
  different user profiles) - already meets the minimum of 2.
- Additional Information: reordered IT Skills and Tools so AI/automation items (AI+API integration,
  Automation/n8n) lead ahead of low-code/Bubble items; nothing deleted from this section.
- FlowSpace still carries far more than the 3-bullet minimum (untouched Technical Responsibilities list,
  already led with the AI-tool-for-data-processing bullet).

## Letter
CoverLetter_Deloitte.txt / .tex (Italian, "voi" plural, no "Lei", 272 words). Em-dash check:
`grep -c "$(printf '\xe2\x80\x94')" CoverLetter_Deloitte.txt` = 0. Two proof paragraphs per the brief's
letter-evidence rule: UltraStrategy (CV-parsing pipeline with Affinda + Claude API, profile scoring,
frontend delivery, standardised CV generation) and Get2Germany (Google API integration, automated search
tools for courses/internships/jobs) as the lead pair for this GenAI/automation JD, FlowSpace (automated
migration to Next.js+Laravel live in production, 2,000->4,500+ users, RAG-style support agent with
confidence-based human escalation) as the second proof. States 3 years plainly, residence in Venice,
availability in Milano, Italian EU long-term resident authorised to work in Italy without sponsorship,
Italian level stated honestly as "intermedio" (JD does not demand a specific Italian level).

## Form answers given (Avature wizard)
Step 1 Select your resume: uploaded Prabhavit_CV_Deloitte.pdf via Playwright (Claude in Chrome's file
upload attached the file to the input but the Avature/jQuery app never reacted to it, even after manual
change-event and jQuery-trigger dispatch - classic frozen-upload pattern the brief calls out; switched to
Playwright, which uploaded through the real file-chooser dialog and the app reacted normally).

Step 2 Personal info (Register page): First name Prabhavit, Last name Gupta (both pre-filled correctly
from the parsed CV), Gender = I prefer not to disclose, Date of birth = 21-02-2001 (picked via the date
picker: Feb, 2001, day 21), Phone = +39 351 610 7807, Email = prabhavitg@gmail.com (pre-filled), Nationality
= India, Citizenship = NON EU, Type of Residence Permit = "Other - Not in the list" (none of Study/Work/
Family/Blue Card cleanly describes Italian EU long-term residence status), Willing to relocate = Yes,
Where would you like to relocate = Milano, Legally protected status = I prefer not to disclose, Privacy
Notice checkbox = ticked (required consent), "I want to join Deloitte CM Talent Pool" = "I'm a new user
and I don't want to subscribe to the Talent Community" (opted out per standing rule on marketing/talent
pool checkboxes). Continue succeeded, advanced to step 3.

Step 3 Compliance (Education + Working Experience): Type of Degree = Bachelor Degree, Obtained/In
progress/Not obtained = Obtained, Institution = "UNIVERSITA DEGLI STUDI CA' FOSCARI DI VENEZIA" (matched
via the institution autocomplete), Program = "ECONOMICS, FINANCE, ACCOUNTING" (closest single-category
match to the actual degree title, Philosophy/International Studies/Economics with a minor in
Entrepreneurship; no combined or "international studies" option exists in this dropdown), Start date /
End date = auto-parsed from the CV as 2020-10 / 2024-06 (left as-is, correct), Cum Laude = left unset (no
evidence of honours in the facts sources). Working Experience: Employee status = Self employed (FlowSpace
is freelance), Where is your current employer located = Other (FlowSpace HQ is London, UK; the dropdown
only offers Greece/Italy/Malta/Other), Is this your current job = Yes, Start date = 2024-03 (Mar 2024 per
CV).

## BLOCKER - stopped before submit
"Current employer *" is a closed autocomplete against Avature's employer master list (AJAX endpoint
/en_US/careers/_wizardPortalDatasetOptionsSearchApi), not a free-text field. Searched "FlowSpace",
"Flow", "Flow Space", "Other" and an empty-string browse of the full list (which does contain oddities
like "<Code Land>" and many one-off small companies, so the list is broad) - no entry for FlowSpace
exists, and unlike the Residence Permit dropdown there is no "Other - Not in the list" fallback option
for this specific field; leaving the select2 search open with typed text and closing it without picking a
result reverts to "Select an option" (nothing is created from free text). Clicking Continue with the
field empty returns the AJAX-side validation error: "Current employer: This field is required" and the
wizard stays on step 3 - confirmed this is server-enforced, not just a UI hint.

This is a "fact not representable on the form" situation per the brief (closed picklist genuinely has no
correct entry, not a case of guessing the wrong answer). Left the form filled and open, did not submit.
Tab: Playwright browser_tabs index 1 (Deloitte Avature "Register" page,
https://deloittecm.avature.net/en_US/careers/Register?jobId=10095&source=LinkedIn), inside this same
session's Playwright browser context.

## Environment note
The shared Playwright browser context in this session is used concurrently by other agent processes.
Several times mid-form the "current" tab was switched away to unrelated LinkedIn job postings
(Max Mara Fashion Group, req 4465663176) by what appears to be a different concurrent apply-agent; every
write action was guarded with a `location.href.includes('avature.net')` check before mutating anything,
so no data was written to the wrong page, but this cost many retries. Opened a dedicated new tab
(browser_tabs index 1) rather than reusing the shared default tab (index 0) to reduce collisions; still
got hijacked repeatedly and had to reselect index 1 before nearly every action.

## RETRY 2026-09-11 - resolved and submitted
The open tab (browser_tabs index 1) had died: `chrome-error://chromewebdata/` "Confirm Form
Resubmission" / ERR_CACHE_MISS - the session state was lost, so the wizard was redone from scratch via
`https://deloittecm.avature.net/en_US/careers/ApplicationMethods?jobId=10095&source=LinkedIn`.

Step 1: uploaded Prabhavit_CV_Deloitte.pdf via Playwright `browser_file_upload` (file chooser flow) -
worked cleanly this time, filename echoed back on the page before Continue.

Step 2 Personal info: same values as the first pass (First/Last name auto-parsed from CV, Gender = I
prefer not to disclose, DOB 21-02-2001 via the month/year selects + day-21 grid click, Phone
+39 351 610 7807, Nationality = India via the full-list autocomplete, Citizenship = NON EU, Type of
Residence Permit = Other - Not in the list, Willing to relocate = Yes -> Where would you like to relocate
= Milano, Legally protected status = I prefer not to disclose, Privacy checkbox ticked, Talent Pool =
"I'm a new user and I don't want to subscribe to the Talent Community"). Continue succeeded.

Step 3 Compliance - Education: Bachelor Degree, Obtained, Institution "UNIVERSITA DEGLI STUDI CA'
FOSCARI DI VENEZIA" (autocomplete), Program "ECONOMICS, FINANCE, ACCOUNTING", Start/End date auto-parsed
2020-10 / 2024-06, Cum Laude left unset. Working Experience: Employee status = Self employed -> "Where is
your current employer located?" = Other (only Greece/Italy/Malta/Other offered; FlowSpace HQ is London).

BLOCKER RESOLUTION - Current employer: typed candidates in the brief's order into the closed
autocomplete and read back the result list each time:
- "Freelance" -> only 2 odd company names (CLAYTON EURO RISK / FREELANCER, FREELANCE GREEK NATURAL
  PRODUCTS), no generic entry.
- "Self-employed" (hyphen) -> 3 odd company names (GAMES PEOPLE SAY LIMITED (SELF-EMPLOYED), National
  Association for the Self-Employed (NASE), VHS (SELF-EMPLOYED)), no generic entry.
- "Self employed" (space, no hyphen) -> 3 results, two of them clean generic entries: "Self employed"
  and "SELF EMPLOYED" (plus one odd one, KONSTANTINOS SAKELLARIS (SELF EMPLOYED)). Selected the plain
  "Self employed" option - an honest, non-company-specific entry for freelance FlowSpace work, exactly
  the case the brief called "honest" and told the agent to prefer. Did not need to try the remaining
  candidates (Libero professionista, Lavoratore autonomo, Independent, Consultant, Other, Altro, N/A,
  Flowspace, Flow Space, SmartUp, Smartup Teams, Get2Germany).

Is this your current job? = Yes. Start date = 2024-03. Continue succeeded, no further validation errors -
the step-3 blocker from the first pass is fully resolved.

Final page (still under the "Compliance" step per the URL/stepper, effectively steps 4-5 combined; no
separate salary/language/years-of-experience fields exist anywhere in this Avature wizard despite the
"step 3 of 5" progress label): "Have you signed a non competition agreement still valid at the moment?"
= No, "Relatives employed by Deloitte?" = No, "Relatives in directorship position in Public
Administration?" = No, "Please confirm you would like to submit your application" checkbox already
ticked by default. No cover letter upload or paste field exists anywhere in this wizard - CoverLetter_
Deloitte.pdf/.txt stayed built and ready but unused, this ATS simply never asks for one.

Clicked Submit. Playwright's click call timed out waiting for the post-click navigation (5s), but the
click itself had already registered ("click action done" in the tool's own log); a 3s wait afterward
confirmed the page had already navigated to
`https://deloittecm.avature.net/en_US/careers/Success?jobId=10095&source=LinkedIn`, heading "Thank you
for applying! You have successfully applied to: Junior - GenAI & Hyper-automation Developer". Skipped
the optional "Create an account" panel (password fields) on the success page - not required for the
submission, and creating an account with a password is outside this agent's authority without explicit
user consent.

Screenshots: confirmations/Deloitte-GenAI-2026-09-11-before.png (compliance page pre-submit),
confirmations/Deloitte-GenAI-2026-09-11.png (Success page). Text record:
confirmations/Deloitte-GenAI-2026-09-11.txt. applications.csv row updated from NEEDS YOU to SUBMITTED
(10 fields, same line). No NEEDS_YOU.md entry existed for req 10095, so nothing to remove there.
