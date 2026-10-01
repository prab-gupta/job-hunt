const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

(async () => {
    try {
        const devToolsInfo = fs.readFileSync('/Users/prab/Library/Application Support/Google/Chrome/DevToolsActivePort', 'utf8').split('\n');
        const port = devToolsInfo[0].trim();
        const browserPath = devToolsInfo[1].trim();
        const wsUrl = 'ws://127.0.0.1:' + port + browserPath;
        
        const browser = await puppeteer.connect({ browserWSEndpoint: wsUrl, defaultViewport: null });
        const pages = await browser.pages();
        let page = pages.find(p => p.url().includes('revstarcareers.com') || p.url().includes('workable.com/revstar'));
        
        if (!page) {
            console.error('Revstar tab not found');
            await browser.disconnect();
            return;
        }

        console.log('Revstar tab found. Bringing to front...');
        await page.bringToFront();

        const typeInput = async (selector, text) => {
            const el = await page.$(selector);
            if (el) {
                await el.click({ clickCount: 3 });
                await el.type(text, { delay: 10 });
            }
        };

        // 1. Personal Info
        await typeInput('input[name="firstname"]', 'Prabhavit');
        await typeInput('input[name="lastname"]', 'Gupta');
        await typeInput('input[name="email"]', 'prabhavitg@gmail.com');
        await typeInput('input[name="headline"]', 'Forward Deployed Engineer & Cloud Solutions Architect');
        await typeInput('input[name="phone"]', '+39 351 610 7807');
        console.log('Filled Personal Info');

        // 2. File Uploads
        const photoPath = path.resolve('/Users/prab/Downloads/claud jobs/cv/photo.jpg');
        const cvPath = path.resolve('/Users/prab/Downloads/claud jobs/loop/CV_Revstar.pdf');
        const fileInputs = await page.$$('input[type="file"]');
        
        if (fileInputs.length >= 2) {
            await fileInputs[0].uploadFile(photoPath);
            console.log('Uploaded Headshot Photo to input 0');
            await fileInputs[1].uploadFile(cvPath);
            console.log('Uploaded Bespoke CV to input 1');
        } else if (fileInputs.length === 1) {
            await fileInputs[0].uploadFile(cvPath);
            console.log('Uploaded CV');
        }

        // 3. Cover letter textarea
        const clText = fs.readFileSync('/Users/prab/Downloads/claud jobs/scratch/cl_revstar_text.txt', 'utf8');
        const clTextarea = await page.$('textarea[name="cover_letter"]');
        if (clTextarea) {
            await clTextarea.click({ clickCount: 3 });
            await page.evaluate((el, text) => {
                el.value = text;
                el.dispatchEvent(new Event('input', { bubbles: true }));
                el.dispatchEvent(new Event('change', { bubbles: true }));
            }, clTextarea, clText);
            console.log('Populated Cover Letter textarea');
        }

        // 4. Screening Questions
        const selectRadio = async (dataUi, choice) => {
            await page.evaluate((ui, ch) => {
                const fs = document.querySelector(`fieldset[data-ui="${ui}"]`);
                if (fs) {
                    const labels = Array.from(fs.querySelectorAll('label'));
                    const target = labels.find(l => l.innerText.trim().toUpperCase() === ch.toUpperCase());
                    if (target) target.click();
                }
            }, dataUi, choice);
        };

        await selectRadio('QA_12508780', 'NO');
        await selectRadio('QA_12508781', 'YES');
        await selectRadio('QA_12508782', 'YES');
        await selectRadio('QA_12508783', 'YES');
        await selectRadio('QA_12508784', 'YES');
        await selectRadio('QA_12508785', 'NO');
        await selectRadio('QA_12508786', 'YES');
        await selectRadio('QA_12508787', 'YES');
        await selectRadio('QA_12508788', 'YES');
        await selectRadio('QA_12508789', 'YES');

        // Compensation
        await typeInput('input[name="QA_12508790"]', '40000');
        console.log('Completed Screening Questions & Compensation');

        await new Promise(r => setTimeout(r, 2000));

        // 5. Click Submit Application button
        const submitBtn = await page.$('button[data-ui="apply-button"]');
        if (submitBtn) {
            console.log('Scrolling to submit button and clicking...');
            await page.evaluate(el => el.scrollIntoView(), submitBtn);
            await new Promise(r => setTimeout(r, 500));
            await submitBtn.click();
            console.log('Clicked Submit Application button!');
        }

        // Wait 10 seconds for completion
        await new Promise(r => setTimeout(r, 10000));

        const resultState = await page.evaluate(() => {
            return {
                url: window.location.href,
                bodyText: document.body.innerText.slice(0, 500)
            };
        });

        console.log('Result URL:', resultState.url);
        console.log('Result Body:\n', resultState.bodyText);

        await browser.disconnect();
    } catch (e) {
        console.error('Error:', e.message);
    }
})();
