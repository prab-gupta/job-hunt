# Xenon Seven - Forward Deployment Engineer - 2026-09-17 retry (Chrome, agent C62)

URL: https://www.linkedin.com/jobs/view/4468277476/
Retry of the earlier 2026-09-17 Playwright attempt (agent P29) that got stuck on the Resume step (2/6): Next button unresponsive after 6 distinct attempts, logged NEEDS_YOU.md row 35. Task instruction: retry the whole flow in Chrome.

## Retry outcome
Live page showed 0 applicants, 11 hours ago, no "Saved"/"Applied" state, so the prior attempt had been fully discarded (not left half-filled). Started a completely fresh Easy Apply flow in Chrome from Contact info. The Resume step this time advanced normally on the first Next click after uploading and confirming Prabhavit_CV_XenonSeven.pdf selected (green radio, top of list) - the earlier blocker did not reproduce. Full 6-page flow completed and submitted cleanly.

## Form (6 pages)
1. Contact info: mobile 3516107807 (Italy +39 pre-set), Location Venice Veneto Italy (combobox typeahead), Photo field left blank (optional, no asterisk).
2. Resume: uploaded via Upload resume -> injected file input -> file_upload with Prabhavit_CV_XenonSeven.pdf, confirmed selected at top of resume list before advancing.
3. Summary + Cover letter (both required-ish; Summary marked with asterisk, Cover letter had no asterisk but a "be sure to include" prompt so filled it too): Summary = 2-sentence AI/automation engineer summary tracing to FlowSpace + UltraStrategy; Cover letter = full CoverLetter_XenonSeven text (UltraStrategy CV-parsing pipeline led, FlowSpace AI listing bot + support agents paired, honest that Snowflake Cortex/Databricks Genie have not been used, Italy work-authorisation line). Filled both via form_input (direct DOM set) after noticing the `computer type` action drops characters on long text on this ATS (same bug seen on CloudFactory today); verified no dropped characters before proceeding.
4. Work experience: LinkedIn-profile auto-import (FlowSpace Lead Software Engineer entry correct, plus older/unrelated entries), capped at "limit of 10 responses". Left as-is, out of scope for this task's material (same precedent as the 2026-09-16 NewRocket row).
5. Education: LinkedIn-profile auto-import (Ca' Foscari Bachelor's + two secondary schools), capped at 3 responses. Left as-is, same reasoning.
6. Additional Questions (JD-specific screening, all required):
   - How many years of hands-on software engineering and AI application development experience: 3
   - Built/deployed in production with Snowflake Cortex or Databricks Genie: No
   - Working experience with enterprise Finance processes/datasets: No direct Finance domain experience
   - Hands-on experience building end-to-end AI apps with a UI + Python backend (FastAPI/Flask): No (honest; his production stack is Next.js/Laravel/TypeScript plus n8n orchestration, not a Python UI+backend combo)
   - LLM frameworks/vector search summary (free text): honest answer naming n8n + Claude API + Eden AI + Affinda as the actual production stack, explicitly stating LangChain/LangGraph/LlamaIndex and a dedicated vector search engine have not been used
   - Confirms seeking hands-on builder role with direct client contact: Yes
   - Comfortable with full-time independent-contractor, compensation-only terms (no social insurance/medical/paid leave): Yes
   - Expected hourly rate in USD (gross, all-inclusive): 40
   - Notice period in days: 14 (two weeks, standing rule)
7. Review: verified resume filename, cover letter text, work experience/education auto-import, and every screening answer matched what was entered. Unticked "Follow Xenon Seven" (not required consent).

## Result
SUBMITTED. Confirmation: "Your application was sent to Xenon Seven!" / "Application submitted - now". Saved to confirmations/XenonSeven-2026-09-17.txt.

Learning for the loop: the Resume-step Next-button freeze reported by two prior agents (Playwright P29 and an earlier Chrome pass per NEEDS_YOU row 35) did not reproduce on a fully fresh Easy Apply session (0 applicants, no stale Saved state). Likely a transient/stuck-session issue rather than a permanent Xenon Seven/Workable ATS defect; a clean retry from the job page (not resuming a half-filled dialog) resolved it.
