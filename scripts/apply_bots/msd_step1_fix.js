const { chromium } = require('playwright');
const P = require('./apply-bot/profile.json');

(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context = browser.contexts()[0];
  const pages = context.pages();
  const page = pages.find(p => p.url().includes('msd.wd5.myworkdayjobs.com'));
  
  if (page) {
    await page.bringToFront();
    
    // Check if we are still on step 1 (My Information)
    const text = await page.evaluate(() => document.body.innerText);
    if (!text.includes("current step 1 of 5")) {
      console.log("Not on step 1 anymore");
      process.exit(0);
    }

    console.log("Fixing missing fields...");
    
    // Fill required comboboxes (Province, Phone Device Type)
    const buttons = await page.$$('button[aria-haspopup="listbox"]');
    for (let btn of buttons) {
      const label = await page.evaluate(b => {
        const id = b.id;
        const l = document.querySelector(`label[for="${id}"]`);
        return l ? l.innerText : "";
      }, btn);
      console.log("Found dropdown:", label);
      
      if (label.includes("Province")) {
        await btn.click();
        await page.waitForTimeout(500);
        // Find Venezia
        const options = await page.$$('[role="option"]');
        for (let opt of options) {
          if ((await opt.innerText()).includes('Venezia')) {
            await opt.click();
            break;
          }
        }
      }
      if (label.includes("Phone Device Type")) {
        await btn.click();
        await page.waitForTimeout(500);
        const options = await page.$$('[role="option"]');
        for (let opt of options) {
          if ((await opt.innerText()).includes('Mobile')) {
            await opt.click();
            break;
          }
        }
      }
    }
    
    await page.waitForTimeout(1000);
    await page.click('button:has-text("Next")');
    console.log("Clicked Next after fixes!");
  }
  process.exit(0);
})();
