const fs = require('fs');
const lines = fs.readFileSync('/Users/prab/.gemini/antigravity/brain/ef77eada-777c-44ce-be2a-d6a8b4c47c87/.system_generated/logs/transcript_full.jsonl', 'utf8').split('\n');

for (let i = lines.length - 1; i >= 0; i--) {
    const line = lines[i];
    if (!line) continue;
    const item = JSON.parse(line);
    if (item.type === 'EPHEMERAL_MESSAGE' && item.source === 'SYSTEM' && item.content.includes('<SYSTEM_MESSAGE>')) {
        if (item.content.includes('NCS Group')) {
            console.log("Found NCS Group. Match attempt:");
            const matches = [...item.content.matchAll(/```latex([\s\S]*?)```/g)];
            console.log("Matches:", matches.length);
            if (matches.length > 0) {
                console.log("Match 0 length:", matches[0][1].length);
                fs.writeFileSync('cv/main_NCSGroup_AIEngineer.tex', matches[0][1].trim());
            }
            if (matches.length > 1) {
                fs.writeFileSync('cover_letters/cover_NCSGroup_AIEngineer.tex', matches[1][1].trim());
            }
        }
        if (item.content.includes('Nadara')) {
            const matches = [...item.content.matchAll(/```latex([\s\S]*?)```/g)];
            if (matches.length > 1) {
                fs.writeFileSync('cv/main_Nadara_AIEngineer.tex', matches[0][1].trim());
                fs.writeFileSync('cover_letters/cover_Nadara_AIEngineer.tex', matches[1][1].trim());
            }
        }
        if (item.content.includes('Intapp')) {
            const matches = [...item.content.matchAll(/```latex([\s\S]*?)```/g)];
            if (matches.length > 1) {
                fs.writeFileSync('cv/main_Intapp_ClientSupport.tex', matches[0][1].trim());
                fs.writeFileSync('cover_letters/cover_Intapp_ClientSupport.tex', matches[1][1].trim());
            }
        }
        if (item.content.includes('BASF')) {
            const matches = [...item.content.matchAll(/```latex([\s\S]*?)```/g)];
            if (matches.length > 1) {
                fs.writeFileSync('cv/main_BASF_AIEngineer.tex', matches[0][1].trim());
                fs.writeFileSync('cover_letters/cover_BASF_AIEngineer.tex', matches[1][1].trim());
            }
        }
    }
}
console.log("Done");
