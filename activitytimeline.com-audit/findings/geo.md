# AI Search Readiness (GEO): 61 / 100

Derived from the seo-geo checklist weights (a heuristic, not a predicted citation rate): Citability 62 x 25%, Structural readability 60 x 20%, Multi-modal 60 x 15% (only partly checked), Authority and brand signals 45 x 20%, Technical accessibility 80 x 20% = 61.5.

Audit date 19 Nov 2026. Evidence: saved live HTML (11:52 UTC), 45 extra curl requests, one Playwright render of /pricing. Three pages not in the saved set were fetched because they carry the cost topic: /finances, /budget-planning, /blog/jira-cost-management.

## What could not be measured today

- **No assistant was queried and Sitechecker AI Chats was unreachable.** Mention rates below are the last scorecard only (week of 9 Nov, window 6 Oct-2 Nov): AI mention rate 56.2% (Tempo 75.4%), weekly 61.5%; AI Overview cited keywords 15 of 188; cost and budget prompt mention rate 7.9% (6 Oct-3 Nov baseline, 0 mentions on all four "cost management tools" prompts on 9 Nov). No newer value exists; nothing here is a new measurement.
- No platform scores (Google AIO, ChatGPT, Perplexity, Copilot): not measured, so none given.
- help.activitytimeline.com (its llms.txt, the raw `.md` copies, 13 llms.txt links) and marketplace.atlassian.com (the listing, the most cited source: 443 citations vs 63 for the site, Sitechecker 29 Sep-1 Nov): not checked, hosts blocked. The `.md` noindex-header issue from 9 Nov stays open and unverified.
- Crawler tests used spoofed user agents from a cloud IP. They show there is no user-agent rule; they cannot show how Cloudflare treats the real, verified bot IPs. Server logs or Cloudflare's AI crawl panel would settle it.
- Brand mentions on YouTube, Reddit, Wikipedia, LinkedIn: not checked (no search tool used). Bing index state: not checked.
- Locale pages (es/fr/pt) beyond a brand-spelling count; blog posts other than /blog/jira-cost-management.

## What works

- **Every AI crawler tested gets HTTP 200 and full HTML** on /cost-tracking, /pricing and /llms.txt: OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User, Googlebot, bingbot, Applebot (search and user-triggered), and GPTBot, ClaudeBot, CCBot, Google-Extended, cohere-ai, meta-externalagent, Amazonbot (training). robots.txt has no AI rule (`User-agent: *`, `Allow: /`, only /order disallowed). No Cloudflare challenge, no `cf-mitigated` header.
- Content is server-rendered: FAQ answers, feature lists and chart descriptions are in the raw HTML (charts carry a full text equivalent, e.g. the October cost walk-through on /cost-tracking).
- The rebuilt solution pages open with a self-contained definition under a "What ... means in ActivityTimeline" H2, carry worked, dated examples (labelled "Sample data"), question FAQs and `dateModified` (2026-11-11 to 2026-11-13).
- /time-tracking has the model passage: H3 "What Does ActivityTimeline Add to Jira's Built-in Time Tracking?", a 40-word direct answer, then a real `<table>` "Jira on its own / Jira with ActivityTimeline", captioned "November 2026", with an honest caveat line. This is the "where native Jira stops" format an assistant can quote.
- /pricing FAQ gives clean, quotable price sentences ("At 100 users, Standard costs $250 a month ($3,000 a year) or $2,500 on annual billing"), and the Tempo comparison figures match facts.md ($29,855 and $38,950 at 500 users).
- /llms.txt exists (53 links, 200, `text/plain`, `X-Robots-Tag: noindex`, which is right). It is not a Google lever and no major provider confirms using it; it is hygiene.

## AI crawler access (each bot against the capability it governs)

| Bot | Governs | robots.txt | Spoofed-UA fetch |
|---|---|---|---|
| Googlebot | Google Search, AI Overviews, AI Mode | allowed | 200 |
| bingbot | Bing, Copilot | allowed | 200 |
| OAI-SearchBot | ChatGPT Search citability | allowed | 200 |
| ChatGPT-User | ChatGPT user-triggered fetch | allowed | 200 |
| Claude-SearchBot | Claude search citability | allowed | 200 |
| Claude-User | Claude user-triggered fetch | allowed | 200 |
| PerplexityBot / Perplexity-User | Perplexity search / user fetch | allowed | 200 / 200 |
| Applebot | Siri, Spotlight, Safari | allowed | 200 |
| GPTBot | OpenAI training only | allowed | 200 |
| ClaudeBot | Anthropic training only | allowed | 200 |
| Google-Extended | Gemini/Vertex training and grounding (not Search) | allowed | 200 (token only) |
| CCBot, cohere-ai, meta-externalagent, Amazonbot | training | allowed | 200 |
| Bytespider | ByteDance | allowed in robots.txt | **403**, Cloudflare "Attention Required" page |

