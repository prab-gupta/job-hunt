const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
    try {
        const devToolsInfo = fs.readFileSync("/Users/prab/Library/Application Support/Google/Chrome/DevToolsActivePort", "utf8").split('\n');
        const wsUrl = `ws://127.0.0.1:${devToolsInfo[0]}${devToolsInfo[1]}`;
        const browser = await puppeteer.connect({ browserWSEndpoint: wsUrl, defaultViewport: null });
        const page = await browser.newPage();
        
        await page.goto("https://www.indeed.com/viewjob?jk=57a989d5172b4fa5", { waitUntil: 'networkidle2' });
        await new Promise(r => setTimeout(r, 2000));
        
        await page.screenshot({ path: 'indeed.png' });
        const html = await page.content();
        fs.writeFileSync("indeed.html", html);
        
        await browser.disconnect();
    } catch(e) { console.error(e); }
})();
