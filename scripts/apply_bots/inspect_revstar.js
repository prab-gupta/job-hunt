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

        const questions = await page.evaluate(() => {
            const fieldsets = Array.from(document.querySelectorAll('fieldset, [data-ui*="question"], [data-ui="application-form"] > div'));
            return fieldsets.map(f => f.innerText.trim().replace(/\n+/g, ' ')).filter(t => t.length > 5 && t.length < 500);
        });

        console.log('RevStar Form Elements:');
        questions.forEach((q, i) => console.log(`${i+1}. ${q}`));

        await browser.disconnect();
    } catch (e) {
        console.error('Error:', e.message);
    }
})();
