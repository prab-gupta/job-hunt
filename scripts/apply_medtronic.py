import sys
import time
import os
from playwright.sync_api import sync_playwright

ACTIVATE_URL = "https://medtronic.wd1.myworkdayjobs.com/MedtronicCareers/activate/u27uktludyprequrblam7qp6jvcjc7c24nmjpimk7gju7jnaljtm6ehlh7q3tfsrdarm4wu24rituvopy10tqyj7kih18w6erwg/?redirect=%2FMedtronicCareers%2Fjob%2FSlovakia-Remote%2FAI---Data-Science-Eng-I_R73677%2Fapply%2FapplyManually"
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
        
        print(f"Navigating to EXACT activation URL...", flush=True)
        page.goto(ACTIVATE_URL, wait_until="networkidle", timeout=45000)
        page.wait_for_timeout(3000)
        
        try:
            accept_btn = page.locator("button[data-automation-id='legalNoticeAcceptButton']")
            if accept_btn.count() > 0:
                accept_btn.click(force=True)
                print("Accepted cookies", flush=True)
                page.wait_for_timeout(1000)
        except Exception as e:
            pass

        print("URL after activation navigation:", page.url, flush=True)
        print("Page title:", page.title(), flush=True)
        page.screenshot(path="scratch/medtronic_activated_exact.png")
        
        # Check if sign in is required or if we landed on login
        if "login" in page.url or page.locator("button[data-automation-id='signInSubmitButton']").count() > 0:
            print("Signing in with verified account...", flush=True)
            page.locator("input[data-automation-id='email']").fill(EMAIL)
            page.locator("input[data-automation-id='password']").fill(PWD)
            page.locator("button[data-automation-id='signInSubmitButton']").click(force=True)
            page.wait_for_timeout(6000)
            print("URL after signing in:", page.url, flush=True)
            print("Page title:", page.title(), flush=True)
            page.screenshot(path="scratch/medtronic_logged_in_exact.png")
            
        snippet = page.inner_text("body")[:800]
        print("Body snippet:\n", snippet, flush=True)
        
        browser.close()

if __name__ == "__main__":
    run()
