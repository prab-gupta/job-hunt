from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.indeed.com/viewjob?jk=57a989d5172b4fa5")
    page.wait_for_timeout(2000)
    print(page.evaluate("document.body.innerText")[:1000])
    browser.close()
