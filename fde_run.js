const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
    try {
        const devToolsInfo = fs.readFileSync("/Users/prab/Library/Application Support/Google/Chrome/DevToolsActivePort", "utf8").split('\n');
        const port = devToolsInfo[0];
        const path = devToolsInfo[1];
        const wsUrl = `ws://127.0.0.1:${port}${path}`;
        
        const browser = await puppeteer.connect({ browserWSEndpoint: wsUrl, defaultViewport: null });
        const page = await browser.newPage();
        
        console.log("Navigating to Id.Me job...");
        await page.goto("https://fdepulse.com/jobs/id-me-manager-forward-deployed-engineering-57ba42/", { waitUntil: 'networkidle2' });
        
        const html = await page.content();
        fs.writeFileSync("id_me.html", html);
        
        // Find apply button or links
        const hrefs = await page.evaluate(() => {
            return Array.from(document.querySelectorAll('a')).map(a => a.href);
        });
        fs.writeFileSync("id_me_links.txt", hrefs.join("\n"));
        
        console.log("Done Id.Me");
        await browser.disconnect();
    } catch(e) {
        console.error(e);
    }
})();
