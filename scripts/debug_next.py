import time
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://medtronic.wd1.myworkdayjobs.com/en-US/MedtronicCareers/login?redirect=%2FMedtronicCareers%2Fjob%2FSlovakia-Remote%2FAI---Data-Science-Eng-I_R73677%2Fapply%2FapplyManually"
EMAIL = "prabhavitg@gmail.com"
PWD = "Jobs@2026"

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
    
    # Wait for phone number field (ensures full page is hydrated)
    print("Waiting for full Step 1 hydration...", flush=True)
    page.wait_for_selector("#phoneNumber--phoneNumber", timeout=30000)
    page.wait_for_timeout(2000)
    
    # Check fields
    fn = page.locator("#name--legalName--firstName").input_value()
    ln = page.locator("#name--legalName--lastName").input_value()
    source = page.locator("div[data-automation-id='formField-source']").inner_text()
    prov = page.locator("#address--countryRegion").inner_text()
    phone = page.locator("#phoneNumber--phoneNumber").input_value()
    print(f"Form values: fn={fn}, ln={ln}, prov={prov}, phone={phone}, source={source}", flush=True)
    
    if not fn:
        page.locator("#name--legalName--firstName").fill("Prabhavit")
    if not ln:
        page.locator("#name--legalName--lastName").fill("Gupta")
    if "select one" in prov.lower():
        page.locator("#address--countryRegion").click(force=True)
        page.wait_for_timeout(1000)
        page.locator("#d8c28926264f412e9d897b8f5eb1042e").click(force=True)
        page.wait_for_timeout(1000)
    if "1 item selected" not in source:
        source_div = page.locator("div[data-automation-id='formField-source']")
        source_div.locator("span[data-automation-id='promptIcon']").click(force=True)
        page.wait_for_timeout(1000)
        page.locator('div[data-automation-id="promptOption"]:has-text("Job Board")').first.click(force=True)
        page.wait_for_timeout(1000)
        page.locator('div[data-automation-id="promptOption"]:has-text("Job Board")').last.click(force=True)
        page.wait_for_timeout(1000)
    if not phone:
        page.locator("#phoneNumber--phoneNumber").fill("3516107807")
        
    page.screenshot(path="scratch/step1_before_click.png", full_page=True)
    print("Clicking Save and Continue...", flush=True)
    page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
    
    for i in range(5):
        page.wait_for_timeout(2000)
        errors = page.eval_on_selector_all('[data-automation-id*="error"], [role="alert"]', 'els => els.map(e => e.innerText.trim()).filter(Boolean)')
        headings = page.eval_on_selector_all('h2, h3, h4', 'els => els.map(e => e.innerText.trim()).filter(Boolean)')
        print(f"[{i*2}s] Errors: {errors} | Headings: {headings[:5]}", flush=True)
        if any("experience" in h.lower() for h in headings):
            print("STEP 2 DETECTED!", flush=True)
            page.screenshot(path="scratch/step2_found.png", full_page=True)
            break
            
    browser.close()
