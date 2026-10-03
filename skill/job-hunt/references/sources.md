# Search playbook — where the roles actually are

Everything here was tested with the WebSearch / WebFetch tools rather than assumed. The point
of writing it down is that a job sweep burns most of its budget on dead ends: SPA boards that
render nothing, aggregators reposting stale listings, and postings that quietly closed weeks
ago. Use the verified paths, skip the graveyard, and spend the saved calls on verification.

**Never fetch job pages with curl, wget, or python requests.** WebSearch and WebFetch are the
only permitted ways to reach the web here. If something is blocked, it stays blocked.
The one exception: boards marked *needs a browser* (hiring.cafe, europa.eu/eures job search) are read
through the Chrome DevTools browser agent, never curl.

---

## 1. The two mechanisms

**WebSearch with `allowed_domains`** — this is a *hard* filter, unlike a `site:` operator which
is only a ranking hint. Restricting to ATS hosts is the single highest-precision move
available: it returns individual live postings instead of SEO farms and aggregators. Prefer it.

```
WebSearch(query="AI automation engineer remote Europe",
          allowed_domains=["jobs.ashbyhq.com","job-boards.greenhouse.io"])
```

**WebFetch on a board listing page** — good boards expose path-based taxonomies (region,
country, category) that return dozens of listings in one call, with posting ages. Use these
for breadth and for freshness, then verify individual postings.

Run several of both in parallel in one message. Sweeping six sources at once and then
verifying is far faster than a serial crawl — with one exception noted below (Himalayas).

---

## 2. ATS domains, ranked by yield

| Domain | Why | Notes |
|---|---|---|
| `jobs.ashbyhq.com` | **Best single source for discovery.** Modern AI companies, EMEA-aware titles, no index-page noise. The only ATS that reliably discloses **salary bands**, often in several currencies. | Canonical URL is `jobs.ashbyhq.com/<org>/<uuid>` — strip `?embed=js`, `/application`, `?utm_data=…`, `?locationId=…`. **But read the posting through the API, not the page:** Ashby HTML pages frequently come back as an unrendered JS shell ("You need to enable JavaScript"), and a shell looks exactly like a closed role. One API call per org covers every posting it has, so it's cheaper anyway. |
| `job-boards.greenhouse.io` | High volume, clean single postings. Salary usually absent. | Note the **hyphenated** host. |
| `job-boards.eu.greenhouse.io` | EU data-residency variant that surfaces European employers the `.com` host misses (JetBrains, Prolific, Clarity AI, saasgroup). | Query it *in addition to* the `.com` host, not instead. |
| `jobs.smartrecruiters.com` | Solid individual postings, location often in the title string. | Use this host. **`careers.smartrecruiters.com` returns only board index pages — skip it.** |
| `join.com` | Good for European startups and, unusually, plenty of explicit contract / part-time listings. | Clean single-posting parse. |
| `jobs.personio.com` | DACH-heavy, low competition. Real host is `<company>.jobs.personio.com/job/<id>`. | Append `?language=en` — many boards default to German. |
| `jobs.lever.co` | Works, but the noisiest. | **Snippets lie about location.** A posting titled "…(Remote, Full-Time)" surfaced under a "remote Europe" query and turned out to be India-only. Also heavy with aggregators (Jobgether) and outsourcing firms. Always fetch before trusting. |
| `jobs.eu.lever.co` | EU-hosted Lever, a **separate host** from `jobs.lever.co` (Everseen, Aave Labs, Skaylink, MARKT-PILOT). | Feed: `api.eu.lever.co/v0/postings/<co>?mode=json`. Same location caveat as `jobs.lever.co`. |
| `ats.rippling.com` | US AI companies' EU roles (Domaine, Hammerspace, Nutrient, Dynamo). | Feed: `ats.rippling.com/api/v2/board/<slug>/jobs`. |
| `jobs.gem.com` | Gem ATS: Productboard (Remote EU), Synthio, Bilt FDE roles. | Read the page; the board API path returned 302. |
| `*.teamtailor.com` | Dominant Nordic/Baltic/Eastern-EU ATS; English postings common (Mintos, Keepit, Axmed, Unikraft). | Feed: `<co>.teamtailor.com/jobs.rss`. |
| `*.pinpointhq.com` | UK/IE/EU scale-ups (Zencargo FDE remote Europe, Scurri). | Feed: `<co>.pinpointhq.com/postings.json`. |
| `jobs.personio.de` | The `.de` host is a **separate domain** from `jobs.personio.com` (Jedox, Chrono24, quantilope, askui). | Append `?language=en`. Feed: `<co>.jobs.personio.de/xml`. German (m/w/d) titles are a language gate. |
| `*.breezy.hr` | Mid-size EU/PL firms (Commerzbank PL AI Solutions Engineer, Doodle Labs). | Feed: `<co>.breezy.hr/json`. |
| `*.bamboohr.com/careers` | Squirro (remote EU), Mercuryo AI Automation Engineer. | Page only. |
| `*.homerun.co` | Small NL/FR startups (Bonx FDE, AppSignal Customer Engineer). | Page only. |
| `*.myworkdayjobs.com` | Large employers with English Italy/EU roles (Veralto, Datasite, Darktrace). | Apply needs an account, so the row is `needs_you` with blocker `login`. |

