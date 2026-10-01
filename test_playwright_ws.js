const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
    try {
        const devToolsInfo = fs.readFileSync("/Users/prab/Library/Application Support/Google/Chrome/DevToolsActivePort", "utf8").split('\n');
        const port = devToolsInfo[0];
        const path = devToolsInfo[1];
        const wsUrl = `ws://127.0.0.1:${port}${path}`;
        console.log("Connecting to", wsUrl);

        const browser = await chromium.connect(wsUrl);
        const contexts = browser.contexts();
        console.log("Contexts:", contexts.length);
        const pages = contexts.length > 0 ? contexts[0].pages() : await browser.pages();
        console.log("Pages:", pages.length);
        await browser.close();
    } catch (e) {
        console.log("Error:", e.message);
    }
})();
