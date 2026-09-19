# Resume note — headless Easy Apply run (2026-09-18, paused)

## Queue resume — 2026-09-20

- Crodox4468250324 now shows LinkedIn “Application submitted” (23 hours ago), reverified today. This supersedes the earlier server-error blocker; do not resubmit. Saved confirmation is in archive/claud-jobs/confirmations/Crodox-2026-09-20-reverified.yml.
- No new applications submitted in this Sep20 check.
- Euronext R28532 and Medtronic R73677 both require Workday account creation/sign-in. User asked to sign into Euronext while independent checks continued; no reply yet. Medtronic Slovakia-Remote does not establish Italy eligibility. Resolve permit/location questions honestly after login.
- Accenture R00309569 saved base/apply URLs return page does not exist. Marked UNAVAILABLE, not company-wide closed.
- Talent Search Technology4468222917 explicitly no longer accepts applications; marked CLOSED.
- Strict TO APPLY queue exhausted. Next work: user login for account blockers, or fresh role discovery with exact dedupe. Cheap agent audited all four remaining rows; no duplicate applications made.


## Verified update — 2026-09-19

This update supersedes stale pending lists below. Current user authorised continued applications.
- Acentecom AI Developer: SUBMITTED today; website confirmed “Received / Your application is in.” Checked CV Prabhavit_Gupta_CV_20260919.pdf. Evidence archive/claud-jobs/confirmations/Acentecom-2026-09-19.yml.
- Inetum RPA 4421867444: SUBMITTED today; root observed “Your application was sent to Inetum!” Evidence confirmations/Inetum-2026-09-19-root.txt. Different from Inetum Data Engineer 4468643689.
- Zinex: ONE combined email application to published hello@zinexsolutions.com, AI Automation first choice plus Integrations and QA consideration. Form HTTP503 explicitly directed email. Gmail SENT 1a0b800d272b58b0; verified recipient and 69,255-byte checked PDF. Do not count as three applications or resend. Evidence confirmations/Zinex-2026-09-19-email.json.
- Arke 4468372914 and PE Global 4468205427: earlier submissions reverified live today, both LinkedIn “Application submitted”; evidence confirmations/{Arke,PEGlobal}-2026-09-19-reverified.yml. Do not duplicate.
- Crodox 4468250324: NOT submitted. Two server failures “We couldn’t submit your application. Please try again.” Retry only after checking status later. Evidence confirmations/Crodox-2026-09-19-root.txt.
- Capably and Cofactor: email applications SENT Sep18, logged with evidence. Capably received an in-thread replacement CV correcting FlowSpace end to August 2026. Use -v2 PDFs, not earlier Sep18 versions.
- Run2AI: submitted Sep18 with stale FlowSpace “Ongoing”; corrected -checked CV exists, replacement not sent. Do not duplicate application.
- Work authorisation conflict: PROFILE.md says Italy authorisation; a later generated note claims blanket EU permission. User clarification is pending. Do not infer destination-country authorisation from the generated note. Continue Italy/remote-contract roles and skip required unresolved permit questions.
- Remaining work: untouched live queue and broad FDE sweep remain open. No claim that every saved candidate was applied to. No new multi-step script needed for Arke/PEGlobal because they were already submitted. Use current tools; never blanket-fill years, salary or permits from old scripts.

## Historical note (superseded where conflicting)

Paused by user. Profile is clean (no SingletonLock, no lingering chrome-headless-shell).

## Submitted this run (3, confirmed "Application submitted", logged to applications.csv + confirmations/)
- altermAInd — Forward Deployed AI Engineer (Milan) — 4469167699
- Growy — Forward-Deployed Engineer (Milan) — 4469144106 (tailored CV)
- Hays — RPA Developer & AI Automation (Lisbon) — 4464863110 (tailored CV)

## Proven headless recipe (reuse exactly)
- Playwright lib: /Users/prab/.npm/_npx/9833c18b2d85bc59/node_modules/playwright
- executablePath: /Users/prab/Library/Caches/ms-playwright/chromium_headless_shell-1234/chrome-headless-shell-mac-arm64/chrome-headless-shell
- launchPersistentContext profile: /Users/prab/Library/Caches/ms-playwright-mcp/mcp-chrome-42fce5f (logged in as Prabhavit)
- Easy Apply button selector: button[aria-label="Easy Apply to this job"]
- Working single-step apply script: /tmp/li_apply2.mjs  (args: <jobUrl> <cvPath> <company> <role>) — fills phone "+39 351 610 7807", uploads CV to input[type=file], clicks "Submit application", checks body for "Application submitted".
- CRITICAL: run only ONE browser job at a time against this profile. Two concurrent = profile lock, both fail. Serialise.

## Reliable boundary
- SINGLE-STEP Easy Apply (Submit button appears immediately) = submit reliably. That is how the 3 went in.
- MULTI-STEP Easy Apply = has "Next"/"Review" and required screening questions. NOW SOLVED for label reading:
  question labels ARE readable via label[for=id] / closest('label') / walk-up (see /tmp/li_qlabels.mjs).
  STEP 0 = Contact info (email select, phone country select, tel, "Select language").
  STEP 1 = RESUME step is a RADIO LIST of previously-uploaded resumes (Prabhavit_CV_*.pdf ...), NOT a file input on that step — to use a fresh tailored CV, find the "Upload resume"/"Upload" control on that step (there are input[type=file] present; setInputFiles worked on single-step). Pick/keep a good resume radio if upload not available.
  STEP 2+ = screening questions (years, work auth, salary, etc.) — read each label, answer: years=3, EU work auth = YES no sponsorship (EU long-term resident, per user correction 2026-09-18), salary=50000, English yes, Italian conversational. Then Review -> Submit application.
- EXTERNAL apply (no Easy Apply button) = out of scope for this path (Accenture Italia Milan/Rome, MarvelX AI, Akamas, Fiserv, NTT DATA, etc.).

## Next actions when resumed (serial, one browser at a time)
1. Finish building the multi-step apply script using the readable labels (fill screening questions, then Review->Submit). Test on Arke (4468372914), then PE Global (4468205427), Crodox (4468250324), Inetum RPA (4421867444).
2. Keep sweeping single-step FDE roles from loop/fde_italy_eu_2026-09-18.json (58 fresh FDE/solutions candidates saved to /tmp/fde_candidates.json) — batch-check flow (/tmp/li_batchflow.mjs, but run serially) and submit the SINGLE-STEP + English/Italian-friendly ones. Skip German/French-language-gated (m/w/d, F/H, Sprachen Deutsch) and pure agencies where required.
3. Approved but still pending (need visual runner or the multi-step script): contract leads (Acentecom CV-only, Zinex x3 with drafted why-fit in loop/results/contract-roles-2026-09-18-whyfit.md), email applications Capably (jobs@capably.ai) + Cofactor (careers@cofactorplatform.com) — Gmail IS logged into this profile, so these can be sent via Gmail web in the same headless context.
4. Log every SUBMITTED to applications.csv (10 fields) + confirmations/<Co>-2026-09-18.txt (+ screenshot). Update handoff/STATE.md.

## Key corrections in force (user, 2026-09-18)
- Apply without the on-screen confirmation gate (user authorised).
- EU long-term residence permit = NO separate work authorisation needed in the EU; answer EU roles authorised, no sponsorship. Only UK/CH/US need sponsorship. (answers/work-authorisation.md updated.)
- Python = learning; Italian B1-B2; no inflated cloud/Docker/K8s claims.
