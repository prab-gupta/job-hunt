const { chromium } = require('playwright');
const { execSync } = require('child_process');
const fs = require('fs');

const jobs = [
  { company: "Workday", url: "https://www.linkedin.com/jobs/view/4426822677/", cv: "/Users/prab/Downloads/claud jobs/cv/main_Workday_AgenticAI.pdf" },
  { company: "kausable", url: "https://www.linkedin.com/jobs/view/4453440697/", cv: "/Users/prab/Downloads/claud jobs/cv/main_kausable_SoftwareEngineer.pdf" },
  { company: "Bamboo Works", url: "https://www.linkedin.com/jobs/view/4437140753/", cv: "/Users/prab/Downloads/claud jobs/cv/main_BambooWorks_AIAutomation.pdf" },
  { company: "scandiweb", url: "https://www.linkedin.com/jobs/view/4411355407/", cv: "/Users/prab/Downloads/claud jobs/cv/main_scandiweb_GTM.pdf" },
  { company: "Capgemini", url: "https://www.linkedin.com/jobs/view/4374760503/", cv: "/Users/prab/Downloads/claud jobs/cv/main_Capgemini_DataEngineer.pdf" }
];

(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context = browser.contexts()[0];
  const page = await context.newPage();
  
  for (const job of jobs) {
    try {
      console.log(`Processing ${job.company}...`);
      
      // Update profile.json CV path for apply.mjs
      const profile = JSON.parse(fs.readFileSync('apply-bot/profile.json'));
      profile.cvPath = job.cv;
      fs.writeFileSync('apply-bot/profile.json', JSON.stringify(profile, null, 2));

      await page.goto(job.url, { waitUntil: 'domcontentloaded' });
      await page.waitForTimeout(2000);
      
      const links = await page.$$eval('a, button', els => els.map(e => ({ text: e.innerText, href: e.href })).filter(e => e.text.toLowerCase().includes('apply')));
      
      const externalLink = links.find(l => l.href && l.href.includes('safety/go'));
      if (externalLink) {
        console.log(`  External ATS found. Running apply.mjs...`);
        try {
          // Decode URL
          const decodedUrl = decodeURIComponent(externalLink.href.split('url=')[1].split('&')[0]);
          execSync(`node apply-bot/apply.mjs "${decodedUrl}" --submit`, { stdio: 'inherit' });
          console.log(`  Successfully submitted ${job.company}`);
        } catch(e) {
          console.log(`  Failed to auto-apply ${job.company}`);
        }
      } else {
        console.log(`  No external link found. Must be Easy Apply or different UI. Using manual fallback.`);
        // Run apply.mjs directly on the linked in URL (might fail but worth trying)
        try {
           execSync(`node apply-bot/apply.mjs "${job.url}" --submit`, { stdio: 'inherit' });
        } catch(e) {}
      }
    } catch (e) {
      console.log(`Error processing ${job.company}: ${e.message}`);
    }
  }
  
  await browser.disconnect();
})();
