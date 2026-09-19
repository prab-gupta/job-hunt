# Current checkpoint

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


Snapshot date: 2026-09-18. This is an archival handoff; stale dates/tab IDs are not live state.

## Headless Easy Apply run (2026-09-18 late) — 3 SUBMITTED
User authorised applying without the on-screen confirmation gate, and corrected work authorisation: an EU long-term residence permit holder needs NO separate work authorisation in the EU (answer EU roles authorised, no sponsorship; only UK/CH/US need sponsorship — see answers/work-authorisation.md updated).
Proven headless recipe (Playwright 1.64 + chromium_headless_shell-1234 + profile mcp-chrome-42fce5f) submits SINGLE-STEP Easy Apply reliably. SUBMITTED this run: altermAInd (4469167699), Growy (4469144106), Hays (4464863110) — all "Application submitted", evidence in confirmations/ + applications.csv.
Boundary found: MULTI-STEP Easy Apply exposes required screening questions whose labels are not readable in this headless build, so they cannot be answered safely and were NOT submitted (Arke, PE Global, Crodox, Inetum RPA). External-apply jobs (no Easy Apply button): Accenture Italia Milan/Rome, MarvelX AI. Perelyn KILLED (German). Full report: loop/results/FDE-ALL-2026-09-18.md. These remaining roles need a visual/browser-capable runner (Claude-in-Chrome / Codex computer-use / the user) or reading the question labels first.

## Current request
User subsequently authorised continuing applications using cheaper agents (2026-09-18). The resume prompt in START_HERE.md is the canonical instruction. Resumed batch reconciled 2026-09-18 ~23:00 CEST (see "Evening reconciliation" below). The earlier active batch (Run2AI, Officine IADR, Cinque Terre Riviera) is now resolved; nine live Easy Apply rows remain.

