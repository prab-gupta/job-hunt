const puppeteer = require('puppeteer-core');

(async () => {
  try {
    const browser = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222' });
    const pages = await browser.pages();
    let page = pages.find(p => p.url().includes('linkedin.com/jobs/view/4465068619'));
    
    if (!page) {
      console.log('LinkedIn tab not found, navigating in a new tab...');
      page = await browser.newPage();
      await page.goto('https://www.linkedin.com/jobs/view/4465068619/', { waitUntil: 'networkidle2' });
    } else {
      console.log('Found existing LinkedIn tab, bringing to front...');
      await page.bringToFront();
    }

    console.log("Page title:", await page.title());

    // Look for the "Apply" button
    const applyBtn = await page.$('.jobs-apply-button');
    if (applyBtn) {
      console.log('Clicking Apply button...');
      await applyBtn.click();
    } else {
      // Find any button or link containing "Apply"
      const buttons = await page.$$('a, button');
      let clicked = false;
      for (const btn of buttons) {
        const text = await page.evaluate(el => el.innerText, btn);
        if (text && text.trim() === 'Apply') {
          console.log('Clicking fallback Apply element...');
          await btn.click();
          clicked = true;
          break;
        }
      }
      if (!clicked) console.log('No Apply button found!');
    }

    await browser.disconnect();
  } catch (error) {
    console.error('Error:', error);
  }
})();
