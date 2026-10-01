const puppeteer = require('puppeteer-core');

(async () => {
    try {
        const browser = await puppeteer.connect({
            browserURL: 'http://localhost:9222'
        });
        const pages = await browser.pages();
        console.log("Connected! Pages:", pages.length);
        await browser.disconnect();
    } catch (e) {
        console.log("Error:", e.message);
    }
})();
