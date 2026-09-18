# Mainloop, 30 min with Edouard: cheat sheet

Format (from their ad): walk through something you built, then justify one decision inside it. Deck: `Listing_Bot_Mainloop.pptx`, speaker notes are the script. Slide 7 is where he should stop you.

## Run-sheet
| min | do |
|---|---|
| 0-2 | Slide 2. Who: 8 companies, 7 countries, 3 years, same loop. |
| 2-10 | Slide 3 only if asked for a CV run-through, then slides 4-9 in their order: mess, functional architecture, agents, in front of people, honest no, handover. |
| 10-22 | His interrupts. Answer with claim / why / cost / what would change my mind. |
| 22-25 | Demo only if it adds something (see below). |
| 25-28 | Your two questions. |
| 28-30 | Ask what the next step is and when. |

## Their words, use them
functional architecture · check what we already have · an honest no · handover pack · increasingly real prototypes · agents are the fastest and least trustworthy part · sizing the benefit from day one.

## Benefit, in numbers
900+ drafts x 30-45 min by hand = roughly 450-675 hours of re-keying removed (3-4 months of one person). Then say plainly: review minutes per card remain; 114 live; 579 proposals waiting on a human by design.

## Five decisions ready
1. **Nothing reaches prod without a person.** Dry-run default on; Send per card; batch auto-push behind 3 switches, ships off. Why: a wrong price/address goes public under an operator's brand; 30 feeds with known defects. Cost: throughput. Changes my mind: correction log (AI draft vs human edit at push) showing a field never corrected. Loosen per field.
2. **Check prod first.** Exact name, then fuzzy + operator, then postcode. Update, never duplicate. 916 rows became 446 UPDATE / 375 NEW. Limit I own: API searches names, not postcodes, so the reverse check never shipped.
3. **Model output untrusted at the boundary.** spec.ts from the prod DB coerces every value; closed enums; sheet values byte-exact, disagreements become flags. Incident: 550 drafts with tenure "PrivateOffice" from a bad brief example, 2,038 offices would badge wrong; closed 3 ways.
4. **Photos on Supabase, not backend S3.** Shipped PR, measured 720x405 live vs 2560 originals, reverted (aa06b05), wrote the re-instate condition. Did not touch the Laravel backend: not my system.
5. **Migration per entity.** API sync for live entities (bookings, users), one-time CSV for frozen records, per-entity cutover. Same story as your essay 2.

## Already told them (essays, 9 Sep). Stay consistent.
E1 bot: agent did extraction, drafting, photo slots, facility enum; you did the checkpoint, the spec, the escalation path. E2 per-entity migration. E3 harness: cost-tier routing, hooks for standing rules, branch + forked route + additive lib. E4 plan, execute, review with human checkpoints; not autonomous. E5 a small null count hid a mapper bug dropping ~29% of a field.
**One fix:** E1 said "n8n for orchestration" in the bot. Not true. If raised: "n8n runs the CRM and GTM automations at FlowSpace; the bot is TypeScript. That line was imprecise, my mistake."

## Don't say
OfficeRnD, Nexudus or n8n inside the bot · 15x · RAG for the bot · "Bubble" or "no-code" (say "a legacy stack") · anything not in `Prabhavit - Master Experience.md`.

## Own before he finds
Two stores (Neon + Supabase) · dead `/review` code · Python and TS evolved in parallel for a week · solo, so review came from agents and me · 114 live listings still untyped.

## Demo, 3 min, zero writes
`https://listing.flowspace.co/admin?s=1c1b7eaa-0c7c-4dff-ae89-6328ed2365d4` (wave 105, 20 cards). Auth wall confirmed live 16 Sep. Log in before the call, keep the tab open. Show one card: `missing[]` flags, Dry-run vs Send LIVE. Never press Send LIVE. Fallback: slide 6.

## Questions to ask (pick 2)
1. How does the portfolio code-intelligence agent answer "what of ours already does this", and how often is it wrong?
2. What is the MVP bar at handover, and what does the Tech Lab most often send back?
3. How do you size a benefit in week one when nobody has measured the manual process?

## Prep, 2-3 days
Day 1: read the notes aloud twice (30 min). Day 2: answer `MOCK_QA.md` aloud, then one demo dry run (40 min). Call day: re-read the essays (5 min), open the demo tab, open the deck in presenter view.
