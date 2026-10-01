const fs = require('fs');
const lines = fs.readFileSync('/Users/prab/.gemini/antigravity/brain/ef77eada-777c-44ce-be2a-d6a8b4c47c87/.system_generated/logs/transcript_full.jsonl', 'utf8').split('\n');

for (let i = lines.length - 1; i >= 0; i--) {
    const line = lines[i];
    if (!line) continue;
    const item = JSON.parse(line);
    if (item.type === 'SYSTEM_MESSAGE' || item.type === 'USER_INPUT' || item.type === 'EPHEMERAL_MESSAGE') {
        const content = item.content || "";
        
        const extract = (text) => {
            const matches = [];
            const regex = /```latex([\s\S]*?)```/g;
            let match;
            while ((match = regex.exec(text)) !== null) {
                matches.push(match[1].trim());
            }
            return matches;
        };

        if (content.includes('Bludigit') && !fs.existsSync('cv/main_Bludigit_AIEngineer.tex')) {
            const matches = extract(content);
            if (matches.length >= 2) {
                fs.writeFileSync('cv/main_Bludigit_AIEngineer.tex', matches[0]);
                fs.writeFileSync('cover_letters/cover_Bludigit_AIEngineer.tex', matches[1]);
            }
        }
        
        if (content.includes('Kyndryl') && !fs.existsSync('cv/main_Kyndryl_ForwardDeployedEngineer.tex')) {
            const matches = extract(content);
            if (matches.length >= 2) {
                fs.writeFileSync('cv/main_Kyndryl_ForwardDeployedEngineer.tex', matches[0]);
                fs.writeFileSync('cover_letters/cover_Kyndryl_ForwardDeployedEngineer.tex', matches[1]);
            }
        }

        if (content.includes('Improove') && !fs.existsSync('cv/main_Improove_ForwardDeployedEngineer.tex')) {
            const matches = extract(content);
            if (matches.length >= 2) {
                fs.writeFileSync('cv/main_Improove_ForwardDeployedEngineer.tex', matches[0]);
                fs.writeFileSync('cover_letters/cover_Improove_ForwardDeployedEngineer.tex', matches[1]);
            }
        }

        if (content.includes('Dots') && !fs.existsSync('cv/main_Dots_ForwardDeployEngineer.tex')) {
            const matches = extract(content);
            if (matches.length >= 2) {
                fs.writeFileSync('cv/main_Dots_ForwardDeployEngineer.tex', matches[0]);
                fs.writeFileSync('cover_letters/cover_Dots_ForwardDeployEngineer.tex', matches[1]);
            }
        }
        
        if (content.includes('TechTree') && !fs.existsSync('cv/main_TechTree_ForwardDeployedEngineer.tex')) {
            const matches = extract(content);
            if (matches.length >= 2) {
                fs.writeFileSync('cv/main_TechTree_ForwardDeployedEngineer.tex', matches[0]);
                fs.writeFileSync('cover_letters/cover_TechTree_ForwardDeployedEngineer.tex', matches[1]);
            }
        }
    }
}
console.log("Parsed using safe regex and right type!");
