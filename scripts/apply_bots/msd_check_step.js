const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context = browser.contexts()[0];
  const pages = context.pages();
  const page = pages.find(p => p.url().includes('msd.wd5.myworkdayjobs.com'));
  if (page) {
    const text = await page.evaluate(() => document.body.innerText.substring(0, 1000));
    console.log(text);
  }
  process.exit(0);
})();
