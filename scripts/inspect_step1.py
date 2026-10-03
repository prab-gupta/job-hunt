import sys
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

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 900})
        page = context.new_page()
        
        print("Logging in...", flush=True)
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
        
        print("Current URL:", page.url, flush=True)
        print("Step title:", page.title(), flush=True)
        page.screenshot(path="scratch/medtronic_step1_actual.png")
        
        # Dump all buttons and inputs
        buttons = page.eval_on_selector_all('button', '''els => els.map(e => ({
            text: e.innerText ? e.innerText.trim() : null,
            dataAutomation: e.getAttribute('data-automation-id') || null,
            className: e.className || null
        })).filter(b => b.text)''')
        
        inputs = page.eval_on_selector_all('input', '''els => els.map(e => ({
            type: e.type,
            name: e.name,
            id: e.id,
            dataAutomation: e.getAttribute('data-automation-id') || null,
            ariaLabel: e.getAttribute('aria-label') || null
        }))''')
        
        print("Buttons found:\n", json.dumps(buttons, indent=2), flush=True)
        print("Inputs found count:", len(inputs), flush=True)
        print("Inputs snippet:\n", json.dumps(inputs[:15], indent=2), flush=True)
        
        browser.close()

if __name__ == "__main__":
    run()
