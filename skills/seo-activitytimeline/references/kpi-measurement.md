# Measuring the charter KPIs

How to read each KPI in `charter.md` the same way every time, so a re-check
compares like with like. Tool names are the short names; the server prefix
depends on which connector the session has (a Sitechecker claude.ai
connector, the Sitechecker plugin, Ahrefs, Webflow, Atlassian). Caveats per
tool are in the memory's `data-sources.md` and `lessons.md`; read the section
for the tool before calling it.

## Windows

- GSC: 28 days ending at the last day Search Console has (about 7 to 10 days
  before today), against the previous 28 days and the same 28 days a year
  earlier. The scorecard names a row by the Monday of the report week (week
  of 2026-11-09 used 6 Oct to 2 Nov).
- Clicks are comparable across the May 2025 to 27 Apr 2026 impression
  inflation; impressions are not.
- AI Chats: the tracker's own window (about 28 to 35 days) plus the weekly
  value. AI Overview and AI Chats have no previous-period comparison in the
  Sitechecker API; AI Traffic does.
- A re-check uses the window length of the baseline it compares against, and
  neither window may contain the change date.

## KPI recipes

| KPI | Read it with | Notes |
|---|---|---|
| Commercial pages indexed in Google (12) | Search Console URL Inspection when a Search Console connector or Google credentials exist (`gsc_inspect.py`); otherwise Sitechecker `gsc_pages` (a page with impressions in the window is indexed) plus `audit_page_details` for live status, canonical, meta robots and found_at | Say which method was used. The live state is not Google's verdict: Google held "Excluded by noindex" for weeks after the 23 Oct 2026 fix. Run `activitytimeline_gate.py --commercial` for the live side. |
| Brand clicks, 28 days | Sitechecker `gsc_performance_summary` with `brand_type=brand`; `gsc_performance_history` with `group_by=brand` for the trend | The weekly reports use the Sitechecker brand filter. |
| Buyer-segment clicks, 28 days | Sitechecker `gsc_keywords`, top 500 by clicks plus top 500 by impressions, classified into category and commercial named queries | Exclude the Clockify and Everhour alternatives queries and the AI persona prompts. Named queries cover only part of the clicks; say how many. |
| AI assistant mention rate (100 prompts) | Sitechecker `ai_chats_summary`; `ai_chats_history` for the weekly value (it takes `ai_model`, not `dimension`) | Report ActivityTimeline and Tempo side by side. |
| Mention rate on cost and budget prompts | Sitechecker `ai_chats_prompts` to find the cost and budget prompts, then `ai_chats_history` filtered to them | Baseline 7.9% (6 Oct to 3 Nov 2026). The cost hub is meant to move it. |
| AI citations on product, pricing or comparison pages | Ahrefs `site-explorer-ai-responses-count` per URL (about 50 units a call) or the `ai_responses` columns of `site-explorer-top-pages`; Sitechecker `ai_chats_citations` and `ai_overview_keywords` for the tracked sets | Baseline 0 (5 Nov 2026). Count per page, not per site. |
| Demos booked, 50+ user trials | GA4 key events through Sitechecker `ga4_*` (default channel organic; pass `all` for every channel) | Consent-exposed and last click. Trial counts are not in any connector: ask, and leave the cell empty rather than guess. |

## Supporting reads

| Question | Tool |
|---|---|
| Which URLs compete for a query | Sitechecker `gsc_cannibalization`, `gsc_cannibalization_pages` |
| Pages and queries won or lost | Sitechecker `gsc_new_lost_pages`, `gsc_new_lost_keywords` (need `date_from` and `date_to`; a lost page is often a redirect, check its live status first) |
| What changed on the site | Sitechecker `monitoring_*`; Webflow `data_pages_tool` updated dates |
| AI Overview citations on tracked keywords | Sitechecker `ai_overview_summary`, `ai_overview_keywords`; `ai_overview_analysis` for one keyword only (a live check) |
| Demand and SERP shape | Ahrefs `keywords-explorer-overview` (about 53 units a row), `serp-overview` |
| Backlinks before a redirect or owner decision | Ahrefs `site-explorer-backlinks-stats` |
| Raw HTML when WebFetch or the proxy fails | Ahrefs `site-audit-page-content` (last crawl), then `activitytimeline_gate.py --file` |
| Where on a page a text sits | Webflow `data_element_tool > query_elements` |
| Ticket state and comments | Atlassian `searchJiraIssuesUsingJql` (project STB), `getJiraIssue` |
| Weekly report page | Atlassian Confluence, space ACTS, parent page id in `ids-and-references.md` |

## Not available (do not guess)

Ahrefs Search Console endpoints at keyword or page level (broken since Sep
2026), Ahrefs Brand Radar (not licensed), Marketplace search positions from
the cloud, Google Ads conversions (no offline import), and weekly trial counts.
Mark a missing number "not measured" with the reason.
