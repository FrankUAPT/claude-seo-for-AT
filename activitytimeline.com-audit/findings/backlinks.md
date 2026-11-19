# Backlinks and AI citations: activitytimeline.com

Score: 55/100. Real authority is thin but clean at the top (Atlassian, a few SaaS peers); about two thirds of the
live referring domains carry link-seller anchors that appeared between April and September 2026.

Source: Ahrefs API, read 19 Nov 2026 (data date 18 Nov). Done in the main session (the seo-backlinks agent has no
Ahrefs access). Moz, Bing and Common Crawl were not used. Ahrefs units used: 1,113.

## Numbers

| Metric | Value |
|---|---|
| Domain Rating | 37 |
| Live referring domains | 960 (2,081 all time) |
| Live backlinks | 3,378 (14,376 all time) |
| Organic keywords (Ahrefs) | 461, of which 210 in positions 1 to 3 |
| AI citations, whole site | 457 citation links on 79 pages (471 on 9 Nov) |
| AI citations by platform | AI Overviews 22 on 15 pages; ChatGPT 9 on 6; Perplexity 2; Gemini 2; AI Mode 1; Copilot 0 |
| AI citations on commercial pages | /pricing 0, /capacity-planning 0, /time-tracking 0, /resource-management 0, /cost-tracking 0, /tempo-alternative 0, /features 0. Home page: 16 |

Referring domains by month (first of month): Nov 2025 193 · Jan 2026 205 · Mar 167 · Apr 180 · May 317 · Jun 416 ·
Jul 543 · Aug 557 · Sep 988 · Oct 959 · Nov 960.

## Findings

### 1. High · CONFIRMED · Two thirds of the referring domains are link-seller pages
- **Evidence:** the top anchors by referring domains (Ahrefs anchors report, live, 18 Nov) are sales text, not
  mentions of the product: "Premium SEO Authority Links for activitytimeline.com Websites and Businesses" (262
  domains, all dofollow); a fake testimonial naming a guest-post seller (220 domains, nofollow); "Talk to us before
  your next campaign. activitytimeline.com covers page speed optimization…" (68); "High Quality Dofollow Backlinks DA
  50 PA 40 Premium PBN Network Service activitytimeline.com…" (54); three more of the same kind (25, 8, 5). Together
  about 640 of 960 domains, allowing for overlap. Referring domains went from 180 (1 Apr 2026) to 988 (1 Sep 2026)
  and have been flat since.
- **What it means:** these pages are generated for any domain name by link-seller networks to advertise to site
  owners; nobody has to buy anything for them to appear. Google normally ignores them. They matter for two reasons:
  the "960 referring domains" and part of DR 37 are not authority, so the real profile is nearer the 180 to 200
  domains of early 2026; and if anyone did order a link package for this domain in spring 2026, that is a different
  situation and needs handling.
- **Fix:** (a) one question for Ostap: did Reliex or an agency order any link building for activitytimeline.com
  between April and September 2026? (b) Reliex checks Search Console > Security & Manual Actions (agents cannot see
  it). (c) If both answers are no, do nothing: no disavow file. A disavow is only for a manual action or links we
  bought. (d) In weekly reports, quote referring domains with the seller anchors excluded.
- **KPI:** protects brand clicks and buyer-segment clicks (a manual action would hit both); stops a false signal in
  the scorecard. **Tier:** 1 (read) and a question; a disavow upload would be tier 4.
- **How we would know it failed:** a manual action appears in Search Console, or rankings drop site-wide with no
  matching Google update.

### 2. Medium · CONFIRMED · No AI citations on any commercial page (charter KPI still 0)
- **Evidence:** Ahrefs ai-responses-count per URL, 19 Nov: 0 on all seven commercial pages checked; 16 on the home
  page; the other 441 citation links sit on blog posts and guides. Baseline 0 on 5 Nov and 0 on 9 Nov.
- **Fix:** none new from this file. It is the measure for the cost hub and the product page work already planned;
  see geo.md and sxo.md. **KPI:** AI citations on product, pricing or comparison pages. **Tier:** 1.
- **How we would know it failed:** still 0 on /cost-tracking and /tempo-alternative at the 4 Dec and 1 Jan re-checks.

### 3. Low · CONFIRMED · Brand anchors are split between two spellings
- **Evidence:** "ActivityTimeline" 24 domains / 62 links; "Activity Timeline" 5 domains / 7 links; the old home
  title as anchor on 24 domains. The site's own header still uses the two-word form (gate, 19 Nov).
- **Fix:** fix the header (see content.md); no outreach needed. **KPI:** brand clicks, AI mention rate (one entity
  name). **Tier:** 3.

## What works
- Atlassian links: atlassian.net (52 links, dofollow) and atlassian.com (19, dofollow), the two strongest real
  sources and the ones assistants trust for this product.
- Editorial links from adjacent SaaS companies, most of them first seen in 2026: tempo.io, toggl.com, myhours.com,
  resourceguruapp.com, gliffy.com, tmetric.com.
- Keyword anchors are few and natural ("Jira time tracking" 5 domains, "Jira Capacity planning" 3): no sign of
  anchor manipulation on the money terms.

## Not checked
- Which page each strong link points to (needed before any redirect: pull backlinks-stats per URL for D1 and D3).
- Spam share by Ahrefs' own flag (is_spam was false on the top 30 by DR; the seller pages sit lower down).
- Lost links and broken backlinks (site-explorer-broken-backlinks), Moz, Bing Webmaster, Common Crawl.
