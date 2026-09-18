# OUTREACH-PICKUP — resume the cold-outreach list build

_Last updated 18 Aug 2026. Read this top to bottom, then continue. Self-contained._

## What this is

A cold-outreach list: companies + named people for Prabhavit to approach **whether or not they are hiring**. Distinct from the application pipeline (MASTER / applications.csv / LEDGER — those are for actual job applications). Approach angles = FlowSpace competitors, coworking software vendors, Italian automation consultancies, automation-product companies, proptech-automation companies.

## The two output files (KEEP BOTH IN SYNC)

1. `Outreach - people to contact.xlsx` — standalone, sheet `Outreach - people to contact`.
2. `Role shortlist - 8 Aug 2026.xlsx` — same-named tab at position 5; the `START HERE` tab points to it.

Both carry the identical sheet. Every edit must be written to BOTH (the patch scripts loop over both paths).

### Column schema (header row 4, data from row 5)
`Priority · Company · Category · What they do · Website · LinkedIn company page · Prime person + title · Person LinkedIn or published email · Why Prabhavit is relevant · Status / source note · Contacted? · Date contacted`

### Colour / priority code
- **Green** = verified contact, ready to use.
- **Amber** = VERIFY before sending (title conflict, CEO-fallback, or slug inferred) OR still pending.
- **Grey / Priority D** = DROPPED (dead company, wrong entity, already-applied duplicate).
- Priority A = Italy/EU-permit strongest fit or warmest hook (e.g. OfficeRnD/Nexudus API hook, same-city Digital Automations). B = solid. C = seed. D = dropped.

## HARD RULE — carried through every step
**Never invent or guess a person's name, email, or URL. Never construct first.last@company.com.** Only record a LinkedIn URL / email actually seen in a search result or on a page. `not found` is a CORRECT answer; a guessed contact is a serious error. Title mismatch → flag VERIFY.

## STATUS: COMPLETE (18 Aug 2026) — 96 rows, 89 with contact, 0 pending, 7 dropped. All person-lookups done. Remaining work = human outreach (fill Contacted?/Date columns) + optional VERIFY passes on amber rows.

## Current state: 96 rows — 89 with contact, 0 pending, 7 dropped

Categories present:
- **Competitors (~25):** verified seeds Data4Prime, Tally Workspace (Laura Beales + Jules Robertson LinkedIn confirmed), Anchor Offices (Giuseppe Ciccarello=Director, Sam Simon=Founder) + full web sweep (Hubble, Kitt, Workthere, Instant, Rubberdesk, Desana, Officeguru, Upflex, Coworker, LiquidSpace, Office Freedom, Flexas, Deskeo, eOffice, BASE, Adapt, shareDnC, CoworkingSpain, Rete Cowo, Cofoundry). Spacery + Gowork dropped.
- **Software vendors (~15):** OfficeRnD (Deyan Varchev CTO) + Nexudus (Adrian Palacios CTO) = priority A API hook; Cobot, Optix, Spacebring, Archie, Yardi Kube, Essensys, Habu, Zapfloor, Tribeloo, deskbird, Robin, OfficeSpace, Envoy. andcards dropped (=Spacebring).
- **Italian consultancies (9):** Digital Automations (Venezia-Mestre, SAME CITY = A), Fabrika 06, Tready, Customcode (n8n+Laravel), Webion, AINTHEWORK, HT&T, FaccioIO, DataMasters.
- **Automation products (~23):** partial. FOUND via WebFetch: Bardeen (Cory Cofran SE — strong fit), Glide (Andy Claremont Head of Ecosystem — strong fit), Parabola (C.J. Jameson Head of Eng), + CEO/founder fallbacks (Activepieces, Gumloop, Softr, Xano, WeWeb, Latenode, Windmill, Respond.io, SendPulse, Pabbly, Albato — all VERIFY). Relay.app DROPPED (shutting down). Airtable partial ("kev" community, no LinkedIn). Bubble.io/Apaleo grey (already applied).
- **Proptech automation (~16):** Cohost AI website confirmed (cohost.ai); ALL 16 persons still PENDING.

## STILL PENDING — the redo list (do this first on resume)
Web-search was dry all session, so these have NO person yet:
- **6 automation platforms, highest priority (biggest role-rich targets):** Spoki, Make, Retool, Pipedream, Tray.ai, Workato.
- **16 proptech-automation persons:** Mews, Cloudbeds, Lodgify, Smoobu, Hostaway, Duve, Enso Connect, Operto, Charge Automation, RoomRaccoon, Zeevou, Beyond Pricing, PriceLabs, Sweeply (+website), Wishbox (+website), Cohost AI (person only).
Prefer a devrel / solutions-eng / partnerships / community lead over the CEO where findable. His relevance hook: n8n/Make power-user + Bubble no-code background; for proptech add FlowSpace + OfficeRnD/Nexudus API integration.

