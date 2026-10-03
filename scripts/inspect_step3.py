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
        context = browser.new_context(viewport={"width": 1280, "height": 1400})
        page = context.new_page()
        
        print("Navigating...", flush=True)
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
        
        print("Waiting after sign in...", flush=True)
        page.wait_for_timeout(6000)
        
        # Check active step and advance if needed
        for s in range(3):
            step_text = page.locator('h3').first.inner_text() if page.locator('h3').count() > 0 else ""
            print(f"Current step heading: {step_text}", flush=True)
            if "questions" in step_text.lower():
                break
            # Click Save and Continue to reach step 3
            next_btn = page.locator("button[data-automation-id='pageFooterNextButton']")
            if next_btn.count() > 0 and next_btn.is_enabled():
                print("Clicking Next to advance...", flush=True)
                next_btn.click(force=True)
                page.wait_for_timeout(5000)

        # Wait for Application Questions to hydrate
        print("Waiting for Step 3 questions to hydrate...", flush=True)
        page.wait_for_timeout(6000)
        
        page.screenshot(path="scratch/step3_questions_hydrated.png", full_page=True)
        
        # Dump all questions and fields
        questions = page.eval_on_selector_all('fieldset, div[data-automation-id*="question"], div[data-automation-id*="formField"]', '''els => els.map(e => ({
            id: e.id,
            automationId: e.getAttribute('data-automation-id'),
            text: e.innerText ? e.innerText.trim() : null
        })).filter(q => q.text)''')
        print(f"Questions/Form fields count: {len(questions)}", flush=True)
        for i, q in enumerate(questions):
            print(f"--- Question {i+1} ---:\n{q['text'][:200]}\n")
            
        # Check inputs / radios / dropdowns
        inputs = page.eval_on_selector_all('input, textarea, button[aria-haspopup="listbox"]', '''els => els.map(e => ({
            tag: e.tagName,
            type: e.type,
            id: e.id,
            name: e.name,
            automationId: e.getAttribute('data-automation-id'),
            ariaLabel: e.getAttribute('aria-label'),
            text: e.innerText ? e.innerText.trim() : null
        }))''')
        print(f"Interactive inputs count on Step 3: {len(inputs)}", flush=True)
        print("Inputs summary:\n", json.dumps(inputs[:20], indent=2), flush=True)

        browser.close()

if __name__ == "__main__":
    run()
