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

        console.log('Revstar tab found:', page.url());
        await page.bringToFront();

        // Helper to type into input
        const typeInput = async (selector, text) => {
            const el = await page.$(selector);
            if (el) {
                await el.click({ clickCount: 3 });
                await el.type(text, { delay: 15 });
            }
        };

        // 1. First name & Last name
        await typeInput('input[name="firstname"]', 'Prabhavit');
        await typeInput('input[name="lastname"]', 'Gupta');
        await typeInput('input[name="email"]', 'prabhavitg@gmail.com');
        await typeInput('input[name="headline"]', 'Forward Deployed Engineer & Cloud Solutions Architect');
        await typeInput('input[name="phone"]', '+39 351 610 7807');
        await typeInput('input[name="city"]', 'Venice');
        await typeInput('input[name="country"]', 'Italy');
        console.log('Filled Personal Information');

        // 2. Upload Resume
        const cvPath = path.resolve('/Users/prab/Downloads/claud jobs/loop/CV_Revstar.pdf');
        const fileInputs = await page.$$('input[type="file"]');
        if (fileInputs.length > 0) {
            await fileInputs[0].uploadFile(cvPath);
            console.log('Uploaded CV to file input 0');
        }

        // 3. Upload or paste Cover Letter
        const clPath = path.resolve('/Users/prab/Downloads/claud jobs/loop/CL_Revstar.pdf');
        if (fileInputs.length > 1) {
            await fileInputs[1].uploadFile(clPath);
            console.log('Uploaded CL to file input 1');
        }

        // 4. Screening Questions (Fieldsets)
        // Helper to select YES or NO
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

        // Q1: 6+ yrs experience (honest assessment: 3+ yrs -> NO)
        await selectRadio('QA_12508780', 'NO');
        // Q2: 3+ yrs client-facing FDE -> YES
        await selectRadio('QA_12508781', 'YES');
        // Q3: Deep AWS Core Expertise -> YES
        await selectRadio('QA_12508782', 'YES');
        // Q4: IaC & CI/CD -> YES
        await selectRadio('QA_12508783', 'YES');
        // Q5: AWS GenAI & Data Services -> YES
        await selectRadio('QA_12508784', 'YES');
        // Q6: AWS Professional Certifications required (he has Microsoft/Tray.AI, not AWS Pro -> NO)
        await selectRadio('QA_12508785', 'NO');
        // Q7: Enterprise Track Record -> YES
        await selectRadio('QA_12508786', 'YES');
        // Q8: Consulting & Communication -> YES
        await selectRadio('QA_12508787', 'YES');
        // Q9: Growth Mindset -> YES
        await selectRadio('QA_12508788', 'YES');
        // Q10: Visa sponsorship for US employment -> YES (EU LTR permit requires US visa)
        await selectRadio('QA_12508789', 'YES');

        // Q11: Expected Compensation (text input)
        await typeInput('input[name="QA_12508790"]', '$40,000 (Open to contract / remote in Europe)');
        console.log('Filled Screening Questions');

        await new Promise(r => setTimeout(r, 2000));

        const state = await page.evaluate(() => {
            return {
                firstname: document.querySelector('input[name="firstname"]')?.value,
                lastname: document.querySelector('input[name="lastname"]')?.value,
                email: document.querySelector('input[name="email"]')?.value,
                phone: document.querySelector('input[name="phone"]')?.value,
                city: document.querySelector('input[name="city"]')?.value,
                country: document.querySelector('input[name="country"]')?.value,
                compensation: document.querySelector('input[name="QA_12508790"]')?.value,
                radiosChecked: Array.from(document.querySelectorAll('input[type="radio"]:checked')).map(r => ({ name: r.name, id: r.id }))
            };
        });

        console.log('Revstar Filled State:\n', JSON.stringify(state, null, 2));

        await browser.disconnect();
    } catch (e) {
        console.error('Error:', e.message);
    }
})();
