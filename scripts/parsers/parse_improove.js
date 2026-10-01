const fs = require('fs');
const lines = fs.readFileSync('/Users/prab/.gemini/antigravity/brain/1f5c8c16-3ee2-4531-a280-8525791b2124/.system_generated/logs/transcript_full.jsonl', 'utf8').split('\n');

for (let i = lines.length - 1; i >= 0; i--) {
    const line = lines[i];
    if (!line) continue;
    const item = JSON.parse(line);
    if (item.type === 'PLANNER_RESPONSE' && item.tool_calls) {
        for (const tc of item.tool_calls) {
            if (tc.name === 'send_message') {
                const content = tc.args.Message;
                const extract = (text) => {
                    const matches = [];
                    const regex = /```latex([\s\S]*?)```/g;
                    let match;
                    while ((match = regex.exec(text)) !== null) {
                        matches.push(match[1].trim());
                    }
                    return matches;
                };

                const matches = extract(content);
                if (matches.length >= 2) {
                    fs.writeFileSync('cv/main_Improove_ForwardDeployedEngineer.tex', matches[0]);
                    fs.writeFileSync('cover_letters/cover_Improove_ForwardDeployedEngineer.tex', matches[1]);
                    console.log("Extracted Improove successfully!");
                }
            }
        }
    }
}
