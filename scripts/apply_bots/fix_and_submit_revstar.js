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

        // Properly clear and set email & phone
        await page.evaluate(() => {
            const setInput = (selector, val) => {
                const el = document.querySelector(selector);
                if (!el) return;
                const proto = window.HTMLInputElement.prototype;
                const setter = Object.getOwnPropertyDescriptor(proto, 'value').set;
                setter.call(el, val);
                el.dispatchEvent(new Event('input', { bubbles: true }));
                el.dispatchEvent(new Event('change', { bubbles: true }));
                el.dispatchEvent(new Event('blur', { bubbles: true }));
            };

            setInput('input[name="email"]', 'prabhavitg@gmail.com');
            setInput('input[name="phone"]', '3516107807');
        });

        await new Promise(r => setTimeout(r, 1000));

        const vals = await page.evaluate(() => ({
            email: document.querySelector('input[name="email"]')?.value,
            phone: document.querySelector('input[name="phone"]')?.value,
            errors: Array.from(document.querySelectorAll('[class*="error"], [aria-invalid="true"]')).map(e => e.innerText.trim()).filter(Boolean)
        }));
        console.log('Cleaned Values:', JSON.stringify(vals, null, 2));

        // Click Submit
        const submitBtn = await page.$('button[data-ui="apply-button"]');
        if (submitBtn) {
            console.log('Clicking Submit button...');
            await page.evaluate(el => el.scrollIntoView(), submitBtn);
            await new Promise(r => setTimeout(r, 500));
            await submitBtn.click();
            console.log('Clicked Submit Application!');
        }

        // Wait 10 seconds for completion
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
