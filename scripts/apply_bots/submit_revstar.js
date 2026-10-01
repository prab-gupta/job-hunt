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
        let page = pages.find(p => p.url().includes('revstar'));
        
        if (!page) {
            console.error('Revstar tab not found');
            await browser.disconnect();
            return;
        }

        console.log('Revstar tab found. Bringing to front...');
        await page.bringToFront();

        const btn = await page.$('button[data-ui="apply-button"]');
        if (btn) {
            console.log('Found button[data-ui="apply-button"]. Scrolling and clicking...');
            await page.evaluate(el => el.scrollIntoView(), btn);
            await new Promise(r => setTimeout(r, 600));
            await btn.click();
            console.log('Clicked via Puppeteer mouse click.');
        } else {
            console.log('Button not found');
        }

        // Wait 10 seconds
        await new Promise(r => setTimeout(r, 10000));

        console.log('URL after click:', page.url());
        const bodySnippet = await page.evaluate(() => document.body.innerText.slice(0, 600));
        console.log('Body snippet:\n', bodySnippet);

        await browser.disconnect();
    } catch (e) {
        console.error('Error:', e.message);
    }
})();
