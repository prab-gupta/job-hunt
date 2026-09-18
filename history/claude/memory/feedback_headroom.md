---
name: feedback_headroom
description: User wants Headroom (context-compression tool at ~/.venvs/headroom-ai/bin/headroom) used where relevant in Claude Code sessions
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 237a3cff-dd16-4810-8bd3-960e29fe6c44
  modified: 2026-09-09T05:24:10.195Z
---

User instruction 2026-09-09: "Use Headroom from now on where relevant". Headroom v0.37 is installed at `/Users/prab/.venvs/headroom-ai/bin/headroom` (Codex already wired via `[mcp_servers.headroom]`). On 2026-09-09 I ran `headroom mcp install --agent claude`, which registers the Headroom MCP server (compress / retrieve / stats tools) for Claude Code; it only appears in sessions started after that.

**Why:** Long job-loop sessions burn context on big tool outputs (page text, CSV dumps, JD files). Headroom's Compress-Cache-Retrieve trims those.

**How to apply:** In a new session check for `mcp__headroom__*` tools via ToolSearch; when present, pass large tool outputs (page text, search dumps, CSV scans) through Headroom compress and retrieve only what is needed. Full proxy routing (`headroom init claude` / `headroom wrap claude`, ANTHROPIC_BASE_URL to 127.0.0.1:8787) does not work inside the Claude Desktop app (doctor: "Desktop overwrites ANTHROPIC_BASE_URL"), so use the MCP path. Related: [[feedback_cheap_agents_apply]], [[project_job_search]].
