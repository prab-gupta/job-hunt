# "Tell us about an agent you put into production"

His strongest answer on any form. Canonical version below — vary the emphasis (reliability /
integrations / human-in-the-loop) to match the posting, don't resend verbatim to a company
that already got it.

## Sent to OpenHands (Enterprise Agent Engineer) — 2026-08-05

> At FlowSpace I built and ran the AI agents behind customer support on a coworking
> marketplace serving 4,500+ users. The agent handled inbound member and prospect questions —
> availability, bookings, pricing, account issues — against live data from our own platform
> plus the Office RnD and Nexudus APIs, and escalated to a human when confidence was low or
> the request touched billing. I built it in n8n with OpenAI models, iterated the prompts and
> tool definitions against real transcripts rather than test cases, and the ongoing work was
> mostly reliability: handling partial API failures, stopping the agent from confidently
> answering things it couldn't verify, and keeping a human in the loop where a wrong answer
> would cost a booking. In the same period I shipped a data scraping and parsing agent that
> increased listings on the platform, and a CV-parsing tool built on n8n and Eden AI.

## The harness-flavoured variant — sent to Viktor ("Why you?") — 2026-08-05

> Because harness work is the part of agent engineering I've actually lived in. I've had
> agents in production for two years — support agents, a scraping and parsing pipeline, a
> CV parser — and almost all the engineering was harness: tool definitions, retries, failure
> recovery, keeping the model inside the boundaries of what it could verify, and evaluating
> changes against real transcripts instead of assuming a prompt tweak was an improvement.
> I work in n8n, TypeScript, Laravel and Claude Code daily, and I've built inside eight
> different European companies' stacks, so I ramp on someone else's codebase quickly.

## Multiple-choice version (Camunda self-assessment) — 2026-08-05

> "I have built and operated agentic systems in production, including testing for
> non-determinism and failure recovery."