Bytespider is blocked at Cloudflare while robots.txt allows it: Info only, no KPI depends on it. No Content-Signal line, no RSL licence, no `/llms-full.txt` (404), no Markdown negotiation (`Accept: text/markdown` returns HTML): all optional, none recommended now.

## Findings

### 1. High. /pricing serves a wrong price to crawlers that do not run JavaScript. CONFIRMED
- Evidence: raw HTML of https://activitytimeline.com/pricing: `<span data-pr="std-amt" ...>$1,000</span> / month` with `≈ $2.08 per user per month · 51–100 user tier` under **Standard**, and the same `$1,000 / month`, `≈ $2.08 per user per month` under **Advanced** (`data-pr="adv-amt"`), while the active tab in the same HTML is "10" users. Rendered in Chromium the cards read "$10 / month, Flat price for up to 10 users" and "$15". The static text is a placeholder that the calculator script overwrites. GPTBot, PerplexityBot and ClaudeBot-class fetchers read raw HTML; the strategy already records Google's brand AI Overview quoting a wrong price ("$10 and $15 per user per month", 5 Nov).
- Also on the page: the H1 is "Planner, Timesheets, and Finances." (no brand, no "pricing"), the price grid is `div` rows rather than a `<table>`, has no heading of its own and sits in a toggled panel, and the only JSON-LD is `Organization`.
- Fix: set the static defaults in the Designer to the true 10-user state ($10 and $15 a month, "Flat price for up to 10 users"); rebuild "See prices for every team size" as a real `<table>` with a caption carrying edition, billing, currency and the date ("List prices checked November 2026"), under an H2 such as "ActivityTimeline price by team size"; put "ActivityTimeline pricing" in the H1. Whether the Advanced column stays is Ostap's open question (f07): this finding does not judge those figures.
- KPI: cost and budget prompt mention rate; AI citations on product, pricing or comparison pages. Tier 3.
- Failed if: after the change, `curl` of /pricing still shows "$1,000" next to Standard, or assistants and the brand AI Overview still quote a per-user price that is not on the page four weeks later.

### 2. High. The three cost pages never say where Jira stops, which edition holds Finances, or what it costs. CONFIRMED
- Evidence: /cost-tracking (2,037 words), /finances (2,204) and /budget-planning (2,376) contain no "Advanced Edition", no price and no statement about native Jira. The only native reference is a link label ("How-tos for Jira on its own ... live in the blog") and a tile "Add what Jira doesn't know" on /finances. Both trial lines say "30-day free trial with Finances" without naming the edition. The clear boundary sentence exists only in a blog post: /blog/jira-cost-management, "Jira does not have built-in features to track employee wages, salaries, or labor costs. It has no way to distinguish billable from non-billable hours...". That post in turn names no edition and no price. None of the three has a table (0 `<table>`).
- Why it matters for the 7.9% KPI: a cost prompt ("how do I track project cost or budget in Jira", "which Jira app does budgets, what does it cost") needs three facts in one quotable block: Jira has no cost or budget feature, ActivityTimeline Finances adds it from Jira worklogs, it is part of the Cloud Advanced Edition at a dated price. Today those facts sit on three different URLs.
- Fix (copy drafts, then Webflow): on each of the three pages add, high on the page, a section built like the /time-tracking one: H2 or H3 "Can Jira track project cost and budget on its own?", a 40-60 word answer, a `<table>` "Jira on its own / Jira with ActivityTimeline" (rates per person, salaries, expenses, billable vs non-billable, budget per project/epic/filter, budget vs spend, forecast, margin, ledger export), captioned with the month, plus one line "Finances is part of the ActivityTimeline Advanced Edition on Jira Cloud" (f03, f04) and a dated price pointer to /pricing. Use only f07-covered figures (1,000 users, $21,950 a year, dated) until Ostap answers the open Advanced-price question. Check the native-Jira column against Atlassian's docs and the help centre export before publishing, and run the fact lint.
- KPI: cost and budget prompt mention rate (7.9% to 40%+); AI citations on product pages. Tier 2 draft, tier 3 to ship.
- Failed if: Sitechecker cost-prompt mention rate is still under 20% (the cost-hub interim target) 6-8 weeks after shipping, or no cost page is cited on a cost prompt.