Legacy `boards.greenhouse.io/<co>/jobs/<id>` 302-redirects off-host (costs two calls), and
`boards.greenhouse.io/embed/job_board` is robots-disallowed. `apply.workable.com` job pages are
a client-side SPA that silently degrade to the company's "Current Openings" page — read Workable
through its widget API instead (§5).

---

## 3. Query recipes that returned real hits

Role phrase + remote + region, domain-restricted:

- `AI automation engineer remote Europe` → n8n, Quora, Quadrivia, Oh (MarTech AI & Automation, remote Europe), Bifrost, DoiT
- `"forward deployed engineer" remote Europe` → Cohere, ElevenLabs, Luma, Camunda EMEA
- `AI solutions engineer remote EMEA` → Mistral, Camunda, WunderGraph, Omni
- `"technical product manager" remote Europe`

**Contract intent — put the literal contract vocabulary in the query.** Asking for "contract"
generically returns permanent roles; these words work:

- `freelance contractor AI automation engineer "contract" remote day rate n8n` → Kairos "Contract Software Engineer", Hippocratic AI "Junior Forward Deployment Engineer (Contract)", a 12-month Ansible AAP contract on join.com, Scalia "AI Automation Specialist (Part time)", G2i
- Also try: `"6-month contract"`, `"12-month contract"`, `"fixed-term"`, `(Contract)`, `B2B`, `part time`, `fractional`

**Stack keywords are his edge.** `n8n`, `low-code`, `AI agents`, `Bubble.io`, `Playwright`,
`Zapier`/`Make`/`Tray.ai` postings are far less crowded than generic "AI Engineer" listings.
Run at least one stack-keyword query per sweep.

**Company-direct.** For a named company, `WebFetch` its board index —
`job-boards.greenhouse.io/<company>` fetches fine as a bulk company-wide listing with no API
token — or query `allowed_domains=["jobs.ashbyhq.com"]` with the company name.

Unrestricted generic queries (`AI solutions engineer remote EMEA jobs`) return aggregator SEO
farms with almost no direct-apply links. Their one use is **host discovery** — that's how
`job-boards.eu.greenhouse.io` turned up.

---

## 4. Job boards worth fetching

| Board | What it gives | Verified URL templates |
|---|---|---|
| **euremotejobs.com** | Best European board tested. Region strings distinguish "Europe" / "EMEA" / worldwide — exactly the filter that matters. Freshest feed seen (listings minutes old). Salary on roughly a third. | `/job-region/remote-jobs-europe/` · `/job-region/remote-jobs-emea/` · `/job-region/{spain,portugal,germany,ireland,uk}/` · `/jobs/remote-software-engineering-jobs/` · `/jobs/remote-data-jobs/` · `/jobs/all-remote-jobs/` |
| **remoterocketship.com** | **Signal only** — it surfaces on-target Italy-remote roles other sources miss, but its pages expose no direct-apply URLs, so a row can't be sourced from here. Use it to learn *company + title*, then find the original posting via an ATS search. Keyword + country + recency compose in one URL; EUR salaries, dates to the minute. | `https://www.remoterocketship.com/country/italy?page=1&sort=DateAdded&jobTitle=AI%20Engineer` · `https://www.remoterocketship.com/?page=1&sort=DateAdded&locations=Europe` |
| **himalayas.app** | Uniquely states the **region restriction per job** ("Netherlands only", "Global", "United Kingdom only") — kills the biggest time-waster, the secretly-US-only "remote" role. | `/jobs` · `/jobs/countries/italy` · `/jobs/python` · `/jobs/engineering` · `?page=N`. **Serialize these calls** — it 429s under concurrency, and paths don't compose (`/jobs/countries/italy/skills/python` → 404). |
| **arbeitnow.com** (JSON) | Clean JSON: title, company, `remote`, `location`, `tags`, `created_at` epoch. DACH-heavy, mixed non-tech — filter hard. | `https://arbeitnow.com/api/job-board-api` |
| **remoteok.com** (JSON only) | HTML page is an empty JS shell; the API works. Global overflow. **Its `salary_min`/`salary_max` are `$0` — ignore them.** | `https://remoteok.com/api` |
| **aijobs.net** | Best salary transparency of any board (EUR bands on most rows), strongly on-target for AI/ML. Company names don't always extract. | `https://aijobs.net/` — filter params unverified, don't invent them |
| **wellfound.com** | US-skewed, no posting dates — but now in scope since he's open to non-EU and contract work. | `https://wellfound.com/role/r/software-engineer` |

## 4b. Additional boards (added 2026-10-03)

All URLs below were fetched on 2026-10-03 and returned live roles unless a note says otherwise. Boards marked *needs a browser* are read through the Chrome DevTools browser agent, never curl. Run at least one query per Tier-1 board on every sweep.

