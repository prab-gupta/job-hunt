const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
    try {
        const devToolsInfo = fs.readFileSync("/Users/prab/Library/Application Support/Google/Chrome/DevToolsActivePort", "utf8").split('\n');
        const port = devToolsInfo[0];
        const path = devToolsInfo[1];
        const wsUrl = `ws://127.0.0.1:${port}${path}`;
        console.log("Connecting to", wsUrl);

        const browser = await puppeteer.connect({
            browserWSEndpoint: wsUrl
        });
        const pages = await browser.pages();
        console.log("Connected! Pages:", pages.length);
        
        await browser.disconnect();
    } catch (e) {
        console.log("Error:", e.message);
    }
})();