### 3. High. llms.txt is behind the site: 1 redirecting link, 1 link off-site in a 301, and 9 live commercial pages missing. CONFIRMED
- Evidence (https://activitytimeline.com/llms.txt against sitemap.xml and live status):
  - `[Jira reports](https://activitytimeline.com/advanced-jira-reports)` returns 301 to /reports.
  - `[Jira project reports](https://activitytimeline.com/how-to-create-jira-project-reports)` returns 301 to /blog/how-to-create-jira-project-reports.
  - Missing although live and in the sitemap: /reports, /tempo-alternative, /how-it-works, and the newer pages **/finances, /budget-planning**, /resource-utilization, /planner, /timesheets, /workspace. The Tempo section lists five blog posts and not the comparison page.
  - Cost coverage is one product page and one post; /blog/jira-budget-tracking-bridging-operations-and-finance and /blog/jira-financial-management are absent.
  - Wording: the opening sentence is a longer variant of f01 ("...time tracking, timesheet reporting, and project cost management app for Jira Cloud and Jira Data Center"), and the file states no price, trial, rating or certification fact, only "consult the pricing page". Nothing in it contradicts facts.md; nothing in it answers a cost question either.
- Fix: replace the two redirecting URLs, add the nine pages (cost group first), use the f01 sentence verbatim, and add a short dated "Key facts" block from confirmed facts only (f03, f04, f05 "from $10 a month for up to 10 users", f11, f13 with date, f16, f17, f18). Add llms.txt to the checklist for every new or moved commercial URL. Expect no effect in Google (Google states it ignores the file).
- KPI: AI citations on product, pricing or comparison pages (weak lever, hygiene). Tier 3 (reversible file edit).
- Failed if: the next gate run still lists a commercial URL as "not in llms.txt" or finds a non-200 link.

### 4. Medium. Product definition and brand spelling are not repeated the same way. CONFIRMED
- Evidence:
  - f01 wording appears on /home ("ActivityTimeline is a resource planning, capacity management and time tracking app for Jira, built by Reliex"), /time-tracking and /reports. /how-it-works says "a Capacity planning & Time tracking app for Jira" (also in its `SoftwareApplication` description); /features opens with a different sentence; /pricing, /tempo-alternative, /capacity-planning, /resource-management, /cost-tracking, /timeline-for-jira have no "ActivityTimeline is ..." sentence at all. No page states "for Jira Cloud and Data Center" in the definition as f01 does.
  - "Activity Timeline" with a space: twice in the shared header on every page except /tempo-alternative (known, 19 Nov gate), 6 times in the capacity guide (FAQ and related-post titles, e.g. "How to do Jira Capacity Planning with Activity Timeline?"), 11-14 times on /es, /fr, /pt. Quotes from reviews stay as they are.
  - JSON-LD: `Organization` is "Reliex" with url activitytimeline.com on some pages and "ActivityTimeline" on others; `sameAs` (home only) has LinkedIn, Facebook, X and YouTube but not the Marketplace listing, the source assistants cite most.
  - Footer on every page: "Admin Guide Server/DC", "User Guide Server/DC" (f10: do not mention Server).
- Fix: one definition sentence (f01) as the first body sentence or FAQ answer on every commercial page and in `SoftwareApplication`/`Organization` descriptions; fix the header component once; correct the guide's own headings; add the listing URL to `sameAs`; rename the footer links to "Data Center". Schema details belong to the schema specialist.
- KPI: AI mention rate; brand clicks. Tier 3.
- Failed if: a grep of the 12 commercial pages still finds "Activity Timeline" outside quotes, or fewer than 12 carry the f01 sentence.

### 5. Medium. Solution-page JSON-LD points at URLs that do not exist. CONFIRMED
- Evidence: `WebPage`, `#webpage`, `#faq` and `#breadcrumb` nodes use `https://activitytimeline.com/solutions/<slug>` on /capacity-planning, /cost-tracking, /resource-management, /time-tracking, and `.../solutions/jira-timelines` on /timeline-for-jira. `https://activitytimeline.com/solutions/cost-tracking` returns 404.
- Fix: set `url` and `@id` to the live canonical URL on the five pages (Webflow schema channel, `bulk_update_pages_schema_markup`). Hand to the schema specialist.
- KPI: AI citations on product pages; commercial pages indexed. Tier 3.
- Failed if: `query_pages_schema_markup` or a grep still returns "/solutions/".

### 6. Medium. Guides and blog posts carry weak or broken freshness and structure signals. CONFIRMED on the pages read, LIKELY template-wide
- Evidence:
  - The three guides, which hold most of the site's AI citations (time-tracking guide 32, resource guide 11, Ahrefs 5 Nov), have `dateModified` equal to `datePublished` (2026-02-27, 2025-11-25, 2026-02-13), 0 tables, generic H2s ("The Advantages of Capacity Planning", "Conclusion") and, for two of them, old descriptions ("Our guide explores how to optimize resource management in Jira...").
  - /blog/jira-cost-management: `"datePublished": "Jun 10, 2026T10:00:15+02:00"` (not a valid ISO 8601 date), no `dateModified`; raw HTML shows "0 min read" and a table of contents reading "Example H2 / Example H3" until a script fills it. The same blog template was noted on 5 Nov for another post.
- Fix: correct the blog template date format and add `dateModified`; when a guide is rebuilt (already planned, pillar-guides-rebuild), give it the bulk-update pattern that earned AI Overview citations in two days: current Cloud steps, a hard limit, a "what Jira can't do" section, a native-vs-app table. No new how-to posts are proposed.
- KPI: AI Overview and assistant citations kept on the guides; AI mention rate. Tier 3.
- Failed if: the guides' Ahrefs AIO citation counts fall after the rebuild, or the Rich Results test still rejects the blog date.

### 7. Low. The same Tempo prices carry two dates. CONFIRMED
- Evidence: /tempo-alternative: "Atlassian Marketplace list prices for Jira Cloud, annual billing, USD, 1 October 2026"; /pricing: the same $29,855 and $38,950 "as of November 2026" and "List prices checked November 2026". facts.md records the source as the 1 Oct 2026 price brief. /pricing hero says 122 reviews, /tempo-alternative 125 (known).
- Fix: one date and one review count on both pages, from facts.md (f13, f25), after someone re-checks the Tempo list prices if "November" is to stay.
- KPI: cost and budget prompt mention rate; AI citations on comparison pages. Tier 3.
- Failed if: the fact lint still reports two dates or two review counts.

### 8. Info. Open questions this audit does not settle
- Advanced Edition prices on /pricing and /tempo-alternative ($12,450 at 500 users and others) are outside f07; "10,000+ teams" is confirmed (f15) and appears as a plain figure; "Structure Gantt" on the home integrations block touches open fact f22; Premium Support in the Advanced list touches the 5 Nov f07 note. All are questions for Ostap, not errors.
- The cost pages use invented sample client names inside examples labelled "Sample data". They are not customers; keep the label next to every example so an assistant does not quote them as case results.

## Passages an assistant can quote for cost and budget questions today

| Question | Best passage found | Gap |
|---|---|---|
| Can Jira track project cost? | /blog/jira-cost-management, first two paragraphs | Not on any product page; post has an invalid date and no edition or price |
| How does ActivityTimeline calculate cost? | /cost-tracking FAQ "How does ActivityTimeline calculate project cost?" (48 words, self-contained) | Good |
| What is the difference between cost tracking and budget planning? | /cost-tracking FAQ and the H2 section | Good |
| What does budget management in Jira involve? | /budget-planning H2 "What Is Project Budget Management in Jira?" | No native-Jira boundary |
| What does ActivityTimeline cost? | /pricing FAQ "How is ActivityTimeline priced?" and the 100-user example | Raw HTML cards say "$1,000 / month" (finding 1); grid is not a table |
| Which edition includes Finances and what does it cost? | /pricing FAQ "What's the difference between Standard and Advanced?" | Not stated on /cost-tracking, /finances, /budget-planning |
| ActivityTimeline vs Tempo cost | /pricing and /tempo-alternative FAQ, dated list prices | Two dates (finding 7) |

## Off-site (from the memory, not re-measured)

Assistants cite the Marketplace listing (443), Atlassian Community (295) and Tempo's help (216) ahead of activitytimeline.com (63). The cost story therefore also has to be on the listing (a Finances highlight with the same sentence as finding 2) and in the help centre's Finances articles. Both are Ostap's surfaces (tier 3, listing copy) and neither could be read today.

## Top 5 changes by expected effect

1. Fix the static price placeholders on /pricing and make the price grid a dated table (finding 1). Small.
2. Add the "Jira on its own vs with ActivityTimeline" block with edition and dated price to /cost-tracking, /finances, /budget-planning (finding 2). Medium.
3. Bring llms.txt up to date, cost pages first (finding 3). Small.
4. One f01 definition and one brand spelling everywhere, listing in `sameAs` (finding 4). Small.
5. Correct the `/solutions/` JSON-LD URLs and the blog date format (findings 5, 6). Small.
