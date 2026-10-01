const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context = browser.contexts()[0];
  const page = await context.newPage();
  await page.goto('https://www.linkedin.com/jobs/view/4446993455/', { waitUntil: 'domcontentloaded' });
  
  // Wait a bit
  await page.waitForTimeout(3000);
  
  // Dump all links that have 'jobs' or 'apply' in them
  const links = await page.$$eval('a, button', els => els.map(e => ({ tag: e.tagName, text: e.innerText, href: e.href, class: e.className })).filter(e => e.text.toLowerCase().includes('apply')));
  console.log(JSON.stringify(links, null, 2));
  
  await browser.close();
})();
