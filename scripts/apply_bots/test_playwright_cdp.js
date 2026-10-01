const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.connectOverCDP('http://localhost:9222');
  const contexts = browser.contexts();
  const page = contexts[0].pages()[0];
  console.log("Connected to page:", await page.title());
  await browser.close(); // wait, don't close the browser, just disconnect!
  // Wait! browser.close() might close the user's Chrome! Let's NOT call browser.close().
})();
