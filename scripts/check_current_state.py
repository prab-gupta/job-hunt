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
    
    page.wait_for_timeout(8000)
    page.screenshot(path="scratch/current_state.png", full_page=True)
    
    # Check all errors or alerts
    errors = page.eval_on_selector_all('[data-automation-id*="error"], [role="alert"]', 'els => els.map(e => e.innerText.trim()).filter(Boolean)')
    print("Page errors:", errors)
    print("Current URL:", page.url)
    
    # Check headings
    tags = page.eval_on_selector_all('h1, h2, h3, h4', 'els => els.map(e => ({tag: e.tagName, text: e.innerText.trim()}))')
    print("Headings:", tags)
    browser.close()