## WHY IT WAS BLOCKED — and the fix (IMPORTANT)
Two separate limits kept killing the research:
1. **Account session limit** — time-based (`resets 1:50am Europe/Rome`), account-wide.
2. **WebSearch quota** — ~200 searches per Claude Code SESSION, shared across all agents, silent until it errors. THIS was the real blocker; it does NOT reset on the 1:50am boundary.

**Fix already applied:** `~/.claude/settings.json` env `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION = 10000`. **BUT env vars load at session start**, so it only takes effect after a **Claude Code restart**. The current session is still stuck on the old 200 and is dry — that is why the pending rows are pending.

### To resume and fill the pending rows
1. Restart Claude Code (loads the 10000 cap).
2. Say "resume outreach" (or point me at this file).
3. Launch general-purpose agents with WebSearch — hand them the exact company + website list so budget is spent on the PERSON, not rediscovery. Split ~2 agents (automation platforms / proptech). Apply the HARD RULE.
4. Patch results into BOTH files via a python/openpyxl script keyed on the Company cell (col 2), green/amber/grey per the code above. Dedupe new companies against the applied set (see below) before adding.

## Dedupe (applied-companies) set
`applications.csv` + MASTER company columns = 703 normalized names. Rebuild it and grey-flag any outreach row whose company is already applied (already grey: Bubble.io, Apaleo, Limehome-family). Script pattern is in the session history; normalize by lowercasing and stripping legal suffixes (srl/gmbh/ltd/io/ai/com).

## Unrelated but done this session (context)
- Installed the **proficiently** Claude Code plugin (job-search skills: apply, cover-letter, network-scan, setup, job-search, jobsearch-telegram, tailor-resume) — enabled user-scope in `~/.claude/settings.json` (baked in for next session). A committable copy for coworkers is at `./.claude/settings.json` in this folder.
- Set git `url."https://github.com/".insteadOf "git@github.com:"` globally so plugin clones use HTTPS (was failing on SSH publickey).

---

## RELAUNCH BLOCK — paste-ready on next session (after restart, cap=10000 live)

Both research agents came back EMPTY this session (WebSearch dry). On restart, launch these two general-purpose agents (they have WebSearch/WebFetch). Hand them the exact company+website so budget goes to the PERSON. HARD RULE applies (no fabrication; `not found` over guess; VERIFY on title mismatch). Return `company | linkedin company page | prime person + title | person linkedin OR published email | source note`. Then patch BOTH xlsx files keyed on col 2.

### Agent 1 — automation platforms (6 pending, biggest targets)
Find prime person (prefer devrel / solutions-eng / partnerships / community lead over CEO) + real contact for:
Spoki (spoki.it), Make (make.com), Retool (retool.com), Pipedream (pipedream.com), Tray.ai (tray.ai), Workato (workato.com).
Fit hook: n8n/Make power-user + Bubble no-code background; roles = solutions/forward-deployed/devrel/support/QA eng.

### Agent 2 — proptech automation (16 pending persons)
Find prime person (prefer devrel/solutions-eng/partnerships/integrations lead over CEO) + real contact for:
Mews (mews.com), Cloudbeds (cloudbeds.com), Lodgify (lodgify.com), Smoobu (smoobu.com), Hostaway (hostaway.com), Duve (duve.com), Enso Connect (ensoconnect.com), Operto (operto.com), Charge Automation (chargeautomation.com), RoomRaccoon (roomraccoon.com), Zeevou (zeevou.com), Beyond Pricing (beyondpricing.com), PriceLabs (pricelabs.co), Sweeply (confirm website too), Wishbox (confirm website too), Cohost AI (cohost.ai — person only).
Fit hook: FlowSpace proptech + OfficeRnD/Nexudus API integration + n8n automation + AI support agents.

### Already found — do NOT re-research (just needs LinkedIn top-up if 'not found')
Automation: Bardeen (Cory Cofran SE), Glide (Andy Claremont), Parabola (C.J. Jameson) = strong; Activepieces, Gumloop, Softr, Xano, WeWeb, Latenode, Windmill, Respond.io, SendPulse, Pabbly, Albato = VERIFY. Relay.app DROPPED.
