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
        
        print("1. Navigating to login...", flush=True)
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
        
        # Advance through Step 1
        print("Waiting for Step 1 hydration...", flush=True)
        page.wait_for_selector("#phoneNumber--phoneNumber", timeout=30000)
        page.wait_for_timeout(2000)
        print("Advancing through Step 1...", flush=True)
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        # Advance through Step 2
        print("Waiting for Step 2...", flush=True)
        page.wait_for_selector('h3:has-text("My Experience")', timeout=20000)
        page.wait_for_timeout(2000)
        print("Advancing through Step 2...", flush=True)
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        # Advance through Step 3
        print("Waiting for Step 3...", flush=True)
        page.wait_for_selector('h3:has-text("Application Questions")', timeout=20000)
        page.wait_for_timeout(2000)
        print("Advancing through Step 3...", flush=True)
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        # Arrive on Step 4 (Voluntary Disclosures)
        print("Waiting for Step 4 (Voluntary Disclosures)...", flush=True)
        page.wait_for_selector('h3:has-text("Voluntary Disclosures")', timeout=20000)
        page.wait_for_timeout(2000)
        print("Landed on Step 4!", flush=True)
        
        # Select Gender: Male
        gender_btn = page.locator('button:has-text("Select One")').first
        print("Clicking Gender dropdown...", flush=True)
        gender_btn.click(force=True)
        page.wait_for_timeout(1000)
        
        male_opt = page.locator('li[role="option"]:has-text("Male"), div[role="option"]:has-text("Male")').first
        print(f"Clicking Male option (count: {male_opt.count()})...", flush=True)
        male_opt.click(force=True)
        page.wait_for_timeout(1000)
        
        # Check I consent
        consent_cb = page.locator('input[type="checkbox"]').first
        if not consent_cb.is_checked():
            print("Checking I consent...", flush=True)
            consent_cb.check(force=True)
            page.wait_for_timeout(500)
            
        page.screenshot(path="scratch/step4_ready_to_review.png", full_page=True)
        
        # Advance to Step 5 Review
        print("Clicking Save and Continue to reach Review step...", flush=True)
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        # Wait for Step 5 Review
        print("Waiting for Step 5 Review...", flush=True)
        page.wait_for_selector('h3:has-text("Review")', timeout=20000)
        page.wait_for_timeout(4000)
        print("LANDED ON STEP 5 REVIEW!", flush=True)
        page.screenshot(path="scratch/step5_review_page.png", full_page=True)
        
        # Click Submit
        submit_btn = page.locator('button:has-text("Submit"), button[data-automation-id*="submit"]').first
        print(f"Submitting application with button: '{submit_btn.inner_text()}'...", flush=True)
        submit_btn.click(force=True)
        page.wait_for_timeout(10000)
        
        page.screenshot(path="scratch/medtronic_submitted_final.png", full_page=True)
        final_texts = page.eval_on_selector_all('h1, h2, h3, [data-automation-id*="status"], [data-automation-id*="banner"]', 'els => els.map(e => e.innerText.trim()).filter(Boolean)')
        print("Final Submission Status:\n", json.dumps(final_texts, indent=2), flush=True)
        
        browser.close()

if __name__ == "__main__":
    run()
