# Autonomous AI Job Search Framework

*A production-grade, multi-agent autonomous job search and application engine.*

---

## Overview

This repository turns AI agents into an end-to-end autonomous job application engine. It handles role discovery across global and local portals, evaluates fit, generates tailored ATS-compliant LaTeX CVs and cover letters, automates browser submissions via Chrome DevTools Protocol (CDP), and audits confirmation emails via Gmail MCP.

```
+-------------+     +-------------------+     +-------------------------+
|   /scrape   | --> |     Evaluation    | --> |    Tailored LaTeX CV    |
| (Portal CLI)|     | (Fit Score 0-100) |     |  (Tectonic, 2-page ATS) |
+-------------+     +-------------------+     +-------------------------+
                                                           |
                                                           v
+-------------+     +-------------------+     +-------------------------+
| Gmail Audit | <-- |  Tracker FastMCP  | <-- |    Browser Submissions  |
| (Gmail MCP) |     | (Dedupe & Claims) |     | (CDP Port 9222 / 9223)  |
+-------------+     +-------------------+     +-------------------------+
```

---

## Key Features

1. **Autonomous Multi-Agent Architecture**:
   - `sweeper`: Discovers matching roles and stages them into the tracker without applying.
   - `needs-you-drainer`: Works through login/account-required portals, registers with a secure shared password, and navigates complex ATS forms.
   - `apply-auditor`: Verifies submitted status exclusively through official Gmail confirmation receipts.
   - `tracker-keeper`: Guarantees atomic deduplication, URL normalization, and CSV sync.
   - `coordinator`: Orchestrates agents to prevent collision.
2. **Deterministic FastMCP Tracker Server**:
   - Built on standard library Python (`mcp/tracker-server/server.py`) with 0 external dependencies.
   - Automated locking (`loop/.applications.lock`), session claim leasing, and status transitions.
3. **CDP & Chrome Automation**:
   - Native integration with existing running Chrome via Chrome DevTools Protocol (`127.0.0.1:9222`).
   - Automated handling of file upload dialogs, multi-step ATS flows (Workday, Greenhouse, Lever, Ashby, LinkedIn EasyApply).
4. **Bespoke LaTeX CV Generation**:
   - 100% hallucination-free tailoring using baseline templates (`tectonic` compiler).
   - Strict 2-page constraint enforcement via `pdfinfo`.
   - Automated negative checks for forbidden claims and facts.
5. **Zero Data Leakage & Supply-Chain Guards**:
   - Strict `.gitignore` prevents committing personal data, generated PDFs, or credentials.
   - Built-in supply-chain guard verification (`tools/security_guards.py`).

---

## 5-Minute Quickstart

### 1. Prerequisites

- **Python 3.11+**
- **Node.js** (or **Bun**)
- **Tectonic** (LaTeX engine):
  ```bash
  brew install tectonic poppler
  ```

### 2. Setup

Clone the repository and run the setup script:

```bash
git clone https://github.com/prab-gupta/job-hunt.git
cd job-hunt
./setup.sh
```

`setup.sh` will:
- Check required system binaries.
- Initialize `.env` from `config/.env.example`.
- Initialize `config/profile.json` from `config/profile.example.json`.
- Initialize `applications.csv` from `templates/applications_template.csv`.
- Install search CLI dependencies.

### 3. Configure Candidate Profile & Secrets

1. Edit `.env` with your settings:
   ```bash
   CDP_URL=http://127.0.0.1:9222
   JOBS_ACCOUNT_PASSWORD=YourSecureSharedPassword123!
   CANDIDATE_EMAIL=you@example.com
   ```
2. Edit `config/profile.json` (or run `/setup` inside Claude Code) with your personal work history, target roles, education, and salary bounds.

### 4. Start Remote Chrome

Launch your daily Chrome browser with remote debugging enabled:

```bash
# macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

# Linux
google-chrome --remote-debugging-port=9222
```

### 5. Verify Readiness

Run the automated readiness suite:

```bash
python3 scripts/verify_readiness.py
```

---

## Core Commands & Workflows

### Manual / Interactive Commands

- `/setup`: Run the conversational onboarding wizard to build or update your profile.
- `/scrape`: Search configured job boards and deduplicate against existing tracker records.
- `/apply <url>`: Evaluate a target posting, generate a tailored CV and cover letter, and submit.
- `/rank`: Rank pending candidate leads by fit score.
- `/upskill`: Analyze skill gaps across tracked postings.

### Autonomous Daemon Pipeline

Run the tracker MCP server:

```bash
python3 mcp/tracker-server/server.py
```

The server exposes tools for agents (`stats`, `search_rows`, `next_needs_you`, `add_row`, `update_row`, `release_claim`, `regenerate_needs_you`, `sync_paths`).

---

## Directory Structure

```
├── .agents/skills/          # Portable search CLI skills (jobindex, freehire, linkedin, etc.)
├── .claude/
│   ├── commands/            # Slash command definitions (/apply, /scrape, /setup, etc.)
│   └── skills/              # Agent skills and methodology
├── config/
│   ├── .env.example         # Environment template (CDP, passwords, email)
│   └── profile.example.json # Structured candidate facts and forbidden claim rules
├── cv/
│   └── main_example.tex     # Baseline ATS moderncv template
├── cover_letters/
│   ├── cover.cls            # XeLaTeX cover letter document class
│   └── cover_example.tex    # Baseline cover letter template
├── mcp/
│   └── tracker-server/      # FastMCP stdlib Python application tracker server
├── scripts/
│   ├── apply_easy_apply.js  # LinkedIn EasyApply automation via CDP
│   ├── generate_canonical_cv.py # Tectonic CV compiler with 2-page enforcement
│   └── verify_readiness.py  # Health check & test runner
├── templates/
│   ├── applications_template.csv # Empty tracker schema
│   └── cv/ats_clean/        # Clean 2-page ATS Tectonic skeleton
├── tools/
│   └── security_guards.py   # Supply-chain and personal data leak guards
├── AGENTS.md                # Multi-agent operating guidelines
├── AGENT-INSTRUCTIONS.md    # Agent instruction contract & status specifications
├── setup.sh                 # 1-step installation script
└── README.md                # Documentation
```

---

## Testing & Quality Assurance

Run the test suite at any time:

```bash
# Run tracker server unit tests
python3 -m unittest discover -s mcp/tracker-server -p 'test_*.py'

# Run supply-chain security guards
python3 tools/security_guards.py

# Run complete readiness check
python3 scripts/verify_readiness.py
```

---

## License

MIT License.
