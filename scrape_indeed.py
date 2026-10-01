from playwright.sync_api import sync_playwright
import time

def scrape_indeed():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.indeed.com/viewjob?jk=f206531b99e04e1a", wait_until="networkidle")
        time.sleep(3)
        print(page.inner_text("body"))
        browser.close()

if __name__ == "__main__":
    scrape_indeed()
