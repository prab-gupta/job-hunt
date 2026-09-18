# Sword Health - Senior ML Engineer (Lever) - essays, 2026-09-06

## Pick one GenAI feature you took from problem definition to production traffic (400 words max)
Feature: the FlowSpace listing pipeline, a GenAI system that turns a workspace operator's brochure in any format (PDF, web page, photo, spreadsheet) into a complete, validated marketplace listing. I owned it end to end: problem definition with the operations team, architecture, prompts and tool schemas, the human review UI, the backend push, and operations after launch. Scale at launch: the whole listing intake of a live marketplace serving about 2,000 users, growing to 4,500+ while the pipeline ran; 900+ records processed.

How I knew it was good enough to ship: reference set of 40 hand-entered listings, scored field by field (exact match for prices and capacities, tolerance for descriptions). Bar: the reviewer accepts a draft with fewer edits than typing from scratch. Tracked acceptance rate, edits per draft, field-level error counts per document type; shipped when photo brochures (worst class) stayed above 80 percent field accuracy. Every prompt or model change had to beat the previous version on that set.

Biggest failure mode after launch: confident extraction of the wrong entity (multi-site brochures merged two buildings into one clean, plausible listing; schema valid). Fix: segment source by building before extraction, cross-field consistency check (address, postcode, price table must agree), route any multi-site document to the human queue by default.

What I cut: fully automatic publishing. Replaced with a mandatory human review step (~2 min per listing); the edit data became the evaluation set.

## What makes you consider a new job position, ideal company (100 words max)
I move when the work stops teaching me. I want a small, senior team where I own production AI systems end to end, from the problem with the customer to the evaluation that says it works, and where shipping is measured by outcomes for real users rather than demos. Ideal environment: remote-first with real ownership, engineers who review each other's work seriously, a product that matters to people, and honest conversations about what the model gets wrong. Sword's clinical setting raises the bar on evaluation and reliability, which is exactly the part of the job I want more of.

## Other answers
Comp: EUR 60,000 to 70,000 gross (band EUR 60-85k). English proficient: Yes. Location Venice, Italy. Company: FlowSpace.co (contract ended Aug 2026).
