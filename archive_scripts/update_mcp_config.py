import json, os

claude_settings = os.path.expanduser("~/.claude/settings.json")
if os.path.exists(claude_settings):
    try:
        with open(claude_settings, "r") as f:
            d = json.load(f)
        
        if "mcpServers" not in d:
            d["mcpServers"] = {}
            
        d["mcpServers"]["jobgpt"] = {
            "type": "stdio",
            "command": "bun",
            "args": ["/Users/prab/Downloads/claud jobs/.agents/plugins/jobgpt-mcp-server/src/stdio.ts"],
            "env": {
                "JOBGPT_API_KEY": os.environ.get("JOBGPT_API_KEY", "")
            }
        }
        with open(claude_settings, "w") as f:
            json.dump(d, f, indent=2)
        print("Registered jobgpt MCP server in ~/.claude/settings.json")
    except Exception as e:
        print("Error updating claude settings:", e)
