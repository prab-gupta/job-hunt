# BLINDSPOTS 2026-09-06

23 verified findings + 6 unverified gaps over applications.csv (3728 rows), loop/gmail_threads.jsonl (326 threads since Aug 18), loop/SCORECARD.md, OUTREACH-TRACKER.md, 93 CV .tex files, github.com/prab-gupta. Refuted findings dropped. Numbers are the corrected ones from verification, not the draft claims.

## 1. Do this week

1. **Send the outreach that is already written.** OUTREACH-TRACKER.md: 5 Round-1 follow-ups (overdue since Aug 25) + 10 Round-2 first touches (Nexudus, Make, Tally, Flexas, Deskeo, Upflex, Retool, Mews, Anchor Offices, Cofoundry). Paste the DM-templates.md Founder cold DM verbatim. Then 15-20 connects/day from LINKEDIN-CONNECT-LIST.md.
   Metric: tracker boxes checked 0/16 -> 16/16 by Sep 13; outreach replies in loop/outreach.csv vs cold-ATS interviews.
2. **Clear live verify links today, before any sweep.** Huzzle Luna chat (4 nudges, last Sep 5). Axmed continuation link in prabhavitg@gmail.com from Sep 3 (fit 74). Then every NEEDS_YOU.md item older than 24h (19 tracked; Leadtech already died at 31 days).
   Metric: age of oldest open VERIFY/ACTION_REQUIRED/NEEDS YOU row: 744h -> under 24h.
3. **Apply by hand to the 5 consultancy leads already in the CSV.** Deloitte Milan + Rome "Experienced, Agentic GenAI and Hyper-Automation", Kirey Rome "GEN AI ENGINEER" (all LEAD since Aug 6), Capgemini NL, Accenture Italia "AI Native Software Engineering Analyst" (Workday auth gate, NEEDS YOU).
   Metric: consultancy-tier SUBMITTED 3 -> 8.
4. **15 minutes on the profile/materials contradiction.** github.com/settings/profile: drop "No-code roots, real-code delivery" from the bio. Customize pins: unpin landmark-space-booking, seo-crawler, jethr-netto-calculator; keep llm-doc-parser + the prab-gupta README. CV template Summary sentence 1: add "scaled FlowSpace from 2,000 to 4,500+ users". Log in to LinkedIn and check headline/About for "Bubble" or "no-code" (never audited).
   Metric: interview-class reply rate (22/326 = 6.7%) for submits after Sep 7 vs before.
5. **Stop the self-inflicted data damage.** Mark the 11 Nearform Senior/Lead LEAD rows (Aug 26 sweep) SKIP. CSV append step: dict keyed by the 10 header names, csv.writer QUOTE_ALL, reject any status outside the RULES.md vocabulary, skip if the URL already has a SUBMITTED row. Reconcile the 22 SCORECARD INTERVIEW+VERIFY names against the CSV and backfill the missing rows (TOPdesk, Mayerfeld, rembrandtadvantage, Ethos, Bending Spoons, Freedom24 Jul 31).
   Metric: malformed rows per sweep 0; duplicate-SUBMITTED URLs 14 -> 0; interview-class companies without a CSV row 7 -> 0.

## 2. What the data says

