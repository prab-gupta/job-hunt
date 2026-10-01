from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.indeed.com/viewjob?jk=57a989d5172b4fa5")
    page.wait_for_timeout(2000)
    print("Indeed URL:", page.url)
    btn = page.locator("button:has-text('Apply now')")
    if btn.count() > 0:
        print("Indeed Easy Apply detected")
    else:
        btn_company = page.locator("button:has-text('Apply on company site')")
        if btn_company.count() > 0:
            print("Apply on company site detected")
        else:
            print("Apply button not found on indeed")
    browser.close()
