const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context = browser.contexts()[0];
  const page = await context.newPage();
  await page.goto('https://www.linkedin.com/jobs/view/4446993455/', { waitUntil: 'domcontentloaded' });
  
  // Click Apply
  const applyLink = await page.$('a.jobs-apply-button') || await page.$('a:has-text("Apply")');
  if (applyLink) {
    console.log("Found apply link, clicking...");
    const [newPage] = await Promise.all([
      context.waitForEvent('page'),
      applyLink.click()
    ]);
    await newPage.waitForLoadState('domcontentloaded');
    console.log("Navigated to:", newPage.url());
  } else {
    console.log("Apply link not found on LinkedIn");
  }
  
  await browser.disconnect();
})();
