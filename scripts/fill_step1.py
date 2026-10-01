import time
import json
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://medtronic.wd1.myworkdayjobs.com/en-US/MedtronicCareers/login?redirect=%2FMedtronicCareers%2Fjob%2FSlovakia-Remote%2FAI---Data-Science-Eng-I_R73677%2Fapply%2FapplyManually"
EMAIL = "prabhavitg@gmail.com"
PWD = "Jobs@2026"

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
        
        print("Waiting for Step 1 form...", flush=True)
        page.wait_for_selector("#name--legalName--firstName", timeout=30000)
        print("Step 1 form loaded!", flush=True)
        
        # Fill standard text inputs
        page.locator("#name--legalName--firstName").fill("Prabhavit")
        page.locator("#name--legalName--lastName").fill("Gupta")
        
        if page.locator("#address--addressLine1").count() > 0:
            page.locator("#address--addressLine1").fill("Via Torino")
        if page.locator("#address--postalCode").count() > 0:
            page.locator("#address--postalCode").fill("30172")
        if page.locator("#address--city").count() > 0:
            page.locator("#address--city").fill("Venezia")
            
        # Inspect phone inputs and all dropdown buttons
        dropdowns = page.eval_on_selector_all('button[aria-haspopup="listbox"], button[id*="dropdown"], div[data-automation-id*="dropdown"], button[aria-expanded]', '''els => els.map(e => ({
            id: e.id,
            text: e.innerText.trim(),
            ariaLabel: e.getAttribute('aria-label'),
            automationId: e.getAttribute('data-automation-id')
        }))''')
        print("Dropdowns / Listbox buttons:\n", json.dumps(dropdowns, indent=2), flush=True)
        
        # Check all form groups and labels
        form_fields = page.eval_on_selector_all('label', '''els => els.map(e => ({
            text: e.innerText.trim(),
            forId: e.getAttribute('for')
        }))''')
        print("Form labels:\n", json.dumps(form_fields, indent=2), flush=True)
        
        page.screenshot(path="scratch/medtronic_step1_partial_fill.png", full_page=True)
        browser.close()

if __name__ == "__main__":
    run()
