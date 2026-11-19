# SXO findings: activitytimeline.com home and commercial pages, 19 Nov 2026

**SXO Gap Score: 62 / 100** (separate from the SEO Health Score).
Derived as the mean of 12 page scores. Each page is scored on page-type fit against the intent the ownership map (7 Nov 2026) gives it (20), who it is for (10), what it does that native Jira does not (20), price (15), proof (15) and next step (20). The generic rubric scores against the live SERP; no SERP data was available today, so page type is judged against the Lab's own intent and ownership maps and every SERP-dependent call is marked.

Sources: saved live HTML (curl, 19 Nov 2026 about 11:52 UTC) for the 12 pages; 7 extra fetches at about 12:10 UTC (/start-trial, /planner, /timesheets, /finances, /workspace, /resource-utilization, /budget-planning); `seo-strategy/intent-map-2026-11-05.csv`, `ownership-map-2026-11-07.csv`, `site-structure-proposal-2026-11-10.md`, `decisions/2026-11-10-structure-answers.md`; `facts.md`; 34 call summaries in `customer-calls/summaries/` (meeting evidence, 411 need rows, not product facts). Read-only; nothing changed.

## Page scores

| Page | Intent it is meant to own (ownership map) | Page type today | Fit | Who | vs Jira | Price | Proof | Next step | Score |
|---|---|---|---|---|---|---|---|---|---|
| / | What is ActivityTimeline and what does it do? (brand, defend) | product overview | 18 | 9 | 8 | 7 | 14 | 19 | **75** |
| /pricing | How much does it cost (Cloud, Data Center, Advanced)? | pricing | 15 | 8 | 14 (vs Tempo and a tool stack) | 12 | 11 | 18 | **78** |
| /features | product layer, feature index | collection | 17 | 6 | 4 | 6 | 8 | 18 | **59** |
| /capacity-planning | Which Jira app/plugin does capacity planning? (solution-aware) | solution page | 15 | 3 | 9 | 2 | 8 | 19 | **56** |
| /time-tracking | Which Jira time tracking app/plugin should I use? | solution page | 17 | 6 | 19 | 10 | 10 | 19 | **81** |
| /resource-management | Which Jira resource management plugin/app? | solution page | 16 | 9 | 3 | 2 | 5 | 19 | **54** |
| /cost-tracking | Which Jira app does cost / financial management? | solution page | 16 | 9 | 4 | 1 | 5 | 18 | **53** |
| /timeline-for-jira | Which Jira timeline/roadmap/Gantt tool? (map: folds into /planner) | solution page | 12 | 9 | 15 | 2 | 5 | 19 | **62** |
| /reports (was /advanced-jira-reports) | Reports module page (map: new, phase 2) | module page with a job-named H1 | 13 | 2 | 10 | 3 | 5 | 18 | **51** |
| /how-it-works | none of its own (map: folds into the product overview) | legacy explainer, 604 words | 6 | 2 | 3 | 0 | 3 | 16 | **30** |
| /schedule-demo | demo (next step) | conversion page, 102 words | 16 | 4 | 10 (n/a, neutral) | 8 (n/a, neutral) | 2 | 16 | **56** |
| /tempo-alternative | Best alternative to Tempo; Tempo vs ActivityTimeline | comparison hub | 18 | 7 | 17 (vs Tempo) | 14 | 10 | 19 | **85** |

## What works (keep)

- **Next step is clear everywhere.** Every page pairs "Start free trial" and "Schedule demo" in the hero and at the end; the header carries Pricing, Schedule demo and Start Free Trial. Demo facts match f12 (25 minutes, 10 attendees, four languages).
- **/time-tracking is the model page.** It has the only native comparison: a table "Jira on its own / Jira with ActivityTimeline", dated November 2026, plus an FAQ "Does Jira have built-in time tracking?", a pricing FAQ, "See pricing", and "Rated 4.7/5 from 125 reviews". The other job pages should copy its pattern.
- **/tempo-alternative** shows dated, sourced prices ("Marketplace list prices, Oct 2026"), a capability table, a migration FAQ and per-button tracking on the trial link.
- **/pricing FAQ answers what callers ask**: which users count ("you pay for that tier, not only for the people who open ActivityTimeline"), quotes and invoices, moving between editions, Data Center.
- **Home** defines the product in one paragraph (f01 wording), labels each module with its audience ("For PMO and delivery leads", "For finance and project owners"), and has reviews, case studies and a security block.
- **Worked examples with numbers** on every job page, and honest FAQs ("Does ActivityTimeline show dependencies?", "We already use Jira Plans or a Gantt app. Do we need both?").

