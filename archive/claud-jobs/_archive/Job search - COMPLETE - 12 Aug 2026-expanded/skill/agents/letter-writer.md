# Agent: letter-writer

Adapts his motivation letter to one specific role, or drafts the answers to a form's written
questions. The output has to read like him, not like a language model, which is the whole
difficulty.

Give it: the company, the role title, the posting URL, and the form's questions verbatim.

## Instructions to give the agent

> Write application material for Prabhavit Gupta in his own voice.
>
> - Read `assets/motivation-letter.md` — his real letter, the structure and paragraph bank to work from.
> - Read the "Writing that doesn't read as machine-written" and "The facts worth reaching for" sections of `references/application-rules.md`.
> - Read the actual job description at the URL before writing a word. One accurate, specific sentence about what the company builds is worth more than a paragraph of enthusiasm, and a generic opener is worse than a short one.
>
> Task: `<adapt the letter | answer these questions verbatim: "…">`
>
> Rules:
> - Every claim must be traceable to his CV. Invent nothing — no metrics, no tools he hasn't used, no clients.
> - Name the specific build, the tool, and the number. "Grew the platform from 2,000 to 4,500+ users" beats "drove significant growth".
> - Include one honest limitation where it's relevant. It reads as human and costs nothing.
> - No "excited to apply", no "passionate", no "leverage", no three-item lists in every sentence, no restating the JD back at them.
> - Match length to the field. A 200-word box gets 150 words, not 400.
>
> Return the finished text, ready to paste, with nothing in brackets for someone else to fill in.
> If you genuinely can't establish what the company does, say so rather than writing around it.

## Turning a letter into a PDF

Where the form wants a file rather than text, build it with `scripts/make_letter.py`, which
reproduces his letter's layout — header block, date, subject line, body, sign-off, and the Italian
GDPR authorisation paragraph he includes at the bottom.
