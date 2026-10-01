import urllib.request
from bs4 import BeautifulSoup
import sys

url = sys.argv[1]
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Try to find the job description container
    jd = soup.find('div', {'class': 'description__text'})
    if not jd:
        jd = soup.find('div', {'class': 'show-more-less-html__markup'})
    
    if jd:
        print(jd.get_text(separator='\n', strip=True))
    else:
        print("Could not find job description div. Falling back to body text:")
        print(soup.body.get_text(separator='\n', strip=True)[:1000])
except Exception as e:
    print(f"Error: {e}")
