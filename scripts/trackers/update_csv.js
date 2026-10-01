const fs = require('fs');

// Update queue.csv
let queue = fs.readFileSync('loop/queue.csv', 'utf8').split('\n');
for (let i = 0; i < queue.length; i++) {
    if (queue[i].startsWith('FINECOBANK BANCA FINECO SPA,')) {
        queue[i] = queue[i].replace('TO APPLY', 'CLOSED');
    } else if (queue[i].startsWith('Accenture na Slovensku,')) {
        queue[i] = queue[i].replace('TO APPLY', 'SUBMITTED');
    } else if (queue[i].startsWith('Allitude,')) {
        queue[i] = queue[i].replace('TO APPLY', 'NEEDS HUMAN');
    } else if (queue[i].startsWith('Sonova Group,')) {
        queue[i] = queue[i].replace('TO APPLY', 'NEEDS HUMAN');
    } else if (queue[i].startsWith('ams OSRAM,')) {
        queue[i] = queue[i].replace('TO APPLY', 'NEEDS HUMAN');
    }
}
fs.writeFileSync('loop/queue.csv', queue.join('\n'));

// Update applications.csv
let apps = fs.readFileSync('loop/applications.csv', 'utf8');
apps += `\nAccenture na Slovensku,Senior Integration Low-Code Developer,Submitted,Completed via Antigravity Chrome Applier subagent,2026-09-27`;
fs.writeFileSync('loop/applications.csv', apps);
console.log("Updated CSVs!");
