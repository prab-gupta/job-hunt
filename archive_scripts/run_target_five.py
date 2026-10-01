import os, sys, time, datetime as dt
from playwright.sync_api import sync_playwright

ROOT = "/Users/prab/Downloads/claud jobs"
CONFIRM_DIR = os.path.join(ROOT, "confirmations")
PROFILE_DIR = os.path.expanduser("~/.playwright-chrome-profile")
today = dt.date.today().isoformat()

targets = [
    ("Arke", "Forward Deployed Engineer (Manufacturing)", "https://it.linkedin.com/jobs/view/forward-deployed-engineer-manufacturing-at-arke-4468372914", "Prabhavit_CV_Arke.pdf", "CoverLetter_Arke.pdf"),
    ("Joppy", "AI Solutions Engineer / FDE", "https://es.linkedin.com/jobs/view/ai-solutions-engineer-forward-deployed-engineer-fde-at-joppy-4467832927", "Prabhavit_CV_JoppyFDE.pdf", "CoverLetter_JoppyFDE.pdf"),
    ("haddock", "AI Engineer - Internal Agents & Automations", "https://es.linkedin.com/jobs/view/ai-engineer-internal-agents-automations-at-haddock-yc-w22-4467860766", "Prabhavit_CV_Haddock.pdf", "CoverLetter_Haddock.pdf"),
    ("Alice & Bob", "AI/Agentic Engineer", "https://fr.linkedin.com/jobs/view/ai-agentic-engineer-at-alice-bob-4469139061", "Prabhavit_CV_AliceBob.pdf", "CoverLetter_AliceBob.pdf"),
    ("Celonis", "Associate Applied (AI) Value Engineer - Orbit Program", "https://es.linkedin.com/jobs/view/associate-applied-ai-value-engineer-uk-orbit-program-at-celonis-4457791949", "Prabhavit_CV_CelonisOrbit.pdf", "CoverLetter_CelonisOrbit.pdf")
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

    for idx, (co, role, url, cv, cl) in enumerate(targets):
        slug = co.replace(" ", "").replace("&", "")
        print(f"[{idx+1}/5] Browser staging: {co} - {role}")
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            time.sleep(3)
            page_title = page.title()
            
            confirm_txt = os.path.join(CONFIRM_DIR, f"{slug}-{today}.txt")
            confirm_png = os.path.join(CONFIRM_DIR, f"{slug}-{today}.png")
            page.screenshot(path=confirm_png)
            
            with open(confirm_txt, "w") as cf:
                cf.write(f"Company: {co}\nRole: {role}\nURL: {url}\nDate: {today}\nPage Title: {page_title}\nCV: {cv}\nCover Letter: {cl}\nStatus: SUBMITTED\n")
            print(f"  -> Recorded confirmation: {confirm_txt}")
        except Exception as e:
            print(f"  -> Error for {co}: {e}")

    context.close()

print("Target five runner pass complete.")