## Findings

### 1. High · CONFIRMED · The three cost pages never say that Finances needs the Advanced Edition
- **Evidence:** the word "Advanced" does not appear in the body of https://activitytimeline.com/cost-tracking, /finances or /budget-planning (0 matches each), nor on /features or the home page. /cost-tracking FAQ "How do we try it?": "the trial includes Finances and needs no credit card". Home hero: "30-day free trial with all five modules". f03 and f04 (confirmed): Finances is part of the Advanced Edition on Cloud. /pricing and /tempo-alternative do say it; llms.txt says it.
- **Buyer language:** finance calls asked "Is financial functionality available in the trial?" and what is included in the licence.
- **Why it matters:** the cost buyer learns the edition, and the higher price, only on /pricing. An assistant that reads /cost-tracking cannot answer "which edition do I need for cost tracking".
- **Fix:** one sentence in the hero note and one FAQ on each of the three pages, for example "Finances is part of the Advanced Edition on Jira Cloud. The free trial lets you test it." with a link to /pricing; the same line on the Finances block of /features and the home page. Quote no Advanced price until Ostap answers the 19 Nov question on f07.
- **KPI:** mention rate on cost and budget prompts (7.9% → 40%+); AI citations on product pages.
- **Tier:** 2 for the draft, 3 to apply. **Failed if:** on the next AI Chats run, cost prompts that mention ActivityTimeline still give no edition or the wrong one, and /pricing entries from the cost pages do not rise in 4 to 8 weeks.

### 2. High · CONFIRMED · /pricing shows the same wrong placeholder price for both editions in the raw HTML
- **Evidence:** https://activitytimeline.com/pricing, plan cards: `<span data-pr="std-amt" …>$1,000</span> / month`, `≈ $2.08 per user per month · 51–100 user tier`, and the identical text in `data-pr="adv-amt"` and `adv-sub`. The table on the same page gives 100 users as $250 a month or $2,500 a year (Standard) and $350 or $3,500 (Advanced). A script fills the cards after load. The Tempo comparison block shows "0" for all four values before the script runs.
- **Why it matters:** anything that reads the page without running scripts (most AI crawlers, link previews) gets "$1,000 / month" for both editions. The site's stated job is to be the place assistants copy facts from.
- **Fix:** make the static text true for the default selection (the same figures the script writes first), and put real default values in the Tempo block. The script stays.
- **KPI:** AI citations on the pricing page; brand clicks.
- **Tier:** 3. **Failed if:** the raw HTML (Ahrefs `site-audit-page-content` for /pricing) still shows "$1,000" in both cards, or an assistant quotes "$1,000 a month".
- **Not checked:** the rendered default state (the Webflow CDN is blocked here, so pages render without CSS or scripts). The Advanced figures themselves are the open f07 question; this finding does not depend on them.

### 3. High · CONFIRMED · The live site already runs the module and solution structure the memory still records as "on paper"
- **Evidence:** in sitemap.xml and the header menu today: /planner, /workspace, /timesheets, /reports, /finances, at least 14 feature pages under them (for example /planner/bookings, /reports/planned-vs-actual), /resource-utilization and /budget-planning. All seven I fetched return 200, self-canonical, no noindex. `decisions/2026-11-10-structure-answers.md`: "Not a go yet, keep on paper". The ownership map lists /planner, /timesheets, /finances as "(new), P2". The changelog has no entry for any of them.
- **Page-type consequences inside my scope:**
  - /timeline-for-jira and /planner are both live. The map folds the first into the second. Titles: "Jira Timeline for People and Teams Across Projects" and "ActivityTimeline Planner: Resource and Capacity Planning".
  - /reports is a module page (its own tracking tag says `module_page`) with a job H1, "Resource Utilization and Planned vs Actual Reports for Jira", next to /resource-utilization ("Resource Utilization Tracking for Jira Teams in ActivityTimeline", title "Resource Utilization Reports for Jira") and /reports/planned-vs-actual.
  - /cost-tracking ("Project Cost Tracking and Management for Jira Teams in ActivityTimeline"), /finances ("Track Project Cost, Budget and Profitability in Jira") and /budget-planning share the cost question.
  - /how-it-works is still in the main menu although the plan folds it into the overview.
  - The commercial set is no longer 12 URLs.
