const fs = require('fs');

const lines = fs.readFileSync('/Users/prab/.gemini/antigravity/brain/ef77eada-777c-44ce-be2a-d6a8b4c47c87/.system_generated/logs/transcript_full.jsonl', 'utf8').split('\n');

for (const line of lines) {
    if (!line) continue;
    const item = JSON.parse(line);
    if (item.type === 'EPHEMERAL_MESSAGE' && item.source === 'SYSTEM') {
        const content = item.content;
        
        if (content.includes('NCS Group')) {
            const matches = [...content.matchAll(/```latex\n([\s\S]*?)\n```/g)];
            if (matches.length >= 2) {
                fs.writeFileSync('cv/main_NCSGroup_AIEngineer.tex', matches[0][1]);
                fs.writeFileSync('cover_letters/cover_NCSGroup_AIEngineer.tex', matches[1][1]);
            }
        }
        
        if (content.includes('Nadara')) {
            const matches = [...content.matchAll(/```latex\n([\s\S]*?)\n```/g)];
            if (matches.length >= 2) {
                fs.writeFileSync('cv/main_Nadara_AIEngineer.tex', matches[0][1]);
                fs.writeFileSync('cover_letters/cover_Nadara_AIEngineer.tex', matches[1][1]);
            }
        }

        if (content.includes('Intapp')) {
            const matches = [...content.matchAll(/```latex\n([\s\S]*?)\n```/g)];
            if (matches.length >= 2) {
                fs.writeFileSync('cv/main_Intapp_ClientSupport.tex', matches[0][1]);
                fs.writeFileSync('cover_letters/cover_Intapp_ClientSupport.tex', matches[1][1]);
            }
        }

        if (content.includes('BASF')) {
            const matches = [...content.matchAll(/```latex\n([\s\S]*?)\n```/g)];
            if (matches.length >= 2) {
                fs.writeFileSync('cv/main_BASF_AIEngineer.tex', matches[0][1]);
                fs.writeFileSync('cover_letters/cover_BASF_AIEngineer.tex', matches[1][1]);
            }
        }
    }
}
console.log("Parsed");
