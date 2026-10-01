from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Use real chrome and user profile to bypass cloudflare
    browser = p.chromium.launch_persistent_context(
        user_data_dir="/tmp/playwright_chrome_profile",
        channel="chrome",
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )
    page = browser.new_page()
    page.goto("https://www.indeed.com/viewjob?jk=57a989d5172b4fa5")
    page.wait_for_timeout(3000)
    print("Title:", page.title())
    print("URL:", page.url)
    try:
        btn = page.locator("a:has-text('Apply on company site'), button:has-text('Apply on company site'), a:has-text('Apply'), button:has-text('Apply')")
        if btn.count() > 0:
            print("Apply button text:", btn.first.text_content())
            print("Apply button href:", btn.first.get_attribute("href"))
        else:
            print("No Apply button found")
    except Exception as e:
        print("Error:", e)
    browser.close()
