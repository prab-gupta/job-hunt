import time
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://medtronic.wd1.myworkdayjobs.com/en-US/MedtronicCareers/login?redirect=%2FMedtronicCareers%2Fjob%2FSlovakia-Remote%2FAI---Data-Science-Eng-I_R73677%2Fapply%2FapplyManually"
EMAIL = "prabhavitg@gmail.com"
import os as _os
PWD = _os.environ.get("JOBS_ACCOUNT_PASSWORD")
if not PWD:
    raise SystemExit("JOBS_ACCOUNT_PASSWORD is not set; export it in the environment before running this script (never hard-code it).")

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
    print("Clicking source prompt icon...", flush=True)
    source_icon.click(force=True)
    page.wait_for_timeout(1000)
    
    # Inspect open popups
    popups = page.eval_on_selector_all('[data-automation-id="promptOption"]', 'els => els.map(e => ({id: e.id, text: e.innerText.trim()}))')
    print("Source root options:", popups, flush=True)
    
    # Click Job Board
    for p_opt in popups:
        if "job board" in p_opt['text'].lower():
            print("Clicking Job Board option:", p_opt['text'], flush=True)
            page.locator(f"#{p_opt['id']}").click(force=True)
            break
            
    page.wait_for_timeout(1500)
    sub_popups = page.eval_on_selector_all('[data-automation-id="promptOption"]', 'els => els.map(e => ({id: e.id, text: e.innerText.trim()}))')
    print("Job Board sub-options:", sub_popups, flush=True)
    
    # Click LinkedIn or first sub option
    for s_opt in sub_popups:
        if "linkedin" in s_opt['text'].lower():
            print("Selecting sub option:", s_opt['text'], flush=True)
            page.locator(f"#{s_opt['id']}").click(force=True)
            break
    else:
        if sub_popups:
            print("Selecting sub option:", sub_popups[0]['text'], flush=True)
            page.locator(f"#{sub_popups[0]['id']}").click(force=True)
            
    page.wait_for_timeout(1000)
    page.screenshot(path="scratch/source_properly_selected.png")
    
    # Check if selected item badge appears in source field
    source_text = page.locator("div[data-automation-id='formField-source']").inner_text()
    print("Final source text:\n", source_text, flush=True)
    
    browser.close()
