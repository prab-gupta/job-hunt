from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.indeed.com/viewjob?jk=9ee98300583e3da4")
    print("Title:", page.title())
    browser.close()
