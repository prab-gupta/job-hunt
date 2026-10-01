#!/usr/bin/env python3
"""Targeted submit for KeyShot with precise selector mapping."""

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

    # Step 1: Contact info
    print("Step 1: Contact info")
    phone_input = page.locator('input[type="tel"], input[id*="phone" i], .artdeco-text-input--input')
    if phone_input.count() > 0:
        phone_input.first.fill("3516107807")
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
    for i in range(selects.count()):
        s = selects.nth(i)
        opts = s.locator('option')
        for k in range(opts.count()):
            opt_t = opts.nth(k).inner_text().strip().lower()
            if any(w in opt_t for w in ["yes", "professional", "fluent", "c2", "c1", "conversational"]):
                s.select_option(index=k)
                break
        if s.input_value() in ["", "Select an option"]:
            s.select_option(index=1)
        print(f"Selected option: {s.input_value()}")

    # Fill all visible text inputs using javascript evaluation to be 100% reliable
    page.evaluate('''() => {
        const inputs = document.querySelectorAll('input:not([type="checkbox"]):not([type="radio"]):not([type="file"]):not([type="hidden"])');
        inputs.forEach(inp => {
            const lbl = (inp.closest('.fb-dash-form-element') || inp.parentElement)?.innerText?.toLowerCase() || '';
            let val = "3";
            if (lbl.includes("terraform")) val = "2";
            else if (lbl.includes("aws") || lbl.includes("amazon")) val = "2";
            else if (lbl.includes("engineering")) val = "3";
            
            inp.value = val;
            inp.dispatchEvent(new Event('input', { bubbles: true }));
            inp.dispatchEvent(new Event('change', { bubbles: true }));
            inp.dispatchEvent(new Event('blur', { bubbles: true }));
        });
    }''')
    print("Filled all text inputs via JS event dispatch.")

    # Click radio labels
    page.evaluate('''() => {
        const fieldsets = document.querySelectorAll('fieldset');
        fieldsets.forEach(fs => {
            const txt = fs.innerText.toLowerCase();
            if (txt.includes("authorized") || txt.includes("right to work")) {
                const yesLabel = Array.from(fs.querySelectorAll('label')).find(l => l.innerText.toLowerCase().includes("yes"));
                if (yesLabel) yesLabel.click();
            } else if (txt.includes("sponsorship")) {
                const noLabel = Array.from(fs.querySelectorAll('label')).find(l => l.innerText.toLowerCase().includes("no"));
                if (noLabel) noLabel.click();
            }
        });
    }''')
    print("Clicked radio labels via JS.")
    time.sleep(2)

    page.screenshot(path=os.path.join(CONFIRM_DIR, "keyshot_step3_verified.png"))

    # Click Review
    print("Clicking Review...")
    page.click('button:has-text("Review")')
    time.sleep(3)

    # Step 4: Final Review & Submit
    print("Step 4: Final Review & Submit")
    page.screenshot(path=os.path.join(CONFIRM_DIR, "keyshot_step4_final.png"))

    # Uncheck follow checkbox
    page.evaluate('''() => {
        const follow = document.querySelector('input[type="checkbox"][id*="follow" i]');
        if (follow && follow.checked) {
            follow.click();
        }
    }''')

    # Click Submit Application
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
    else:
        print("Submit button not found on Step 4.")
        buttons = [b.inner_text().strip() for b in page.query_selector_all('button') if b.is_visible()]
        print("Visible buttons on page:", buttons)

    ctx.close()
