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
        
        print("Waiting for Step 1 form...", flush=True)
        page.wait_for_selector("#name--legalName--firstName", timeout=30000)
        
        # Give enough time for lower sections (Phone, Email, Province) to hydrate
        page.wait_for_timeout(8000)
        
        # Fill name & address
        page.locator("#name--legalName--firstName").fill("Prabhavit")
        page.locator("#name--legalName--lastName").fill("Gupta")
        if page.locator("#address--addressLine1").count() > 0:
            page.locator("#address--addressLine1").fill("Via Torino")
        if page.locator("#address--postalCode").count() > 0:
            page.locator("#address--postalCode").fill("30172")
        if page.locator("#address--city").count() > 0:
            page.locator("#address--city").fill("Venezia")

        # Click Province dropdown to open and inspect options
        prov_btn = page.locator("#address--countryRegion")
        if prov_btn.count() > 0:
            print("Clicking Province dropdown...", flush=True)
            prov_btn.click(force=True)
            page.wait_for_timeout(1500)
            
            # Find listbox items
            options = page.eval_on_selector_all('li[role="option"], div[role="option"]', '''els => els.map(e => ({
                text: e.innerText.trim(),
                id: e.id
            }))''')
            print(f"Province options count: {len(options)}", flush=True)
            venice_opts = [o for o in options if "ven" in o['text'].lower()]
            print("Venice matching options:", venice_opts, flush=True)
            
            # Select Venezia if found
            for opt in options:
                if "venezia" in opt['text'].lower() or "venice" in opt['text'].lower():
                    print("Selecting province:", opt['text'], flush=True)
                    page.locator(f"#{opt['id']}").click(force=True)
                    break
            page.wait_for_timeout(1000)
            
        # Inspect Source dropdown / input
        source_inputs = page.eval_on_selector_all('div[data-automation-id*="source"], input[data-automation-id*="source"], button[id*="source"], [aria-label*="Hear About"]', '''els => els.map(e => ({
            tag: e.tagName,
            id: e.id,
            automationId: e.getAttribute('data-automation-id'),
            ariaLabel: e.getAttribute('aria-label'),
            text: e.innerText ? e.innerText.trim() : null
        }))''')
        print("Source elements:", json.dumps(source_inputs, indent=2), flush=True)

        # Inspect Phone fields
        phone_fields = page.eval_on_selector_all('input[id*="phone"], button[id*="phone"], input[type="tel"]', '''els => els.map(e => ({
            tag: e.tagName,
            id: e.id,
            name: e.name,
            automationId: e.getAttribute('data-automation-id'),
            ariaLabel: e.getAttribute('aria-label'),
            type: e.type
        }))''')
        print("Phone fields:", json.dumps(phone_fields, indent=2), flush=True)

        page.screenshot(path="scratch/medtronic_step1_hydrated.png", full_page=True)
        browser.close()

if __name__ == "__main__":
    run()
