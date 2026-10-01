const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

(async () => {
    try {
        const devToolsInfo = fs.readFileSync('/Users/prab/Library/Application Support/Google/Chrome/DevToolsActivePort', 'utf8').split('\n');
        const port = devToolsInfo[0].trim();
        const browserPath = devToolsInfo[1].trim();
        const wsUrl = 'ws://127.0.0.1:' + port + browserPath;
        
        console.log('Connecting to Chrome via:', wsUrl);
        const browser = await puppeteer.connect({ browserWSEndpoint: wsUrl, defaultViewport: null });
        const pages = await browser.pages();
        let page = pages.find(p => p.url().includes('ashbyhq.com/lindus'));
        
        if (!page) {
            console.error('Lindus page not found in open tabs');
            await browser.disconnect();
            return;
        }

        console.log('Lindus tab found:', page.url());

        // Focus tab
        await page.bringToFront();

        // 1. Name
        const nameInput = await page.$('input[name="_systemfield_name"]');
        if (nameInput) {
            await nameInput.click({ clickCount: 3 });
            await nameInput.type('Prabhavit Gupta', { delay: 25 });
        }

        // 2. Email
        const emailInput = await page.$('input[name="_systemfield_email"]');
        if (emailInput) {
            await emailInput.click({ clickCount: 3 });
            await emailInput.type('prabhavitg@gmail.com', { delay: 25 });
        }

        // 3. Resume Upload (if not already uploaded)
        const cvPath = path.resolve('/Users/prab/Downloads/claud jobs/loop/CV_Lindus.pdf');
        const resumeInput = await page.$('input[id="_systemfield_resume"]');
        if (resumeInput) {
            await resumeInput.uploadFile(cvPath);
            console.log('Uploaded CV');
        }

        // 4. Visa Sponsorship Radio
        await page.evaluate(() => {
            const labels = Array.from(document.querySelectorAll('label'));
            const targetLabel = labels.find(l => l.innerText.includes('would not require Lindus Health to help me'));
            if (targetLabel) targetLabel.click();
        });

        // 5. Notice Period
        const noticeInput = await page.$('input[name="7bbd7244-bca4-411c-95a4-8f6846df8d3f"]');
        if (noticeInput) {
            await noticeInput.click({ clickCount: 3 });
            await noticeInput.type('2 weeks notice (remote from Italy with EU Long Term Residence)', { delay: 15 });
        }

        // 6. Holiday
        const holidayInput = await page.$('textarea[name="38b9ee3d-e52a-4e37-a09c-f6daee4df82c"]');
        if (holidayInput) {
            await holidayInput.click({ clickCount: 3 });
            await holidayInput.type('None booked; fully available for onboarding.', { delay: 15 });
        }

        // 7. Adjustments
        const adjInput = await page.$('textarea[name="5c111547-708a-45a5-93b4-4def8726d059"]');
        if (adjInput) {
            await adjInput.click({ clickCount: 3 });
            await adjInput.type('None needed, thank you.', { delay: 15 });
        }

        await new Promise(r => setTimeout(r, 1000));

        const state = await page.evaluate(() => ({
            name: document.querySelector('input[name="_systemfield_name"]')?.value,
            email: document.querySelector('input[name="_systemfield_email"]')?.value,
            resumeFiles: document.querySelector('input[id="_systemfield_resume"]')?.files?.length,
            notice: document.querySelector('input[name="7bbd7244-bca4-411c-95a4-8f6846df8d3f"]')?.value,
            holiday: document.querySelector('textarea[name="38b9ee3d-e52a-4e37-a09c-f6daee4df82c"]')?.value,
            adjustments: document.querySelector('textarea[name="5c111547-708a-45a5-93b4-4def8726d059"]')?.value
        }));

        console.log('Verified Form State:\n', JSON.stringify(state, null, 2));

        await browser.disconnect();
    } catch (e) {
        console.error('Error:', e.message);
    }
})();
