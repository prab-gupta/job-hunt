const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context = browser.contexts()[0];
  const page = await context.newPage();
  await page.goto('https://www.linkedin.com/jobs/view/4446993455/', { waitUntil: 'domcontentloaded' });
  
  // Find the apply link
  const applyLink = await page.$('a.jobs-apply-button') || await page.$('a:has-text("Apply")');
  if (applyLink) {
    const [newPage] = await Promise.all([
      context.waitForEvent('page'),
      applyLink.click()
    ]);
    await newPage.waitForLoadState('domcontentloaded');
    console.log("Navigated to SmartRecruiters:", newPage.url());
    
    // Check if it's SmartRecruiters
    if (newPage.url().includes('smartrecruiters')) {
      // Find "Apply" or "Create Account"
      const text = await newPage.evaluate(() => document.body.innerText.substring(0, 1000));
      console.log("SmartRecruiters text:", text);
    }
  } else {
    console.log("Apply link not found on LinkedIn");
  }
  
  await browser.close();
})();
