from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://fdepulse.com/jobs/sinch-senior-forward-deployed-engineer-333e7a/")
    print("Page title:", page.title())
    apply_btn = page.locator("a:has-text('Apply')")
    if apply_btn.count() > 0:
        href = apply_btn.first.get_attribute("href")
        print("Apply link:", href)
    else:
        print("Apply button not found")
    browser.close()
