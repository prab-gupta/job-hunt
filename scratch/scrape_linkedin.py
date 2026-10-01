import urllib.request
from bs4 import BeautifulSoup
import sys

url = "https://it.linkedin.com/jobs/view/forward-deployed-engineer-software-engineer-italy-at-elevenlabs-4451481181"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
try:
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    desc = soup.find('div', class_='description__text')
    if desc:
        print(desc.get_text(separator='\n').strip())
    else:
        print("Description not found")
except Exception as e:
    print(e)
