from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.indeed.com/viewjob?jk=9ee98300583e3da4")
    print(page.title())
    if "Cloudflare" in page.title() or "Security" in page.title() or "Just a moment" in page.title():
        print("Blocked by Cloudflare/Captcha")
    elif "Log In" in page.content() or "Sign In" in page.content():
        print("Login required")
    else:
        print("Page loaded")
    browser.close()