Ranking = (roles per query that fit Prabhavit: EU/remote-EU, 0-4 yrs, no local language) x (how cleanly a browser agent can read it) x (direct employer apply links). "Login" = needed to read listings. All are free to read unless noted.

| # | Board | Tier | Login? | Browser agent, no paywall? | Why it fits |
|---|---|---|---|---|---|
| 1 | **jobs-radar.com** | 1 | No | Yes, plain fetch | 1.2M jobs from 14k company ATS feeds with direct links. `q`, `location` and `range` params really filter (Italy+"solutions engineer" = 470 hits, Europe = 134, Europe+week = 38). |
| 2 | **hiring.cafe** | 1 | No | **Needs a browser** (Cloudflare blocks curl, renders in headless Chrome) | ATS-direct aggregator, `searchState` URL carries query, remote, region and age. Europe+remote+"forward deployed engineer" = 122 jobs / 80 companies. Already named in `GEMINI-SWEEP-PROMPT.md`. |
| 3 | **jobdex.io** | 1 | No | Yes | EU tech jobs with parsed **language requirements** and real remote policy ("98% don't require German"). `/remote-from/Italy` = 409 roles, `/stack/n8n` = 26, `/stack/LLM` = 495. Directly kills his biggest rejection reason. |
| 4 | **deployaijobs.com** | 1 | No | Yes | FDE / solutions / customer-facing roles, 2,324 roles. Server-side filters: `location=Italy` (20), `location=Europe` (526), `remote=remote`, `seniority=junior`, `q=`. |
| 5 | **deployedjobs.com** | 1 | No | Yes | FDE, solutions engineer, applied-AI, implementation split by role; `?location=Italy` gives 16 verified rows incl. Telnyx, Databricks, Datadog, Anthropic Milan. |
| 6 | **community.n8n.io Jobs** | 1 | No | Yes (public Discourse JSON) | His differentiator is n8n. Category is mostly `[HIRING]` with EU-remote n8n/AI-automation roles and contracts. Mixed with `[For Hire]`, so filter titles. One listing seen requires German, read each. |
| 7 | **`jobs.eu.lever.co`** | 1 | No | Yes | EU-hosted Lever (separate host from the `jobs.lever.co` row already in §2): Everseen, Aave Labs, Skaylink, MARKT-PILOT. API works: `api.eu.lever.co/v0/postings/<co>?mode=json`. |
| 8 | **`ats.rippling.com`** | 1 | No | Yes | Fast-growing ATS used by US AI companies' EU roles (Domaine, Hammerspace, Nutrient, Dynamo). API 200: `ats.rippling.com/api/v2/board/<slug>/jobs`. |
| 9 | **`jobs.gem.com`** | 1 | No | Yes | Gem ATS: Productboard (Remote EU), Synthio, Bilt FDE roles. |
| 10 | **`*.teamtailor.com`** | 1 | No | Yes | Dominant Nordic/Baltic/Eastern-EU ATS, English postings common (Mintos, Keepit, Axmed, Unikraft). Feed: `<co>.teamtailor.com/jobs.rss`. |
| 11 | **`*.pinpointhq.com`** | 2 | No | Yes | UK/IE/EU scale-ups (Zencargo FDE remote Europe, Scurri AI platform). Feed: `<co>.pinpointhq.com/postings.json`. |
| 12 | **`jobs.personio.de`** (and `.com`) | 2 | No | Yes | The `.de` host is a **separate domain** from the `jobs.personio.com` row already in §2: Jedox, Chrono24, quantilope AI Automation Engineer, askui. Append `?language=en`. XML feed `<co>.jobs.personio.de/xml`. |
| 13 | **`*.breezy.hr`** | 2 | No | Yes | Mid-size EU/PL firms: Commerzbank PL AI Solutions Engineer, Doodle Labs Solutions Engineer EU. Feed: `<co>.breezy.hr/json`. |
| 14 | **`*.bamboohr.com/careers`** | 2 | No | Yes | Squirro (remote EU), Mercuryo AI Automation Engineer (remote-first). |
| 15 | **`*.homerun.co`** | 3 | No | Yes | Small NL/FR startups: Bonx FDE, AppSignal Customer Engineer (remote CET). |
| 16 | **`*.myworkdayjobs.com`** | 3 | No (apply = account) | Yes | Large employers with English Italy/EU roles (Veralto Solutions Engineer remote Italy/UK, Datasite Senior AI Engineer remote Europe, Darktrace Milan). Many need an account at apply time, matching the drainer's `login` blocker. |
| 17 | **remotery.co** | 2 | No | Yes | Fully-remote only, Europe and Italy slices, salary filter. Role slugs that exist: `ai-engineer`, `solutions-engineer`. |
| 18 | **airemotelyjobs.com** | 2 | No | Yes | Hand-curated remote AI/ML roles open to Europe, read from company career pages, daily. |
| 19 | **latchhire.com** | 2 | No | Yes | Role-family boards (FDE 877 roles, Solutions Eng, Agentic, GTM Eng 134) fed from ATS with links to the original posting. No URL location filter, filter by the location text. |
| 20 | **thehub.io** | 2 | No | Yes | Nordic and EU startup board, English, `search=` and `remote=true` filters work server-side. |
| 21 | **ycombinator.com/jobs** | 2 | No to read (YC account to apply) | Yes | YC-backed startups, Europe and Remote pages and role pages; many FDE and solutions roles. Apply through the company's own ATS link where shown. US-heavy. |
| 22 | **hnhiring.com** + HN Algolia | 2 | No | Yes | Searchable "Who is hiring". Old `sweep.py` already hits Algolia for the current month thread; this adds a human-searchable view (current thread id 49922569). |
| 23 | **fdepulse.com/jobs/** | 2 | No | Yes (all 1,340 rows are in the HTML, filter client-side) | FDE-only. Not location-URL filterable, but each row carries city, seniority (Junior/Mid) and remote flag. Repo already has `fdepulse_check.py`, so it was used ad hoc. |
| 24 | **Venture-capital portfolio boards (Getro)** | 2 | No | Yes | Nine EU funds, one `q=` pattern. See section 3. Startups, EU-heavy, direct ATS links. |
| 25 | **nodesk.co** | 3 | No | Yes (the repo's dead list says 403; plain fetch now returns 200) | `/remote-jobs/europe/`, `/emea/`, `/ai/`. Listings can be 3-25 weeks old, check the age column. |
| 26 | **fde.traversaal.ai** | 3 | No | Yes | FDE Field Guide: 997 FDE roles US/Europe/India, region tabs and a seniority tag. Duplicates much of #4/#5/#23. |
| 27 | **fwddeploy.com** | 3 | No | Yes | FDE board with city and country pages. Smaller, partly duplicated. |
| 28 | **eurotechjobs.com** | 3 | No | Yes | Europe tech jobs with 0-2 yr / 3-4 yr experience facets, Remote facet, per-country pages (`/jobs/italy`). About 400 jobs, many senior. |
| 29 | **berlinstartupjobs.com** | 3 | No | Yes | English-language Berlin startups, "AI", "GTM" skill tags, 149 jobs. Small but readable. |
| 30 | **irishjobs.ie / jobs.ie** | 3 | No | Yes | Ireland is English-only, EU, no language wall. Path URLs by title (`/jobs/solutions-engineer`). Low count and many agencies, which trip the repo's staffing-agency hard gate. |
| 31 | **EURES job portal** | 3 | No | **Needs a browser** (Angular SPA) | Official EU vacancy index (2.6M). Fuzzy keyword match, mostly local-language and industrial "automation engineer". Use only with country + English-language checks. `sort` param unverified. |

Not included on purpose: remote1stjobs (free tier hides descriptions, paid), aijobs.ai (ignores `q`/`location`, US-skewed), relocate.me (27 visa-focused jobs, `query` ignored), rungcode.io (13 big companies only), startup.jobs (JS search shell), levels.fyi/jobs (query ignored), germantechjobs/duunitori/startupjobs.com/jooble/glassdoor/indeed (Cloudflare or login), techleap jobs (dead), `jobs.balderton.com`/`jobs.lakestar.com` (no such host), remote.co, englishjobs.nl/.de (empty or no relevant roles).

### Ready-to-use search URLs


Query set: **FDE** = forward deployed engineer, **SE** = solutions engineer, **IE** = integration engineer, **AE** = automation engineer, **AI** = AI engineer.

#### 4b.1 jobs-radar.com (rank 1)
Pattern: `https://jobs-radar.com/en/search?q=<query>&location=<Country|Europe>&range=<today|3d|week|month>`.
Country names work (Italy, Germany, Ireland, Spain, Netherlands, Portugal, Poland). `Europe` also works but is a name match, so run both `Europe` and `Italy`.

- FDE: https://jobs-radar.com/en/search?q=forward+deployed+engineer&location=Europe&range=month
- SE: https://jobs-radar.com/en/search?q=solutions+engineer&location=Europe&range=month
- IE: https://jobs-radar.com/en/search?q=integration+engineer&location=Europe&range=month
- AE: https://jobs-radar.com/en/search?q=automation+engineer&location=Europe&range=month
- AI: https://jobs-radar.com/en/search?q=AI+engineer&location=Europe&range=month
- Italy variants: swap `location=Europe` for `location=Italy`.
The UI also has an "exclude keywords" field. Seniority is not URL-filterable, so filter client-side.

#### 4b.2 hiring.cafe (rank 2, needs a browser)
URL carries a JSON `searchState`: Europe region, Remote, last 14 days. Change `searchQuery` only.

- FDE: https://hiring.cafe/?searchState=%7B%22searchQuery%22%3A%22forward%20deployed%20engineer%22%2C%22workplaceTypes%22%3A%5B%22Remote%22%5D%2C%22dateFetchedPastNDays%22%3A14%2C%22locations%22%3A%5B%7B%22id%22%3A%22eu%22%2C%22formatted_address%22%3A%22Europe%22%2C%22types%22%3A%5B%22continent%22%5D%2C%22address_components%22%3A%5B%7B%22long_name%22%3A%22Europe%22%2C%22short_name%22%3A%22Europe%22%2C%22types%22%3A%5B%22continent%22%5D%7D%5D%2C%22options%22%3A%7B%22flexible_regions%22%3A%5B%22european_union%22%5D%7D%7D%5D%7D
- SE: https://hiring.cafe/?searchState=%7B%22searchQuery%22%3A%22solutions%20engineer%22%2C%22workplaceTypes%22%3A%5B%22Remote%22%5D%2C%22dateFetchedPastNDays%22%3A14%2C%22locations%22%3A%5B%7B%22id%22%3A%22eu%22%2C%22formatted_address%22%3A%22Europe%22%2C%22types%22%3A%5B%22continent%22%5D%2C%22address_components%22%3A%5B%7B%22long_name%22%3A%22Europe%22%2C%22short_name%22%3A%22Europe%22%2C%22types%22%3A%5B%22continent%22%5D%7D%5D%2C%22options%22%3A%7B%22flexible_regions%22%3A%5B%22european_union%22%5D%7D%7D%5D%7D
- IE: https://hiring.cafe/?searchState=%7B%22searchQuery%22%3A%22integration%20engineer%22%2C%22workplaceTypes%22%3A%5B%22Remote%22%5D%2C%22dateFetchedPastNDays%22%3A14%2C%22locations%22%3A%5B%7B%22id%22%3A%22eu%22%2C%22formatted_address%22%3A%22Europe%22%2C%22types%22%3A%5B%22continent%22%5D%2C%22address_components%22%3A%5B%7B%22long_name%22%3A%22Europe%22%2C%22short_name%22%3A%22Europe%22%2C%22types%22%3A%5B%22continent%22%5D%7D%5D%2C%22options%22%3A%7B%22flexible_regions%22%3A%5B%22european_union%22%5D%7D%7D%5D%7D
- AE: https://hiring.cafe/?searchState=%7B%22searchQuery%22%3A%22automation%20engineer%22%2C%22workplaceTypes%22%3A%5B%22Remote%22%5D%2C%22dateFetchedPastNDays%22%3A14%2C%22locations%22%3A%5B%7B%22id%22%3A%22eu%22%2C%22formatted_address%22%3A%22Europe%22%2C%22types%22%3A%5B%22continent%22%5D%2C%22address_components%22%3A%5B%7B%22long_name%22%3A%22Europe%22%2C%22short_name%22%3A%22Europe%22%2C%22types%22%3A%5B%22continent%22%5D%7D%5D%2C%22options%22%3A%7B%22flexible_regions%22%3A%5B%22european_union%22%5D%7D%7D%5D%7D
- AI: https://hiring.cafe/?searchState=%7B%22searchQuery%22%3A%22AI%20engineer%22%2C%22workplaceTypes%22%3A%5B%22Remote%22%5D%2C%22dateFetchedPastNDays%22%3A14%2C%22locations%22%3A%5B%7B%22id%22%3A%22eu%22%2C%22formatted_address%22%3A%22Europe%22%2C%22types%22%3A%5B%22continent%22%5D%2C%22address_components%22%3A%5B%7B%22long_name%22%3A%22Europe%22%2C%22short_name%22%3A%22Europe%22%2C%22types%22%3A%5B%22continent%22%5D%7D%5D%2C%22options%22%3A%7B%22flexible_regions%22%3A%5B%22european_union%22%5D%7D%7D%5D%7D
Notes: default location is the United States if `locations` is dropped. Results carry employer, region, remote flag, YOE and apply link to the employer ATS. For Italy only, replace the location object's `formatted_address` and `short_name` with `Italy` and the type with `country` (unverified, test once). Cloudflare blocks curl and WebFetch, a real browser passes.

#### 4b.3 jobdex.io (rank 3)
- Remote from Italy (409 roles, 98% no German): `https://jobdex.io/remote-from/Italy`
- n8n: `https://jobdex.io/stack/n8n` (26) · LLM: `https://jobdex.io/stack/LLM` (495) · Zapier: `https://jobdex.io/stack/Zapier` · LangChain: `https://jobdex.io/stack/LangChain` · MCP: `https://jobdex.io/stack/MCP` · OpenAI: `https://jobdex.io/stack/OpenAI` · Playwright: `https://jobdex.io/stack/Playwright` · Laravel: `https://jobdex.io/stack/Laravel` · Next.js: `https://jobdex.io/stack/Next.js`
- Junior / English-only / fresh: `https://jobdex.io/seniority/junior` · `https://jobdex.io/english-jobs` · `https://jobdex.io/fresh-jobs`
- Full filter UI (remote policy, language, salary): `https://jobdex.io/jobs`
No title keyword in the URL. Scan each page for FDE / solutions / integration / automation / AI titles and read the language tag (for example "English (B1), Dutch (B1)" means reject).

#### 4b.4 deployaijobs.com (rank 4)
- FDE Europe: `https://deployaijobs.com/jobs?location=Europe` (526) · Italy: `https://deployaijobs.com/jobs?location=Italy` (20)
- SE Europe: `https://deployaijobs.com/jobs?q=solutions+engineer&location=Europe` (20)
- IE: `https://deployaijobs.com/jobs?q=integration+engineer&location=Europe`
- AE: `https://deployaijobs.com/jobs?q=automation+engineer&location=Europe`
- AI: `https://deployaijobs.com/jobs?q=AI+engineer&location=Europe`
- Entry level remote EU: `https://deployaijobs.com/jobs?location=Europe&remote=remote&seniority=junior` (5)
- Other countries: `location=Germany|Ireland|Spain|Netherlands|France|Portugal|Poland|Sweden`.
Only `location=Italy`, `location=Europe`, `q=solutions...`, `remote=remote`, `seniority=` were run and confirmed. The other `q=` values use the same param.

#### 4b.5 deployedjobs.com (rank 5)
`https://deployedjobs.com/?location=Italy` · `?location=Germany` · `?location=Ireland` · `?location=Spain` · `?location=Netherlands` · `?location=France` · `?location=Sweden`. Facets on the page: Applied AI Engineer, FDE, Solutions / Sales Engineer, Implementation / Delivery Engineer, plus Remote-eligible and Junior/Associate toggles (UI only).

#### 4b.6 n8n community Jobs (rank 6)
- Latest topics JSON: `https://community.n8n.io/c/jobs/13.json?order=created` (30 topics per page; titles starting `[HIRING]` are employers, `[For Hire]` are freelancers, skip those)
- Human page: `https://community.n8n.io/c/jobs/13`
- Search JSON: `https://community.n8n.io/search.json?q=HIRING%20Europe%20category%3Ajobs%20order%3Alatest` (43 topics at test time)
Fit check per topic: look for "Europe", "EU", "remote", pay, and German-language lines.

#### 4b.7 ATS-direct (ranks 7-16): WebSearch `site:` queries
Run each host with each role phrase. Add `Europe` or `Italy` or `remote EMEA`. Verified to return live roles:

| Host | Query template (swap the role) | Notes / feed |
|---|---|---|
| jobs.eu.lever.co | `site:jobs.eu.lever.co "solutions engineer" remote Europe` | `https://api.eu.lever.co/v0/postings/<co>?mode=json` (200, tested everseen) |
| ats.rippling.com | `site:ats.rippling.com "forward deployed engineer" OR "solutions engineer" Europe remote` | `https://ats.rippling.com/api/v2/board/<slug>/jobs` (200) |
| jobs.gem.com | `site:jobs.gem.com "solutions engineer" OR "forward deployed engineer" OR "AI engineer" Europe remote` | Gem board API path guess returned 302, read the page |
| teamtailor.com | `site:teamtailor.com "AI engineer" OR "automation engineer" remote Europe English` | `https://<co>.teamtailor.com/jobs.rss` (200) |
| pinpointhq.com | `site:pinpointhq.com "forward deployed" OR "solutions engineer" OR "AI engineer" remote Europe` | `https://<co>.pinpointhq.com/postings.json` (200) |
| jobs.personio.de | `site:jobs.personio.de OR site:jobs.personio.com "AI engineer" OR "automation engineer" OR "solutions engineer" remote language=en` | `https://<co>.jobs.personio.de/xml` (200). German (m/w/d) titles = language gate |
| breezy.hr | `site:breezy.hr "solutions engineer" OR "AI engineer" OR "automation engineer" remote Europe` | `https://<co>.breezy.hr/json` (200) |
| bamboohr.com | `site:bamboohr.com/careers "AI engineer" OR "solutions engineer" remote Europe` | page only |
| homerun.co | `site:homerun.co "forward deployed" OR "customer engineer" OR "solutions engineer"` | page only |
| myworkdayjobs.com | `site:myworkdayjobs.com "solutions engineer" OR "AI engineer" remote Italy English` | account at apply = `login` blocker |

Per role (swap into any row): `"forward deployed engineer"`, `"solutions engineer"`, `"integration engineer"`, `"automation engineer"` (add `n8n OR "Make" OR Zapier` to dodge QA/industrial results), `"AI engineer"` (add `agents OR LLM`).

#### 4b.8 remotery.co (rank 17)
- AI Europe: `https://www.remotery.co/remote-ai-engineer-jobs/europe-remote` · AI Italy: `https://www.remotery.co/remote-ai-engineer-jobs/italy-remote`
- SE Europe: `https://www.remotery.co/remote-solutions-engineer-jobs/europe-remote` · SE Italy: `https://www.remotery.co/remote-solutions-engineer-jobs/italy-remote`
`forward-deployed-engineer`, `integration-engineer`, `automation-engineer` and `implementation-engineer` slugs 404, so cover those via #1-#5.

#### 4b.9 airemotelyjobs.com (rank 18)
`https://airemotelyjobs.com/?region=Europe` (42 roles at test time). `q=` is ignored, scan titles.

#### 4b.10 latchhire.com (rank 19)
FDE: `https://latchhire.com/board/fde` · SE: `https://latchhire.com/board/solutions_eng` · Agentic: `https://latchhire.com/board/agentic` · GTM engineer: `https://latchhire.com/board/gtm_eng` · Solutions architect: `https://latchhire.com/board/solutions_arch` · AI/ML: `https://latchhire.com/board/ml_ai` · pagination `?page=N`. Rows show location and date, filter to EU/remote and drop Staff/Sr/Principal in code.

#### 4b.11 thehub.io (rank 20)
`https://thehub.io/jobs?search=solutions+engineer&remote=true` · `https://thehub.io/jobs?search=ai+engineer&remote=true` · `https://thehub.io/jobs?search=automation&remote=true` · `https://thehub.io/jobs?search=forward+deployed&remote=true` · `https://thehub.io/jobs?search=integration+engineer`. Unfiltered `search=zzqq` returns 0, so the filter is real.

#### 4b.12 YC (rank 21)
`https://www.ycombinator.com/jobs/location/europe` · `https://www.ycombinator.com/jobs/location/remote` · role pages `https://www.ycombinator.com/jobs/role/software-engineer` and `/jobs/role/solutions-engineer` (generic software feed, scan for FDE / solutions / applied AI titles). No keyword param.

#### 4b.13 HN (rank 22)
- `https://hnhiring.com/search?q=forward+deployed` (US-heavy, add `europe` or `remote` and scan)
- Algolia (current thread id from `https://hn.algolia.com/api/v1/search_by_date?tags=story,author_whoishiring`): `https://hn.algolia.com/api/v1/search?tags=comment,story_49922569&query=europe%20remote%20solutions&hitsPerPage=50`. Swap `49922569` each month (October 2026 now).

#### 4b.14 Remaining boards
- FDE Pulse: `https://fdepulse.com/jobs/` (filter rows by city, seniority Mid/Junior, remote).
- nodesk: `https://nodesk.co/remote-jobs/europe/` · `https://nodesk.co/remote-jobs/emea/` · `https://nodesk.co/remote-jobs/ai/`
- FDE Field Guide: `https://fde.traversaal.ai/` (Europe tab is UI-only)
- fwddeploy: `https://www.fwddeploy.com/s/remote-jobs` · `https://www.fwddeploy.com/s/germany-jobs` · `https://www.fwddeploy.com/s/amsterdam-north-holland-the-netherlands-jobs`
- eurotechjobs: `https://www.eurotechjobs.com/jobs/italy` · `https://www.eurotechjobs.com/jobs/search?keywords=solutions+engineer` (experience facet `0-2 Years`, workplace facet `Remote` are UI-only)
- Berlin Startup Jobs: `https://berlinstartupjobs.com/engineering/` · `https://berlinstartupjobs.com/?s=ai`
- IrishJobs / Jobs.ie: `https://www.irishjobs.ie/jobs/solutions-engineer` · `https://www.jobs.ie/jobs/ai-engineer`
- EURES (browser): `https://europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&keywordsEverywhere=solutions%20engineer&lang=en` (+ `&locationCodes=it` for Italy). Expect noise.

#### 4b.15 VC portfolio boards, Getro (rank 24)
Pattern `https://<host>/jobs?q=<query>`. `q` filters server-side (Index: 10,876 jobs unfiltered, 179 for "solutions engineer"). Location is **not** a working URL param, so open the page and use the location chip or read each row's location.

| Fund | Host | Seen at test |
|---|---|---|
| Atomico | `https://careers.atomico.com/jobs?q=solutions%20engineer` | live |
| Speedinvest | `https://careers.speedinvest.com/jobs?q=solutions%20engineer` | live |
| Creandum | `https://careers.creandum.com/jobs?q=solutions%20engineer` | live |
| Point Nine | `https://jobs.pointnine.com/jobs?q=solutions%20engineer` | live |
| Earlybird | `https://jobs.earlybird.com/jobs?q=solutions%20engineer` | live |
| Index Ventures | `https://indexventures.getro.com/jobs?q=solutions%20engineer` | live, large |
| HV Capital | `https://hv.getro.com/jobs?q=ai%20engineer` | live |
| MMC | `https://jobs.mmc.vc/jobs?q=solutions%20engineer` | live, small |
| Northzone | `https://portfolio.northzone.com/jobs?q=ai%20engineer` | live, tiny |

Query swaps for each: `forward%20deployed%20engineer`, `integration%20engineer`, `automation%20engineer`, `ai%20engineer`. Global US-leaning Getro boards also load (`jobs.accel.com`, `jobs.generalcatalyst.com`, `jobs.a16z.com`, `jobs.sequoiacap.com`) but have low EU yield, leave them out.


**Dead or blocked — don't spend calls here:** weworkremotely.com (returns binary),
welcometothejungle.com, landing.jobs, jobicy.com, linkedin.com/jobs (all robots-disallowed),
nofluffjobs.com (403), workatastartup.com (renders fragments only), remotive.com and
workingnomads.com (listing pages render navigation only — no jobs), freelancermap.com (paths 404
without discovery), germantechjobs.de, duunitori.fi, adzuna, jooble, glassdoor (403), indeed
(login wall).

**Moved out of dead on 2026-10-03:** `nodesk.co` (`/remote-jobs/europe/`, `/emea/`, `/ai/` return
200; check the age column, some listings are weeks old) and `wellfound.com` location and role pages
(`wellfound.com/location/europe`, `wellfound.com/role/l/ai-engineer/europe`; query params are
still ignored, so use the path pages).

**Reachable only in a real browser (Chrome DevTools browser agent, never curl or WebFetch):**
hiring.cafe and the EURES portal (europa.eu/eures job search, jobs.eu).

Freelance marketplaces — Malt, Braintrust, Contra, Upwork, Toptal — are login-walled or
client-rendered. Don't burn a sweep on them. Contract work comes through the ATS contract
queries in §3, contract-first shops with public boards (e.g. **G2i** on Ashby), and the
part-time/contract listings on **join.com** and **euremotejobs.com**.

---

## 5. Public JSON APIs — use these to verify

These fetch as text and expose exactly the fields needed to confirm a posting is live:

- **Greenhouse:** `https://boards-api.greenhouse.io/v1/boards/<token>/jobs?content=true` → `absolute_url`, `updated_at`, locations. Best freshness check available.
- **Ashby:** `https://api.ashbyhq.com/posting-api/job-board/<org>?includeCompensation=true` → `isRemote`, `isListed`, `publishedAt`, `compensation`.
- **Lever:** `https://api.lever.co/v0/postings/<co>?mode=json` → `workplaceType` (Remote/Hybrid), location. Fails on very large aggregator boards.
- **Workable:** `https://apply.workable.com/api/v1/widget/accounts/<subdomain>?details=true` → the only readable route into Workable.
- Lever EU: `https://api.eu.lever.co/v0/postings/<co>?mode=json`
- Rippling: `https://ats.rippling.com/api/v2/board/<slug>/jobs`
- Pinpoint: `https://<co>.pinpointhq.com/postings.json`
- Personio (.de host): `https://<co>.jobs.personio.de/xml`
- Breezy: `https://<co>.breezy.hr/json`
- Teamtailor: `https://<co>.teamtailor.com/jobs.rss`
- n8n community: `https://community.n8n.io/c/jobs/13.json`

**WebFetch truncates long JSON**, and its summariser will quietly under-report: asking
"list all jobs" on a big board returned 7 of N and omitted roles that exist. Ask a *targeted*
question instead — "does this board currently list a Forward Deployed Engineer role, and what
is its location and posted date?"

**A negative answer from a board API is not evidence on its own.** Truncation produces
*fabricated* negatives — one read stated four target roles were "not present" when the board
simply hadn't been fully returned. Before concluding a role is closed, either get two
independent reads that agree, or corroborate with a differently-shaped source. Concluding
"closed" wrongly costs him a real opportunity, so the burden of proof sits on the negative.

---

## 6. Verification traps

Search indexes run stale across every ATS, so a posting found in search may already be gone.
These are the specific failure modes, and the first one is dangerous because the fetch
*succeeds*:

1. **Greenhouse closed postings degrade to the board index.** Fetching a dead job URL returns the company's entire open-roles list with the target role absent, and nothing flags it. **Detection rule: if a single-posting fetch comes back describing many different jobs, the posting is closed.** Drop it.
2. **Personio closed postings hard-404** even while still indexed in search. Clean failure — just drop.
3. **Lever snippets misstate location.** Fetch the posting and read the location from the page body.
4. **"Remote" ≠ eligible.** Read the eligibility sentence, not the word "Remote" in the title. Titles like "AI Automation Engineer (Remote – ES/UK only)" are common, and boards sometimes label a region-locked role "worldwide".
5. **Aggregators masquerade as employers.** Jobgether, Jobgether-on-Lever, and similar reposts have no named end client. Skip them; find the original posting if the role looks good.
6. **Himalayas orders results non-chronologically** — page 1 mixed "2 mins ago" with "27 days ago". Read the date on each row rather than trusting position.
7. **Ashby pages return JS shells intermittently.** `meta-title: Jobs` or "You need to enable JavaScript to run this app" means the fetch failed, *not* that the role closed. Go to the org's posting API (§5) — and remember §5's rule that a negative there needs a second read. Three failures like this nearly cost the highest-relevance company of one sweep.

---

## 7. Freshness

- Minute-level ages: euremotejobs, remoterocketship, himalayas, aijobs.net (parse from the page).
- Sortable by recency in the URL: only `remoterocketship.com/?sort=DateAdded` is verified.
- Programmatic date filtering: only via the JSON APIs (`created_at` / `date` / `epoch` / `updated_at`).
- No board tested exposes a verified "posted within N days" parameter — filter client-side.
