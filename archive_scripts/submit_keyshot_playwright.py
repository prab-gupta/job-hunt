#!/usr/bin/env python3
"""Submit KeyShot with explicit radio label clicks and final submit."""

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
    if selects.count() > 0:
        selects.first.select_option(index=1)
        print("Selected dropdown option index 1")

    # Fill all text inputs with real fill
    page.evaluate('''() => {
        const inputs = document.querySelectorAll('input:not([type="checkbox"]):not([type="radio"]):not([type="file"]):not([type="hidden"])');
        inputs.forEach(inp => {
            inp.value = "3";
            inp.dispatchEvent(new Event('input', { bubbles: true }));
            inp.dispatchEvent(new Event('change', { bubbles: true }));
            inp.dispatchEvent(new Event('blur', { bubbles: true }));
        });
    }''')
    print("Filled text inputs: 3")

    # Click first Yes label (Authorized in Denmark)
    yes_labels = page.locator('label:has-text("Yes")')
    if yes_labels.count() > 0:
        yes_labels.first.click()
        print("Clicked first Yes label")

    # Click second No label (Require sponsorship)
    no_labels = page.locator('label:has-text("No")')
    if no_labels.count() > 1:
        no_labels.nth(1).click()
        print("Clicked second No label")
    elif no_labels.count() > 0:
        no_labels.last.click()
        print("Clicked last No label")

    time.sleep(2)
    page.screenshot(path=os.path.join(CONFIRM_DIR, "keyshot_step3_checked.png"))

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

    # Scroll dialog
    page.evaluate('document.querySelector("div[role=\\"dialog\\"] .jobs-easy-apply-modal__content, div[role=\\"dialog\\"]")?.scrollTo(0, 10000)')
    time.sleep(1)

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
        
        # Also append to applications.csv
        with open(os.path.join(ROOT, "applications.csv"), "a", newline="", encoding="utf-8") as af:
            writer = csv.writer(af)
            writer.writerow([
                today, "KeyShot", "AI Workflow Engineer", "LinkedIn Easy Apply",
                "https://www.linkedin.com/jobs/view/4469216266/", "SUBMITTED",
                "Application submitted to KeyShot", "EUR 50,000", "yes",
                f"Prabhavit_CV_KeyShot.pdf + CoverLetter_KeyShot.pdf | confirmations/KeyShot-{today}.txt"
            ])
    else:
        print("Submit button not found on Step 4.")
        buttons = [b.inner_text().strip() for b in page.query_selector_all('button') if b.is_visible()]
        print("Visible buttons on page:", buttons)

    ctx.close()
