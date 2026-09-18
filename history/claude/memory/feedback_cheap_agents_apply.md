---
name: feedback_cheap_agents_apply
description: Job-search loop - applying/form-filling must run in cheaper subagents (sonnet/haiku); Fable session model only plans and orchestrates
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 237a3cff-dd16-4810-8bd3-960e29fe6c44
  modified: 2026-09-09T05:24:03.822Z
---

User instruction 2026-09-09: "to apply use cheaper model agents, fable only for planning".

**Why:** Fable tokens are expensive; form filling, letter drafting from existing templates and CSV bookkeeping are mechanical. Fable's job is deciding what to apply to, briefing agents, and verifying results.

**How to apply:** For each application spawn `Agent` with `model: "sonnet"` (haiku for pure verification/harvest) and a self-contained brief (loop/APPLY_AGENT_BRIEF.md + queue row + letter path). Browser: Playwright MCP is a single shared instance, so run apply agents one at a time; Claude in Chrome tabs can run in parallel when connected. Agents write results to loop/results/<Co>.txt and append applications.csv; Fable merges queue.csv/STATE.md. See [[project_job_search]], [[feedback_headroom]].
