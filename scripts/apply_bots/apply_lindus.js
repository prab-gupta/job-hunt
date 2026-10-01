const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

(async () => {
    try {
        const devToolsInfo = fs.readFileSync("/Users/prab/Library/Application Support/Google/Chrome/DevToolsActivePort", "utf8").split("\n");
        const wsUrl = `ws://127.0.0.1:${devToolsInfo[0].trim()}${devToolsInfo[1].trim()}`;
        const browser = await puppeteer.connect({ browserWSEndpoint: wsUrl, defaultViewport: null });
        const pages = await browser.pages();
        let page = pages.find(p => p.url().includes("ashbyhq.com/lindus"));
        
        if (!page) {
            console.error("Lindus application page not found");
            await browser.disconnect();
            return;
        }

        console.log("Found Lindus application tab. Filling fields...");

        // 1. Full name
        await page.type('input[name="_systemfield_name"]', 'Prabhavit Gupta', { delay: 30 });
        console.log("Filled Name");

        // 2. Email
        await page.type('input[name="_systemfield_email"]', 'prabhavitg@gmail.com', { delay: 30 });
        console.log("Filled Email");

        // 3. Resume Upload
        const cvPath = path.resolve("/Users/prab/Downloads/claud jobs/loop/CV_Lindus.pdf");
        const resumeInput = await page.$('input[id="_systemfield_resume"]');
        if (resumeInput) {
            await resumeInput.uploadFile(cvPath);
            console.log("Uploaded CV:", cvPath);
        } else {
            console.log("Resume input not found by id, searching generic file input...");
            const fileInputs = await page.$$('input[type="file"]');
            if (fileInputs.length > 0) {
                await fileInputs[fileInputs.length - 1].uploadFile(cvPath);
                console.log("Uploaded CV via file input");
            }
        }
        await new Promise(r => setTimeout(r, 2000));

        // 4. Visa sponsorship radio
        // Option 2: "Yes - but I would not require Lindus Health to help me in securing a visa or permit" (remote from Italy/EU LTR)
        const radioSelected = await page.evaluate(() => {
            const labels = Array.from(document.querySelectorAll('label'));
            const targetLabel = labels.find(l => l.innerText.includes('would not require Lindus Health to help me'));
            if (targetLabel) {
                targetLabel.click();
                return targetLabel.innerText;
            }
            // Fallback: radio with id ending in -2
            const r2 = document.querySelector('input[id*="labeled-radio-2"]');
            if (r2) { r2.click(); return 'radio-2 clicked'; }
            return 'not found';
        });
        console.log("Selected Visa Radio:", radioSelected);

        // 5. Notice period (text input)
        const noticeInput = await page.$('input[name="7bbd7244-bca4-411c-95a4-8f6846df8d3f"]');
        if (noticeInput) {
            await noticeInput.type("2 weeks notice (remote from Italy with EU Long Term Residence)", { delay: 20 });
            console.log("Filled Notice Period");
        }

        // 6. Holiday textarea
        const holidayTextarea = await page.$('textarea[name="38b9ee3d-e52a-4e37-a09c-f6daee4df82c"]');
        if (holidayTextarea) {
            await holidayTextarea.type("None booked; fully available for onboarding.", { delay: 20 });
            console.log("Filled Holiday textarea");
        }

        // 7. Adjustments textarea
        const adjustmentsTextarea = await page.$('textarea[name="5c111547-708a-45a5-93b4-4def8726d059"]');
        if (adjustmentsTextarea) {
            await adjustmentsTextarea.type("None needed, thank you.", { delay: 20 });
            console.log("Filled Adjustments textarea");
        }

        await new Promise(r => setTimeout(r, 2000));
        await page.screenshot({ path: "scratch/lindus_filled.png" });
        console.log("Saved screenshot to scratch/lindus_filled.png");

        await browser.disconnect();
    } catch (e) {
        console.error("Error:", e.message);
    }
})();
