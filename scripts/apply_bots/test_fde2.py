import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://fdepulse.com/jobs/fullstack-forward-deployed-ai-engineer-python-remote-latin-america-7d38f4/')
        
        # Check links that say Apply
        apply_buttons = await page.locator("a", has_text="Apply").all()
        for btn in apply_buttons:
            href = await btn.get_attribute("href")
            target = await btn.get_attribute("target")
            print(f"Apply link found: href={href}, target={target}")
            
        await browser.close()

asyncio.run(main())
