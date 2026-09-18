#!/bin/bash
echo "Starting scrape..."
echo "[]" > results.json
cd ".agents/skills/linkedin-search/cli"
bun run src/cli.ts search --query "AI Engineer" --location "Italy" --format json > ../../../../linkedin_ai_italy.json
bun run src/cli.ts search --query "Next.js" --location "Remote" --format json > ../../../../linkedin_nextjs_remote.json
bun run src/cli.ts search --query "TypeScript" --location "Italy" --format json > ../../../../linkedin_ts_italy.json
cd "../../../../.agents/skills/freehire-search/cli"
bun run src/cli.ts search --query "AI Engineer" --format json > ../../../../freehire_ai.json
bun run src/cli.ts search --query "Next.js" --format json > ../../../../freehire_nextjs.json
cd ../../../../
echo "Scrape complete."
