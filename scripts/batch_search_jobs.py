import asyncio
import re
import json
import csv
from playwright.async_api import async_playwright

def get_applied_ids():
    applied = set()
    for path in ['loop/applications.csv', 'data/csvs/applications.csv', 'applications.csv']:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    url = row.get('url', '')
                    m = re.search(r'/jobs/view/(\d+)', url)
                    if m:
                        applied.add(m.group(1))
                    applied.add(url.strip())
        except Exception:
            pass
    return applied

QUERIES = [
    ("Solutions Engineer", "European Union"),
    ("Integration Engineer", "European Union"),
    ("Forward Deployed Engineer", "European Union"),
    ("Python Developer", "European Union"),
    ("Generative AI", "European Union"),
    ("AI Automation", "European Union"),
    ("Full Stack Engineer", "Italy"),
    ("Software Engineer", "Italy"),
    ("AI Engineer", "Italy")
]

async def collect_all():
    applied = get_applied_ids()
    print(f"Loaded {len(applied)} applied targets.")
    
    candidates = {}
    
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp('http://127.0.0.1:9222')
        page = browser.contexts[0].pages[0]
        
        for kw, loc in QUERIES:
            query_url = f"https://www.linkedin.com/jobs/search/?keywords={kw}&location={loc}&f_AL=true&f_WT=2&f_TPR=r604800&sortBy=DD"
            print(f"Searching: {kw} in {loc}...")
            try:
                await page.goto(query_url, wait_until='domcontentloaded', timeout=25000)
                await asyncio.sleep(3)
                
                for _ in range(2):
                    await page.mouse.wheel(0, 1000)
                    await asyncio.sleep(0.8)
                    
                cards = await page.locator('.job-card-container, [data-job-id], .jobs-search-results__list-item').all()
                print(f"  Found {len(cards)} cards.")
                
                for card in cards:
                    try:
                        cid = await card.get_attribute('data-job-id') or await card.get_attribute('data-occludable-job-id')
                        if not cid:
                            link = card.locator('a[href*="/jobs/view/"]').first
                            if await link.count() > 0:
                                href = await link.get_attribute('href')
                                m = re.search(r'/jobs/view/(\d+)', href)
                                if m:
                                    cid = m.group(1)
                        if not cid or cid in applied or cid in candidates:
                            continue
                            
                        text = await card.inner_text()
                        lines = [l.strip() for l in text.split('\n') if l.strip()]
                        title = lines[0] if lines else ""
                        company = lines[1] if len(lines) > 1 else ""
                        candidates[cid] = {
                            'id': cid,
                            'title': title,
                            'company': company,
                            'url': f"https://www.linkedin.com/jobs/view/{cid}/",
                            'query': f"{kw} - {loc}"
                        }
                    except Exception:
                        pass
            except Exception as e:
                print(f"  Error on {kw}: {e}")
                
        print(f"\nTotal unique unapplied candidates found: {len(candidates)}")
        with open('scripts/all_unapplied_candidates.json', 'w', encoding='utf-8') as f:
            json.dump(list(candidates.values()), f, indent=2)

if __name__ == '__main__':
    asyncio.run(collect_all())
