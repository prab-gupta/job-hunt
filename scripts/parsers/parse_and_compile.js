const fs = require('fs');

function extractCode(text, type) {
    const regex = new RegExp("```latex\\n([\\s\\S]*?)\\n```", "g");
    let match;
    let matches = [];
    while ((match = regex.exec(text)) !== null) {
        matches.push(match[1]);
    }
    return matches;
}

// NCS Group
const ncs_cv = fs.readFileSync('/Users/prab/.gemini/antigravity/brain/0b1bf64a-d3cf-44f3-8ea2-340f5a5c7d81/.system_generated/logs/transcript.jsonl', 'utf8');
const ncs_matches = extractCode(ncs_cv);
fs.writeFileSync('cv/main_NCSGroup_AIEngineer.tex', ncs_matches[0]);
fs.writeFileSync('cover_letters/cover_NCSGroup_AIEngineer.tex', ncs_matches[1]);

// Nadara
const nadara_cv = fs.readFileSync('/Users/prab/.gemini/antigravity/brain/dc9adbf2-97f3-45ae-b572-89c15152b53b/.system_generated/logs/transcript.jsonl', 'utf8');
const nadara_matches = extractCode(nadara_cv);
fs.writeFileSync('cv/main_Nadara_AIEngineer.tex', nadara_matches[0]);
fs.writeFileSync('cover_letters/cover_Nadara_AIEngineer.tex', nadara_matches[1]);

// Intapp
const intapp_cv = fs.readFileSync('/Users/prab/.gemini/antigravity/brain/510f18c5-1fff-4dae-a97d-2d1cd922a62b/.system_generated/logs/transcript.jsonl', 'utf8');
const intapp_matches = extractCode(intapp_cv);
fs.writeFileSync('cv/main_Intapp_ClientSupport.tex', intapp_matches[0]);
fs.writeFileSync('cover_letters/cover_Intapp_ClientSupport.tex', intapp_matches[1]);

// BASF
const basf_cv = fs.readFileSync('/Users/prab/.gemini/antigravity/brain/962e02c8-cb39-4c2d-9fbf-e849908b74ed/.system_generated/logs/transcript.jsonl', 'utf8');
const basf_matches = extractCode(basf_cv);
fs.writeFileSync('cv/main_BASF_AIEngineer.tex', basf_matches[0]);
fs.writeFileSync('cover_letters/cover_BASF_AIEngineer.tex', basf_matches[1]);

console.log("Extracted files successfully!");
