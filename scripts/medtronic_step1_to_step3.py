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
        
        # 2. STEP 1
        print("2. Hydrating Step 1...", flush=True)
        page.wait_for_selector("#phoneNumber--phoneNumber", timeout=30000)
        page.wait_for_timeout(2000)
        
        # Verify Name
        if not page.locator("#name--legalName--firstName").input_value():
            page.locator("#name--legalName--firstName").fill("Prabhavit")
        if not page.locator("#name--legalName--lastName").input_value():
            page.locator("#name--legalName--lastName").fill("Gupta")
            
        # Address
        if page.locator("#address--addressLine1").count() > 0 and not page.locator("#address--addressLine1").input_value():
            page.locator("#address--addressLine1").fill("Via Torino")
        if page.locator("#address--postalCode").count() > 0 and not page.locator("#address--postalCode").input_value():
            page.locator("#address--postalCode").fill("30172")
        if page.locator("#address--city").count() > 0 and not page.locator("#address--city").input_value():
            page.locator("#address--city").fill("Venezia")
            
        # Province
        prov_btn = page.locator("#address--countryRegion")
        if prov_btn.count() > 0 and "select one" in prov_btn.inner_text().lower():
            prov_btn.click(force=True)
            page.wait_for_timeout(1000)
            page.locator("#d8c28926264f412e9d897b8f5eb1042e").click(force=True)
            page.wait_for_timeout(1000)
            
        # Source
        source_div = page.locator("div[data-automation-id='formField-source']")
        if "1 item selected" not in source_div.inner_text():
            source_div.locator("span[data-automation-id='promptIcon']").click(force=True)
            page.wait_for_timeout(1000)
            page.locator('div[data-automation-id="promptOption"]:has-text("Job Board")').first.click(force=True)
            page.wait_for_timeout(1000)
            page.locator('div[data-automation-id="promptOption"]:has-text("Job Board")').last.click(force=True)
            page.wait_for_timeout(1000)
            
        # Phone
        if not page.locator("#phoneNumber--phoneNumber").input_value():
            page.locator("#phoneNumber--phoneNumber").fill("3516107807")
            
        # Prior experience -> No
        labels = page.locator("label")
        for i in range(labels.count()):
            l = labels.nth(i)
            if l.inner_text().strip().lower() == "no":
                l.click(force=True)
                break

        print("Advancing to Step 2...", flush=True)
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        # 3. STEP 2
        print("3. Waiting for Step 2...", flush=True)
        page.wait_for_selector('h3:has-text("My Experience")', timeout=20000)
        page.wait_for_timeout(3000)
        
        # Upload CV and CL
        file_input = page.locator('input[type="file"]').first
        uploaded_items = page.locator('[data-automation-id="file-upload-item"]')
        if uploaded_items.count() < 2:
            print("Uploading CV and CL...", flush=True)
            file_input.set_input_files([CV_PATH, CL_PATH])
            page.wait_for_timeout(5000)

        # Work Experience
        exp_title = page.locator('input[id*="jobTitle"]')
        if exp_title.count() == 0:
            print("Clicking Add Work Experience...", flush=True)
            page.locator('button:has-text("Add")').first.click(force=True)
            page.wait_for_timeout(2000)
            
        page.locator('input[id*="jobTitle"]').first.fill("AI Operations & Automation Engineer")
        page.locator('input[id*="companyName"]').first.fill("FlowSpace.co")
        page.locator('input[id*="location"]').first.fill("Venice, Italy")
        curr_box = page.locator('input[id*="currentlyWorkHere"]').first
        if not curr_box.is_checked():
            curr_box.check(force=True)
        page.locator('input[data-automation-id="dateSectionMonth-input"]').first.fill("06")
        page.locator('input[data-automation-id="dateSectionYear-input"]').first.fill("2023")
        page.locator('textarea[id*="roleDescription"]').first.fill("Designed and deployed end-to-end AI agentic workflows, Azure OpenAI / LLM integrations, and process automations.")
        page.wait_for_timeout(1000)
        
        print("Advancing to Step 3...", flush=True)
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        # 4. STEP 3
        print("4. Waiting for Step 3 (Application Questions)...", flush=True)
        page.wait_for_selector('h3:has-text("Application Questions")', timeout=20000)
        page.wait_for_timeout(6000)
        print("STEP 3 HYDRATED!", flush=True)
        
        page.screenshot(path="scratch/step3_questions_real.png", full_page=True)
        
        # Dump all questions text and elements
        fieldsets = page.eval_on_selector_all('fieldset, div[data-automation-id*="question"], div[data-automation-id*="formField"]', '''els => els.map(e => ({
            automationId: e.getAttribute('data-automation-id'),
            text: e.innerText ? e.innerText.trim() : null
        })).filter(f => f.text && f.text.length > 5)''')
        
        print("Step 3 Questions found:", len(fieldsets), flush=True)
        for i, f in enumerate(fieldsets):
            print(f"Q{i+1}: {f['text']}\n")
            
        browser.close()

if __name__ == "__main__":
    run()
