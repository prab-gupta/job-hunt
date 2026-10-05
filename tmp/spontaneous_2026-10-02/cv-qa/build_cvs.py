from pathlib import Path
import json
ROOT=Path('/Users/prab/Downloads/claud jobs')
BASE=(ROOT/'cv/main_MVLabs_FullStackAIAutomationDeveloper.tex').read_text()
CONFIGS=[
 {'company':'APPSTYX','source':'cv/main_APPSTYX_AIAutomationIntegrationDeveloper.tex','pdf':'output/pdf/Prabhavit_Gupta_APPSTYX_CV.pdf','summary':[
  'AI and automation developer building AI agents, OpenAI integrations, and n8n workflows for European web platforms.',
  'Integrates external APIs and CRM systems, with hands-on LLM data parsing and RAG skills.',
  "Oversees FlowSpace's migration from Bubble.io to Next.js and Laravel, combining product coordination with QA and client delivery."],
  'ai':'OpenAI/ChatGPT integration, AI Agents, RAG, Chatbot development, API integration, Eden AI',
  'automation':'n8n, Playwright; data processing, CRM integrations and workflow automation'},
 {'company':'Totaliweb','source':'cv/main_Totaliweb_AIAutomationWebDeveloper.tex','pdf':'output/pdf/Prabhavit_Gupta_Totaliweb_CV.pdf','summary':[
  'AI and automation developer building n8n workflows, CRM integrations, and lead capture automations for business operations.',
  'Built CV parsing with n8n and Eden AI, AI tools for platform listings, and customer support agents.',
  "Combines OpenAI integration and AI-assisted development with Supabase experience and FlowSpace's Next.js and Laravel migration."],
  'ai':'AI Agents, OpenAI/ChatGPT integration, Eden AI, LLM data parsing, RAG, Chatbot development',
  'automation':'n8n, Playwright; CRM integration, lead capture, enrichment and outbound automation'},
 {'company':'SeisNet','source':'cv/main_SeisNet_WebIntegrationAutomationDeveloper.tex','pdf':'output/pdf/Prabhavit_Gupta_SeisNet_CV.pdf','summary':[
  'Web and automation developer integrating external APIs, CRM systems, and automated booking workflows.',
  'Experience delivering frontend features, Figma implementations, unit testing, and quality assurance across European projects.',
  "Oversees FlowSpace's migration from Bubble.io to Next.js and Laravel and documents product logic with developers."],
  'ai':'API integration, AI Agents, RAG, Chatbot development, Eden AI, OpenAI/ChatGPT integration',
  'automation':'n8n, Playwright; CRM integrations, lead capture, data processing and workflow automation'}]
start=BASE.index('\\section{Career Summary}')
end=BASE.index('\\section{Visa \\& Language}')
for cfg in CONFIGS:
    section='\\section{Career Summary}\n\\begin{itemize}\n'+'\n'.join('\\item '+s for s in cfg['summary'])+'\n\\end{itemize}\n\n'
    section+='\\section{Technical Skills}\n\\begin{itemize}\n'
    section+='\\item \\textbf{AI/ML} -- '+cfg['ai']+'\n'
    section+='\\item \\textbf{Automation} -- '+cfg['automation']+'\n'
    section+='\\item \\textbf{Development} -- Claude Code, Laravel, Typescript; Next.js migration, Bubble.io, Supabase\n'
    section+='\\item \\textbf{Project/Design} -- Figma, Jira, GitHub, Postman, Trello\n\\end{itemize}\n\n'
    content=BASE[:start]+section+BASE[end:]
    (ROOT/cfg['source']).write_text(content)
(ROOT/'tmp/spontaneous_2026-10-02/cv-qa/configs.json').write_text(json.dumps(CONFIGS,indent=2))
print('Created three bespoke CV sources with three summary bullets each.')
