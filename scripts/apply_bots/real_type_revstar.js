const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
    try {
        const devToolsInfo = fs.readFileSync('/Users/prab/Library/Application Support/Google/Chrome/DevToolsActivePort', 'utf8').split('\n');
        const port = devToolsInfo[0].trim();
        const browserPath = devToolsInfo[1].trim();
        const wsUrl = 'ws://127.0.0.1:' + port + browserPath;
        
        const browser = await puppeteer.connect({ browserWSEndpoint: wsUrl, defaultViewport: null });
        const pages = await browser.pages();
        let page = pages.find(p => p.url().includes('revstarcareers.com') || p.url().includes('workable.com/revstar'));
        
        if (!page) {
            console.error('Revstar tab not found');
            await browser.disconnect();
            return;
        }

        console.log('Revstar tab found. Bringing to front...');
        await page.bringToFront();

        const clearAndType = async (selector, text) => {
            await page.focus(selector);
            await new Promise(r => setTimeout(r, 100));
            await page.keyboard.down('Meta');
            await page.keyboard.press('KeyA');
            await page.keyboard.up('Meta');
            await page.keyboard.press('Backspace');
            await new Promise(r => setTimeout(r, 100));
            await page.type(selector, text, { delay: 15 });
        };

        console.log('Retyping email...');
        await clearAndType('input[name="email"]', 'prabhavitg@gmail.com');

        console.log('Retyping phone...');
        await clearAndType('input[name="phone"]', '351 610 7807');

        await new Promise(r => setTimeout(r, 1000));

        const vals = await page.evaluate(() => ({
            email: document.querySelector('input[name="email"]')?.value,
            phone: document.querySelector('input[name="phone"]')?.value,
            errors: Array.from(document.querySelectorAll('[class*="error"], [aria-invalid="true"]')).map(e => e.innerText.trim()).filter(Boolean)
        }));
        console.log('Resulting Values & Errors:', JSON.stringify(vals, null, 2));

        // Now click Submit
        const submitBtn = await page.$('button[data-ui="apply-button"]');
        if (submitBtn) {
            console.log('Clicking Submit button...');
            await page.evaluate(el => el.scrollIntoView(), submitBtn);
            await new Promise(r => setTimeout(r, 500));
            await submitBtn.click();
            console.log('Clicked!');
        }

        await new Promise(r => setTimeout(r, 10000));

        const postSubmit = await page.evaluate(() => ({
            url: window.location.href,
            bodySnippet: document.body.innerText.slice(0, 500)
        }));

        console.log('Post-submit URL:', postSubmit.url);
        console.log('Post-submit Snippet:\n', postSubmit.bodySnippet);

        await browser.disconnect();
    } catch (e) {
        console.error('Error:', e.message);
    }
})();
