# Technical SEO findings: activitytimeline.com, 19 Nov 2026

**Category score: 82 / 100.** Derived by starting at 100 and subtracting for confirmed defects: pricing figures in
server HTML differ from what the page shows (-6), noindex URLs in hreflang clusters and the sitemap (-3), security
headers incomplete (-3), internal links to 301s (-2), orphaned localized posts and no case folding (-2), og:url only
set by JavaScript (-1), /order blocked and noindexed at once (-1). Core Web Vitals, schema and sitemap internals are
not scored here (other specialists).

Evidence base: 24 saved pages in SCRATCH/live, 53 extra live requests (status, headers, HTML) and 6 Chromium
renders (home, /capacity-planning, /pricing, each with and without JavaScript). Working files:
`/tmp/claude-0/-home-user-claude-seo-for-AT/59906b2c-085a-5d20-be69-6c6e01a02638/scratchpad/work-seo-technical/`.

## Pass / fail by category

| Category | Status | Note |
|---|---|---|
| Crawlability | Pass | robots.txt allows all, blocks only /order; sitemap declared; no X-Robots-Tag on any response |
| Indexability | Pass | 21 of 21 saved pages: one live canonical, self-referencing, no meta robots |
| Redirects and status codes | Pass with notes | http, trailing slash and old URLs all 301 in one hop; real 404 status |
| URL structure | Pass with notes | lowercase, hyphenated; uppercase variants 404 (no folding) |
| Security | Partial | HTTPS, HSTS, nosniff, frame protection present; four headers missing |
| Mobile basics | Pass | `width=device-width, initial-scale=1` on every page |
| JavaScript dependence (G2) | Pass for home and /capacity-planning; **fail for /pricing price figures** | |
| Hreflang and html lang | Pass with notes | reciprocal, valid codes, x-default; noise from noindex pages |
| Internal links | Pass with notes | 36 targets sampled: 34 x 200, 2 x 301, 0 x 4xx |

## Findings

### 1. High: /pricing server HTML carries placeholder prices that differ from the rendered page (G2)  CONFIRMED
- **Evidence.** Raw HTML of https://activitytimeline.com/pricing, calculator cards:
  `<span ...>$1,000</span> <span data-pr="std-per">/ month</span>` followed by
  `<span data-pr="std-sub">≈ $2.08 per user per month · 51–100 user tier</span>` and `$500 less than paying monthly`.
  The Advanced card holds the same `$1,000 / month`, `≈ $2.08 per user per month · 51–100 user tier`, `$700 less`.
  With JavaScript the same cards read `$10 / month` and `$15 / month`, "Flat price for up to 10 users". The
  placeholder is internally inconsistent ($1,000 a month is not $2.08 per user in a 51-100 tier) and shows both
  editions at one price. /fr/pricing carries the same English placeholder string (2 occurrences).
- **Why it matters.** Crawlers that do not run JavaScript (most AI crawlers, and Bing on first pass) read the
  placeholder as the price. The tier table lower on the page is in the HTML and is fine. LIKELY effect: wrong or
  no price quoted in AI answers. I make no claim about which figures are correct (f07 question is open).
- **Fix.** Set the static text of the `data-pr` spans to the calculator's default state (what the script writes on
  load), in all four locales, so server HTML and rendered page agree. Adds to lessons.md "wrong numbers need a
  location": this is a third location beside the calculator and the modal.
- **KPI.** AI citations on product, pricing or comparison pages; mention rate on cost and budget prompts.
- **Tier.** 3 (reversible copy change in Webflow, Ostap approves and publishes).
- **How we would know it failed.** `curl` of /pricing still shows `51–100 user tier` in the two cards; or an AI
  answer quotes $1,000 a month as the Standard price.

### 2. Medium: noindex and error URLs sit in hreflang clusters, and noindex category pages sit in the sitemap  CONFIRMED
- **Evidence.** /order: `<meta content="noindex" name="robots"/>` plus `<meta name="robots" content="none" />`, with
  five hreflang links (`/es/order` ...). /start-trial and /es/start-trial: `noindex` plus `noindex, nofollow`, with
  hreflang. /partner-portal/login: noindex with hreflang. The 404 page: `hrefLang="es" href=".../es/404"`.
  /blog-categories/tips-tricks: `<meta name="robots" content="noindex, nofollow">` yet all 12 /blog-categories URLs
  (3 x 4 locales) are `<loc>` entries in sitemap.xml. Sitechecker counted 48 pages with hreflang to noindex URLs on
  26 Oct; this is the source.
