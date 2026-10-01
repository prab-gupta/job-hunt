import time
import os
import json
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://medtronic.wd1.myworkdayjobs.com/en-US/MedtronicCareers/login?redirect=%2FMedtronicCareers%2Fjob%2FSlovakia-Remote%2FAI---Data-Science-Eng-I_R73677%2Fapply%2FapplyManually"
EMAIL = "prabhavitg@gmail.com"
PWD = "Jobs@2026"
CV_PATH = os.path.abspath("cv/main_Medtronic_AIDeveloper.pdf")

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
    
    # Wait for phone number field
    page.wait_for_selector("#phoneNumber--phoneNumber", timeout=30000)
    page.wait_for_timeout(2000)
    
    # Click Save and Continue
    page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
    
    # Wait for Step 2
    page.wait_for_selector('h3:has-text("My Experience")', timeout=20000)
    page.wait_for_timeout(3000)
    
    # Dump all file inputs, including hidden ones
    file_inputs = page.eval_on_selector_all('input[type="file"]', '''els => els.map(e => ({
        id: e.id,
        name: e.name,
        automationId: e.getAttribute('data-automation-id'),
        className: e.className,
        accept: e.accept
    }))''')
    print("File inputs on Step 2:\n", json.dumps(file_inputs, indent=2))
    
    # Upload CV
    print("Setting CV file on input[type='file']...", flush=True)
    page.set_input_files('input[type="file"]', CV_PATH)
    page.wait_for_timeout(4000)
    
    # Dump all elements with uploaded file info
    uploaded = page.eval_on_selector_all('[data-automation-id*="file"], [data-automation-id*="upload"], [data-automation-id*="attachment"]', '''els => els.map(e => ({
        tag: e.tagName,
        automationId: e.getAttribute('data-automation-id'),
        text: e.innerText ? e.innerText.trim() : null
    }))''')
    print("Uploaded elements state:\n", json.dumps(uploaded, indent=2))
    
    # Screenshot full page
    page.screenshot(path="scratch/step2_with_cv.png", full_page=True)
    
    browser.close()
