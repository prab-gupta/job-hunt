import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

WB = '/home/claude/sheet/Role shortlist - 8 Aug 2026.xlsx'
wb = openpyxl.load_workbook(WB)
HDR = PatternFill('solid', fgColor='1F3864')
DUE = PatternFill('solid', fgColor='FFF2CC')
SOON= PatternFill('solid', fgColor='FFF9E6')
BLK = PatternFill('solid', fgColor='FCE4E4')
thin = Side(style='thin', color='BBBBBB'); BOX = Border(left=thin,right=thin,top=thin,bottom=thin)

name = 'Follow up'
if name in wb.sheetnames: wb.remove(wb[name])
ws = wb.create_sheet(name, 1)
ws.sheet_view.showGridLines = False

ws['A1'] = 'Follow up - every application sent, with the company LinkedIn to chase on'
ws['A1'].font = Font(bold=True, size=14, color='1F3864')
ws['A2'] = ('Rule of thumb: give it 7 working days from the send date, then message someone on the team on LinkedIn. '
            'Small companies (under ~20 people) respond to a direct message far more often than to the ATS. '
            'Where I could not verify a company LinkedIn page I left it blank rather than guess a URL.')
ws['A2'].font = Font(size=10, italic=True, color='555555')

H = ['Company','Role','Sent','Follow up from','Status','Company LinkedIn','Named contact from the posting','Notes for the message']
for i,h in enumerate(H,1):
    c=ws.cell(row=4,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=HDR; c.border=BOX

R = [
 ('Reasonable AI','Forward Deployed Engineer (FDE)','12 Aug 2026','21 Aug 2026','FILLED - YOU MUST TICK THE CAPTCHA',
  'https://uk.linkedin.com/company/reasonableai','Ferenc and Craig (named in the posting)',
  'Form is complete at apply.workable.com/reasonable/j/5F34A88D3B/apply - a Cloudflare human-check appeared and I do not touch those. Tick it and submit. The posting names Ferenc and Craig; they say outright they reward introductions and want to hear from near-misses.'),
 ('SolveAI','Forward Deployed Engineer','12 Aug 2026','21 Aug 2026','SENT',
  'https://www.linkedin.com/company/solveai','-',
  'Ex-Palantir team, GV and Accel backed. They said they want engineers making the jump into FDE - lead with that if you message.'),
 ('Seamflow','Forward Deployed Engineer','12 Aug 2026','21 Aug 2026','SENT',
  'https://www.linkedin.com/company/seamflow','-',
  'Just raised $4.5m seed (14x oversubscribed). Entrepreneur First posted about it, so the founders are active on LinkedIn right now - good moment to message.'),
 ('Zauber','Forward Deployed Engineer','12 Aug 2026','21 Aug 2026','SENT',
  'https://www.linkedin.com/company/zauber','Dennis Agidigbi (listed as the referral contact)',
  'The posting advertises a EUR 10,000 referral bonus via Dennis Agidigbi on LinkedIn. Messaging him directly is a legitimate route in.'),
 ('STRATOS Technologies','Forward Deployed Engineer','12 Aug 2026','21 Aug 2026','SENT',
  'https://uk.linkedin.com/company/stratos-technologies-ltd','-',
  'Backed by Accel, founded by ex-Fortune 500 execs. 2-4 years is your exact band and they sponsor visas - the strongest UK row you have.'),
 ('Otherworldly','Forward Deployed Engineer (f/m/x)','12 Aug 2026','21 Aug 2026','SENT',
  'https://www.linkedin.com/company/otherworldly','Thomas Klein, Recruiting Team',
  'Contact person named on the posting. Music-tech, seed round closed, small team.'),
 ('dexter health','Applied AI Developer','12 Aug 2026','21 Aug 2026','SENT',
  'https://www.linkedin.com/company/dexter-health/','Marc Margulan, CEO',
  'The CEO is the named contact on the posting and has a public LinkedIn. Tiny company - a direct note lands.'),
 ('Laioutr','AI Engineer - Full Stack','12 Aug 2026','21 Aug 2026','SENT',
  'https://de.linkedin.com/company/laioutr','Sebastian Langer, CTO & Founder',
  'CTO is the named contact. Worth telling him directly that your EU long-term residence permit needs no sponsorship - the form only let me answer a narrow yes/no.'),
 ('Atmen Solutions','Customer Solutions Engineer','12 Aug 2026','21 Aug 2026','SENT',
  'https://www.linkedin.com/company/atmen-cert/','Natacha Zouein, Recruiting Team',
  'Green-certification RegTech, active on LinkedIn (Siemens partnership posts). EUR 40-90k band.'),
 ('OMMAX','Forward Deployed AI Engineer','-','-','BLOCKED - SEND ME 2 FILES',
  'https://de.linkedin.com/company/ommax','anna.dylla@ommax.de (given on the form for upload problems)',
  'MILAN is one of their offices. Personio needs an employment reference letter and academic transcripts. If you would rather not dig those out, email anna.dylla@ommax.de directly - the form itself offers that address for document problems.'),
 ('GTM Base','Forward-Deployed CRM Architect','-','-','BLOCKED - NEEDS YOUR ANSWER',
  'https://www.linkedin.com/company/gtmbase','Taimoor Tariq, Recruiting Team',
  'They run on Claude Code and n8n; clients include Groupon and Blinkist. Blocked on a HubSpot build-design question. Give me a few lines or message Taimoor directly.'),
 ('GTM Base','Senior GTM Engineer','-','-','BLOCKED - NEEDS YOUR LOOM',
  'https://www.linkedin.com/company/gtmbase','Taimoor Tariq, Recruiting Team',
  'Needs a walkthrough video of Clay tables you built.'),
 ('Reflection','Forward Deployed Engineer - AI Engineer','12 Aug 2026','21 Aug 2026','SENT BY YOU',
  '','-','You submitted this one yourself. 3+ yrs, they sponsor visas, NY or SF on-site.'),
 ('Luma AI','Forward Deployed Engineer','8 Aug 2026','19 Aug 2026','SENT - FOLLOW UP DUE',
  'https://www.linkedin.com/company/luma-ai','-','Sent four days ago. Chase from 19 Aug.'),
 ('Camunda','AI Forward Deployed Engineer, EMEA','8 Aug 2026','19 Aug 2026','SENT - FOLLOW UP DUE',
  '','-','Note their rule: max 2 applications per 30 days, no re-apply to the same role within 60 days. Do not burn it.'),
 ('Cohere','FDE, Agentic Platform','8 Aug 2026','19 Aug 2026','SENT - FOLLOW UP DUE',
  '','-','Large company, ATS-driven. A LinkedIn message to the hiring manager is worth more than a follow-up email.'),
 ('Taktile','Forward Deployed Engineer','8 Aug 2026','19 Aug 2026','SENT - FOLLOW UP DUE',
  '','-','They have three more FDE reqs open in Berlin and London (Senior, Lead, Ops). If they reply, ask which is the best fit rather than applying to all of them.'),
]

FILL = {'SENT':SOON,'SENT BY YOU':SOON,'SENT - FOLLOW UP DUE':DUE}
r=5
for row in R:
    st = row[4]
    fill = FILL.get(st, BLK)
    for i,v in enumerate(row,1):
        c=ws.cell(row=r,column=i,value=v)
        c.alignment=Alignment(vertical='top',wrap_text=(i in (2,7,8)))
        c.border=BOX; c.fill=fill
        if i==5: c.font=Font(bold=True)
        if i==6 and v:
            c.hyperlink=v; c.value='LinkedIn'; c.font=Font(color='0563C1',underline='single')
    r+=1

r+=1
c=ws.cell(row=r,column=1,value='How to actually follow up (this is the part that moves the needle)')
c.font=Font(bold=True,size=11,color='1F3864'); r+=1
for t in [
 '1. Wait 7 working days from the send date. Chasing sooner reads as anxious and does not speed anything up.',
 '2. Message a person, not the company page. Founder or CTO at anything under 20 people; the named recruiting contact at anything bigger.',
 '3. Three sentences maximum: which role, one specific thing about what they build that you actually noticed, and one line on what you would do in the first month. No attachments, no CV re-send.',
 '4. If nothing after the follow-up, leave it. A second chase costs you more than the role is worth.',
 '5. Zauber and Reasonable AI both invite introductions or referrals in the posting itself. Those two are the ones where a direct message is not a cold approach - they asked for it.',
]:
    c=ws.cell(row=r,column=1,value=t)
    c.font=Font(size=10); c.alignment=Alignment(wrap_text=True,vertical='top')
    ws.merge_cells(start_row=r,start_column=1,end_row=r,end_column=8)
    ws.row_dimensions[r].height=24
    r+=1

for col,w in zip('ABCDEFGH',[24,38,13,15,32,14,34,84]):
    ws.column_dimensions[col].width=w
ws.freeze_panes='A5'
ws.auto_filter.ref=f'A4:H{4+len(R)}'
wb.save(WB)
print('follow-up tab built:', len(R))
