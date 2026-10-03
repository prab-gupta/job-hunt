---
framework_version: 1.0.0
---

# Agent Guidelines: AI Job Search

This workspace is structured to manage job search activities, scraper tools, CVs, cover letters, and interview preparation.

## Thin-Pointer Design (Single Source of Truth)

To prevent duplication and configuration drift across different AI agent frameworks (Claude Code, Google Antigravity, Codex, Cursor, Gemini CLI, etc.), this workspace uses a unified thin-pointer design. All agent runtimes should load the canonical specifications and candidate profiles from the files and directories below:

1. **Personal Candidate Profile:**
   - The candidate profile, contact details, education, and target preferences are defined in [AGENT-INSTRUCTIONS.md](AGENT-INSTRUCTIONS.md) (the authority for facts, salary, availability and policy; `CLAUDE.md` does not exist in this repo) and the individual profile methodology files under [.claude/skills/job-application-assistant/](.claude/skills/job-application-assistant/) (specifically `01-*.md` etc.).
2. **Canonical Workflow Specifications:**
   - The step-by-step instructions and triggers for tasks (setup, scrape, rank, apply, upskill, interview) are defined in the [.claude/](.claude/) directory (specifically under `.claude/skills/` and `.claude/commands/`).
   - Do not duplicate these rules or specifications. Treat `.claude/` files as the single source of truth.
3. **Portal Search Skills:**
   - Job-portal search CLIs live under [.agents/skills/](.agents/skills/) in the portable Agent Skills format (with a `SKILL.md` per portal). Codex and Antigravity discover these automatically; the `/scrape` workflow in [.claude/skills/job-scraper/](.claude/skills/job-scraper/) orchestrates them.

## Browser Agent Execution Rules
When using browser subagents via `mcp_chrome_devtools` to automate application portals:
1. **Never run browser agents in parallel.** Attempting to spawn multiple browser subagents simultaneously triggers Chrome's CDP "Allow remote debugging?" popup multiple times and severely locks the websocket. They must be executed strictly **sequentially**.
2. **Form Autofill Reliability:** External systems like Workday and YC will reject forms unless exact constraints are met. Master profiles and agents must be instructed to:
   - Provide LinkedIn/GitHub URLs strictly with the `https://` prefix (e.g., `https://www.linkedin.com/in/...`).
   - Never leave required text-area fields blank.
   - Pause for CAPTCHAs ("I am human") and notify the user to resolve them before clicking Submit.
3. **Existing Chrome Server Only (127.0.0.1:9222)**: Always attach strictly to the existing running Chrome instance at `127.0.0.1:9222` via Chrome DevTools MCP. Never launch a new Chrome process, open a new browser window, or spawn detached headless browser sessions.

## Parallel Generation and Robust Extraction
When generating multiple CVs/Cover Letters for a batch of jobs:
1. **Parallel Drafting:** Spawn `research` subagents in parallel to fetch job requirements, apply templates, and generate raw LaTeX code.
2. **Robust Extraction:** Do not use fragile `bash` or `awk` scripts to pull LaTeX from the `transcript_full.jsonl` logs. Since JSON encodes newlines as `\n`, use a robust `python` or Node script to `json.loads()` the transcript, locate the `PLANNER_RESPONSE` steps containing `send_message`, and extract the `Message` string using `re.findall()`.
3. **Mandatory PDF Compilation:** Always compile generated LaTeX CVs and Cover Letters to PDF immediately upon extraction: CVs with `tectonic`, cover letters with XeLaTeX (the `cover.cls` class needs fontspec). Do not use a blanket `pdflatex`. Verify compiled PDF page counts (strictly 2 pages for CVs, 1 page for Cover Letters).

## Non-Negotiable AI-in-the-Loop Application Rule
Every single job application MUST follow this strict 4-step sequence (sole exception: Datapizza, which uses its existing approved profile with no CV or cover letter; see `AGENT-INSTRUCTIONS.md`):
1. **Read the JD**: Read and evaluate the target job description for its specific technical requirements, architecture, and responsibilities.
2. **AI Makes a Curated CV**: Curate a bespoke LaTeX CV using candidate instructions (tailoring 3 Career Summary bullets and emphasizing matching technical skills in `cv/main_<Company>_<Role>.tex`), compile with `tectonic`, and enforce strictly 2 pages via `pdfinfo`.
3. **Uploads a New PDF**: Stage the freshly compiled bespoke PDF and upload it into the application form (never fall back to a generic default or uncurated CV).
4. **Applies & Audits**: Complete screening fields with domain understanding, submit the application, verify confirmation via Gmail MCP, and record into `loop/applications.csv` and `data/csvs/applications.csv`.



## Automated Email Verification & Final Confirmation (Gmail MCP)
The lazy-loaded Gmail MCP server (`ServerName: "gmail"`) is connected and must be used for email automation:
1. **Verification & Security Codes**: When any job portal sends a security code or verification PIN to `prabhavitg@gmail.com`, **never prompt the user**. Immediately call `call_mcp_tool(ServerName="gmail", ToolName="list_messages", Arguments={"q": "security code OR verification code", "maxResults": 3})`, retrieve the snippet with `get_message`, parse the code, and enter it into the form.
2. **Mandatory Final Step (Confirmation Audit)**: For every submitted application, the **mandatory final step** before marking the role complete is checking Gmail MCP for the official confirmation email (e.g. `q: "<Company>"`), extracting confirmation timestamp/subject, and recording in `loop/applications.csv` and `data/csvs/applications.csv`.
