const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
    try {
        const devToolsInfo = fs.readFileSync("/Users/prab/Library/Application Support/Google/Chrome/DevToolsActivePort", "utf8").split('\n');
        const wsUrl = `ws://127.0.0.1:${devToolsInfo[0]}${devToolsInfo[1]}`;
        const browser = await puppeteer.connect({ browserWSEndpoint: wsUrl, defaultViewport: null });
        const page = await browser.newPage();
        
        const urls = [
            "https://www.indeed.com/viewjob?jk=57a989d5172b4fa5",
            "https://www.indeed.com/viewjob?jk=2a71d98634bc2bfa"
        ];
        
        for (let url of urls) {
            console.log("Navigating to", url);
            await page.goto(url, { waitUntil: 'networkidle2' });
            await new Promise(r => setTimeout(r, 3000));
            
            const btnLink = await page.evaluate(() => {
                const applyBtn = document.querySelector('#applyButtonLinkContainer a, a[aria-label*="Apply on company site"], button[aria-label*="Apply"]');
                return applyBtn ? applyBtn.href || 'button' : 'Not found';
            });
            console.log("Apply URL for", url, "is", btnLink);
            
            if (btnLink && btnLink !== 'button' && btnLink !== 'Not found') {
                await page.goto(btnLink, { waitUntil: 'networkidle2' });
                await new Promise(r => setTimeout(r, 3000));
                console.log("Final ATS URL:", page.url());
            } else {
                console.log("Button or not found:", btnLink);
            }
        }
        await browser.disconnect();
    } catch(e) { console.error(e); }
})();
