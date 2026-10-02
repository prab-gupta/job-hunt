# Tracker MCP server

Stdio MCP server for this repo's job tracker. `applications.csv` stays the stored data. `data/csvs/applications.csv` and `loop/applications.csv` are byte copies. `docs/needs-you.md` is a view. The server is the access layer agents should use. It does not commit git, and it does not read or store `JOBS_ACCOUNT_PASSWORD`.

Python 3.11+ from the standard library. No extra packages.

```bash
python3 mcp/tracker-server/server.py
python3 -m unittest discover -s mcp/tracker-server -p 'test_*.py'
```

## Tools

| Tool | What it does |
| --- | --- |
| `stats` | Counts per status and per `needs_you` blocker type |
| `search_rows` | Filter by `status`, `blocker`, `company`, or `text` |
| `next_needs_you` | Claim the next row the autonomous drainer can work. Login/account rows with no human step come first, then other rows with no human step. Captcha and human sign-in are not returned. One claim per row. |
| `release_claim` | Drop claims held by that agent |
| `add_row` | Validate columns and status. Reject a duplicate normalized URL (lowercase, query string removed, trailing slash stripped). |
| `update_row` | Validate the status change. `submitted` is only accepted from actor `apply-auditor` with a `gmail:` note and `date_applied`. A skipped row cannot be reapplied. |
| `regenerate_needs_you` | Rewrite `docs/needs-you.md` from the CSV |
| `sync_paths` | Copy the root CSV onto the other two paths and check that all three sha256 hashes match |

Writes take `loop/.applications.lock`. If the lock exists, the write is refused. Claims live in gitignored `loop/.needs-you-claims.json`. That file is not an application list.

Do not pass a password, token, or `JOBS_ACCOUNT_PASSWORD=...` as a tool argument. The server rejects those values and does not write them.

## Claude Code

Commit this as `.mcp.json` in the repo root (already in this repo):

```json
{
  "mcpServers": {
    "tracker": {
      "command": "python3",
      "args": ["mcp/tracker-server/server.py"]
    }
  }
}
```

Restart Claude Code in this directory. The server is named `tracker`.

## Cursor

`.cursor/mcp.json` in this repo:

```json
{
  "mcpServers": {
    "tracker": {
      "command": "python3",
      "args": ["mcp/tracker-server/server.py"]
    }
  }
}
```

Reload the window. In Cursor Settings, MCP, `tracker` should list the eight tools.

If either client starts the process from another working directory, the server still finds the repo from its own file path. `TRACKER_ROOT` overrides that path for tests only. Do not point it at a second copy of the tracker.

## Fallback

If this server is not connected, agents follow the CSV procedure in the skills: read `applications.csv`, and let `tracker-keeper` write the root file, copy it to the other two paths, and regenerate `docs/needs-you.md`.
