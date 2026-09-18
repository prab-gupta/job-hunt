---
name: feedback_outreach_italian
description: Cold outreach emails - user wants more volume and Italian-language emails for Italian companies (2026-09-09)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 237a3cff-dd16-4810-8bd3-960e29fe6c44
  modified: 2026-09-09T18:12:42.570Z
---

User instruction 2026-09-09 evening: "do more cold reach outs via mail and if the company is italian write in italian".

**Why:** Warm/direct channels were the weakest part of the funnel (0 replies from ATS spray); the user wants the email channel pushed harder and made native for Italian SMBs, which are the best legal fit (authorised to work in Italy, no permit).

**How to apply:** Standing cap 20 emails/day, window 08:00-21:00 Europe/Rome, but the user asks for one-off bursts ("send more outreach 50 more" at 22:50 on 2026-09-09: 63 sent in 25 min, late evening, explicitly wanted). When asked, run the burst: haiku scouts (JSON: company, site, email, email_source_url, quote) -> planner check (email domain == site domain, dedupe vs outreach.csv/applications.csv) -> parallel sonnet senders in Chrome Gmail web (compose URL + file_upload, log each send with the Gmail message id immediately). Gmail MCP attachments are too heavy for agents. Italian companies get the whole email in Italian (subject included), same 4-6 line value-first structure, "voi" to a team inbox, "tu" only to a named founder of a small startup; keep English for non-Italian companies. Guardrails unchanged: address published on the company's own site, one email per company, CV attached (Prabhavit_CV_Original_EN.pdf, or an Italian CV if one is ever requested), log every send in loop/outreach.csv. See [[project_job_search]], [[feedback_cheap_agents_apply]].
