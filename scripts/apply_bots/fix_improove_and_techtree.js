const fs = require('fs');

// Fix TechTree cover letter
let techtree = fs.readFileSync('cover_letters/cover_TechTree_ForwardDeployedEngineer.tex', 'utf8');
techtree = techtree.replace('\\documentclass[]{cover}', '\\documentclass[10.5pt,a4paper]{article}');
fs.writeFileSync('cover_letters/cover_TechTree_ForwardDeployedEngineer.tex', techtree);

// Fix Improove extraction
const transcript = fs.readFileSync('/Users/prab/.gemini/antigravity/brain/1f5c8c16-3ee2-4531-a280-8525791b2124/.system_generated/logs/transcript_full.jsonl', 'utf8');
const regex = /```latex\\n([\\s\\S]*?)\\n```/g;
const matches = [];
let match;
while ((match = regex.exec(transcript)) !== null) {
    // Need to unescape the json string manually or parse it
    matches.push(match[1]);
}
if (matches.length >= 2) {
    let cv = matches[matches.length - 2].replace(/\\\\n/g, '\n').replace(/\\\\"/g, '"');
    let cl = matches[matches.length - 1].replace(/\\\\n/g, '\n').replace(/\\\\"/g, '"');
    fs.writeFileSync('cv/main_Improove_ForwardDeployedEngineer.tex', cv);
    fs.writeFileSync('cover_letters/cover_Improove_ForwardDeployedEngineer.tex', cl);
    console.log("Fixed Improove!");
} else {
    console.log("Regex failed to find matches");
}

