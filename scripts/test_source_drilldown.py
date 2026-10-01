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
    
    page.wait_for_selector("#name--legalName--firstName", timeout=30000)
    page.wait_for_timeout(4000)
    
    # Click prompt icon to open root list
    page.locator("span[data-automation-id='promptIcon']").first.click(force=True)
    page.wait_for_timeout(1000)
    
    # Click "Job Board"
    print("Clicking 'Job Board'...", flush=True)
    page.locator('div[role="option"]:has-text("Job Board"), li[role="option"]:has-text("Job Board")').first.click(force=True)
    page.wait_for_timeout(1500)
    
    sub_opts = page.eval_on_selector_all('[role="option"], [data-automation-id="promptOption"]', 'els => els.map(e => e.innerText.trim()).filter(Boolean)')
    print("Sub options under Job Board:\n", sub_opts, flush=True)
    
    # Click first leaf option or LinkedIn if present
    for opt_text in sub_opts:
        if "linkedin" in opt_text.lower():
            print("Clicking option:", opt_text, flush=True)
            page.locator(f'[role="option"]:has-text("{opt_text}")').first.click(force=True)
            break
    else:
        if sub_opts:
            print("Clicking first sub-option:", sub_opts[0], flush=True)
            page.locator(f'[role="option"]:has-text("{sub_opts[0]}")').first.click(force=True)
            
    page.wait_for_timeout(1000)
    page.screenshot(path="scratch/source_selected.png")
    
    # Check if selected item badge appears
    badge = page.eval_on_selector_all('div[data-automation-id="formField-source"] [data-automation-id*="selectedItem"], div[data-automation-id="formField-source"] span', 'els => els.map(e => e.innerText.trim()).filter(Boolean)')
    print("Source container text:", badge, flush=True)
    browser.close()
