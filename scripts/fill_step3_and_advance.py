import time
import os
import json
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://medtronic.wd1.myworkdayjobs.com/en-US/MedtronicCareers/login?redirect=%2FMedtronicCareers%2Fjob%2FSlovakia-Remote%2FAI---Data-Science-Eng-I_R73677%2Fapply%2FapplyManually"
EMAIL = "prabhavitg@gmail.com"
import os as _os
PWD = _os.environ.get("JOBS_ACCOUNT_PASSWORD")
if not PWD:
    raise SystemExit("JOBS_ACCOUNT_PASSWORD is not set; export it in the environment before running this script (never hard-code it).")
CV_PATH = os.path.abspath("cv/main_Medtronic_AIDeveloper.pdf")
CL_PATH = os.path.abspath("cover_letters/cover_Medtronic_AIDeveloper.pdf")

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
        page.wait_for_selector("#phoneNumber--phoneNumber", timeout=30000)
        page.wait_for_timeout(2000)
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        # Advance through Step 2
        page.wait_for_selector('h3:has-text("My Experience")', timeout=20000)
        page.wait_for_timeout(2000)
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        # Reached Step 3
        print("Waiting for Step 3 questions...", flush=True)
        page.wait_for_selector('h3:has-text("Application Questions")', timeout=20000)
        page.wait_for_timeout(4000)
        
        # Find all dropdown buttons inside the questions container
        dropdown_btns = page.locator('button[aria-haspopup="listbox"]')
        print(f"Dropdown buttons on Step 3: {dropdown_btns.count()}", flush=True)
        
        # We need to answer 4 questions:
        # Q1: Non-compete / confidentiality -> No
        # Q2: Legal right to work -> Yes
        # Q3: Prior Medtronic work -> No
        # Q4: AI tools consent -> Yes
        answers = ["No", "Yes", "No", "Yes"]
        
        # Filter to only the buttons that say "Select One" or are question dropdowns
        q_btns = []
        for i in range(dropdown_btns.count()):
            btn = dropdown_btns.nth(i)
            btn_text = btn.inner_text().strip().lower()
            if "select one" in btn_text or btn.get_attribute("id") and "question" in btn.get_attribute("id").lower():
                q_btns.append(btn)
                
        print(f"Matching question dropdowns: {len(q_btns)}", flush=True)
        
        for idx, (btn, target_val) in enumerate(zip(q_btns, answers)):
            print(f"Answering Q{idx+1} with '{target_val}'...", flush=True)
            btn.click(force=True)
            page.wait_for_timeout(1000)
            
            # Select target_val option
            opt = page.locator(f'li[role="option"]:has-text("{target_val}"), div[role="option"]:has-text("{target_val}")').first
            opt.click(force=True)
            page.wait_for_timeout(1000)
            
        page.screenshot(path="scratch/step3_answered.png", full_page=True)
        print("Answered all questions on Step 3. Clicking Save and Continue...", flush=True)
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        # Wait for Step 4
        print("Waiting for Step 4 (Voluntary Disclosures)...", flush=True)
        page.wait_for_timeout(6000)
        
        page.screenshot(path="scratch/step4_reached.png", full_page=True)
        
        headings = page.eval_on_selector_all('h2, h3, h4', 'els => els.map(e => e.innerText.trim()).filter(Boolean)')
        errors = page.eval_on_selector_all('[data-automation-id*="error"], [role="alert"]', 'els => els.map(e => e.innerText.trim()).filter(Boolean)')
        print(f"Headings on Step 4: {headings[:5]} | Errors: {errors}", flush=True)
        
        browser.close()

if __name__ == "__main__":
    run()
