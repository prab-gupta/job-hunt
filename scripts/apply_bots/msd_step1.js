const { chromium } = require('playwright');
const P = require('./apply-bot/profile.json');

(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context = browser.contexts()[0];
  const pages = context.pages();
  const page = pages.find(p => p.url().includes('msd.wd5.myworkdayjobs.com'));
  
  if (page) {
    await page.bringToFront();
    
    // How did you hear about us?
    // It's an input with role=combobox? Or just text? It says tag="INPUT", type="text", label="How Did You Hear About Us?*"
    const howDidYouHear = await page.$('input[aria-label="How Did You Hear About Us?*"]');
    if (howDidYouHear) {
      await howDidYouHear.click();
      await page.keyboard.type('LinkedIn');
      await page.waitForTimeout(1000);
      await page.keyboard.press('Enter');
    }
    
    // Have you worked here before (No) -> it's the second radio
    const radios = await page.$$('input[type="radio"]');
    if (radios.length >= 2) await radios[1].click();

    // Given Name(s)*
    const givenName = await page.$('input:not([type="hidden"]):not([type="radio"]):not([type="checkbox"])[id*="firstName"]');
    if (givenName) await givenName.fill(P.firstName || 'Prabhavit');
    else {
      // Find by label
      const labels = await page.$$('label');
      for (let l of labels) {
        if ((await l.innerText()).includes('Given Name')) {
          const id = await l.getAttribute('for');
          await page.fill(`input[id="${id}"]`, 'Prabhavit');
        }
        if ((await l.innerText()).includes('Family Name')) {
          const id = await l.getAttribute('for');
          await page.fill(`input[id="${id}"]`, 'Gupta');
        }
        if ((await l.innerText()).includes('Street or Place Name')) {
          const id = await l.getAttribute('for');
          await page.fill(`input[id="${id}"]`, 'Santa Croce 1561');
        }
        if ((await l.innerText()).includes('Postal Code')) {
          const id = await l.getAttribute('for');
          await page.fill(`input[id="${id}"]`, '30175');
        }
        if ((await l.innerText()).includes('City')) {
          const id = await l.getAttribute('for');
          await page.fill(`input[id="${id}"]`, 'Venezia');
        }
        if ((await l.innerText()).includes('Phone Number')) {
          const id = await l.getAttribute('for');
          await page.fill(`input[id="${id}"]`, '3516107807');
        }
      }
    }
    
    // Next
    await page.click('button:has-text("Next")');
    console.log("Clicked Next!");
  }
  process.exit(0);
})();
