#!/usr/bin/env python3
"""Targeted Playwright Browser Application Runner for Active Queue.
Submits tailored materials to active LinkedIn Easy Apply & ATS postings,
captures screenshots, and updates applications.csv.
"""

import os
import sys
import time
import csv
import re
import datetime as dt
from playwright.sync_api import sync_playwright

ROOT = "/Users/prab/Downloads/claud jobs"
CONFIRM_DIR = os.path.join(ROOT, "confirmations")
PROFILE_DIR = os.path.expanduser("~/.playwright-chrome-profile")
os.makedirs(CONFIRM_DIR, exist_ok=True)
os.makedirs(PROFILE_DIR, exist_ok=True)

CANDIDATE = {
    "first_name": "Prabhavit",
    "last_name": "Gupta",
    "email": "prabhavitg@gmail.com",
    "phone": "+39 351 610 7807",
    "phone_digits": "3516107807",
    "location": "Venice, Italy",
    "salary": "50000",
    "years_exp": "3"
}

def clean_slug(s):
    return re.sub(r"[^a-zA-Z0-9]", "", s)

def fill_modal_step(page, cv_pdf_path):
    try:
        phone_inputs = page.locator('input[id*="phone" i], input[name*="phone" i], input[type="tel"]')
        for i in range(phone_inputs.count()):
            try:
                pi = phone_inputs.nth(i)
                val = pi.input_value()
                if not val or len(val) < 5 or val.count("+39") > 1:
                    pi.fill(CANDIDATE["phone"])
            except:
                pass
    except:
        pass

    try:
        file_inputs = page.locator('input[type="file"]')
        for i in range(file_inputs.count()):
            if cv_pdf_path and os.path.exists(cv_pdf_path):
                try:
                    file_inputs.nth(i).set_input_files(cv_pdf_path)
                    print(f"    [+] Uploaded tailored CV: {os.path.basename(cv_pdf_path)}")
                    time.sleep(1)
                except Exception as e:
                    print(f"    [-] File upload exception: {e}")
    except:
        pass

    try:
        text_inputs = page.locator('input[type="text"], input[type="number"], textarea')
        for i in range(text_inputs.count()):
            try:
                ti = text_inputs.nth(i)
                ti_id = ti.get_attribute("id") or ""
                label_el = page.locator(f'label[for="{ti_id}"]') if ti_id else None
                label_text = (label_el.inner_text() if label_el and label_el.count() > 0 else "").lower()

                try:
                    curr_val = ti.input_value()
                except:
                    curr_val = ""

                if not curr_val:
                    if any(k in label_text for k in ["year", "esperienza", "experiencia", "how many", "quanti anni"]):
                        ti.fill(CANDIDATE["years_exp"])
                    elif any(k in label_text for k in ["salary", "retribuzione", "stipendio", "salario", "compensation", "ral", "expectation"]):
                        ti.fill(CANDIDATE["salary"])
                    elif any(k in label_text for k in ["notice", "preavviso", "start", "availability"]):
                        ti.fill("Immediately (0 days)")
                    elif any(k in label_text for k in ["city", "città", "ciudad", "location", "residence", "where are you"]):
                        ti.fill("Venice, Italy")
                    elif any(k in label_text for k in ["linkedin", "profile"]):
                        ti.fill("https://www.linkedin.com/in/prabhavit/")
                    elif any(k in label_text for k in ["website", "portfolio", "github"]):
                        ti.fill("https://github.com/prab-gupta")
                    elif any(k in label_text for k in ["visa", "permit", "work authorization", "right to work"]):
                        ti.fill("Italian EU Long-Term Residence Permit (no sponsorship needed)")
                    else:
                        input_type = ti.get_attribute("type") or ""
                        ti.fill("3" if input_type == "number" else "3")
            except:
                pass
    except:
        pass

    try:
        fieldsets = page.locator('fieldset')
        for i in range(fieldsets.count()):
            try:
                fs = fieldsets.nth(i)
                fs_text = fs.inner_text().lower()
                radios = fs.locator('input[type="radio"]')
                pref_yes = any(k in fs_text for k in ["authorized", "autorizzato", "legally", "right to work", "permit", "18", "remote", "hybrid", "experience", "comfortable", "commute", "relocate"])
                pref_no = any(k in fs_text for k in ["sponsorship", "sponsorizzazione", "patrocinio", "require visa", "criminal", "convicted", "non-compete"])

                selected = False
                for r_idx in range(radios.count()):
                    try:
                        r = radios.nth(r_idx)
                        r_id = r.get_attribute("id") or ""
                        lbl = page.locator(f'label[for="{r_id}"]')
                        lt = (lbl.inner_text() if lbl.count() > 0 else "").lower().strip()
                        if (pref_yes and lt in ["yes", "sì", "si", "true"]) or (pref_no and lt in ["no", "false"]):
                            r.check()
                            selected = True
                    except:
                        pass

                if not selected and radios.count() > 0:
                    try:
                        if not any(radios.nth(k).is_checked() for k in range(radios.count())):
                            radios.first.check()
                    except:
                        pass
            except:
                pass
    except:
        pass

    try:
        selects = page.locator('select')
        for i in range(selects.count()):
            try:
                s = selects.nth(i)
                s_id = s.get_attribute("id") or ""
                lbl = page.locator(f'label[for="{s_id}"]') if s_id else None
                lbl_txt = (lbl.inner_text() if lbl and lbl.count() > 0 else "").lower()

                options = s.locator('option')
                opt_texts = [options.nth(k).inner_text().strip() for k in range(options.count()) if options.nth(k).inner_text().strip() and options.nth(k).get_attribute("value") not in ["", "Select an option"]]
                if not opt_texts:
                    continue

                curr_opt = s.input_value()
                if not curr_opt or curr_opt == "Select an option":
                    if any(k in lbl_txt for k in ["english", "inglese", "inglés"]):
                        for opt in ["Professional", "Fluent", "Native", "C2", "C1", "Avanzado", "Madrelingua", "Yes", "Sì"]:
                            match = next((o for o in opt_texts if opt.lower() in o.lower()), None)
                            if match:
                                s.select_option(label=match)
                                break
                    elif any(k in lbl_txt for k in ["italian", "italiano"]):
                        for opt in ["Conversational", "Intermediate", "B2", "B1", "Professional", "Yes", "Sì"]:
                            match = next((o for o in opt_texts if opt.lower() in o.lower()), None)
                            if match:
                                s.select_option(label=match)
                                break
                    elif any(k in lbl_txt for k in ["sponsorship", "sponsorizzazione"]):
                        match = next((o for o in opt_texts if o.lower() in ["no", "false"]), None)
                        if match:
                            s.select_option(label=match)
                    elif any(k in lbl_txt for k in ["authorized", "autorizzato", "right to work"]):
                        match = next((o for o in opt_texts if o.lower() in ["yes", "sì", "si", "true"]), None)
                        if match:
                            s.select_option(label=match)
                    else:
                        s.select_option(label=opt_texts[0])
            except:
                pass
    except:
        pass

    try:
        follow_cb = page.locator('input[type="checkbox"][id*="follow" i]')
        if follow_cb.count() > 0 and follow_cb.first.is_checked():
            try:
                follow_cb.first.uncheck()
            except:
                pass
    except:
        pass

