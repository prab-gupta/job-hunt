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
        let page = pages.find(p => p.url().includes('ashbyhq.com/lindus'));
        
        if (!page) {
            console.error('Lindus page not found');
            await browser.disconnect();
            return;
        }

        console.log('Submitting Lindus application...');
        await page.bringToFront();

        const clicked = await page.evaluate(() => {
            const btns = Array.from(document.querySelectorAll('button'));
            const target = btns.find(b => b.innerText.includes('Submit Application'));
            if (target) {
                target.scrollIntoView();
                target.click();
                return 'Clicked Submit Application';
            }
            return 'Submit button not found';
        });

        console.log('Submit Action:', clicked);

        // Wait 6 seconds
        await new Promise(r => setTimeout(r, 6000));

        const postSubmitState = await page.evaluate(() => {
            return {
                url: window.location.href,
                bodySnippet: document.body.innerText.slice(0, 500)
            };
        });

        console.log('Post-submit URL:', postSubmitState.url);
        console.log('Post-submit Text:\n', postSubmitState.bodySnippet);

        await browser.disconnect();
    } catch (e) {
        console.error('Error:', e.message);
    }
})();