## Evening reconciliation (2026-09-18 ~23:00 CEST)
Reconciled handoff/open-queue.csv against fresh evidence plus a LinkedIn guest-API liveness check of all 13 TO APPLY rows.
- SUBMITTED: Run2AI (4465998795) — evidence "Application submitted now" (confirmations/Run2AI-2026-09-18.txt).
- CLOSED: Officine IADR (4459175293) and Cinque Terre Riviera (4468374668) — both "no longer accepting"; Talent Search Technology (4468222917) — guest API no-longer-accepting marker on re-verify.
- LIVE, still TO APPLY (9): PE Global, Hays, Crodox, Inetum (RPA), Accenture FDE Dublin, Luxoft FDE Warsaw, Carpiness FDE Barcelona, Bertrandt QA Python Bucharest, Inetum Data Eng Lisbon.
- Materials: PE Global, Hays, Crodox, Inetum (RPA) were already READY (2026-09-17). The other five are now BUILT and verified (slugs AccentureDublinFDE, LuxoftFDE, Carpiness, Bertrandt, InetumDataEng) — each Prabhavit_CV_*.pdf is 2 pages and each CoverLetter_*.pdf is 1 page with 0 em-dashes; prep notes in loop/results/*-2026-09-18-prep.txt. Bertrandt and Inetum Data Eng are Python-heavy: letters state Python is learning and lead with Playwright/TypeScript/n8n. So all nine live Easy Apply rows now have materials ready.
- FDE-ALL campaign: a single agent was launched 2026-09-18 ~23:10 to harvest every LinkedIn Forward Deployed Engineer posting in Italy first then the EU, dedupe/gate, build materials, and Easy Apply via the logged-in LinkedIn profile (~/Library/Caches/ms-playwright-mcp/mcp-chrome-42fce5f). Progress (23:5x): harvest running via guest API text-location params (locationId ignored), Playwright profile NOT locked, Node+Playwright+chromium available, no 429. Gated FDE shortlist (24h harvest, deduped) saved to archive/claud-jobs/loop/fde_gated_2026-09-18.json: NEW Italy = altermAInd (4469167699), Arke (4468372914), Growy (4469144106); HIT-company Italy = Accenture Italia FDE Specialist Milan (4444007214) + Rome (4443895338). NEW EU = Perelyn FDE m/w/d (4466685759), MarvelX AI (4467866066); known-company EU = Wonderful x2, NTT DATA Europe&Latam x2 (German w/m/x), Salesforce FDE Lead, develop. Report will land at archive/claud-jobs/loop/results/FDE-ALL-2026-09-18.md when done.
- Repair: loop/results/sweep-2026-09-18-contract-validated.json (trailing-comma source fixed into a validated copy). Four verified contract survivors: Acentecom (CV-only, fit 91) and Zinex x3 (AI Automation / Integrations / QA, each requires a "Why Are You a Fit?" answer). Drafted answers in loop/results/contract-roles-2026-09-18-whyfit.md (NEEDS HIM to approve).
- Tool limit: this runtime has no browser/Gmail MCP, so the actual Submit and email-send steps remain for the browser-capable runner or the user. Capably (jobs@capably.ai) and Cofactor (careers@cofactorplatform.com) email applications remain READY_FOR_PARENT_TO_SEND.

User requested all job-search work from Claude Code and the claud jobs folder in a private GitHub repository, condensed so any agent can continue. Repository: https://github.com/prab-gupta/job-hunt. Original folder preserved.

## Last overnight application loop
Source: `archive/claud-jobs/loop/STATE.md`, updated 06:31 Europe/Rome on 2026-09-18. It reports 71 submissions on Sep 17 and three on Sep 18; those are historical reported counts, not reverified in this consolidation. The copied queue contains 13 TO APPLY and 118 NEEDS YOU variants (131 open total), differing from the older checkpoint’s 14/117. Reconcile with current evidence before resuming. Saved interviews and deadlines must be checked against current messages/calendar, not repeated as upcoming automatically.

The held Easy Apply set includes Run2AI, Officine IADR, Cinque Terre Riviera, Crodox, Inetum, Talent Search, Barden, PE Global and Hays with materials reportedly ready; five further rows include Accenture Dublin FDE, Luxoft, Carpiness, Bertrandt and Inetum Data Engineering. Exact URLs and statuses are in the queue. The historical Easy Apply cap may have reset; verify once when applying is requested.

Thirteen batch-10 outreach threads were reported as missing CV attachments. A Sep 18 08:00 repair was planned, not verified here. Check Sent and attachments before sending any repair. User-only items are in `archive/claud-jobs/NEEDS_YOU.md` and the detailed loop checkpoint.

## Most recent sweep
Three cheaper agents searched ATS, remote boards and contracts on Sep 18. They stopped on usage limits before completing follow-up passes. Saved files: `archive/claud-jobs/loop/results/sweep-2026-09-18-{ats,boards,contract}.json`. Do not claim the requested 12–20-role target was completed.

ATS file: 52 raw candidates reported, zero surviving roles. Boards file: 35 raw, one retained Sysdig Junior AI & Product Enablement Specialist (reported €29k–€36k, Italy). These source counts can overlap. Contract file has invalid JSON (trailing comma); preserve the source, validate a separate copy before consuming it. All listing claims need fresh verification before action. An agent used an outdated salary floor; no €40k floor applies to this sweep.

## Next bounded actions
1. Browser-capable runner (or the user): submit the nine live Easy Apply rows (tailored CVs ready for all nine), then the seven FDE roles in loop/results/FDE-handoff-2026-09-18.md (Italy first), then send the two ready email applications (Capably jobs@capably.ai, Cofactor careers@cofactorplatform.com).
2. The headless browser recipe is proven (see FDE-handoff file): Playwright 1.64 + chromium_headless_shell-1234 + profile mcp-chrome-42fce5f loads LinkedIn logged in. The Easy Apply click needs visual step-through (a recruiter-messaging overlay intercepted a blind click), so do the actual submit in a browser-capable session, not a blind script.
3. Present the four contract-survivor leads (Acentecom CV-only; Zinex x3 with drafted "why fit") to the user for a go/approve decision before any submission.
4. Update handoff/open-queue.csv and this checkpoint again after each action; keep status, attempt and evidence separate.

## Other known uncertainty
Mediatica submission in the earlier Codex run was not confirmed before interruption; Metes was only at upload. Do not infer their present status from that older turn. Yuxme had a salary question. Check later Claude results/queue before reapplying. Lexroom Python preparation is copied under `archive/interview-prep/python-drills`; verify current interview needs.
