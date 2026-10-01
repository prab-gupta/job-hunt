const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context = browser.contexts()[0];
  const pages = context.pages();
  const page = pages.find(p => p.url().includes('msd.wd5.myworkdayjobs.com'));
  if (!page) { console.log('MSD Workday page not found'); process.exit(1); }
  
  await page.bringToFront();
  console.log('Found page:', await page.title());

  // Find the hidden input[type="file"]
  const fileInputs = await page.$$('input[type="file"]');
  console.log(`Found ${fileInputs.length} file inputs`);
  if (fileInputs.length > 0) {
    await fileInputs[0].setInputFiles('/Users/prab/Downloads/claud jobs/cv/main_msd_ai-engineer.pdf');
    console.log('Successfully uploaded CV via setInputFiles');
  } else {
    console.log('Could not find input[type="file"]');
  }
  
  await browser.disconnect();
})();
