import time
import os
import json
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://medtronic.wd1.myworkdayjobs.com/en-US/MedtronicCareers/login?redirect=%2FMedtronicCareers%2Fjob%2FSlovakia-Remote%2FAI---Data-Science-Eng-I_R73677%2Fapply%2FapplyManually"
EMAIL = "prabhavitg@gmail.com"
PWD = "Jobs@2026"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 1400})
        page = context.new_page()
        
        print("Navigating...", flush=True)
        page.goto(LOGIN_URL, wait_until="networkidle", timeout=45000)
        
        try:
            accept_btn = page.locator("button[data-automation-id='legalNoticeAcceptButton']")
            if accept_btn.count() > 0:
                accept_btn.click(force=True)
        except: pass
        
        page.wait_for_selector("input[data-automation-id='email']", timeout=15000)
        page.locator("input[data-automation-id='email']").fill(EMAIL)
        page.locator("input[data-automation-id='password']").fill(PWD)
        page.locator("button[data-automation-id='signInSubmitButton']").click(force=True)
        
        # Advance through until Step 4
        for s in range(5):
            page.wait_for_timeout(3000)
            heading = page.locator('h3').first.inner_text() if page.locator('h3').count() > 0 else ""
            print(f"Step {s+1}: heading={heading}", flush=True)
            if "disclosures" in heading.lower():
                print("Landed on Step 4 (Voluntary Disclosures)!", flush=True)
                break
            page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)

        page.wait_for_timeout(4000)
        
        # 1. Gender dropdown
        gender_btn = page.locator('button[aria-haspopup="listbox"]').first
        print("Clicking Gender dropdown...", flush=True)
        gender_btn.click(force=True)
        page.wait_for_timeout(1000)
        
        gender_opts = page.eval_on_selector_all('li[role="option"], div[role="option"]', 'els => els.map(e => e.innerText.trim()).filter(Boolean)')
        print("Gender options:", gender_opts, flush=True)
        
        # Click Male
        male_opt = page.locator('li[role="option"]:has-text("Male"), div[role="option"]:has-text("Male")').first
        if male_opt.count() > 0:
            male_opt.click(force=True)
            print("Selected Male", flush=True)
        page.wait_for_timeout(1000)
        
        # 2. I consent checkbox
        consent_box = page.locator('input[type="checkbox"]').first
        if not consent_box.is_checked():
            print("Checking I consent...", flush=True)
            consent_box.check(force=True)
            page.wait_for_timeout(500)
            
        page.screenshot(path="scratch/step4_completed.png", full_page=True)
        
        # Click Save and Continue to reach Step 5 (Review)
        print("Clicking Save and Continue to reach Review step...", flush=True)
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        # Wait for Step 5 Review
        page.wait_for_timeout(8000)
        page.screenshot(path="scratch/step5_review_page.png", full_page=True)
        
        review_heading = page.locator('h3').first.inner_text() if page.locator('h3').count() > 0 else ""
        print("Step 5 Heading:", review_heading, flush=True)
        
        # Inspect submit button
        submit_btn = page.locator('button:has-text("Submit"), button[data-automation-id*="submit"]')
        print("Submit button found:", submit_btn.count(), flush=True)
        if submit_btn.count() > 0:
            print("Submit button text:", submit_btn.first.inner_text(), flush=True)
            print("SUBMITTING APPLICATION...", flush=True)
            submit_btn.first.click(force=True)
            page.wait_for_timeout(10000)
            
            page.screenshot(path="scratch/medtronic_submitted_result.png", full_page=True)
            result_heading = page.locator('h2, h3, [data-automation-id*="banner"], [role="status"]').all_inner_texts()
            print("Result after submit:", result_heading, flush=True)

        browser.close()

if __name__ == "__main__":
    run()
