const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
    try {
        const devToolsInfo = fs.readFileSync("/Users/prab/Library/Application Support/Google/Chrome/DevToolsActivePort", "utf8").split("\n");
        const wsUrl = `ws://127.0.0.1:${devToolsInfo[0].trim()}${devToolsInfo[1].trim()}`;
        const browser = await puppeteer.connect({ browserWSEndpoint: wsUrl, defaultViewport: null });
        
        // Find existing idle tab or open new tab
        const pages = await browser.pages();
        // Check if there is an empty/inspect tab or create one
        let targetPage = null;
        for (let p of pages) {
            const url = p.url();
            if (url === 'about:blank' || url.includes('chrome://inspect')) {
                targetPage = p;
                break;
            }
        }
        if (!targetPage) {
            targetPage = await browser.newPage();
        }

        console.log("Navigating to Indeed job...");
        await targetPage.goto("https://www.indeed.com/viewjob?jk=419115b4b37379d9", { waitUntil: 'domcontentloaded', timeout: 20000 });
        
        await new Promise(r => setTimeout(r, 4000));
        
        const title = await targetPage.title();
        const currentUrl = targetPage.url();
        console.log("Page Title:", title);
        console.log("Current URL:", currentUrl);

        // Check for apply buttons / links
        const applyInfo = await targetPage.evaluate(() => {
            const btns = Array.from(document.querySelectorAll('button, a'));
            const matches = btns.filter(b => {
                const text = (b.innerText || b.textContent || b.getAttribute('aria-label') || '').toLowerCase();
                return text.includes('apply');
            }).map(b => ({
                text: (b.innerText || b.getAttribute('aria-label') || '').trim().replace(/\n+/g, ' '),
                tag: b.tagName,
                href: b.href || null,
                id: b.id || null
            }));
            return {
                buttons: matches,
                bodyText: document.body.innerText.slice(0, 500)
            };
        });

        console.log("Apply Elements Found:", JSON.stringify(applyInfo.buttons, null, 2));
        console.log("Body snippet:", applyInfo.bodyText.slice(0, 200));

        await browser.disconnect();
    } catch (e) {
        console.error("Error:", e.message);
    }
})();
