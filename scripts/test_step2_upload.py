import time
import os
import json
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://medtronic.wd1.myworkdayjobs.com/en-US/MedtronicCareers/login?redirect=%2FMedtronicCareers%2Fjob%2FSlovakia-Remote%2FAI---Data-Science-Eng-I_R73677%2Fapply%2FapplyManually"
EMAIL = "prabhavitg@gmail.com"
PWD = "Jobs@2026"

CV_PATH = os.path.abspath("cv/main_Medtronic_AIDeveloper.pdf")
CL_PATH = os.path.abspath("cover_letters/cover_Medtronic_AIDeveloper.pdf")

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 1200})
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
        
        print("Waiting for page load after sign in...", flush=True)
        page.wait_for_timeout(6000)
        
        # Click Save and Continue on Step 1
        print("Clicking Save and Continue on Step 1...", flush=True)
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        print("Waiting for Step 2 (h3: My Experience)...", flush=True)
        page.wait_for_selector('h3:has-text("My Experience")', timeout=25000)
        page.wait_for_timeout(5000)
        print("REACHED STEP 2!", flush=True)
        
        page.screenshot(path="scratch/medtronic_step2_verified.png", full_page=True)
        
        # Inspect file input inside dropzone
        dropzones = page.eval_on_selector_all('[data-automation-id*="file"], [data-automation-id*="upload"], [data-automation-id*="attachment"]', '''els => els.map(e => ({
            tag: e.tagName,
            automationId: e.getAttribute('data-automation-id'),
            id: e.id,
            text: e.innerText ? e.innerText.trim().slice(0, 100) : null
        }))''')
        print("Dropzones/Upload elements:\n", json.dumps(dropzones, indent=2), flush=True)
        
        # Look for input[type="file"]
        file_inputs = page.locator('input[type="file"]')
        print(f"File inputs count on Step 2: {file_inputs.count()}", flush=True)
        
        if file_inputs.count() > 0:
            print("Uploading CV to first file input...", flush=True)
            file_inputs.first.set_input_files(CV_PATH)
            page.wait_for_timeout(5000)
            print("CV uploaded!", flush=True)
            
        page.screenshot(path="scratch/medtronic_step2_cv_done.png", full_page=True)
        
        # Check headings and sections on Step 2
        h4s = page.eval_on_selector_all('h4', 'els => els.map(e => e.innerText.trim())')
        print("H4 sections on Step 2:", h4s, flush=True)

        browser.close()

if __name__ == "__main__":
    run()
