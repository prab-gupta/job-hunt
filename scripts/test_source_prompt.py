import time
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://medtronic.wd1.myworkdayjobs.com/en-US/MedtronicCareers/login?redirect=%2FMedtronicCareers%2Fjob%2FSlovakia-Remote%2FAI---Data-Science-Eng-I_R73677%2Fapply%2FapplyManually"
EMAIL = "prabhavitg@gmail.com"
import os as _os
PWD = _os.environ.get("JOBS_ACCOUNT_PASSWORD")
if not PWD:
    raise SystemExit("JOBS_ACCOUNT_PASSWORD is not set; export it in the environment before running this script (never hard-code it).")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 1000})
    page.goto(LOGIN_URL, wait_until="networkidle")
    try:
        page.locator("button[data-automation-id='legalNoticeAcceptButton']").click(force=True)
    except: pass
    page.wait_for_selector("input[data-automation-id='email']", timeout=15000)
    page.locator("input[data-automation-id='email']").fill(EMAIL)
    page.locator("input[data-automation-id='password']").fill(PWD)
    page.locator("button[data-automation-id='signInSubmitButton']").click(force=True)
    
    page.wait_for_selector("#name--legalName--firstName", timeout=30000)
    page.wait_for_timeout(4000)
    
    # Try typing "LinkedIn" and Enter
    source_input = page.locator("#source--source")
    print("Clicking source input...", flush=True)
    source_input.click(force=True)
    source_input.fill("LinkedIn")
    page.keyboard.press("Enter")
    page.wait_for_timeout(2000)
    
    # Check if any list or popup appeared
    popup_text = page.eval_on_selector_all('[role="listbox"], [role="option"], [data-automation-id="promptOption"]', 'els => els.map(e => e.innerText.trim()).filter(Boolean)')
    print("After Enter listbox options:", popup_text[:10], flush=True)
    
    # Check if a badge appeared
    badges = page.eval_on_selector_all('div[data-automation-id="formField-source"] [data-automation-id*="selectedItem"], div[data-automation-id="formField-source"] button[data-automation-id*="delete"]', 'els => els.map(e => e.innerText.trim())')
    print("Source badges:", badges, flush=True)
    
    # Take screenshot
    page.screenshot(path="scratch/source_test.png")
    browser.close()