- **Fix.** Webflow emits hreflang for every localized page, so the lever is the sitemap: set "exclude from sitemap"
  on the three category template pages (sitemap specialist owns the detail). Leave the hreflang noise; it is
  harmless once the URLs are out of the sitemap. Decide separately whether /start-trial should stay noindex: it is
  the main conversion page and receives about 66 internal links per page.
- **KPI.** Commercial pages indexed (crawl attention and a clean sitemap signal); demos and 50+ user trials for the
  /start-trial question.
- **Tier.** 3. **Failure test.** `grep -c blog-categories sitemap.xml` is still 12 after publish.

### 3. Medium: two internal links point at 301s, one of them a live blog card  CONFIRMED
- **Evidence.** https://activitytimeline.com/blog lists `<a rel="dofollow" href="/blog/availability-report"
  class="card-medium ...">`; that URL answers `301 location: /how-to-create-utilization-reports-in-jira`. So a CMS
  item is still published and listed while a redirect rule overrides its URL. The Spanish home footer links
  `https://activitytimeline.com/blog/jira-project-timelines-comprehensive-guide` (English URL, absolute) which
  answers `301 location: /blog/jira-timeline`; /fr and /pt footers no longer have it.
- **Fix.** Unpublish or archive the availability-report CMS item (the redirect already exists, so this is cleanup,
  but unpublishing is tier 4 by charter: Ostap plus devil's advocate). Point the Spanish footer link at
  /es/blog/jira-timeline if that page exists, else /blog/jira-timeline (tier 3; lessons.md notes localized footer
  edits sometimes do not save through the tool, so read back).
- **KPI.** Commercial pages indexed (internal link equity and crawl paths). **Failure test.** Either href still
  returns 301 on a re-crawl. Sitechecker's "pages linking to 3xx" (1,019 on 1 Nov) should fall.
- **Scope note.** Only 36 of 326 distinct internal targets were requested; about 100 blog links were not sampled.

### 4. Low: localized posts left alive after the English original was redirected  CONFIRMED
- **Evidence.** /blog/how-to-do-resource-planning-in-jira-using-apps is `301 -> /how-to-do-resource-management-in-jira`
  but /es/, /fr/ and /pt/ versions return 200, self-canonical, with hreflang for es, fr-FR, pt-BR only (no en, no
  x-default). /blog/jira-workload-management-tips-with-activitytimeline is `301 -> /blog/workload-management` while
  the /fr/ version is 200 with a single hreflang (fr-FR). Hreflang is technically valid; the pages are orphans of a
  retired topic.
- **Fix.** Add both to the D3 redirect list for Ostap: redirect each to the same-language target (decision D4,
  9 Nov: redirects stay in the same language). **Tier 4.** **KPI.** Commercial pages indexed (less duplicate topic
  coverage competing with the guides). **Failure test.** The localized URLs still return 200 after the batch ships.

### 5. Low: security headers incomplete  CONFIRMED
- **Evidence.** Every response: `strict-transport-security: max-age=31536000` (no includeSubDomains, no preload),
  `content-security-policy: frame-ancestors 'self'` (no script or object policy), `x-content-type-options: nosniff`,
  `x-frame-options: SAMEORIGIN`. Absent: Referrer-Policy, Permissions-Policy, a full CSP, COOP.
- **Fix.** Webflow hosting does not expose response headers. Only worth doing if the Cloudflare zone is under the
  team's control (open question D7); otherwise accept. No ranking effect; it is a trust item for enterprise
  security reviews. **KPI.** Demos and 50+ user trials (weak link). **Tier.** 3. **Failure test.** `curl -I` shows
  the same header set.

### 6. Low: uppercase URLs return 404 instead of redirecting  CONFIRMED
- **Evidence.** `/Blog` -> 404, `/Blog/jira-timesheets` -> 404, `/PRICING` -> 404 (21,744-byte "Not Found" page,
  correct status). So the old "/Blog duplicate" no longer exists as a duplicate: it is gone, not in the sitemap, and
  no saved page links to it.
- **Fix.** None needed unless /Blog has backlinks or Search Console impressions (not measured today). If it does,
  one Webflow 301 `/Blog -> /blog` (tier 4). **KPI.** Brand clicks. **Failure test.** n/a until measured.

### 7. Low: og:url exists only after JavaScript runs  CONFIRMED
- **Evidence.** No `og:url` in the raw HTML of any saved page; a footer script ("Add og:url tag based on Canonical")
  appends it on DOMContentLoaded. Social and chat link unfurlers do not run scripts.
- **Fix.** Put a static `<meta property="og:url">` in page head custom code, or drop the script. **KPI.** Brand
  clicks (shared links). **Tier.** 3. **Failure test.** `curl | grep og:url` returns nothing.

### 8. Low: /order is blocked in robots.txt and noindexed at once  CONFIRMED
- **Evidence.** robots.txt `Disallow: /order`; the page carries two robots metas (above). A blocked page's noindex
  is never read, so the URL can still be indexed without a snippet if linked. /es/order, /fr/order, /pt/order are
  not blocked (the rule matches the root path only).
- **Fix.** Remove the two Disallow lines and rely on noindex (covers all locales). **KPI.** Commercial pages indexed
  (index hygiene). **Tier.** 3. **Failure test.** `site:activitytimeline.com/order` shows a result.

### Info
- **Commented-out canonicals are not live tags.** The guides, /become-a-partner, /start-trial and
  /blog-categories show 2-3 raw `rel="canonical"` matches, but the extra ones sit inside `<!-- -->` or inside a
  script string, and the browser DOM has exactly one canonical. Example: `<!--<link
  href="https://activitytimeline.com/partners" rel="canonical">`. A naive grep reports them as duplicates. Worth
  deleting the dead comments so the next audit is not misled (tier 3).
- **The double canonical of 10 Nov is fixed.** /capacity-planning, /es/capacity-planning and /time-tracking each
  have one self-canonical now. This closes question 1 in `decisions/open/2026-11-10-meta-list-questions.md`.
- **A script rewrites the canonical on /blog-categories pages** ("Replace canonical tag", sets it to /blog or
  /es/blog). The pages are noindex, so it has no effect, but /fr and /pt category pages get the Spanish target.
- **Stale Early Hints.** /blog/jira-timesheets sent a 103 preload for `...shared.d187f131e.min.css` while the 200
  response uses `...shared.f1d483372.min.css`: one wasted CSS download until the edge cache refreshes (for the
  performance specialist).
- **Profile drift.** `data/activitytimeline/profile.json` still lists /advanced-jira-reports as a commercial path;
  it 301s to /reports (single hop, `location: /reports`). No saved page links to the old URL.

## What works
- All 21 saved pages (and 4 localized ones fetched live): one canonical, self-referencing, absolute, https; no meta
  robots; no X-Robots-Tag; `<html lang>` matches the locale (en, es, fr-FR, pt-BR).
- Hreflang in the head on every page: x-default, en, es, fr-FR, pt-BR; valid codes; x-default equals en. Return
  links confirmed for home, /capacity-planning, /pricing, /tempo-alternative, /blog and two blog posts in the
  locales fetched. The sitemap repeats the same sets (177 of 179 URL groups have all four locales).
- Redirects are single hop: http -> https, `/pricing/` -> `/pricing`, `/es/` -> `/es`, `/blog/` -> `/blog`.
- Unknown URLs return a real 404. No mixed content on home, /pricing, /capacity-planning.
- G2 for home and /capacity-planning: text, H1, canonical, hreflang, JSON-LD count and link count are the same
  with JavaScript off and on (home 5,692 visible words both ways; /capacity-planning 2,554 vs 2,557). No inline
  `opacity:0` text. `?utm_source=` variants keep the clean canonical.

## Not checked
- www.activitytimeline.com redirect, help.activitytimeline.com, files.activitytimeline.com PDFs (footer links, 61
  per page) and Marketplace links: host blocked.
- The render ran without the Webflow CDN (cdn.prod.website-files.com blocked in Chromium, so the site stylesheet
  and webflow.js did not load). The G2 result therefore proves the content is in server HTML, but not what
  Webflow's own script or CSS hides or reveals; no screenshots are usable.
- Google index status, Search Console coverage, backlinks to /Blog: not measured (no credentials, Sitechecker down).
- About 290 of 326 internal link targets, and hreflang reciprocity beyond the pages listed above.
