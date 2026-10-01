const fs = require('fs');
const transcript = fs.readFileSync('/Users/prab/.gemini/antigravity/brain/cb434447-43f1-4c91-b4ec-acb40c3c0e62/.system_generated/logs/transcript_full.jsonl', 'utf8');
const regex = /```latex\\n([\\s\\S]*?)\\n```/g;
const matches = [];
let match;
while ((match = regex.exec(transcript)) !== null) {
    matches.push(match[1]);
}
if (matches.length >= 2) {
    let cv = matches[matches.length - 2].replace(/\\\\n/g, '\n').replace(/\\\\"/g, '"');
    let cl = matches[matches.length - 1].replace(/\\\\n/g, '\n').replace(/\\\\"/g, '"');
    fs.writeFileSync('cv/main_AnalogDevices_SeniorPrincipalFDE.tex', cv);
    fs.writeFileSync('cover_letters/cover_AnalogDevices_SeniorPrincipalFDE.tex', cl);
    console.log("Extracted Analog Devices!");
}
