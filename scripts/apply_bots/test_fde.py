import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://fdepulse.com/jobs/fullstack-forward-deployed-ai-engineer-python-remote-latin-america-7d38f4/')
        print(f"Title: {await page.title()}")
        print(f"URL: {page.url}")
        
        # Look for Apply button
        apply_button = page.locator("text=Apply").first
        if await apply_button.count() > 0:
            print("Found Apply button")
            
            async with page.expect_navigation():
                await apply_button.click()
            
            print(f"New URL: {page.url}")
        else:
            print("No Apply button found")
            print(await page.content())
        await browser.close()

asyncio.run(main())
