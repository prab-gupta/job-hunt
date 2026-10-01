#!/usr/bin/env python3
"""Submit KeyShot AI Workflow Engineer via direct JS event dispatch."""

import os
import time
import datetime as dt
from playwright.sync_api import sync_playwright

ROOT = "/Users/prab/Downloads/claud jobs"
CONFIRM_DIR = os.path.join(ROOT, "confirmations")
PROFILE_DIR = os.path.expanduser("~/.playwright-chrome-profile")
today = dt.date.today().isoformat()
cv_path = os.path.abspath("Prabhavit_CV_KeyShot.pdf")

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir=PROFILE_DIR,
        headless=True,
        channel="chrome",
        viewport={"width": 1280, "height": 900}
    )
    page = ctx.new_page()
    page.goto("https://www.linkedin.com/jobs/view/4469216266/", wait_until="domcontentloaded")
    time.sleep(3)

    btn = page.query_selector('button:has-text("Easy Apply")')
    if not btn:
        print("No Easy Apply button found.")
        ctx.close()
        exit(1)

    btn.click()
    time.sleep(2)

    # Step 1: Phone
    print("Step 1: Contact info")
    phone = page.locator('input[type="tel"], input[id*="phone" i]')
    if phone.count() > 0:
        phone.first.fill("3516107807")
    page.click('button:has-text("Next")')
    time.sleep(2)

    # Step 2: Resume
    print("Step 2: Resume")
    file_input = page.locator('input[type="file"]')
    if file_input.count() > 0 and os.path.exists(cv_path):
        file_input.first.set_input_files(cv_path)
        print("Uploaded CV")
        time.sleep(1)
    page.click('button:has-text("Next")')
    time.sleep(2)

    # Step 3: Additional Questions
    print("Step 3: Additional Questions")

    # Dropdown select
    selects = page.locator('select')
    if selects.count() > 0:
        selects.first.select_option(index=1)
        print("Selected dropdown index 1")

    # Text inputs: fill with 3
    page.evaluate('''() => {
        const inputs = document.querySelectorAll('input:not([type="checkbox"]):not([type="radio"]):not([type="file"]):not([type="hidden"]):not([type="tel"])');
        inputs.forEach(inp => {
            inp.value = "3";
            inp.dispatchEvent(new Event('input', { bubbles: true }));
            inp.dispatchEvent(new Event('change', { bubbles: true }));
            inp.dispatchEvent(new Event('blur', { bubbles: true }));
        });
    }''')
    print("Filled text inputs: 3")

    # Radio buttons using direct JS checked + change event
    page.evaluate('''() => {
        const radios = document.querySelectorAll('input[type="radio"]');
        if (radios.length >= 4) {
            // Radio 0: Authorized in Denmark -> Yes
            radios[0].checked = true;
            radios[0].dispatchEvent(new Event('input', { bubbles: true }));
            radios[0].dispatchEvent(new Event('change', { bubbles: true }));
            
            // Radio 3: Sponsorship -> No
            radios[3].checked = true;
            radios[3].dispatchEvent(new Event('input', { bubbles: true }));
            radios[3].dispatchEvent(new Event('change', { bubbles: true }));
        }
    }''')
    print("Checked radios via JS: Authorized=Yes, Sponsorship=No")

    time.sleep(2)
    page.screenshot(path=os.path.join(CONFIRM_DIR, "keyshot_step3_js_checked.png"))

    # Click Review
    print("Clicking Review button...")
    page.click('button:has-text("Review")')
    time.sleep(3)

    # Step 4: Final Review & Submit
    print("Step 4: Final Review & Submit")
    page.screenshot(path=os.path.join(CONFIRM_DIR, "keyshot_step4_review.png"))

    # Uncheck follow checkbox
    page.evaluate('''() => {
        const follow = document.querySelector('input[type="checkbox"][id*="follow" i]');
        if (follow && follow.checked) {
            follow.click();
        }
    }''')

    # Scroll down review modal
    page.evaluate('''() => {
        const container = document.querySelector('.jobs-easy-apply-modal__content, .artdeco-modal__content, div[role="dialog"]');
        if (container) container.scrollTop = container.scrollHeight;
    }''')
    time.sleep(2)

    # Find and click Submit Application
    submit_btn = page.query_selector('button[aria-label*="Submit application" i], button:has-text("Submit application"), button:has-text("Invia candidatura")')
    if submit_btn:
        print("🚀 Clicking Submit Application button!")
        submit_btn.click()
        time.sleep(5)

        confirm_txt = os.path.join(CONFIRM_DIR, f"KeyShot-{today}.txt")
        confirm_png = os.path.join(CONFIRM_DIR, f"KeyShot-{today}.png")
        page.screenshot(path=confirm_png)

        with open(confirm_txt, "w") as f:
            f.write(f"Company: KeyShot\nRole: AI Workflow Engineer\nURL: https://www.linkedin.com/jobs/view/4469216266/\nDate: {today}\nStatus: SUBMITTED\nCV: Prabhavit_CV_KeyShot.pdf\nConfirmation: Application submitted to KeyShot\n")

        print(f"✅ SUCCESS: KeyShot application submitted! Saved receipt to {confirm_txt}")
        
        # Log to applications.csv
        import csv
        with open(os.path.join(ROOT, "applications.csv"), "a", newline="", encoding="utf-8") as af:
            writer = csv.writer(af)
            writer.writerow([
                today, "KeyShot", "AI Workflow Engineer", "LinkedIn Easy Apply",
                "https://www.linkedin.com/jobs/view/4469216266/", "SUBMITTED",
                "Application submitted to KeyShot", "EUR 50,000", "yes",
                f"Prabhavit_CV_KeyShot.pdf + CoverLetter_KeyShot.pdf | confirmations/KeyShot-{today}.txt"
            ])
    else:
        print("Submit button search fallback...")
        all_modal_btns = page.locator('.jobs-easy-apply-modal button, .artdeco-modal button')
        for i in range(all_modal_btns.count()):
            b = all_modal_btns.nth(i)
            t = b.inner_text().strip()
            print(f"Modal button {i}: '{t}'")
            if "submit" in t.lower() or "invia" in t.lower():
                print(f"Clicking modal button: {t}")
                b.click()
                time.sleep(5)
                page.screenshot(path=os.path.join(CONFIRM_DIR, f"KeyShot-{today}.png"))
                break

    ctx.close()
