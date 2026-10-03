import time
import json
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://medtronic.wd1.myworkdayjobs.com/en-US/MedtronicCareers/login?redirect=%2FMedtronicCareers%2Fjob%2FSlovakia-Remote%2FAI---Data-Science-Eng-I_R73677%2Fapply%2FapplyManually"
EMAIL = "prabhavitg@gmail.com"
import os as _os
PWD = _os.environ.get("JOBS_ACCOUNT_PASSWORD")
if not PWD:
    raise SystemExit("JOBS_ACCOUNT_PASSWORD is not set; export it in the environment before running this script (never hard-code it).")

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 1200})
        page = context.new_page()
        
        print("Navigating to login...", flush=True)
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
        
        print("Waiting after sign in...", flush=True)
        page.wait_for_timeout(8000)
        
        print("URL:", page.url, flush=True)
        
        # Check active step
        active_step = page.locator('[data-automation-id="activeStep"]').inner_text() if page.locator('[data-automation-id="activeStep"]').count() > 0 else "unknown"
        print("Active step:", active_step, flush=True)
        
        # If on Step 1, click next
        if "information" in active_step.lower() or page.locator("#name--legalName--firstName").count() > 0:
            print("Advancing through Step 1...", flush=True)
            page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
            page.wait_for_timeout(8000)

        page.screenshot(path="scratch/medtronic_step2_full_view.png", full_page=True)
        
        # Inspect all inputs, buttons, file uploaders on Step 2
        file_inputs = page.eval_on_selector_all('input[type="file"]', '''els => els.map(e => ({
            id: e.id,
            name: e.name,
            automationId: e.getAttribute('data-automation-id')
        }))''')
        print("File inputs:", json.dumps(file_inputs, indent=2), flush=True)

        buttons = page.eval_on_selector_all('button', '''els => els.map(e => ({
            text: e.innerText ? e.innerText.trim() : null,
            automationId: e.getAttribute('data-automation-id')
        })).filter(b => b.text)''')
        print("Step 2 Buttons:", json.dumps(buttons, indent=2), flush=True)
        
        browser.close()

if __name__ == "__main__":
    run()
