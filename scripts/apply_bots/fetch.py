import urllib.request
from bs4 import BeautifulSoup
req = urllib.request.Request("https://fdepulse.com/jobs/braintrust-ai-solutions-delivery-lead-forward-deployed-engineer-us-remote-014193/", headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req).read().decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')
print(soup.get_text(separator=' ', strip=True))
