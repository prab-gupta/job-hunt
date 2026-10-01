# project44 / p44LSP.ai - Phone Screen

## 1. Likely Questions
*   **Motivation & Role Clarity:** "Why p44LSP.ai, and why transition into a Forward-Deployed Engineer role specifically?"
*   **The Logistics Gap (Fit evaluation):** "You don't have direct experience with TMS, WMS, or logistics domains like freight procurement. How will you quickly learn our customers' world?" 
    *   *Bridge Strategy:* Acknowledge the lack of direct logistics experience. Connect to your extensive experience mapping complex domains as a Lead Developer and building client-driven automations (Urlink, UltraStrategy). Emphasize your eagerness to sit with operators, learn their language, and serve as the "ground truth" bridge to product.
*   **The Scale Gap (Fit evaluation):** "Your API and webhook experience with n8n is great, but we run event-driven pipelines on Kafka/PubSub processing millions of events per day. Are you comfortable operating at that scale?"
    *   *Bridge Strategy:* Acknowledge that n8n was perfect for startup prototyping, but emphasize your solid grasp of event-driven architectures and your readiness to transition to enterprise-scale streaming data.
*   **Debugging Agentic Workflows:** "How do you debug an AI agent when it makes an incorrect decision or hallucinates in a production pipeline?" (Directly addresses the JD requirement).

## 2. STAR Answer Mapping

**1. Debugging Agentic Workflows (FlowSpace)**
*   **S:** At FlowSpace, we had an AI bot that ingested multi-format brochures to draft workspace listings. Occasionally, it would hallucinate details or misinterpret layouts.
*   **T:** I needed to ensure agent reliability and prevent bad data from reaching the live platform, ensuring a tight feedback loop.
*   **A:** I implemented a human-in-the-loop escalation step and built tracing mechanisms. When an error occurred, we could trace the failure back to the specific chunk of the brochure and the prompt that generated it.
*   **R:** This drastically improved data quality and provided a direct debugging loop—proving I know how to trace failures back to specific data points or tool use.
*   *Use for:* "Tell me about a time you debugged an AI agent," "How do you handle agent hallucinations?"

**2. API Integration & Event-Driven Workflows (UltraStrategy/Get2Germany)**
*   **S:** Clients needed a seamless way to match candidates with courses and process their data automatically across disjointed systems.
*   **T:** Build an automated, event-driven pipeline between various LLMs and core business systems.
*   **A:** I engineered bi-directional webhooks using n8n to connect AI (Eden AI/Claude) with core external services (Google APIs).
*   **R:** We replaced manual workflows with an automated pipeline—a smaller-scale parallel to automating agent-to-agent coordination in logistics.
*   *Use for:* "Tell me about your experience with webhooks and APIs," "Describe a complex integration you built."

## 3. Consistency Brief
The interviewer is likely looking at a CV featuring these claims. Every claim must be defensible in depth:
*   **Lead Developer at FlowSpace:** Scaling a legacy stack to Next.js/Laravel for 4,500+ users without downtime.
*   **Agentic Expertise:** Deploying RAG-based AI agents to answer customer queries against live platform data.
*   **Solo Client Delivery:** Acting as a solo implementer bridging the gap between product capability and client needs (Urlink).

## 4. Tough Questions, Customized

### "Why this company specifically?"
> "The recent launch of p44LSP.ai in July really caught my eye. The thesis makes total sense to me—shippers need end-to-end applications, but LSPs are selling logistics as their product, so they need scalable AI and API infrastructure to build their own competitive edge. I want to build at that edge. The fact that you are pairing the speed and scope of an AI startup with project44's massive $124M infrastructure and carrier network is exactly where I want to be: moving fast with agents, but with real, scaled data to make those agents actually useful."

### "You don't have direct experience with logistics, TMS, or WMS."
> "That's true. My background is in building multi-agent systems and integrating complex APIs across various domains. What I've learned from leading projects at FlowSpace and acting as a solo implementer is that the first step to building great workflow automation is sitting with the operators, understanding their 'ground truth', and speaking their language. I'm very comfortable diving into complex enterprise systems, and I know how to bridge the gap between how an LSP operates in reality and how we program our agents to serve them."

## 5. Questions You Should Ask (Pick 2-3)
*   **Role/Product Link:** "You mention FDEs serve as the 'ground truth' for the product team. How does the feedback loop practically work between FDEs embedded with LSP accounts and the core product engineering team?"
*   **Tech Focus:** "When customizing agent logic for LSPs in the field, what is the biggest challenge right now—is it data latency, prompt hallucination, or something else?"
*   **Culture/Process:** "With customers testing these agents in weeks rather than quarters, how do you handle rollbacks or exception handling when an agent acts on incomplete data in production?"

## 6. Logistics
*   **Date/Time:** [To be confirmed]
*   **Format:** Phone / Video Screen
*   **Interviewers:** [To be confirmed]
*   **Tips:**
    *   Have these STAR examples printed or open on a separate screen.
    *   It's perfectly OK to take 5 seconds to think before answering complex technical questions.
    *   Smile when speaking—it changes your tone significantly on phone/video.
