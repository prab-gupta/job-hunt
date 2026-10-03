import time
import json
import os
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://medtronic.wd1.myworkdayjobs.com/en-US/MedtronicCareers/login?redirect=%2FMedtronicCareers%2Fjob%2FSlovakia-Remote%2FAI---Data-Science-Eng-I_R73677%2Fapply%2FapplyManually"
EMAIL = "prabhavitg@gmail.com"
import os as _os
PWD = _os.environ.get("JOBS_ACCOUNT_PASSWORD")
if not PWD:
    raise SystemExit("JOBS_ACCOUNT_PASSWORD is not set; export it in the environment before running this script (never hard-code it).")

CV_PATH = os.path.abspath("cv/main_Medtronic_AIDeveloper.pdf")
CL_PATH = os.path.abspath("cover_letters/cover_Medtronic_AIDeveloper.pdf")

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
        
        print("2. Waiting for Step 1 form hydration...", flush=True)
        page.wait_for_selector("#name--legalName--firstName", timeout=30000)
        page.wait_for_timeout(4000)
        
        # Verify and complete Step 1
        fn = page.locator("#name--legalName--firstName").input_value()
        if not fn:
            page.locator("#name--legalName--firstName").fill("Prabhavit")
        ln = page.locator("#name--legalName--lastName").input_value()
        if not ln:
            page.locator("#name--legalName--lastName").fill("Gupta")
            
        # Address
        if page.locator("#address--addressLine1").count() > 0 and not page.locator("#address--addressLine1").input_value():
            page.locator("#address--addressLine1").fill("Via Torino")
        if page.locator("#address--postalCode").count() > 0 and not page.locator("#address--postalCode").input_value():
            page.locator("#address--postalCode").fill("30172")
        if page.locator("#address--city").count() > 0 and not page.locator("#address--city").input_value():
            page.locator("#address--city").fill("Venezia")
            
        # Source check
        source_div = page.locator("div[data-automation-id='formField-source']")
        if "1 item selected" not in source_div.inner_text():
            print("Selecting Source: Job Board...", flush=True)
            source_icon = source_div.locator("span[data-automation-id='promptIcon']")
            source_icon.click(force=True)
            page.wait_for_timeout(1000)
            page.locator('div[data-automation-id="promptOption"]:has-text("Job Board")').first.click(force=True)
            page.wait_for_timeout(1000)
            page.locator('div[data-automation-id="promptOption"]:has-text("Job Board")').last.click(force=True)
            page.wait_for_timeout(1000)

        # Prior experience check
        labels = page.locator("label")
        for i in range(labels.count()):
            l = labels.nth(i)
            if l.inner_text().strip().lower() == "no":
                l.click(force=True)
                break

        # Province check
        prov_btn = page.locator("#address--countryRegion")
        if prov_btn.count() > 0 and "select one" in prov_btn.inner_text().lower():
            print("Selecting Province: Venezia...", flush=True)
            prov_btn.click(force=True)
            page.wait_for_timeout(1000)
            page.locator("#d8c28926264f412e9d897b8f5eb1042e").click(force=True)
            page.wait_for_timeout(1000)
            
        # Phone Type check
        pt_btn = page.locator("#phoneNumber--phoneType")
        if pt_btn.count() > 0 and "select one" in pt_btn.inner_text().lower():
            print("Selecting Phone Type: Mobile...", flush=True)
            pt_btn.click(force=True)
            page.wait_for_timeout(1000)
            page.locator('li[role="option"]:has-text("Mobile"), div[role="option"]:has-text("Mobile")').first.click(force=True)
            page.wait_for_timeout(1000)

        # Phone Number check
        if page.locator("#phoneNumber--phoneNumber").count() > 0:
            pn = page.locator("#phoneNumber--phoneNumber").input_value()
            if not pn:
                page.locator("#phoneNumber--phoneNumber").fill("3516107807")

        print("Clicking Save and Continue on Step 1...", flush=True)
        page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
        
        print("3. Waiting for Step 2 (h2: My Experience)...", flush=True)
        page.wait_for_selector('h2:has-text("My Experience")', timeout=30000)
        page.wait_for_timeout(4000)
        print("Successfully reached Step 2!", flush=True)
        page.screenshot(path="scratch/medtronic_step2_verified.png", full_page=True)

        # Now inspect file inputs and elements on Step 2
        file_inputs = page.locator('input[type="file"]')
        print(f"File inputs found: {file_inputs.count()}", flush=True)
        for i in range(file_inputs.count()):
            f_el = file_inputs.nth(i)
            print(f"File input {i}: id={f_el.get_attribute('id')}, automationId={f_el.get_attribute('data-automation-id')}", flush=True)

        if file_inputs.count() > 0:
            print(f"Uploading CV to file input 0: {CV_PATH}", flush=True)
            file_inputs.nth(0).set_input_files(CV_PATH)
            page.wait_for_timeout(5000)
            print("Uploaded CV successfully!", flush=True)

        page.screenshot(path="scratch/medtronic_step2_after_cv.png", full_page=True)
        
        # Check all Add buttons on Step 2
        add_btns = page.eval_on_selector_all('button', '''els => els.map(e => ({
            text: e.innerText ? e.innerText.trim() : null,
            automationId: e.getAttribute('data-automation-id'),
            id: e.id
        })).filter(b => b.text && b.text.toLowerCase().includes('add'))''')
        print("Add buttons on Step 2:", json.dumps(add_btns, indent=2), flush=True)

        browser.close()

if __name__ == "__main__":
    run()
