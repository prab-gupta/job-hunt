import urllib.request
from bs4 import BeautifulSoup

url = "https://fdepulse.com/jobs/fullstack-forward-deployed-ai-engineer-python-remote-usa-7e37de/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.get_text(separator='\n', strip=True))
except Exception as e:
    print(f"Error: {e}")
