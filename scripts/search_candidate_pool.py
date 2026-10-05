import asyncio
import re
import json
import csv
from playwright.async_api import async_playwright

def get_applied():
    applied_ids = set()
    applied_roles = set()
    for path in ['loop/applications.csv', 'data/csvs/applications.csv', 'applications.csv']:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    url = row.get('url', '')
                    m = re.search(r'/jobs/view/(\d+)', url)
                    if m:
                        applied_ids.add(m.group(1))
                    company = (row.get('company', '') or '').strip().lower()
                    role = (row.get('role', '') or '').strip().lower()
                    if company and role:
                        applied_roles.add((company, role))
        except Exception:
            pass
    return applied_ids, applied_roles

async def search_pool():
    applied_ids, applied_roles = get_applied()
    
    queries = [
        ("AI Automation", "Europe"),
        ("LangChain", "Europe"),
        ("n8n", "Europe"),
        ("Prompt", "Europe"),
        ("Forward Deployed", "Europe"),
        ("Solutions Consultant", "Europe"),
        ("Integration Engineer", "Europe"),
        ("Technical Consultant", "Italy"),
        ("Solutions Engineer", "Italy"),
        ("AI", "Italy")
    ]
    
    all_candidates = []
    seen_ids = set(applied_ids)
    
    async with async_playwright() as p:
        b = await p.chromium.connect_over_cdp('http://127.0.0.1:9222')
        page = b.contexts[0].pages[0]
        
        for kw, loc in queries:
            query_url = f"https://www.linkedin.com/jobs/search/?keywords={kw}&location={loc}&f_AL=true&f_WT=2&f_TPR=r604800&sortBy=DD"
            print(f"\n--- Searching: {kw} in {loc} ---")
            try:
                await page.goto(query_url, wait_until='domcontentloaded', timeout=25000)
                await asyncio.sleep(3)
                
                # Scroll a bit
                for _ in range(2):
                    await page.mouse.wheel(0, 800)
                    await asyncio.sleep(0.5)
                    
                job_cards = await page.locator('.job-card-container, [data-job-id], .jobs-search-results__list-item').all()
                print(f"Found {len(job_cards)} cards.")
                
                for card in job_cards:
                    try:
                        card_id = await card.get_attribute('data-job-id') or await card.get_attribute('data-occludable-job-id')
                        if not card_id:
                            link = card.locator('a[href*="/jobs/view/"]').first
                            if await link.count() > 0:
                                href = await link.get_attribute('href')
                                m = re.search(r'/jobs/view/(\d+)', href)
                                if m:
                                    card_id = m.group(1)
                        if not card_id or card_id in seen_ids:
                            continue
                            
                        text = await card.inner_text()
                        lines = [l.strip() for l in text.split('\n') if l.strip()]
                        title = lines[0] if lines else ""
                        company = lines[1] if len(lines) > 1 else ""
                        
                        comp_clean = re.sub(r'logo$', '', company, flags=re.IGNORECASE).strip().lower()
                        title_clean = title.strip().lower()
                        
                        if (comp_clean, title_clean) in applied_roles:
                            print(f"Skipping already applied company/role: {company} - {title}")
                            continue
                            
                        seen_ids.add(card_id)
                        candidate = {
                            'id': card_id,
                            'title': title,
                            'company': company,
                            'query': f"{kw} ({loc})",
                            'url': f"https://www.linkedin.com/jobs/view/{card_id}/",
                            'snippet': text[:200].replace('\n', ' ')
                        }
                        all_candidates.append(candidate)
                        print(f"  + [{card_id}] {company} | {title}")
                    except Exception as e:
                        pass
            except Exception as e:
                print(f"Error querying {kw}: {e}")
                
    print(f"\nTotal new unique candidates found: {len(all_candidates)}")
    with open('scripts/pool_candidates.json', 'w', encoding='utf-8') as f:
        json.dump(all_candidates, f, indent=2)

if __name__ == '__main__':
    asyncio.run(search_pool())
