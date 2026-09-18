# Lawrence Harvey (Italy) - Senior AI Engineer - 2026-09-16

JD: https://www.linkedin.com/jobs/view/4452363857/ (LinkedIn Easy Apply, LI-PICK row, italian_jd)
Recruiting agency Lawrence Harvey posting on behalf of an undisclosed client. Role: Senior AI Engineer, agentic AI / enterprise Generative AI, Milan, hybrid (JD states explicitly "non può essere svolta in remoto").

## LI-PICK gate check
- Posting open: Easy Apply button present, no "Application submitted" state, no closed banner.
- Dedupe: `python3 loop/dedupe.py --check "Lawrence Harvey" "https://www.linkedin.com/jobs/view/4452363857/"` -> HIT COMPANY~ (fuzzy). `grep -i "lawrence" applications.csv` -> zero rows, no literal company match anywhere in history. Fuzzy hit is a false positive on an unrelated name; not a block.
- Language: JD is Italian, he has conversational Italian (B1-B2) plus English C2, so this does not trigger the "language he lacks" kill.
- Senior title + 3-5 anni richiesti vs his 3 years: per LI-PICK rule, apply anyway with an honest letter naming 3 years plainly.
- No anti-AI clause, no MSc/PhD requirement found in the JD.

## CV tailoring (Prabhavit_CV_LawrenceHarvey.tex, from Prabhavit_CV_EN.tex, verbatim bullets only, parity-checked against EN.tex)
- Career Summary: kept 2 of 3 bullets (AI Solutions & Automation Engineer / LLM-driven applications; Transformed business requirements into production-ready features, AI agents, LLM-powered data parsing, QA). Dropped the "AI-assisted development, prompt engineering, API integrations" bullet.
- FlowSpace Product: reordered "Streamlined customer support with AI agents" to top, kept migration bullet and scaled-platform bullet (3 total); dropped 2 generic collaboration/communication bullets as not JD-relevant.
- FlowSpace Technical: removed the 2 literal duplicate lines (repeat of the AI listing-bot bullet and the migration bullet already covered in Product) and dropped "Developed a tool for companies to calculate commute times" as irrelevant. Kept AI tool for processing/scraping data (top), OfficeRnD/Nexudus API integration, CRM lead consolidation, GTM automations (4 bullets). FlowSpace total: 3 Product + 4 Technical = 7, above the minimum of 3.
- UltraStrategy: both existing bullets kept unchanged (CV-parsing tool bullet + user-profiles platform bullet), satisfying the AI/automation-JD rule requiring at least 2 kept there.
- Get2Germany: kept the required pair (AI-based automation tools for courses/internships/jobs bullet + Google APIs integration bullet), reordered AI bullet first; dropped the UI/UX-to-Bubble bullet and the database-optimisation bullet as not JD-relevant (Bubble/low-code has no bearing on this JD).
- Urlink: kept all 3 bullets, reordered "Implementing automations in regards to client requirements" above "Implementing UIs made with AI" (AI-platform-build bullet already led).
- Qomodo: dropped the Figma-implementation bullet (not JD-relevant), kept the dashboard bullet (min 1 satisfied).
- Clubee: dropped "Developed tools for domain integration, shop, federation dashboard" as more generic; kept API integration bullet and unit-testing/QA bullet (2 bullets, above min 1).
- Tractionboard: kept only "ChatGPT/OpenAI integration" (directly relevant, an LLM integration precedent); dropped the 4 other bullets (Figma-to-Bubble, Sendgrid, responsive design/debugging, Google Ads) as not relevant to this AI-engineering JD.
- Technical Skills / Additional Information: left unchanged, already led with AI/ML category; no Bubble-only items to drop (no bare "Bubble" list items outside role bullets already handled).
- No sentences rewritten, no new claims added (did not add "Python"/"FastAPI" as standalone skill-list items since the master CV does not list them explicitly, even though they are claimable per the brief; the letter addresses the framework gap honestly instead). Compiled 2 pages via tectonic, clean.

## Cover letter (CoverLetter_LawrenceHarvey.tex/.pdf/.txt, Italian, "voi" register)
- Lead paragraph: FlowSpace (AI listing bot with human-in-the-loop, 900+ drafts; support AI agents with confidence-based escalation; OfficeRnD/Nexudus integrations) - traces to OUTREACH_FACTS.md FlowSpace section.
- Second paragraph: UltraStrategy (CV-parsing pipeline: upload, extraction, relevance scoring, Ultra CV generation; Affinda + Claude API; built with n8n and Eden AI) - traces to OUTREACH_FACTS.md UltraStrategy section.
- Honest disclosure paragraph: named the specific gap on LangGraph, LangChain, Google ADK, MCP/A2A (not on file, never claimed) and stated the real orchestration experience is n8n plus the Claude API/Claude Code, offering to close the framework-specific gap quickly. No invented claims.
- Years stated plainly: "tre anni di esperienza continuativa" (per LI-PICK rule for a Senior-titled row).
- Work authorisation: role is in Italy (Milan, hybrid, on-site required), so used the Italy authorised-Yes-no-sponsorship line plus explicit availability for the hybrid/on-site requirement (not a relocation-transparency-line case since Venice-to-Milan is domestic, no cross-border work-permit issue).
- Language levels stated: Italian B1-B2 conversational, English C2 professional.
- 0 em-dashes confirmed via grep on the .txt. No legacy-platform brand named in text written for this letter.

## Standing form answers used in Easy Apply
- Years of experience: 3.
- Italian level: Intermediate/Conversational (never Fluent/Native).
- Salary: EUR 50,000 or 45-55k band; JD states "RAL fino a €55.000 + MBO" so this is within band.
- Work authorisation (Italy): Yes, no sponsorship needed.
- Relocation/hybrid/on-site: Yes (role requires Milan hybrid, explicitly non-remote).
- Tools not on file (LangGraph, LangChain, Google ADK, LlamaIndex, MCP, A2A, Cursor, Gemini CLI): answered honestly as 0 years / No where a numeric or yes/no field exists, per the task instruction "honest 0/No on tools not on file". Claude Code / Claude API experience claimed where relevant (on file).
- How did you hear: LinkedIn.
