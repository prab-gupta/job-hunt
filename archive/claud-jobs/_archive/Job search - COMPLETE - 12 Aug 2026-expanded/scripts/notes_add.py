import openpyxl
from openpyxl.styles import Font, Alignment

wb = openpyxl.load_workbook('Role shortlist - 8 Aug 2026.xlsx')
ws = wb['Search notes']

r = ws.max_row + 3
def head(t):
    global r
    c = ws.cell(row=r, column=1, value=t)
    c.font = Font(bold=True, size=12)
    r += 1
def line(a, b=None):
    global r
    ws.cell(row=r, column=1, value=a).alignment = Alignment(vertical='top')
    if b is not None:
        c = ws.cell(row=r, column=2, value=b)
        c.alignment = Alignment(vertical='top', wrap_text=True)
    r += 1

head('DEEP DIVE - 12 August 2026 (evening)')
line('Brief', 'You asked for a deep dive to find genuinely new roles. Two parallel sweeps: one on AI/automation/applied-AI across the EU and remote-Europe, one on forward-deployed / solutions / implementation / GTM across the EU and UK.')
line('Raw candidates', 'Roughly 90 postings opened across both sweeps.')
line('Returned as verified by the sweeps', 28)
line('Actually live when I opened them', 19)
line('Applied to today', 12)
line('Dead on arrival', '9 (Novosafe, Arize FDE EMEA, Zeotap, Qdrant, Space Inch, Quadrivia, Action1, plus Mistral and Reasonable AI carried over)')
r += 1

head('THE MOST IMPORTANT THING I LEARNED TODAY')
line('Aggregator mirrors are not verification.',
     'Three roles were verified by the sweep only through RemoteRocketship mirrors rather than the ATS page itself: Space Inch, Action1 and Quadrivia. All three were dead when I opened the real page. A fourth, Novosafe, had metadata claiming it was updated on 12 August and the live page said "archived 6 months ago". Rule going forward: nothing goes in this sheet unless the actual ATS page loaded in a browser.')
r += 1

head('WHAT THE MARKET LOOKS LIKE FROM THIS SWEEP')
line('Pay, where it was disclosed',
     'Reedsy EUR 70-120k (remote Europe). Avery EUR 42-60k/yr (Amsterdam). Spyrosoft PLN 110-150/hr, roughly EUR 25-35/hr. Teleport GBP 72-93k (London). Space Inch was quoting EUR 5,100-6,800/month before it closed. Your stated EUR 30-40k is BELOW almost every disclosed band in this sweep. At Avery you asked for less than their published floor. That is a real cost and it is the one number in this process that is entirely in your control.')
line('Which titles are actually being posted',
     'Forward Deployed Engineer is now a real, growing category in Europe rather than a US-only title - Spyrosoft, Hexa, Arize and Pigment all posted one. GTM Engineer is the other growth title. Plain "AI Engineer" postings increasingly mean prompt engineering and production integration rather than ML research, which is exactly your lane.')
line('Which titles have dried up',
     'Junior and mid Solutions Engineer roles in continental Europe are scarce and the ones that exist gate on German. Nearly every remaining "Europe remote" FDE role sits at 5+ years. The EMEA Solutions/Sales Engineer roles that do exist are London-based and want years of pre-sales you do not have.')
r += 1

head('THE THREE THINGS COSTING YOU APPLICATIONS')
line('1. No public code',
     'Still the most frequent hard blocker. It was a required field at Adaptyv, Augment and xAI. One public repo with a real n8n workflow or a small LLM integration, plus a README explaining the design decision, would unblock a whole category of forms. This has now come up on three separate sweeps.')
line('2. No German',
     'Twelve German-market roles died on fluent or native German in the last sweep. This one added more. B2 German is the single highest-leverage skill fix available to you, because Germany is where the volume of matching roles actually is.')
line('3. Your salary number',
     'EUR 30-40k reads as junior in a market where the roles you are matching disclose 42-120k. It also caps what you can be offered if they like you. Consider whether 45-55k is closer to true; I will keep writing whatever number you tell me, but you should decide it with the bands above in front of you.')
r += 1

head('WHAT NEEDS YOU, IN PRIORITY ORDER')
line('1. Capco Poland', 'One question stands between you and a submitted application on the closest cert match found: what have you ACTUALLY built in Microsoft Copilot Studio? You hold the Agent Academy and Power Automate certifications but I have no record of a shipped Copilot Studio solution, and I will not write one. Tell me and I finish the form.')
line('2. otonomee x2', 'Run a speedtest. Three fields: internet provider, download speed, upload speed. Then Ireland and Portugal are both CV-only, with no years bar at all.')
line('3. Pigment', 'Say the word and I send it. Requires a top-tier CS/engineering degree and UK sponsorship, so it is a long shot, but the title and the 2-5 year band fit you better than anything else found.')
line('4. Reasonable AI', 'Still sitting on the Cloudflare human-verification tick. Form is complete behind it.')
line('5. ElevenLabs', 'Their own application throttle refused the submission. Retry from about 19 August.')

wb.save('Role shortlist - 8 Aug 2026.xlsx')
print('search notes updated to row', r)
