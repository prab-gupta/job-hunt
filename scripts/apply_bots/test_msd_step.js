const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context = browser.contexts()[0];
  const pages = context.pages();
  const page = pages.find(p => p.url().includes('msd.wd5.myworkdayjobs.com'));
  
  if (page) {
    console.log("URL:", page.url());
    const btns = await page.$$eval('button', els => els.map(e => e.innerText));
    console.log("Buttons:", btns);
  }
  process.exit(0);
})();