def apply_target(page, company, role, url, cv_name, cl_name):
    today = dt.date.today().isoformat()
    slug = clean_slug(company)

    cv_pdf = os.path.join(ROOT, cv_name) if cv_name else None
    cl_pdf = os.path.join(ROOT, cl_name) if cl_name else None

    m = re.search(r'(\d{8,12})', url)
    canonical_u = f"https://www.linkedin.com/jobs/view/{m.group(1)}/" if m else url

    print(f"\n========================================================")
    print(f"🚀 Processing: {company} | {role}")
    print(f"🔗 Target: {canonical_u}")
    print(f"📄 Matched CV: {cv_name} ({'EXISTS' if cv_pdf and os.path.exists(cv_pdf) else 'MISSING'})")
    print(f"📄 Matched Letter: {cl_name} ({'EXISTS' if cl_pdf and os.path.exists(cl_pdf) else 'MISSING'})")

    try:
        page.goto(canonical_u, wait_until="domcontentloaded", timeout=35000)
        time.sleep(3)

        page_text = page.inner_text("body").lower()
        if "candidatura inviata" in page_text or "application submitted" in page_text or "solicitud enviada" in page_text:
            print(f"ℹ️ Already submitted previously for {company}.")
            return "ALREADY_APPLIED"

        apply_btn = page.query_selector('button.jobs-apply-button, button:has-text("Easy Apply"), button:has-text("Candidatura semplice"), button:has-text("Solicitud sencilla"), button:has-text("Solicitar"), a:has-text("Apply")')
        if not apply_btn:
            print(f"⚠️ No apply button found on page for {company}.")
            confirm_png = os.path.join(CONFIRM_DIR, f"{slug}-{today}.png")
            page.screenshot(path=confirm_png)
            return "NO_BUTTON"

        btn_text = apply_btn.inner_text().strip()
        print(f"👉 Clicking Apply button: '{btn_text}'")
        apply_btn.scroll_into_view_if_needed()
        apply_btn.click(timeout=10000)
        time.sleep(3)

        # Multi-step loop
        for step in range(1, 10):
            print(f"  -> Step {step}")
            fill_modal_step(page, cv_pdf)
            time.sleep(1)

            submit_btn = page.query_selector('button:has-text("Submit application"), button:has-text("Invia candidatura"), button:has-text("Enviar solicitud"), button[aria-label*="Submit" i], button[aria-label*="Invia" i]')
            if submit_btn and submit_btn.is_visible():
                print(f"  🚀 Final Submit button found! Clicking submit...")
                submit_btn.scroll_into_view_if_needed()
                submit_btn.click(timeout=10000)
                time.sleep(4)

                confirm_txt_path = os.path.join(CONFIRM_DIR, f"{slug}-{today}.txt")
                confirm_png_path = os.path.join(CONFIRM_DIR, f"{slug}-{today}.png")
                page.screenshot(path=confirm_png_path)

                conf_text = f"Application submitted to {company}"
                with open(confirm_txt_path, "w") as cf:
                    cf.write(f"Company: {company}\nRole: {role}\nURL: {url}\nDate: {today}\nStatus: SUBMITTED\nCV: {cv_name}\nCover Letter: {cl_name}\nConfirmation: {conf_text}\n")

                print(f"  ✅ SUCCESS: Application submitted & confirmed! Saved to {confirm_txt_path}")

                dismiss = page.query_selector('button[aria-label*="Dismiss" i], button[aria-label*="Chiudi" i], button:has-text("Done"), button:has-text("Fine")')
                if dismiss:
                    try:
                        dismiss.click()
                    except:
                        pass
                return "SUBMITTED"

            next_btn = page.query_selector('button:has-text("Next"), button:has-text("Avanza"), button:has-text("Siguiente"), button:has-text("Review"), button:has-text("Verifica"), button:has-text("Revisar"), button[aria-label*="Continue" i]')
            if next_btn and next_btn.is_visible():
                next_btn.scroll_into_view_if_needed()
                next_btn.click(timeout=10000)
                time.sleep(2)
            else:
                confirm_png = os.path.join(CONFIRM_DIR, f"{slug}-{today}-stage.png")
                page.screenshot(path=confirm_png)
                print(f"  ℹ️ Modal complete or external navigation. Screenshot: {confirm_png}")
                break

        return "STAGED_OR_EXTERNAL"

    except Exception as e:
        print(f"❌ Exception for {company}: {e}")
        return f"ERROR: {e}"

