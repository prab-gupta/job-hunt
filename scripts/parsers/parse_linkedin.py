import urllib.request
import re
from bs4 import BeautifulSoup
import sys
url = "https://it.linkedin.com/jobs/view/enterprise-solutions-engineer-at-verkada-4469938833"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    match = re.search(r'"description":"(.*?)","', html)
    if match:
        desc = match.group(1)
        desc = desc.replace('&lt;', '<').replace('&gt;', '>').replace('\\u003C', '<').replace('\\u003E', '>')
        soup = BeautifulSoup(desc, 'html.parser')
        print(soup.get_text('\n'))
    else:
        soup = BeautifulSoup(html, 'html.parser')
        main = soup.find('div', class_='description__text') or soup.find('div', class_='show-more-less-html__markup')
        if main:
            print(main.get_text('\n'))
        else:
            print("Could not find description")
except Exception as e:
    print(e)
