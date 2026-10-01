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
    
    # Click prompt icon specifically inside formField-source
    source_icon = page.locator("div[data-automation-id='formField-source'] span[data-automation-id='promptIcon']")
    source_icon.click(force=True)
    page.wait_for_timeout(1000)
    
    # Click Job Board
    page.locator('div[data-automation-id="promptOption"]:has-text("Job Board")').click(force=True)
    page.wait_for_timeout(1500)
    
    page.screenshot(path="scratch/source_job_board_open.png")
    
    # Dump all visible text in popups
    popups = page.eval_on_selector_all('div[role="listbox"], div[data-uxi-widget-type="selectlist"], [data-automation-id="popup"]', 'els => els.map(e => e.innerText)')
    print("Popups text:\n", popups)
    
    browser.close()
