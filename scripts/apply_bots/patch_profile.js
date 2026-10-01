const fs = require('fs');
const profile = JSON.parse(fs.readFileSync('apply-bot/profile.json'));
profile.cvPath = '/Users/prab/Downloads/claud jobs/cv/main_FINECOBANK_LeadAIEngineer.pdf';
fs.writeFileSync('apply-bot/profile.json', JSON.stringify(profile, null, 2));
console.log('Updated profile.json for FINECOBANK');
