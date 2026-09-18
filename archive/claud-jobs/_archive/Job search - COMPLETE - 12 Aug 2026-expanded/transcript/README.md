# The session record

## `research-agent-reports.md` — read this one

**76 research subagents** ran across this job search. Each was given a slice of the market (a track, a country, a source family, a blindspot category) and sent back a report. This file is every one of those reports in full, in the order they finished, with the brief each agent was given.

This is where the roles in the shortlists actually came from, including the ones that were found and then rejected. If you want to know whether something was looked at, search here first.

## `subagents/` — the raw agent transcripts

106 files, ~33 MB. Every search query each agent ran, every page it fetched, and what came back. `agent-<id>.jsonl` is the transcript, `agent-<id>.meta.json` says what it was asked to do.

Useful when a report says "dead on the real ATS" and you want to see the actual page that came back.

## `session-transcript.md` and `.jsonl` — the main conversation

The `.md` is readable; the `.jsonl` is the raw record.

**One honest caveat.** The main conversation was compacted partway through 12 August, and compaction rewrites this file — it keeps the summary plus everything after it, and the earlier turn-by-turn history is not recoverable from disk. So `session-transcript.jsonl` holds the final stretch of 12 August, not all of 5–12 August.

Nothing of substance is actually lost, because the content was written down as it happened rather than left in the conversation:

| What | Where it lives |
|---|---|
| Every application, with the verbatim confirmation text | `raw-logs/under75_run.jsonl`, `raw-logs/applied.jsonl`, `sheets/MASTER…xlsx` |
| Every role found, including rejected ones | `transcript/research-agent-reports.md`, `sweeps/` |
| Every rule Prabhavit set or changed, and why | `docs/working-rules.md`, `docs/sessions/session-log-2026-08-12.md` |
| Every mistake made and what was learned | `docs/sessions/handover-2026-08-12.md` |
| His own words, quoted, in order | `docs/sessions/session-log-2026-08-12.md` |
| Every letter sent | `letters/` (28 PDFs) + `role-inputs/` (the JSON each was generated from) |

## `tool-results/`

Page images from PDFs that were opened during the session — mostly CV renders used for checking layout.
