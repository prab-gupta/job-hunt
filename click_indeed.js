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
        
        console.log("Clicking Apply Now");
        
        // Sometimes "Apply now" opens a new tab. We need to catch it.
        const newPagePromise = new Promise(x => browser.once('targetcreated', target => x(target.page())));
        
        const clicked = await page.evaluate(() => {
            const btn = Array.from(document.querySelectorAll('button, a')).find(el => el.innerText && el.innerText.includes('Apply now'));
            if (btn) {
                btn.click();
                return true;
            }
            return false;
        });
        
        console.log("Clicked:", clicked);
        
        if (clicked) {
            await new Promise(r => setTimeout(r, 3000));
            // Try to find if a new page opened or if URL changed
            console.log("Current URL after click:", page.url());
            
            // Wait for new page just in case
            try {
                const newPage = await Promise.race([newPagePromise, new Promise((_, rej) => setTimeout(rej, 3000))]);
                if (newPage) {
                    await newPage.waitForNavigation({ waitUntil: 'networkidle2' }).catch(() => {});
                    console.log("New page opened! URL:", newPage.url());
                    fs.writeFileSync("id_me_ats.txt", newPage.url());
                }
            } catch (e) {
                console.log("No new page detected");
            }
        }
        await browser.disconnect();
    } catch(e) { console.error(e); }
})();