- 326 Gmail threads since Aug 18: 14 INTERVIEW, 8 VERIFY, 39 REJECT, 253 pure ACK. Interview-class = 22/326 = 6.7%.
- 7 of 11 interview-class companies have no applications.csv row (TOPdesk, Mayerfeld, rembrandtadvantage, Ethos among them). The FeverUp row behind the Sep 3 interview is itself a malformed row.
- 211/3728 rows (5.7%) malformed; 208 of them fall on 7 sweep dates (Aug 26-28, Sep 2-5), the same days interview signal arrived. Date token sits in 7 different column positions = several broken writers.
- 703 distinct status strings for about 10 real states. 125 URLs appear more than once; 87 carry conflicting statuses for the same posting.
- 14 URLs have 2+ SUBMITTED rows (Mastra Customer Engineer submitted Sep 3, 4 and 5).
- 37/348 SUBMITTED rows (10.6%) carry a Senior title against ~3 yrs experience. Nearform rejected on "Python + senior bar" Aug 12 and received a Senior Python & AI submit Sep 2.
- Consultancy tier: 3 SUBMITTED of 36 rows (8%). Every interview so far came from mid-market/agency shops (TOPdesk, Nearform, Fever, Telnyx).
- Warm outreach: 0/16 and 0/73 boxes checked since Aug 18-19. Cold volume: 197/298 dated SUBMITTED rows (66%) landed after Aug 20. Zero sent replies from prabhavit in tracked mail.
- Sweep yield: 68+ rounds, last ~50 produced 0-1 new apps each. Sep 1-6 submits: 57 rows vs ~190+ in August.
- GitHub: bio contains "No-code roots"; 88/93 CVs forbid that phrase; first pinned repo = 1 commit, no README, no description. Zero of 326 threads mention GitHub.
- CV: Summary is 5 sentences, zero numbers. The only hard metric (2,000 to 4,500+ users) is Experience bullet 5, line 72.
- ATS mix of SUBMITTED: Ashby 27.4%, Greenhouse 15.9%, Workable 7.8%, Lever 2.9%.

## 3. Findings by lens

### Targeting
- **Tracker blind to 40%+ of interview signal (high).** 7/11 interview companies absent from CSV; 211 malformed rows silently dropped by any parse.
  Fix: reconcile SCORECARD names vs CSV weekly, backfill. Metric: interview companies without CSV row 7 -> 0.
- **Known-bad senior/Python signal resubmitted (high).** Nearform rejected Aug 12 on that exact basis; 11 more Senior/Lead LEAD rows Aug 26; new Senior submit Sep 2.
  Fix: no submit to a company with a REJECT/feedback thread on matching seniority; Senior/Staff/Lead out of the SWE lane. Metric: Senior-titled submits/week -> 0 outside FDE/Solutions/GTM.
- **Consultancy channel found, never worked (high).** 4 leads LEAD since Aug 6; 21 more (12 Accenture GR, 9 Solirius Reply) LEAD since Aug 26; 3 SUBMITTED ever.
  Fix: action 3. Metric: consultancy SUBMITTED weekly.
- **Duplicate submissions inflate hot-brand reach (low).** 14 URLs with multiple SUBMITTED rows; burns CAPTCHA/essay cycles.
  Fix: URL guard before append. Metric: dup-SUBMITTED URLs 14 -> 0.
- Warm outreach abandoned at the first human reply: see Channel.

### Materials
- **GitHub bio broadcasts the scrubbed phrase (high).** "No-code roots, real-code delivery" renders under the name on every hovercard while 88/93 CVs say "off a legacy stack".
  Fix: edit bio (action 4). Metric: interview-class rate before/after.
- **First pinned repo is a 1-commit stub (rated high, impact unproven).** landmark-space-booking: no README, null description, shown ahead of llm-doc-parser which DM-templates.md sends people to. Zero GitHub mentions in 326 threads, so severity is a presupposition.
  Fix: repin (action 4). Metric: any recruiter reference to GitHub.
- **Summary has zero numbers (medium).** Five sentences of capability jargon; the one metric sits below the fold.
  Fix: number into sentence 1 of the template. Metric: ATS-to-human rate on Ashby/Greenhouse.
- **84 distinct headlines, one static GitHub anchor (medium).** QA/Support/Frontend-tailored CVs land on an agents-first README.
  Fix: broaden README to a 4-line range list, or drop the GitHub link on QA/Support/Frontend/GTM CVs. Metric: qualitative.
- **Two-minipage photo header risks ATS text scramble (low).** 90/93 CVs; Musixmatch/Lever already parsed "http://Map-marker-alt" into a field. Bulk of submits is Ashby/Greenhouse/Workable (51%), not Lever.
  Fix: single-column header for ATS-heavy submits. Metric: garbled fields in next 10 confirmations.

### Channel
- **Warm outreach built once, never executed (high).** 0/16 tracker, 0/73 connect list, files untouched since Aug 18-19; Round 1 follow-up 12 days overdue, Round 2 15 days. Only 1 verified open human door (Mayerfeld, see gap 2).
  Fix: action 1. Metric: checked boxes/week (target 15-20).
