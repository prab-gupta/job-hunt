const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
    try {
        const devToolsInfo = fs.readFileSync("/Users/prab/Library/Application Support/Google/Chrome/DevToolsActivePort", "utf8").split('\n');
        const wsUrl = `ws://127.0.0.1:${devToolsInfo[0]}${devToolsInfo[1]}`;
        const browser = await puppeteer.connect({ browserWSEndpoint: wsUrl });
        const page = await browser.newPage();
        await page.goto("https://fdepulse.com/jobs/marsh-full-stack-engineer-forward-deployed-digital-client-experience-marsh-0b9e4a/", { waitUntil: 'networkidle2' });
        const hrefs = await page.evaluate(() => Array.from(document.querySelectorAll('a')).map(a => a.href));
        fs.writeFileSync("marsh_links.txt", hrefs.join("\n"));
        await browser.disconnect();
    } catch(e) { console.error(e); }
})();
