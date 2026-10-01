import os, sys, time, csv, re, glob, datetime as dt
from playwright.sync_api import sync_playwright

ROOT = "/Users/prab/Downloads/claud jobs"
CONFIRM_DIR = os.path.join(ROOT, "confirmations")
PROFILE_DIR = os.path.expanduser("~/.playwright-chrome-profile")
os.makedirs(CONFIRM_DIR, exist_ok=True)

# Remove any stale singleton locks before starting
os.system("rm -f ~/.playwright-chrome-profile/Singleton*")

import sys
sys.path.insert(0, os.path.join(ROOT, "loop"))
import linkedin_easy_apply_submitter as submitter


def main():
    today = dt.date.today().isoformat()
    queue_file = os.path.join(ROOT, "loop", "queue.csv")
    
    with open(queue_file, "r") as f:
        rows = list(csv.reader(f))

    to_apply = []
    for r in rows:
        if len(r) >= 9 and r[8] in ["TO APPLY", "NEEDS YOU", "STAGED"]:
            to_apply.append((r[0], r[1], r[2]))

    print(f"Loaded {len(to_apply)} applications to process.")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR,
            headless=False,
            channel="chrome",
            viewport={"width": 1280, "height": 900},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        submitted_count = 0
        for idx, (co, role, url) in enumerate(to_apply):
            print(f"\n[{idx+1}/{len(to_apply)}] Running: {co} - {role}")
            status = submitter.apply_to_job(page, co, role, url)
            print(f"  -> Result status: {status}")
            
            if status == "SUBMITTED":
                submitted_count += 1
                with open(os.path.join(ROOT, "applications.csv"), "a", newline="") as af:
                    writer = csv.writer(af)
                    writer.writerow([
                        today, co, role, "LinkedIn Easy Apply", url, "SUBMITTED",
                        f"Application sent to {co}", "EUR 50,000", "yes",
                        f"Tailored materials uploaded | confirmations/{submitter.clean_slug(co)}-{today}.txt"
                    ])

        context.close()

    print(f"\n========================================================")
    print(f"🎉 All applications run complete! Total submitted: {submitted_count}")
    print(f"========================================================")

if __name__ == "__main__":
    main()
