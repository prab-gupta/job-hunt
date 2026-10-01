import urllib.request
import json
from bs4 import BeautifulSoup
import re

url = "https://www.linkedin.com/jobs/view/4416694774/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    desc = soup.find('div', {'class': 'show-more-less-html__markup'})
    if not desc:
        desc = soup.find('div', {'class': 'description__text'})
    if desc:
        print(desc.get_text(separator='\n', strip=True))
    else:
        print("Could not find description. Body length:", len(html))
except Exception as e:
    print("Error:", e)
