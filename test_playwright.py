from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    default_context = browser.contexts[0]
    page = default_context.pages[0] if default_context.pages else default_context.new_page()
    print("Connected to:", page.title())
