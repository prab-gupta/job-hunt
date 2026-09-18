---
name: project_mainloop_interview
description: Mainloop (Leyton group, Barcelona) Forward Deployed Engineer process — round 3 prep pack built 2026-09-16; facts, decisions chosen, essay-consistency fixes
metadata:
  type: project
---

Mainloop FDE (Leyton group, Barcelona). Applied 2026-09-09 via leyton.teamtailor.com (5 essays, saved at
`~/Downloads/claud jobs/answers/leyton-2026-09-09.md`). 15-min Edouard + HR call done by 2026-09-15.
Round 3 = 30-min with Edouard ("walk through something you built, justify one decision"), around 2026-09-18/19.
Round 4 = Casablanca tech lab; round 5 = take-home project with Claude Code. Hackathon 9-16 Oct = skip to final.

Prep pack (2026-09-16) in `~/Downloads/claud jobs/mainloop/`: `Listing_Bot_Mainloop.pptx` (12 slides incl. experience timeline as slide 3, notes =
script), `INTERVIEW_CHEATSHEET.md`, `MOCK_QA.md`. Project presented = FlowSpace listing bot
([[project_flowspace_listing_web]]) plus UltraStrategy CV pipeline, FlowSpace migration, Urlink.

Decisions Prab chose to defend, in order: human-in-the-loop always; check prod first / honest no; model output
untrusted at DB boundary; photos on Supabase (revert aa06b05); per-entity migration API vs CSV (= his essay 2).

Facts corrected vs the Gemini-made deck and his own essay: the bot has NO OfficeRnD/Nexudus, NO RAG, NO n8n
(Prab confirmed 2026-09-16 n8n was never in the bot; n8n = CRM/GTM automations). No "15x" metric exists.
Benefit sizing he gave: 30-45 min per listing by hand; 900+ drafts = ~450-675 h.

**Why:** later rounds (Casablanca, take-home review) will probe the same project; keep the story identical.
**How to apply:** for any Mainloop follow-up, reuse the cheat sheet numbers and the don't-say list; check
`~/flowspace-archive/handover/` and `repos/flowspace-listing-web` for facts, never the Gemini deck.
