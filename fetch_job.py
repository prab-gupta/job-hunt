import urllib.request
import re
req = urllib.request.Request('https://fdepulse.com/jobs/cresta-senior-forward-deployed-engineer-ai-agent-germany-25e9e8/', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
from html.parser import HTMLParser
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)
s = MLStripper()
s.feed(html)
text = s.get_data()
text = re.sub(r'\n\s*\n', '\n', text)
with open('job_desc.txt', 'w') as f:
    f.write(text)
