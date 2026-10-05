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

async def find_jobs(keyword, location="European Union", count=10):
    applied = get_applied_ids()
    print(f"Loaded {len(applied)} applied targets.")
    
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp('http://127.0.0.1:9222')
        context = browser.contexts[0]
        page = context.pages[0]
        
        # Remote & Easy Apply & Past week & Sort by DD (most recent)
        # f_WT=2 is Remote, f_AL=true is Easy Apply
        query_url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}&location={location}&f_AL=true&f_WT=2&f_TPR=r604800&sortBy=DD"
        print(f"Navigating to {query_url}...")
        await page.goto(query_url, wait_until='domcontentloaded', timeout=30000)
        await asyncio.sleep(4)
        
        # Scroll down to load jobs
        for _ in range(3):
            await page.mouse.wheel(0, 1000)
            await asyncio.sleep(1)
            
        job_cards = await page.locator('.job-card-container, [data-job-id], .jobs-search-results__list-item').all()
        print(f"Found {len(job_cards)} job elements.")
        
        candidates = []
        for card in job_cards:
            try:
                card_id = await card.get_attribute('data-job-id') or await card.get_attribute('data-occludable-job-id')
                if not card_id:
                    # try link
                    link = card.locator('a[href*="/jobs/view/"]').first
                    if await link.count() > 0:
                        href = await link.get_attribute('href')
                        m = re.search(r'/jobs/view/(\d+)', href)
                        if m:
                            card_id = m.group(1)
                
                if not card_id or card_id in applied:
                    continue
                
                text = await card.inner_text()
                lines = [l.strip() for l in text.split('\n') if l.strip()]
                title = lines[0] if lines else ""
                company = lines[1] if len(lines) > 1 else ""
                
                candidates.append({
                    'id': card_id,
                    'title': title,
                    'company': company,
                    'url': f"https://www.linkedin.com/jobs/view/{card_id}/",
                    'snippet': text[:150].replace('\n', ' ')
                })
            except Exception as e:
                pass
                
        # Deduplicate
        seen = set()
        unique = []
        for c in candidates:
            if c['id'] not in seen and c['id'] not in applied:
                seen.add(c['id'])
                unique.append(c)
                
        print(f"Unique unapplied candidates: {len(unique)}")
        for c in unique[:count]:
            print(f"- [{c['id']}] {c['company']} | {c['title']} ({c['url']})")
            
        with open('scripts/live_candidates.json', 'w', encoding='utf-8') as f:
            json.dump(unique, f, indent=2)

if __name__ == '__main__':
    import sys
    kw = sys.argv[1] if len(sys.argv) > 1 else "AI Engineer"
    loc = sys.argv[2] if len(sys.argv) > 2 else "European Union"
    asyncio.run(find_jobs(kw, loc))
