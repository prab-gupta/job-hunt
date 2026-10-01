const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
    try {
        const devToolsInfo = fs.readFileSync("/Users/prab/Library/Application Support/Google/Chrome/DevToolsActivePort", "utf8").split("\n");
        const wsUrl = `ws://127.0.0.1:${devToolsInfo[0].trim()}${devToolsInfo[1].trim()}`;
        const browser = await puppeteer.connect({ browserWSEndpoint: wsUrl, defaultViewport: null });
        const pages = await browser.pages();
        
        for (let i = 0; i < pages.length; i++) {
            const url = pages[i].url();
            if (url.includes("fdepulse.com") || url.includes("linkedin") || url.includes("ycombinator")) {
                const title = await pages[i].title();
                const webdriver = await pages[i].evaluate(() => navigator.webdriver);
                console.log(`Tab: ${title.slice(0, 30)} | URL: ${url.slice(0, 45)} | navigator.webdriver: ${webdriver}`);
            }
        }
        await browser.disconnect();
    } catch (e) {
        console.error("Error:", e.message);
    }
})();