- **3 of ~8 conversions invisible to the pipeline (high).** TOPdesk (screening Aug 21 + on-site Aug 24), Mayerfeld (Aug 29), Freedom24 (interview Jul 31, both CSV rows still LEAD).
  Fix: source_channel + prior_interview_at_company columns, backfill. Metric: converting companies with zero CSV row 3 -> 0.
- **Huzzle agency funnel lapsing (medium).** 4 nudges Aug 28 to Sep 5, Luna chat never done; "Huzzle support email" outstanding since Aug 18.
  Fix: complete the Luna chat today. Metric: Huzzle thread class flips from OTHER.
- **Deloitte/Kirey exact-title leads stale 31 days despite an inbound ping (high).** No systematic crawl of Reply/Accenture Italia/Kirey career pages exists.
  Fix: action 3, then add those career pages as sources. Metric: those rows LEAD -> SUBMITTED.

### Process
- **211 malformed rows cluster on 7 dates, several writers (high).** 6-col rows show two different column orders; row 833 Almawave reads "Rome Hybrid" as status.
  Fix: dict + QUOTE_ALL writer; keyword-match repair pass over the 211. Metric: malformed per sweep 0; backlog re-parsed.
- **703 status strings, 87 URLs with conflicting status (high).** Nearform FDE 7834813003 = Applied, LEAD, SKIP-SENIORITY across 3 sweeps. A 7-value enum validates only 64% of rows; needs a mapping table, not a typo collapse.
  Fix: validator on append; dedupe.py keyed on URL, newest valid status wins. Metric: distinct statuses under 15; conflicts 0.
- **Leadtech AI Full Stack Developer died on an unfinished verify (high).** VERIFY email Aug 21, still ACTION_REQUIRED at 744h; role dead on 3 mirrors by Sep 4.
  Fix: verify/needs-you check opens every tick. Metric: oldest open item under 24h.
- **Axmed continuation link unclicked since Sep 3 (medium).** Fit 74/100, duplicate-application email to prabhavitg@gmail.com.
  Fix: click, update row 2959 in place. Metric: resolved within 48h.
- **Bending Spoons: CSV says "not submitted", Gmail shows ACK Aug 21 + 2 REJECTs (medium).**
  Fix: scorecard.py flags companies with Gmail activity but no/skip CSV row. Metric: such companies -> 0.
- **Sweep runs at near-zero yield while follow-up sits idle (high).** 68+ rounds, 0-1 apps each; zero outbound replies in tracked mail. Camunda is an ATS ack, not an open door; Capital.com thread absent.
  Fix: pause the sweep cron for the week; time goes to actions 1-3. Metric: outreach completion; replies within 7 days to named humans.

### Positioning
- **n8n carpet-bombed with 21 URLs, 2 on-lane (high).** Correction: the Sep 12 cooldown was triggered by the on-lane FDE submit Aug 28; the off-lane Sr AI Engineer was BLOCKED, not submitted. 10+ off-lane LEAD rows still sit there.
  Fix: one company = 1-2 on-lane titles; mark n8n off-lane LEADs SKIP; no n8n form before Sep 12, then outreach not another form. Metric: distinct URLs per company per month <= 2.
- **Proptech vendors unsourced despite the hardest-to-fake credential (medium).** 4 touches total; 0 to OfficeRnD, Nexudus, Cobot, Zapfloor, Tribeloo, Optix, Archie, Yardi Kube, Essensys, Robin, Envoy. Named contacts already in LINKEDIN-CONNECT-LIST.md.
  Fix: add them as direct application targets (Solutions/Customer/Integrations Engineer). Metric: proptech SUBMITTED 0 -> 8.
