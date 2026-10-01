import time
import json
from playwright.sync_api import sync_playwright

APPLY_URL = "https://medtronic.wd1.myworkdayjobs.com/MedtronicCareers/job/Slovakia-Remote/AI---Data-Science-Eng-I_R73677/apply/applyManually"
EMAIL = "prabhavitg@gmail.com"
PWD = "Jobs@2026"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 1200})
        page = context.new_page()
        
        print("Navigating...", flush=True)
        page.goto(APPLY_URL, wait_until="networkidle", timeout=45000)
        
        try:
            accept_btn = page.locator("button[data-automation-id='legalNoticeAcceptButton']")
            if accept_btn.count() > 0:
                accept_btn.click(force=True)
        except: pass
        
        if page.locator("input[data-automation-id='email']").count() > 0:
            print("Logging in...", flush=True)
            page.locator("input[data-automation-id='email']").fill(EMAIL)
            page.locator("input[data-automation-id='password']").fill(PWD)
            page.locator("button[data-automation-id='signInSubmitButton']").click(force=True)
            page.wait_for_timeout(6000)
            
        print("Current URL:", page.url, flush=True)
        page.wait_for_timeout(4000)
        
        # Check active step
        active_step = page.locator('[data-automation-id="activeStep"]').inner_text() if page.locator('[data-automation-id="activeStep"]').count() > 0 else "unknown"
        print("Active step:", active_step, flush=True)
        
        # If still on Step 1, click next
        if "information" in active_step.lower():
            print("On Step 1, advancing to Step 2...", flush=True)
            page.locator("button[data-automation-id='pageFooterNextButton']").click(force=True)
            page.wait_for_timeout(8000)

        page.screenshot(path="scratch/medtronic_step2_full.png", full_page=True)
        
        # Dump file inputs
        file_inputs = page.eval_on_selector_all('input[type="file"]', '''els => els.map(e => ({
            id: e.id,
            name: e.name,
            automationId: e.getAttribute('data-automation-id'),
            multiple: e.multiple
        }))''')
        print("File inputs:", json.dumps(file_inputs, indent=2), flush=True)
        
        # Dump Add buttons
        add_buttons = page.eval_on_selector_all('button', '''els => els.map(e => ({
            text: e.innerText ? e.innerText.trim() : null,
            automationId: e.getAttribute('data-automation-id'),
            id: e.id
        })).filter(b => b.text && b.text.toLowerCase().includes('add'))''')
        print("Add buttons:", json.dumps(add_buttons, indent=2), flush=True)
        
        # Dump all sections
        sections = page.eval_on_selector_all('h3, h4, fieldset legend, div[data-automation-id]', '''els => els.map(e => ({
            tag: e.tagName,
            text: e.innerText ? e.innerText.trim().slice(0, 50) : null,
            automationId: e.getAttribute('data-automation-id')
        })).filter(s => s.automationId && s.automationId.includes('Section'))''')
        print("Sections:", json.dumps(sections, indent=2), flush=True)

        browser.close()

if __name__ == "__main__":
    run()
