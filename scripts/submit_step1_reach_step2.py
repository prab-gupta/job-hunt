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
        
        print("2. Waiting for Step 1 form...", flush=True)
        page.wait_for_selector("#name--legalName--firstName", timeout=30000)
        page.wait_for_timeout(5000)
        
        # 1. Source: "How Did You Hear About Us?"
        print("Selecting Source: Job Board...", flush=True)
        source_icon = page.locator("div[data-automation-id='formField-source'] span[data-automation-id='promptIcon']")
        source_icon.click(force=True)
        page.wait_for_timeout(1000)
        
        # Click Job Board category
        page.locator('div[data-automation-id="promptOption"]:has-text("Job Board")').click(force=True)
        page.wait_for_timeout(1000)
        
        # Click Job Board leaf
        page.locator('div[data-automation-id="promptOption"]:has-text("Job Board")').last.click(force=True)
        page.wait_for_timeout(1000)
        print("Source selected!", flush=True)

        # 2. Prior experience -> No
        print("Setting prior experience -> No...", flush=True)
        labels = page.locator("label")
        for i in range(labels.count()):
            l = labels.nth(i)
            txt = l.inner_text().strip().lower()
            if txt == "no":
                l.click(force=True)
                break
        page.wait_for_timeout(500)

        # 3. Given Name & Family Name
        print("Filling Name...", flush=True)
        page.locator("#name--legalName--firstName").fill("Prabhavit")
        page.locator("#name--legalName--lastName").fill("Gupta")

        # 4. Address
        print("Filling Address...", flush=True)
        if page.locator("#address--addressLine1").count() > 0:
            page.locator("#address--addressLine1").fill("Via Torino")
        if page.locator("#address--postalCode").count() > 0:
            page.locator("#address--postalCode").fill("30172")
        if page.locator("#address--city").count() > 0:
            page.locator("#address--city").fill("Venezia")

        # 5. Province -> Select Venezia
        print("Selecting Province Venezia...", flush=True)
        prov_btn = page.locator("#address--countryRegion")
        if prov_btn.count() > 0:
            prov_btn.click(force=True)
            page.wait_for_timeout(1000)
            page.locator("#d8c28926264f412e9d897b8f5eb1042e").click(force=True)
            page.wait_for_timeout(1000)

        # 6. Phone Device Type -> Mobile
        print("Selecting Phone Device Type...", flush=True)
        phone_type_btn = page.locator("#phoneNumber--phoneType")
        if phone_type_btn.count() > 0:
            phone_type_btn.click(force=True)
            page.wait_for_timeout(1000)
            p_options = page.eval_on_selector_all('li[role="option"], div[role="option"]', '''els => els.map(e => ({
                text: e.innerText.trim(),
                id: e.id
            }))''')
            for opt in p_options:
                if "mobile" in opt['text'].lower():
                    page.locator(f"#{opt['id']}").click(force=True)
                    break
            page.wait_for_timeout(1000)

        # 7. Phone Number -> 3516107807
        print("Filling Phone Number...", flush=True)
        page.locator("#phoneNumber--phoneNumber").fill("3516107807")

        page.screenshot(path="scratch/medtronic_step1_ready.png", full_page=True)

        # 8. Save and Continue
        print("Clicking Save and Continue...", flush=True)
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        print("Waiting for Step 2...", flush=True)
        page.wait_for_timeout(10000)
        
        print("URL after Next:", page.url, flush=True)
        page.screenshot(path="scratch/medtronic_step2_reached.png", full_page=True)

        # Check step labels
        labels = page.eval_on_selector_all('label, h2, h3, [data-automation-id="activeStep"]', '''els => els.map(e => e.innerText.trim()).filter(Boolean)''')
        print("Headings/Labels on new page snippet:", labels[:15], flush=True)
        
        errors = page.eval_on_selector_all('[data-automation-id*="error"], [role="alert"]', '''els => els.map(e => e.innerText.trim()).filter(Boolean)''')
        if errors:
            print("Errors on page:", errors, flush=True)

        browser.close()

if __name__ == "__main__":
    run()
