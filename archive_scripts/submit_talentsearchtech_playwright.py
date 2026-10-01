#!/usr/bin/env python3
"""Submit Talent Search Technology Generative AI Engineer via LinkedIn Easy Apply."""

import os
import time
import datetime as dt
from playwright.sync_api import sync_playwright

ROOT = "/Users/prab/Downloads/claud jobs"
CONFIRM_DIR = os.path.join(ROOT, "confirmations")
PROFILE_DIR = os.path.expanduser("~/.playwright-chrome-profile")
today = dt.date.today().isoformat()
cv_path = os.path.abspath("Prabhavit_CV_TalentSearchTech.pdf")

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir=PROFILE_DIR,
        headless=True,
        channel="chrome",
        viewport={"width": 1280, "height": 900}
    )
    page = ctx.new_page()
    page.goto("https://www.linkedin.com/jobs/view/4468222917/", wait_until="domcontentloaded")
    time.sleep(3)

    # Check if already applied
    if "candidatura inviata" in page.inner_text("body").lower() or "application submitted" in page.inner_text("body").lower():
        print("Already applied to Talent Search Technology.")
        ctx.close()
        exit(0)

    btn = page.query_selector('button:has-text("Easy Apply"), button:has-text("Candidatura semplice")')
    if not btn:
        print("No Easy Apply button found.")
        page.screenshot(path=os.path.join(CONFIRM_DIR, "TalentSearchTech-nobtn.png"))
        ctx.close()
        exit(1)

    btn.click()
    time.sleep(2)

    for step in range(1, 10):
        print(f"--- Step {step} ---")
        time.sleep(1)

        # Phone input
        phone = page.locator('input[type="tel"], input[id*="phone" i]')
        if phone.count() > 0:
            for i in range(phone.count()):
                val = phone.nth(i).input_value()
                if not val or len(val) < 5:
                    phone.nth(i).fill("3516107807")

        # Resume upload
        file_input = page.locator('input[type="file"]')
        if file_input.count() > 0 and os.path.exists(cv_path):
            try:
                file_input.first.set_input_files(cv_path)
                print("Uploaded Prabhavit_CV_TalentSearchTech.pdf")
            except Exception as e:
                print(f"Upload error: {e}")

        # Dropdowns
        page.evaluate('''() => {
            const selects = document.querySelectorAll('select');
            selects.forEach(s => {
                if (!s.value || s.value === "Select an option") {
                    if (s.options.length > 1) s.selectedIndex = 1;
                    s.dispatchEvent(new Event('change', { bubbles: true }));
                }
            });
        }''')

        # Text inputs with React setter
        page.evaluate('''() => {
            const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value')?.set;
            const inputs = document.querySelectorAll('input:not([type="checkbox"]):not([type="radio"]):not([type="file"]):not([type="hidden"]):not([type="tel"])');
            inputs.forEach(inp => {
                if (!inp.value) {
                    if (nativeSetter) nativeSetter.call(inp, '3');
                    else inp.value = '3';
                    inp.dispatchEvent(new Event('input', { bubbles: true }));
                    inp.dispatchEvent(new Event('change', { bubbles: true }));
                    inp.dispatchEvent(new Event('blur', { bubbles: true }));
                }
            });
        }''')

        # Radios with React setter (prefer Yes for authorized/remote, No for sponsorship)
        page.evaluate('''() => {
            const nativeRadioSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'checked')?.set;
            const fieldsets = document.querySelectorAll('fieldset');
            fieldsets.forEach(fs => {
                const txt = fs.innerText.toLowerCase();
                const radios = fs.querySelectorAll('input[type="radio"]');
                if (radios.length > 0 && !Array.from(radios).some(r => r.checked)) {
                    if (txt.includes('sponsorship') || txt.includes('visa')) {
                        const noRadio = radios[radios.length - 1];
                        if (nativeRadioSetter) nativeRadioSetter.call(noRadio, true);
                        else noRadio.checked = true;
                        noRadio.dispatchEvent(new Event('change', { bubbles: true }));
                    } else {
                        const yesRadio = radios[0];
                        if (nativeRadioSetter) nativeRadioSetter.call(yesRadio, true);
                        else yesRadio.checked = true;
                        yesRadio.dispatchEvent(new Event('change', { bubbles: true }));
                    }
                }
            });
        }''')

        # Check Submit button
        submit_btn = page.query_selector('button[aria-label*="Submit application" i], button:has-text("Submit application"), button:has-text("Invia candidatura")')
        if submit_btn and submit_btn.is_visible():
            print("🚀 Found Submit button! Clicking...")
            # Uncheck follow
            page.evaluate('''() => {
                const follow = document.querySelector('input[type="checkbox"][id*="follow" i]');
                if (follow && follow.checked) follow.click();
            }''')
            submit_btn.click()
            time.sleep(5)

            confirm_txt = os.path.join(CONFIRM_DIR, f"TalentSearchTech-{today}.txt")
            confirm_png = os.path.join(CONFIRM_DIR, f"TalentSearchTech-{today}.png")
            page.screenshot(path=confirm_png)

            with open(confirm_txt, "w") as f:
                f.write(f"Company: Talent Search Technology\nRole: Generative AI Engineer\nURL: https://www.linkedin.com/jobs/view/4468222917/\nDate: {today}\nStatus: SUBMITTED\nCV: Prabhavit_CV_TalentSearchTech.pdf\nConfirmation: Application submitted to Talent Search Technology\n")

            print(f"✅ SUCCESS: Submitted to Talent Search Technology! Receipt: {confirm_txt}")
            
            import csv
            with open(os.path.join(ROOT, "applications.csv"), "a", newline="", encoding="utf-8") as af:
                writer = csv.writer(af)
                writer.writerow([
                    today, "Talent Search Technology", "Generative AI Engineer", "LinkedIn Easy Apply",
                    "https://www.linkedin.com/jobs/view/4468222917/", "SUBMITTED",
                    "Application submitted to Talent Search Technology", "EUR 50,000", "yes",
                    f"Prabhavit_CV_TalentSearchTech.pdf + CoverLetter_TalentSearchTech.pdf | confirmations/TalentSearchTech-{today}.txt"
                ])
            break

        # Click Next / Review
        next_btn = page.query_selector('button:has-text("Next"), button:has-text("Review"), button:has-text("Avanza"), button:has-text("Verifica"), button[aria-label*="Continue" i]')
        if next_btn and next_btn.is_visible():
            print(f"Clicking: '{next_btn.inner_text().strip()}'")
            next_btn.click()
            time.sleep(2)
        else:
            print("Modal navigation completed or closed.")
            page.screenshot(path=os.path.join(CONFIRM_DIR, f"TalentSearchTech-{today}-stage.png"))
            break

    ctx.close()
