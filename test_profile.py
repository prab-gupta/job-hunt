from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="/Users/prab/Library/Application Support/Google/Chrome",
            headless=False
        )
        print("Success")
        browser.close()
    except Exception as e:
        print("Error:", e)
