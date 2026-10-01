const fs = require('fs');

const lines = fs.readFileSync('/Users/prab/.gemini/antigravity/brain/ef77eada-777c-44ce-be2a-d6a8b4c47c87/.system_generated/logs/transcript_full.jsonl', 'utf8').split('\n');

for (let i = lines.length - 1; i >= 0; i--) {
    const line = lines[i];
    if (!line) continue;
    const item = JSON.parse(line);
    if (item.type === 'EPHEMERAL_MESSAGE' && item.source === 'SYSTEM') {
        const content = item.content;
        
        const extract = (text) => {
            const matches = [];
            const regex = /```latex([\s\S]*?)```/g;
            let match;
            while ((match = regex.exec(text)) !== null) {
                matches.push(match[1].trim());
            }
            return matches;
        };

        if (content.includes('NCS Group') && !fs.existsSync('cv/main_NCSGroup_AIEngineer.tex')) {
            const matches = extract(content);
            if (matches.length >= 2) {
                fs.writeFileSync('cv/main_NCSGroup_AIEngineer.tex', matches[0]);
                fs.writeFileSync('cover_letters/cover_NCSGroup_AIEngineer.tex', matches[1]);
            }
        }
        
        if (content.includes('Nadara') && !fs.existsSync('cv/main_Nadara_AIEngineer.tex')) {
            const matches = extract(content);
            if (matches.length >= 2) {
                fs.writeFileSync('cv/main_Nadara_AIEngineer.tex', matches[0]);
                fs.writeFileSync('cover_letters/cover_Nadara_AIEngineer.tex', matches[1]);
            }
        }

        if (content.includes('Intapp') && !fs.existsSync('cv/main_Intapp_ClientSupport.tex')) {
            const matches = extract(content);
            if (matches.length >= 2) {
                fs.writeFileSync('cv/main_Intapp_ClientSupport.tex', matches[0]);
                fs.writeFileSync('cover_letters/cover_Intapp_ClientSupport.tex', matches[1]);
            }
        }

        if (content.includes('BASF') && !fs.existsSync('cv/main_BASF_AIEngineer.tex')) {
            const matches = extract(content);
            if (matches.length >= 2) {
                fs.writeFileSync('cv/main_BASF_AIEngineer.tex', matches[0]);
                fs.writeFileSync('cover_letters/cover_BASF_AIEngineer.tex', matches[1]);
            }
        }
    }
}
console.log("Parsed using safe regex!");
