# Job Sweep Handoff - Sep 6, 2026

## Current State

- **applications.csv:** 3720 rows, 383 SUBMITTED
- **Market:** fully saturated across ALL channels. 68+ sweep rounds, last ~50 yielded 0-1 new apps each. Fresh inventory appears every 1-2 days.
- **Cron:** was running `*/5 * * * *` (job f3c49f6e) - recreate in new session
- **NEEDS_YOU.md:** ~25 items requiring human action (CAPTCHAs, essays, account creation, email apps)

## This Session's Results

- **Mastra Customer Engineer (EMEA remote):** SUBMITTED via Ashby. reCAPTCHA passed. Prabhavit_CV_Mastra.pdf.
- **HICX Solutions:** DEAD (posting removed, redirects to not_found)
- **Honu.ai:** DEAD (posting removed, zero open roles)
- **LiteLLM:** SKIP (SF onsite only)
- **All other leads from HN Sep 2026, WebSearch x12, euremotejobs, agentic-engineering-jobs, startup.jobs, workatastartup, LinkedIn, Lever, Workable, Ashby:** already in CSV as SKIP/SUBMITTED/DEAD

## Channels Searched (all saturated)

LinkedIn, WebSearch, HN, Wellfound, workatastartup, remoterocketship, startup.jobs, 4dayweek.io, euremotejobs, remoteok, himalayas, remotive, berlinstartupjobs, arc.dev, hiring.cafe, weworkremotely, agentic-engineering-jobs.com, n8n community

## Key Standing Rules

- Salary: Italy/remote EUR 45-55k, NL/Northern EU EUR 55-65k, USD 54-70k, GBP ~50k, B2B EUR 250-300/day
- CV tailoring: edit ONLY HEADLINE (~line 39), SUMMARY (~line 52-53), SKILLS (~lines 57-61). Compile with tectonic.
- Claim ladder (updated 2026-09-06, confirmed by Prabhavit): FastAPI/Flask, Docker/Kubernetes, and ML work (fine-tuning, embeddings, evals, PyTorch) ARE claimable as working knowledge in SKILLS; write them as production experience only when Prabhavit has given a concrete example for that role. Still never claim: BPMN, cloud admin (AWS/GCP/Azure), computer vision, edge computing, ML research, any language beyond English C1 and beginner Italian.
- Never say "no-code" or "Bubble" - say "off a legacy stack"
- No em-dashes. No Claude/Anthropic attribution anywhere.
- Cover letter field: NEVER leave blank
- CV: ALWAYS attach
- Phone: "+39 351 610 7807" (full, with plus)
- Email for apps: prabhavitg@gmail.com
- DOB: 21/02/2001
- Location: Venice, Italy. EU Long Term Residence Permit.
- EU LTR does NOT auto-grant work rights in other EU states (NL requires TWV)
- On-site EU roles valid targets (open to relocation anywhere in EU)
- Autonomous form submission OK after visual review
- Must see success page screenshot before logging as SUBMITTED
- Re-read JD + template fresh for EACH role (context rot prevention)
- Privacy defaults: decline non-essential cookies, leave optional consents unchecked
- Skip agencies: Scale Army, Remote Recruitment, ISTA, Teamified, Activate Talent, Pavago, Jobgether, Oowlish
- Skip reposters: Hire Feed, Quik Hire Staffing, Crossing Hurdles, FetchJobs.co

## Cooldowns

- **n8n:** next eligible Sep 12, 2026 (15-day cooldown)
- **ElevenLabs:** next eligible ~Nov 3, 2026 (90-day cooldown)

## Chrome MCP Bug (CRITICAL)

browser_batch and computer actions with coordinates execute on the FOREGROUND Chrome tab, not the specified tabId. Only ref-based actions (form_input, find, read_page, computer with ref=) and javascript_tool respect tabId correctly.

## ATS Notes

- Ashby: JS rendering, WebFetch returns minimal content. Use Chrome MCP.
- Ashby: invisible reCAPTCHA can block. Sometimes passes on retry.
- Lever: WebFetch returns 403. Use Chrome MCP.
- Workable: WebFetch returns 403 or minimal. Use Chrome MCP.
- WeWorkRemotely, hnhiring.com, RemoteRocketship, startup.jobs: WebFetch 403. Use Chrome MCP or WebSearch.

## Files

- `~/Downloads/claud jobs/applications.csv` - master dedupe source
- `~/Downloads/claud jobs/NEEDS_YOU.md` - human action items
- CV template: any recent `Prabhavit_CV_*.tex` (Vidalytics variant = generic AI headline)
- photo.jpg must be in same folder as .tex for compilation
