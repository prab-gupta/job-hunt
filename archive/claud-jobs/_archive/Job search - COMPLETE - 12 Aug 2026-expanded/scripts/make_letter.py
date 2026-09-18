from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

BODY = ParagraphStyle("body", fontName="Helvetica", fontSize=9.0, leading=12.2,
                      alignment=TA_JUSTIFY, spaceAfter=5.2)
NAME = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=13, leading=16, spaceAfter=1)
META = ParagraphStyle("meta", fontName="Helvetica", fontSize=9, leading=12, spaceAfter=1)
SUBJ = ParagraphStyle("subj", fontName="Helvetica-Bold", fontSize=10, leading=13, spaceAfter=8, spaceBefore=8)
GDPR = ParagraphStyle("gdpr", fontName="Helvetica-Oblique", fontSize=7.6, leading=10,
                      alignment=TA_JUSTIFY, spaceBefore=10)

ROLE = "Analytics Implementation Consultant"
LOCATION = "Europe, Remote"
DATE = "6 August 2026"

paras = [
"Dear Hiring Manager,",

"I am writing to apply for the Analytics Implementation Consultant role at Sporty Group. What drew me "
"to this posting specifically is the ownership it describes: curating a tracking schema across front-end "
"and back-end events, with triggers, event parameters and user properties documented, and then being the "
"person other teams come to when an event stops firing correctly. That is a systems and documentation "
"problem as much as an analytics one, and it is close to how I have spent the last three years.",

"Over the past three years, I have successfully transformed abstract business requirements into "
"production-ready features across multiple European technology projects spanning different countries and "
"sectors; from a sports management platform in Luxembourg to strategic consultant platforms in France and Spain.",

"Operating extensively as a freelance AI Solutions Developer, I engineered AI-based data parsing tools "
"using n8n for UltraStrategy, automated complex workflows for Get2Germany, and executed rigorous quality "
"assurance and API integrations for Clubee.",

"During my tenure at FlowSpace (based in London), I took over an already built system and managed it until "
"its eventual migration to Laravel. Debugging the system, I also partook in go-to-market automations using "
"their CRM. I engineered AI agents and automated data parsing tools that directly contributed to scaling the "
"platform from 2,000 to over 4,500 active users.",

"I want to be straightforward about where I stand against your first requirement. My work has run alongside "
"Google Tag Manager and GA4 rather than at the centre of them: I have not spent three years administering GTM "
"containers at scale, and I would rather you hear that from me now than discover it in a later round. What I "
"do bring is the layer underneath. I am proficient in HTML, CSS and JavaScript and comfortable with how a data "
"layer gets populated and read. I have built and debugged the event and webhook flows that carry conversions "
"into CRMs and third-party platforms, where attribution is only as good as the payload. I have owned the "
"awkward part of that work, which is establishing a testing process with product and engineering so a broken "
"event is caught before a campaign reports on it, and writing the documentation that lets other people use the "
"system without me. Data privacy is not an afterthought for me either; I work under GDPR by default.",

"I extensively leverage AI coding assistants like Claude Code and bolt.new alongside modern frameworks "
"(TypeScript, Next.JS, Laravel, Supabase) to rapidly test hypotheses and deploy MVP architectures. Recently I "
"oversaw a migration from a low-code infrastructure to a Next.JS and Laravel stack, ensuring rapid prototypes "
"evolved into scalable, reliable and secure products.",

"I am also open to learning new systems and techstack. I recently completed a course in Microsoft Co Pilot and "
"AI agent orchestration, and closing the gap on GA4 and server-side GTM is exactly the kind of thing I would "
"expect to do quickly and properly rather than claim I already had.",

"As a graduate of Ca' Foscari University, I have been living in Venice for 5 years, hold a European Long-Term "
"Residence Permit requiring no visa sponsorship, and have the professional English proficiency required for "
"international collaboration. Your core hours of 10am to 3pm local time sit comfortably with mine. I am also "
"fully available for short and medium-term business travel as project demands.",

"I would welcome the chance to talk about the tracking schema you are building and where the current "
"implementation hurts most.",

"Thank you for your time and consideration.",
]

doc = SimpleDocTemplate("/home/claude/sheet/letters/Sporty_Group_Motivation_Letter.pdf",
                        pagesize=A4, leftMargin=18*mm, rightMargin=18*mm,
                        topMargin=13*mm, bottomMargin=11*mm, title="Motivation letter - Prabhavit Gupta")
story = [
    Paragraph("<u>Prabhavit Gupta</u>", NAME),
    Paragraph("Venice, Italy +39 3516107807 | prabhavitg@gmail.com", META),
    Paragraph("LinkedIn: https://www.linkedin.com/in/prabhavit", META),
    Spacer(1, 7),
    Paragraph(DATE, META),
    Paragraph(f"Motivation letter for Application for {ROLE} - {LOCATION}", SUBJ),
]
for p in paras:
    story.append(Paragraph(p, BODY))
story += [
    Spacer(1, 5),
    Paragraph("Sincerely,", BODY),
    Spacer(1, 9),
    Paragraph("Prabhavit Gupta", BODY),
    Paragraph("I hereby authorize the processing of my personal data contained in this document in compliance "
              "with the European General Data Protection Regulation (EU Regulation 2016/679) and Italian "
              "Legislative Decree 196/2003, as modified by Legislative Decree 101/2018, for the purposes of "
              "recruitment and selection.", GDPR),
]
doc.build(story)
print("built")
