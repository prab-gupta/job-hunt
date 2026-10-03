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

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 1200})
    page.goto(LOGIN_URL, wait_until="networkidle")
    try:
        page.locator("button[data-automation-id='legalNoticeAcceptButton']").click(force=True)
    except: pass
    page.wait_for_selector("input[data-automation-id='email']", timeout=15000)
    page.locator("input[data-automation-id='email']").fill(EMAIL)
    page.locator("input[data-automation-id='password']").fill(PWD)
    page.locator("button[data-automation-id='signInSubmitButton']").click(force=True)
    
    # Wait for hydration
    page.wait_for_selector("#phoneNumber--phoneNumber", timeout=30000)
    page.wait_for_timeout(2000)
    
    # Click Save and Continue
    page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
    
    # Wait for Step 2
    page.wait_for_selector('h3:has-text("My Experience")', timeout=20000)
    page.wait_for_timeout(3000)
    
    # Try uploading both CV and Cover Letter
    file_input = page.locator('input[type="file"]').first
    print("Uploading CV and Cover Letter...", flush=True)
    file_input.set_input_files([CV_PATH, CL_PATH])
    page.wait_for_timeout(4000)
    
    # Click Add for Work Experience
    print("Clicking Add Work Experience...", flush=True)
    add_exp_btn = page.locator('button:has-text("Add")').first
    add_exp_btn.click(force=True)
    page.wait_for_timeout(2000)
    
    # Dump inputs inside work experience
    exp_inputs = page.eval_on_selector_all('input, textarea', '''els => els.map(e => ({
        id: e.id,
        name: e.name,
        type: e.type,
        automationId: e.getAttribute('data-automation-id'),
        placeholder: e.placeholder
    }))''')
    print("Inputs after Add Exp:\n", json.dumps(exp_inputs, indent=2))
    
    page.screenshot(path="scratch/step2_add_exp.png", full_page=True)
    browser.close()
