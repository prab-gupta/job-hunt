# Mock Q&A: likely interrupts from Edouard

Answer aloud, 60-90 seconds each. Shape: claim, why, cost, what would change my mind. Every fact below is in the deck appendix or the master experience file.

**1. Why Haiku as the default model?**
Extraction against a fixed schema with coercion behind it does not need the biggest model. Haiku was good enough and cheap, so I could run it on every building. Sonnet sits behind a switch for hard sources, and the batch flow always uses Sonnet for the one job that is genuinely hard: reading a broker workbook's layout. The quality floor comes from the spec coercion and the human card, not from model size. If the correction log showed Haiku fields being corrected more often, I would move that field to Sonnet, not the whole pipeline.

**2. Why rewrite the Python prototype in TypeScript?**
The Python version was a single-user tool on a laptop. Operations needed a URL: login, uploads, several people, deployed. Next.js on Vercel gave me that in days. I kept the Python as ground truth: I regenerated its output as fixtures and ported until twenty parity checks over seventy-seven real listings went green. The cost was a week where both evolved in parallel and I tracked the deltas in a ledger. I froze the Python once the port was live.

**3. Why two data stores?**
Honest answer: constraints, not design. Supabase was already there for photos and the review sessions the admin page renders. Neon arrived with Vercel for the relational listing rows. It caused a real bug: drafts written only to Supabase came back "listing not found" when someone pressed Send, because Send reads Neon. Today I would collapse to one store. It is the first thing on my "would change" slide.

**4. Why not use structured outputs or tool calling for the JSON?**
I tried server-side structured outputs; the grammar compile timed out on a schema this size. Schema in the prompt plus local parsing gave the same guarantee where it matters, at the database boundary, where every value is coerced anyway. So the extra machinery bought nothing the coercion layer was not already doing.

**5. What broke?**
Four things worth telling. Five hundred and fifty drafts carried a tenure value copied from a bad example in the agent brief; it mapped to null and would have badged two thousand offices wrongly on the public site. Two drafts renamed to the same live building wrote to the same path and one vanished silently: 579 built, 578 files. A broker sheet's own price table was never read, so offices shipped at zero pounds. And the photo endpoint crushed images to 720 pixels. Each one became a validator or a guard on the one path every draft passes through.

**6. How do you know the extraction is right?**
Three layers. Coercion and closed enums at build, so a wrong shape cannot reach the API. Source values byte-exact, so if the model disagrees with the sheet the card shows a flag instead of a substitution. Then a person. For end-to-end proof I ran an acceptance workbook I knew the answers for: twelve of twelve buildings, offices byte-faithful, sixty-five photos verified by downloading every one. What I do not have is a per-field accuracy number; the correction log was built to produce exactly that and was never switched on.

**7. How did you size the benefit?**
By hand a listing took thirty to forty-five minutes: find the building, type about forty fields, source five photos, build the offices table. Nine hundred drafts is roughly 450 to 675 hours. The honest caveats: review minutes per card remain, only 114 are live, and the rest are proposals. The second benefit is harder to count: 812 backlog buildings nobody had capacity to triage became 446 updates and 375 new, with reasons attached.

**8. What would the Tech Lab hate about inheriting this?**
Two stores. Feature switches in environment variables in three places. Dependence on quirks of the platform API: name-only search, a 422 you have to adopt the slug from. One building per 300-second function on Vercel. Dead review code. What helps them: one spec file as the contract, six hundred tests, the port ledger, and a handover pack that says what cannot be run from where they sit.

**9. When do you stop researching a building?**
When the caps hit or the evidence resolves, and I write down which. Crawl: depth two, twelve fetches, forty megabytes, sixty seconds. Photos: five typed slots, gap-fill from the operator's site, never a kitchen shot, and if nothing exists, list every source checked. Identity: if I cannot confirm who operates the building, it holds. Thirty-one units held with a written reason each is a result; a guessed address published under the wrong floor is not.

**10. What did an agent get badly wrong, and how did you catch it?**
The one I gave you in writing: a migration agent reported a small null count as a clean run; asking it to classify every null as source-absent or mapper-bug showed a mapper had dropped about twenty-nine percent of a field. Two more from this project. A parent agent that delegated to child agents returned nothing verifiable, so I moved to one agent per building and treat disk as the truth. And my first attempt at the photo revert was based on the wrong commit and would have removed an unrelated dedup fix; the diff review caught it before merge.

**11. Walk me through the UltraStrategy pipeline and one decision in it.**
Recruiters were reading every CV by hand. A candidate uploads a CV; Affinda extracts it; Claude assesses relevance per role type; the result shows in their frontend; then a standardised Ultra CV is generated. n8n and Eden AI sit in the workflow. The decision: three separate steps, extraction, assessment, generation, so each could be checked on its own and swapped without touching the others.

**12. Why per-entity migration, and what went wrong?**
One blanket CSV export assumes nothing changes between export and go-live, and members were booking the whole time. So anything still changing synced through the API until cutover, frozen records went once by CSV, and each entity cut over on its own date. The cost was one path per entity instead of one script. What went wrong is question ten: a clean-looking null count hiding a dropped field. I now ask for that split on every migration count.

**13. You were on your own. Who were the stakeholders?**
The operations team at FlowSpace who used the card and pressed Send on the 114 that are live, and the team I handed the pack to on 31 July. I was lead developer, so I also carried the product owner's decisions. That is the honest limit of the example: the feedback loop was real but small. It is one reason your structure, with a product owner on the other side of the handover, appeals to me.
