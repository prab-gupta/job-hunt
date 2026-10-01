const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context = browser.contexts()[0];
  const pages = context.pages();
  const page = pages.find(p => p.url().includes('msd.wd5.myworkdayjobs.com'));
  
  if (page) {
    await page.bringToFront();
    
    // Check if we are on step 2 (My Experience)
    const text = await page.evaluate(() => document.body.innerText.substring(0, 1000));
    console.log("PAGE TEXT:", text);

    // If it says "My Experience" or "Step 2 of 5" or similar, we can click Next
    // since Work Experience is parsed from the CV!
    // Often we don't need to add anything. We just click Next.
    
    // Wait a bit to ensure parsing is done
    await page.waitForTimeout(2000);
    
    // Let's just try to click Next to proceed to Step 3 (Application Questions)
    const nextBtn = await page.$('button:has-text("Next")');
    if (nextBtn) {
      await nextBtn.click();
      console.log("Clicked Next on My Experience step!");
    } else {
      console.log("Next button not found on this step.");
    }
  }
  process.exit(0);
})();
