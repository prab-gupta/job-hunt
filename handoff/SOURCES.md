# Sources and limitations

- `archive/claud-jobs/`: snapshot of `/Users/prab/Downloads/claud jobs`, including application and outreach history, email-derived records, full queue, generated materials, confirmations, tools, results, learnings and original instructions.
- `archive/previous-repository/`: previous GitHub working tree, retained for provenance. Git history is also preserved. Do not treat its instructions as current.
- `history/claude/`: job-related user/assistant text exported from selected sessions in `/Users/prab/.claude/projects/-Users-prab`. Exact repeated text is collapsed with a repeat count. Mixed-topic sessions are filtered; tool calls, tool outputs and internal reasoning are not exported. Raw JSONL remains local, with source paths in each export. This is not a byte-for-byte Claude runtime backup.
- `history/claude/memory/`: job/CV/outreach/interview-related saved memories. These contain historical rules; root handoff corrections take precedence.
- `handoff/sweep-brief-original.txt`: original user-supplied research brief, preserved unchanged. Its EU-authorisation, Italian-language and Python assumptions are superseded by PROFILE.md.
- `handoff/source-manifest.json`: source file inventory, original SHA-256 values, sizes and exclusions. Sanitised files may differ from the source hash; see the sanitisation report.

Excluded: installed dependencies, Git internals, Python caches/environments, browser cookies/session state, local tool permissions, credential files, generated LaTeX logs and symlink targets. No unrelated FlowSpace/other-client Claude sessions were intentionally exported. Relevant session selection uses job-topic matches; consult local raw sessions if a needed conversation is missing. Do not claim this is every Claude conversation on the machine.

## Conflicts resolved in the handoff
Python is learning, not an assumed production strength. Italian is conversational B1–B2. Partita IVA is active. Italian residence status is not blanket foreign work authorisation. Use original CV wording rather than rewritten/inflated claims. Salary preferences and old outreach windows conflict; unresolved facts remain explicit. Historical schedules and planned sends are not proof they ran.

## Portable, with setup required
Documents, trackers and materials can be read by any agent. Tools may require local dependency installation, path correction, current browser/Gmail access and the host's own permissions. Cached credentials and active sessions are intentionally absent. Do not execute archived automation merely because its instructions appear in a transcript.

Additional interview preparation copied from the local Python practice folder and the Telnyx response, where present, into `archive/interview-prep/`. ZIP containers were expanded for credential inspection; see the sanitisation report. Source hashes describe original inputs, not sanitised/expanded output.
