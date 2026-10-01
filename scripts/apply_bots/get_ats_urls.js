const { chromium } = require('playwright');
const jobs = [
  "https://www.linkedin.com/jobs/view/4426822677/", // Workday
  "https://www.linkedin.com/jobs/view/4453440697/", // kausable
  "https://www.linkedin.com/jobs/view/4437140753/", // Bamboo Works
  "https://www.linkedin.com/jobs/view/4411355407/", // scandiweb
  "https://www.linkedin.com/jobs/view/4374760503/"  // Capgemini
];

(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context = browser.contexts()[0];
  const page = await context.newPage();
  
  for (const url of jobs) {
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded' });
      await page.waitForTimeout(2000);
      const links = await page.$$eval('a, button', els => els.map(e => ({ tag: e.tagName, text: e.innerText, href: e.href, class: e.className })).filter(e => e.text.toLowerCase().includes('apply')));
      
      const externalLink = links.find(l => l.href && l.href.includes('safety/go'));
      if (externalLink) {
        console.log(`URL for ${url}: ${externalLink.href}`);
      } else {
        console.log(`No external link found for ${url}`);
      }
    } catch (e) {
      console.log(`Failed for ${url}: ${e.message}`);
    }
  }
  
  await browser.disconnect(); // Use disconnect, not close!
})();
