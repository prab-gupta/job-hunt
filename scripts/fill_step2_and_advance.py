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
        
        # Wait for hydration
        page.wait_for_selector("#phoneNumber--phoneNumber", timeout=30000)
        page.wait_for_timeout(2000)
        
        # Click Save and Continue on Step 1
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        # Wait for Step 2
        page.wait_for_selector('h3:has-text("My Experience")', timeout=20000)
        page.wait_for_timeout(3000)
        
        # Check if CV/CL already uploaded or upload now
        uploaded_items = page.locator('[data-automation-id="file-upload-item"]')
        print(f"Already uploaded files count: {uploaded_items.count()}", flush=True)
        if uploaded_items.count() < 2:
            file_input = page.locator('input[type="file"]').first
            print("Uploading CV and Cover Letter...", flush=True)
            file_input.set_input_files([CV_PATH, CL_PATH])
            page.wait_for_timeout(5000)

        # Work Experience: Check if workExperience section already open or click Add
        exp_title = page.locator('input[id*="jobTitle"]')
        if exp_title.count() == 0:
            print("Clicking Add Work Experience...", flush=True)
            add_exp_btn = page.locator('button:has-text("Add")').first
            add_exp_btn.click(force=True)
            page.wait_for_timeout(2000)
            
        print("Filling Work Experience...", flush=True)
        page.locator('input[id*="jobTitle"]').first.fill("AI Operations & Automation Engineer")
        page.locator('input[id*="companyName"]').first.fill("FlowSpace.co")
        page.locator('input[id*="location"]').first.fill("Venice, Italy")
        
        # Currently work here
        curr_box = page.locator('input[id*="currentlyWorkHere"]').first
        if not curr_box.is_checked():
            curr_box.check(force=True)
            page.wait_for_timeout(500)
            
        # Start date: MM=06, YYYY=2023
        month_inputs = page.locator('input[data-automation-id="dateSectionMonth-input"]')
        year_inputs = page.locator('input[data-automation-id="dateSectionYear-input"]')
        if month_inputs.count() > 0:
            month_inputs.first.fill("06")
        if year_inputs.count() > 0:
            year_inputs.first.fill("2023")
            
        # Role description
        desc = page.locator('textarea[id*="roleDescription"]')
        if desc.count() > 0:
            desc.first.fill("Designed and deployed end-to-end AI agentic workflows, Azure OpenAI / LLM integrations, and process automations.")
            
        # Education: Click Add under Education
        edu_section = page.locator('div:has-text("Education")')
        edu_add = page.locator('button:has-text("Add")').last
        print("Checking Education section...", flush=True)
        edu_inputs = page.locator('input[id*="school"], input[id*="degree"]')
        if edu_inputs.count() == 0:
            print("Clicking Add Education...", flush=True)
            edu_add.click(force=True)
            page.wait_for_timeout(2000)
            
        # Inspect education inputs
        edu_fields = page.eval_on_selector_all('input[id*="education"], button[id*="education"], div[data-automation-id*="education"]', '''els => els.map(e => ({
            id: e.id,
            name: e.name,
            automationId: e.getAttribute('data-automation-id'),
            tag: e.tagName
        }))''')
        print("Education fields:\n", json.dumps(edu_fields, indent=2), flush=True)

        page.screenshot(path="scratch/step2_filled_exp_edu.png", full_page=True)
        
        # Save and Continue
        print("Clicking Save and Continue to reach Step 3...", flush=True)
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        # Wait up to 10s and inspect page state
        for i in range(5):
            page.wait_for_timeout(2000)
            headings = page.eval_on_selector_all('h2, h3, h4', 'els => els.map(e => e.innerText.trim()).filter(Boolean)')
            errors = page.eval_on_selector_all('[data-automation-id*="error"], [role="alert"]', 'els => els.map(e => e.innerText.trim()).filter(Boolean)')
            print(f"[{i*2}s] Headings: {headings[:5]} | Errors: {errors}", flush=True)
            if any("questions" in h.lower() for h in headings):
                print("STEP 3 REACHED!", flush=True)
                page.screenshot(path="scratch/step3_reached.png", full_page=True)
                break
                
        browser.close()

if __name__ == "__main__":
    run()
