import time
import json
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://medtronic.wd1.myworkdayjobs.com/en-US/MedtronicCareers/login?redirect=%2FMedtronicCareers%2Fjob%2FSlovakia-Remote%2FAI---Data-Science-Eng-I_R73677%2Fapply%2FapplyManually"
EMAIL = "prabhavitg@gmail.com"
PWD = "Jobs@2026"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 900})
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
        
        print("2. Waiting for form elements to mount...", flush=True)
        # Wait up to 30s for the loading spinner/dots to disappear and inputs to appear
        for i in range(15):
            page.wait_for_timeout(2000)
            inputs = page.locator("input").count()
            print(f"[{i*2}s] Inputs found: {inputs}", flush=True)
            if inputs > 3:
                break
                
        page.screenshot(path="scratch/medtronic_step1_loaded.png")
        print("URL:", page.url, flush=True)
        
        # List all inputs with data-automation-id
        inputs_info = page.eval_on_selector_all('input', '''els => els.map(e => ({
            id: e.id,
            name: e.name,
            automationId: e.getAttribute('data-automation-id'),
            ariaLabel: e.getAttribute('aria-label'),
            type: e.type,
            value: e.value
        }))''')
        print("Inputs details:\n", json.dumps(inputs_info, indent=2), flush=True)
        
        # Also check selects or dropdowns or buttons
        buttons_info = page.eval_on_selector_all('button', '''els => els.map(e => ({
            text: e.innerText ? e.innerText.trim() : null,
            automationId: e.getAttribute('data-automation-id')
        })).filter(b => b.text || b.automationId)''')
        print("Buttons details:\n", json.dumps(buttons_info, indent=2), flush=True)
        
        browser.close()

if __name__ == "__main__":
    run()
