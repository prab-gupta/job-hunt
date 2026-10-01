const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context = browser.contexts()[0];
  const pages = context.pages();
  const page = pages.find(p => p.url().includes('msd.wd5.myworkdayjobs.com'));
  
  if (page) {
    const inputs = await page.$$eval('input, select, textarea, button, [role="button"], [role="listbox"]', els => els.map(el => {
      let label = '';
      if (el.id) {
        const labelEl = document.querySelector(`label[for="${el.id}"]`);
        if (labelEl) label = labelEl.innerText;
      }
      return { tag: el.tagName, type: el.type, label, text: el.innerText, role: el.getAttribute('role') };
    }));
    console.log(JSON.stringify(inputs.filter(i => i.type !== 'hidden'), null, 2));
  }
  process.exit(0);
})();
