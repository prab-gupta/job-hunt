import urllib.request
import re
from bs4 import BeautifulSoup
import sys

url = "https://www.linkedin.com/jobs/view/forward-deployed-engineer-at-domino-data-lab-4470713537"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    desc = soup.find('div', class_='description__text')
    if desc:
        print(desc.get_text(separator='\n', strip=True))
    else:
        print("Could not find description text. Full text:")
        print(soup.get_text(separator='\n', strip=True)[:3000])
except Exception as e:
    print(f"Error: {e}")