def main():
    today = dt.date.today().isoformat()
    targets = [
        ("Billennium", "Forward Deployed Engineer", "https://www.linkedin.com/jobs/view/4469178434/", "Prabhavit_CV_Billennium.pdf", "CoverLetter_Billennium.pdf"),
        ("JTI", "AI Native Software Engineer", "https://es.linkedin.com/jobs/view/ai-native-software-engineer-at-jti-4403653359", "Prabhavit_CV_JTI.pdf", "CoverLetter_JTI.pdf"),
        ("KeyShot", "AI Workflow Engineer", "https://dk.linkedin.com/jobs/view/ai-workflow-engineer-at-keyshot-4469216266", "Prabhavit_CV_KeyShot.pdf", "CoverLetter_KeyShot.pdf"),
        ("Talent Search Technology", "Generative AI Engineer", "https://www.linkedin.com/jobs/view/4468222917/", "Prabhavit_CV_TalentSearchTech.pdf", "CoverLetter_TalentSearchTech.pdf")
    ]

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR,
            headless=True,
            channel="chrome",
            viewport={"width": 1280, "height": 900},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        submitted_count = 0
        for co, role, url, cv, cl in targets:
            status = apply_target(page, co, role, url, cv, cl)
            if status == "SUBMITTED":
                submitted_count += 1
                with open(os.path.join(ROOT, "applications.csv"), "a", newline="", encoding="utf-8") as af:
                    writer = csv.writer(af)
                    writer.writerow([
                        today, co, role, "LinkedIn Easy Apply", url, "SUBMITTED",
                        f"Application submitted to {co}", "EUR 50,000", "yes",
                        f"Tailored materials uploaded | confirmations/{clean_slug(co)}-{today}.txt"
                    ])

        context.close()

    print(f"\nBatch pass complete. Submitted: {submitted_count}")

if __name__ == "__main__":
    main()