- **Interview data proves the lane, shots still spent outside it (medium).** Interviews: Fever FDE, Telnyx Support, TOPdesk AI engineer. Accenture Greece Aug 26 spray still full of Senior React/.NET/Data Scientist. (Panel's "33 Senior submits" was wrong; use 37/348 SUBMITTED.)
  Fix: hard-filter Senior/Staff unless the title says Forward Deployed, Solutions, AI Automation, Support. Metric: Senior submits/week.
- Outreach list with the exact right people unsent: see Channel and action 1.

## 4. Blind spots we still cannot see

1. **LinkedIn profile never audited.** Pasted into most forms and every DM. Check: log in yourself; compare headline, About, Experience titles, endorsements against "off a legacy stack"; check photo and open-to-work banner.
2. **Mayerfeld may be a EUR 139 paid practicum, not a job.** NEEDS_YOU.md line 45 says do not pay; SCORECARD still classes the Aug 29 email INTERVIEW and FUNNEL-STATS lists it as a door to revive. Check: re-read the Aug 13-17 and Aug 29 threads; if it is a course pitch, relabel SCAM/PAID and drop it from every revive list. Until then, do not reply.
3. **No interview debrief exists.** Nearform (lost), Fever (pending), Telnyx (take-home filled by the loop, not rehearsed). Check: write a one-page Nearform debrief from memory now; repeat within 24h of each Fever/Telnyx step; keep as answers/debrief-<co>.md.
4. **Visa answers may be wrong.** Forms say "EU work permit yes, no sponsorship" for DE/BE/PL/NL roles; memory note says Italian EU LTR does not auto-grant work rights elsewhere (NL needs an employer-filed TWV). Check: pick 3-4 SUBMITTED DE/NL/PL rows, verify the exact step per country with an immigration source before repeating the answer.
5. **Salary answer is one pasted default.** "EUR 30,000-40,000" on 6+ unrelated roles including a GBP 82.7K PM role. RULES.md now says 45-55K. Check: grep salary_stated for the old string; set a per-role floor from the posting band.
6. **Sourcing is drying up as EU hiring reopens.** Sep 1-6 = 57 submits vs ~190+ in August; all interviews came from Aug 5-28 sourcing. Check: weekly new-req count sourced (not applied), late Aug vs early Sep; if flat, add the consultancy career pages and the proptech vendor list as sources instead of re-running the same sweep.

## 5. Loop changes (paste into loop/RULES.md)

- Scope: hard skip any title containing Senior/Staff/Principal/Lead unless it also contains Forward Deployed, Solutions, AI Automation, Customer/Support Engineer, or GTM. Enforce in sweep.py and again at queue time.
- Scope: never submit to a company with a REJECT or interview-feedback thread in gmail_threads.jsonl on a matching-seniority req. Nearform is closed for Senior titles.
- Scope: one company = max 2 on-lane titles per 30 days. Mark n8n and Accenture Greece off-lane LEAD rows SKIP - LANE.
- Query weights: top tier = Italian consultancies (Deloitte IT, Kirey, Reply group, Accenture Italia, Lutech, Var Group) and proptech vendors (OfficeRnD, Nexudus, Cobot, Zapfloor, Tribeloo, Optix, Archie, Yardi Kube, Essensys, Robin, Envoy, deskbird); add their career pages as sources. Lowest tier = hot-AI-brand cold pools (n8n, Cohere, Scale, Arize, Camunda).
- Tick order: (1) Gmail VERIFY/NEEDS YOU older than 24h, (2) outreach batch, (3) queue, (4) sweep. Sweep runs only when new-req yield in the last 3 rounds was above 1.
- Outreach targets this week: the 15 OUTREACH-TRACKER.md Round 1+2 names, then LINKEDIN-CONNECT-LIST.md at 15-20/day. Log to loop/outreach.csv. Mayerfeld excluded until gap 2 is checked.
- CSV: append via dict keyed by the 10 header names + csv.QUOTE_ALL; reject any status outside the RULES vocabulary; skip if the url already has a SUBMITTED row; dedupe.py keyed on URL, newest valid status wins, prints the prior status.
- scorecard.py: emit the list of companies with Gmail ACK/REJECT/INTERVIEW but no well-formed CSV row; that list is a NEEDS YOU item.
- Materials: GitHub bio and pins fixed before the next batch; CV template Summary sentence 1 carries the 2,000 to 4,500+ number; single-column header on CVs for Ashby/Greenhouse/Workable.