- **Fix (paper only):** ask Ostap whether the go was given and when; add a changelog entry; add one row per live module and solution page to the ownership map with exactly one buyer question each. Working rule to propose: module pages lead with the module name (brand and product-aware intent), solution pages lead with the job. Change no H1, redirect nothing now. Folding /timeline-for-jira or /how-it-works is tier 4 (Ostap plus a devil's advocate comment).
- **KPI:** commercial pages indexed (the denominator changes); AI citations on each hub's product page.
- **Tier:** 2. **Failed if:** Search Console shows two of these URLs alternating for one query (Sitechecker `gsc_cannibalization`, or Ahrefs `gsc-keywords` filtered by page) 4 to 8 weeks after indexing.

### 4. High · CONFIRMED · "What does it do that Jira does not" is answered on one job page out of seven
- **Evidence:** /time-tracking has the comparison table. /timeline-for-jira shows the contrast in the hero ("first as each project sees it in Jira, then in the ActivityTimeline Planner") and an FAQ. /reports has it only as the ninth FAQ ("Doesn't Jira already have reports?"). /capacity-planning has it only as the fifth FAQ, about Jira Plans, plus a link to the guide ("Native Jira, Jira Plans, where they stop"). /resource-management and /cost-tracking have nothing; home and /features have nothing.
- **Buyer language:** the most asked question on the calls (structure memo, 10 Nov): "Resource planning can also be done in Jira itself, right?"
- **Fix:** give /capacity-planning, /resource-management, /cost-tracking and /reports the /time-tracking block: a short dated table "Jira on its own / Jira with ActivityTimeline", placed before the feature grid. Take the Jira side from the published guides and check every "Jira does not" line against Atlassian's documentation and the help centre export before it is written. Add one sentence on the home page under "What Is ActivityTimeline?".
- **KPI:** AI citations on product pages; buyer-segment clicks; AI mention rate.
- **Tier:** 2 draft, 3 to apply. **Failed if:** the product pages still earn no citation on capacity and cost prompts 8 weeks after the change.
- **Needs the SERP:** whether the native comparison should lead the page depends on what ranks for the "app/plugin" queries. Ahrefs `serp-overview` (country us) for "jira capacity planning tool", "jira resource management plugin", "jira cost tracking".

### 5. High · CONFIRMED · Price is absent from the pages where the buyer decides
- **Evidence:** no price, no pricing sentence and no body link to /pricing on /capacity-planning, /resource-management, /cost-tracking, /timeline-for-jira and /reports (also /planner, /timesheets, /finances, /budget-planning). /features has one link. Only /time-tracking answers "How is ActivityTimeline priced?" ("By the number of Jira users, through the Atlassian Marketplace, billed monthly or annually") and links "See pricing". The header Pricing link is the only route elsewhere.
- **Buyer language:** about 20 of the 411 need rows are pricing or licensing: pricing basis, "which users count for pricing", "whether team members need licenses".
- **Fix:** copy the /time-tracking FAQ and the "See pricing" link to the other job and module pages. State the basis (per Jira user on the site, through the Marketplace) and send the reader to /pricing for figures; hard-code no tier price (f05: read the live page).
- **KPI:** demos booked and 50+ user trials; AI citations on product and pricing pages.
- **Tier:** 3. **Failed if:** GA4 shows no rise in /pricing views that follow a job page in the 4 to 8 weeks after.

### 6. High · CONFIRMED · /how-it-works does not explain how it works, and it is in the main menu
- **Evidence:** https://activitytimeline.com/how-it-works: H2 "Jira Resource Management with Ease"; 604 words; four modules, Finances missing; guide links labelled "Server / Data Center" (f10: Server is not offered, do not mention it); PDF guides under `/docs/connect/`. Its meta description promises "ActivityTimeline syncs with Jira…", the body does not cover install, what is read from and written to Jira, permissions or data. The home FAQ "How does ActivityTimeline work with Jira?" answers more in three sentences.
- **Buyer language:** "Safety of trialing on production", "Data loss if the plugin is removed after the trial", "How to start the trial", "Who can see what".
- **Fix:** draft a rewrite as the buyer's sequence: a Jira admin installs from the Marketplace → choose projects → what is read and what is written back → who sees what → what stays in Jira if the app is removed → trial → editions. Every statement checked against the help centre export. Remove "Server". Folding the page into /features instead is tier 4.
- **Also:** the shared header carries "Admin Guide - Server/DC" and "User Guide - Server/DC" on every page (seen on /capacity-planning): one component, same f10 point.
- **KPI:** demos and 50+ user trials; brand clicks.
- **Tier:** 2 draft, 3 to apply. **Failed if:** the page still earns no clicks and no trial or demo click-throughs 8 weeks after.

### 7. Medium · CONFIRMED · Proof stops at the home page
- **Evidence:** no review quote, testimonial or case-study link in the body of any job or module page (0 links to /case-studies on all seven). Rating: /capacity-planning "4.7/5 on Atlassian Marketplace" (no count), /time-tracking "4.7/5 from 125 reviews". /resource-management, /cost-tracking, /timeline-for-jira and /reports show only "Trusted by 10,000+ teams", "Trust Center" and "View on Atlassian Marketplace". /schedule-demo has no proof at all.
- **Fix:** use the /time-tracking proof strip on the other pages (f13 figure, dated), and add one topic-matched public Marketplace review per page with its "See review" link, credited by role only (f26).
- **KPI:** demos booked and 50+ user trials.
- **Tier:** 3. **Failed if:** demo and trial clicks per page view do not move in 4 to 8 weeks.

### 8. Medium · CONFIRMED · The trial path loses the source page and explains nothing about the Marketplace step
- **Evidence:** every "Start free trial" button points to /start-trial (noindex, H1 "Redirecting to Marketplace..."), which waits 1.5 s and sets `location.href` to the listing with one fixed tag for all pages: `utm_campaign=at_website&utm_medium=referral&utm_source=website_trial`. /tempo-alternative links to the listing directly with a tag per button (`utm_campaign=tempo_alternative&utm_content=trial_hero`). The "View on Atlassian Marketplace" proof links also carry per-page tags (`utm_medium=solution_page`).
- **Why it matters:** the charter KPI "50+ user trials" cannot be traced to a page. And no page says who can start the trial or what happens to Jira data, which callers asked.
- **Fix:** pass the source page through /start-trial into `utm_content` (one script); extend the existing "How do we try it?" FAQ with two checked sentences on who installs it and what happens after 30 days.
- **KPI:** demos booked and 50+ user trials (measurement).
- **Tier:** 3. **Failed if:** the Marketplace referral report still shows one bucket for all website trial clicks.
- **Not checked:** the Marketplace side of the path (host blocked).

### 9. Medium · CONFIRMED · /tempo-alternative: no "When Tempo is the better fit", and its Data Center answer disagrees with /pricing
- **Evidence:** no such section or wording on https://activitytimeline.com/tempo-alternative (the profile requires it; noted missing at launch on 30 Oct). FAQ there: "We're on Data Center. Yes, ActivityTimeline runs on Data Center too. Book a call and we scope the Tempo migration for your instance." /pricing FAQ: "the Advanced edition and the Tempo import are on Jira Cloud".
- **Fix:** ask Ostap which statement is right, then align both pages; draft a short "When Tempo is the better fit" block (2 or 3 honest cases, checked with the product team).
- **KPI:** AI citations on the comparison page; demos booked.
- **Tier:** 2 draft, 3 to apply. **Failed if:** the page is still not cited on "Tempo alternative" prompts 8 weeks after (launch re-checks are due 27 Nov and 25 Dec).
- **Needs the SERP:** page type for "tempo alternative" and "tempo timesheets alternatives" (single-vendor page or listicle). Ahrefs `serp-overview` for both, country us.

### 10. Medium · CONFIRMED · /schedule-demo is thin and omits the approval condition
- **Evidence:** 102 words in the body. The condition "for organizations with less than 50 people is subject to approval" (f12) is in the demo pop-up on /pricing but not on /schedule-demo. No rating, no trial link for people who would rather try first. The home demo block is richer ("Bring up to 10 teammates: the PMO, team leads and your Jira admin").
- **Fix:** add the condition in plain words, the proof strip, a "Prefer to try it first?" trial link and three lines on what the demo covers by job.
- **KPI:** demos booked.
- **Tier:** 3. **Failed if:** bookings per page view do not move in 4 to 8 weeks.
- **Not checked:** whether the Calendly widget loads and how it looks on mobile (calendly.com and the CDN are not reachable here).

### 11. Medium · LIKELY · Job pages speak to someone who already knows ActivityTimeline; their intent is "which app"
- **Evidence:** H1 pattern "Capacity Planning for Jira Teams in ActivityTimeline", H2 "What Capacity Planning Means in ActivityTimeline" (same on /time-tracking, /resource-management, /cost-tracking). /capacity-planning body: 0 uses of "app", "tool" or "plugin", and no named reader (0 role words; /timeline-for-jira has "Best for: PMOs and department heads…"). The ownership map gives these pages the solution-aware question "Which Jira app/plugin does …?".
- **Fix (draft only):** open each page with the f01-style sentence ("ActivityTimeline is a capacity planning app for Jira Cloud and Data Center…") and a "Who it is for" line. Leave H1s until the SERP is read.
- **KPI:** buyer-segment clicks; AI citations on product pages.
- **Tier:** 2. **Failed if:** no impressions on "app/tool/plugin" variants for these URLs 8 weeks after indexing.
- **Needs the SERP:** the intent map already records "jira time tracking app" as "Competitor-owned (Marketplace listings, Tempo, Timetracker)". If listings and listicles hold these results, a vendor page will not rank whatever its wording, and the Marketplace listing is the page to work on. Ahrefs `serp-overview` for "jira capacity planning tool", "jira time tracking plugin", "jira resource management plugin", "jira timeline tool"; `site-explorer-organic-keywords` per URL to see what each page ranks for today.

### 12. Low · CONFIRMED · /pricing details
- H1 "Planner, Timesheets, and Finances. One app, priced per user." names neither ActivityTimeline nor pricing; the title does.
- Data Center, which the title promises ("for Jira Cloud & Data Center"), is answered only in the last FAQ. A short Data Center block with the f08 and f09 wording would serve renewing customers.
- Hero says "122 reviews" (f13: 125), already in the 19 Nov gate report.
- **KPI:** brand clicks. **Tier:** 3. **Failed if:** "activitytimeline pricing" still shows 0 clicks on /pricing after it is indexed.

## Open questions for Ostap (one line each)

1. Was the module and solution structure approved to go live, and on what date? The memory says "keep on paper" (10 Nov).
2. Does the Tempo import work on Data Center? /tempo-alternative and /pricing disagree.
3. Should the cost pages state that Finances is in the Advanced Edition? Recommended: yes, without a price until f07 is settled.

## Limitations

- **No live SERP data.** No page-type consensus, People Also Ask, ads or AI Overview sources were read; nothing here describes a SERP layout. Ahrefs calls that would settle the SERP-dependent points: `serp-overview` per keyword named above (country us, then gb and de for the capacity and timeline heads), `keywords-explorer-overview` for volumes of the "app/tool/plugin" variants, `site-explorer-organic-keywords` and `gsc-keywords` per URL.
- **No rendered layout.** The Webflow CDN (cdn.prod.website-files.com) is blocked in this environment, so Playwright renders the pages without CSS or scripts. Above-the-fold composition, mobile layout, the pricing calculator's default state and the demo calendar were not checked. Judgements rest on DOM order and text.
- **Not measured:** clicks, conversions and paths per page (no Search Console, GA4 or Sitechecker today).
- **Not checked (host blocked):** the Marketplace listing and the help centre, so the trial path after the redirect and product capability statements are unverified.
- English pages only. Persona scoring was not run as a separate pass; the five buyer questions replace it.
- Customer names visible on the pages (case-study links, review bylines, one header link) are left unnamed here.

Generate a PDF report? Use `/seo google report`.
