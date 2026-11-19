# Skill routing and overrides for activitytimeline.com

ActivityTimeline is a B2B SaaS app for Jira (resource planning, capacity,
time tracking, cost) sold through the Atlassian Marketplace, with a Webflow
site in four locales. The strategy (`seo-strategy/strategy-2026-11-05.md` in
the memory) treats the site as the place assistants and partners copy their
facts from, not a traffic engine. Apply the overrides below on top of each
skill's own instructions. Facts, decisions and IDs come from the memory.

## Who does which job

Account skills exist in the claude.ai account and may not be loaded in every
session; when one is missing, use the plugin skill and these overrides.

| Job | Owner |
|---|---|
| What is the state, what is due, what next | `/seo activitytimeline status` |
| Fix or refresh one existing article; decaying pages; GEO rewrite of an article | account skill activitytimeline-content-refresh, else seo-content plus seo-geo |
| Score one page on the Visibility Scale, before and after a change | account skill activitytimeline-visibility-optimizer; `/seo activitytimeline gate` for the gates |
| Site structure, what should exist, quarterly re-plan | account skill activitytimeline-seo-strategist (structure is "on paper only" until Ostap says go) |
| New landing or product page | account skills activitytimeline-landing-page-builder and activitytimeline-webflow-styles |
| Turn a feature or article into a feature page | account skill activitytimeline-feature-page |
| Tickets, board hygiene, decisions log | account skill seo-lab-pm |
| Challenge a proposal before an irreversible change | account skill seo-lab-devils-advocate, run isolated (charter and facts only) |
| Sitechecker charts and API reports | account skill sitechecker-api-insights |
| Technical, schema, sitemap, hreflang, backlinks, clustering, SXO, drift | the plugin skills below, with their overrides |

## Plugin skills: overrides

**seo-audit.** Business type is SaaS (Jira Marketplace app); do not re-detect.
Spawn technical, content, schema, sitemap, performance, visual, geo, agentic,
sxo, cluster and backlinks. Never spawn local, maps or ecommerce. Pull the
Sitechecker crawl (`audit_summary`, `audit_issues`) and GSC data in the main
session and pass them to subagents. Exclude the Webflow `/design` staging
folder. Score with the Visibility Scale gates and the charter KPIs, not only
the SEO Health Score.

**seo-page, seo-content.** Use the Visibility Scale page types (product, paid
landing page, pricing, pillar guide, blog post, comparison, help article).
Before any copy: `facts.md`. Run `/seo activitytimeline facts` on the draft.
Guides carry no personal author line (credit the ActivityTimeline team or
Reliex). Meta descriptions name ActivityTimeline and how it solves the
problem (decision of 10 Nov 2026); the /pricing description stays as it is.
Buyer language comes from `customer-calls/summaries/` (meeting evidence,
never product facts). Check capabilities in the help centre export
(FrankUAPT/activitytimeline-docs) before writing that the product lacks
something.

**seo-content-brief.** Only for owner pages on a hub question: cost and
finances, planned vs actual and reports, time tracking and timesheets,
capacity and workload, resource planning, the Tempo comparison. The cost hub
is next on the roadmap. No briefs for generic Jira how-tos or new localized
posts (off-limits). Position each page "where native Jira stops" and name the
KPI it moves.

**seo-geo, seo-agentic.** The KPIs are the Sitechecker AI Chats mention rate
(100 prompts) and the cost-prompt mention rate. Assistants cite the
Marketplace listing most, then Atlassian Community and Tempo's help, so the
listing and the help centre are citation surfaces too. Check llms.txt lists
the commercial pages. Known issue: the help centre publishes raw `.md` copies
that Google indexes; the fix is an `X-Robots-Tag: noindex` header on `.md`
responses, not a robots.txt block. Pattern worth repeating: the 5 Nov refresh
of /blog/jira-bulk-update was cited in AI Overviews within two days.

**seo-technical.** Count every `rel="canonical"` (two were live on
/capacity-planning and /time-tracking on 10 Nov 2026). Webflow writes
`<meta content="..." name="...">`, content first. Robots and canonical tags
live in page custom code (`data_scripts_tool`), not the pages API. WebFetch
strips JSON-LD and hreflang and hides redirects: use the gate script,
Sitechecker `audit_page_details` or Ahrefs `site-audit-page-content` instead.
Indexing requests are Reliex's job (STB-2, internal); agents monitor only.

**seo-schema.** SoftwareApplication plus Organization; no review snippet; the
rating and review count equal facts.md f13. Write schema through Webflow
`data_pages_tool > bulk_update_pages_schema_markup` (page settings did not
persist on 30 Oct 2026) and read it back with `query_pages_schema_markup`.
FAQ rich results are retired: do not add FAQPage for a SERP feature.

**seo-competitor-pages.** One comparison hub: /tempo-alternative. Like for
like (Standard vs Tempo Timesheets + Capacity Planner; Advanced vs Timesheets
+ Financial Manager; and the full suite), every Tempo price dated and sourced
(the Oct 2026 partner price brief backs 45 to 76% less), a "When Tempo is the
better fit" section, comparisons never in a headline. No new alternatives
pages for non-Jira tools; the Clockify, Everhour and Harvest posts are frozen
(D6, review 19 Nov 2026 and in February).

**seo-hreflang.** Locales en, es, fr (fr-FR), pt (pt-BR). D4: keep and
maintain es, fr and pt (blog included), no German for now, redirects stay in
the same language. Editing English text in Webflow can reset that element's
translations: read back every locale after an English edit.

**seo-cluster.** Cannibalisation is the core problem (9 to 16 URLs per head
query). Start from `seo-strategy/ownership-map-2026-11-07.csv` and
`intent-map-2026-11-05.csv`; one owner URL per buyer question. The capacity
owner (D1) and the redirect list (D3) are still open: no 301 before Ostap
decides.

**seo-backlinks.** Use Ahrefs `site-explorer-backlinks-stats` per URL before
any redirect or owner decision; it is cheap and decided D1 and D3 row 8 fast.

**seo-sitemap.** Webflow generates sitemap.xml; the only per-page control is
`includeInSitemap`. Watch for noindex URLs in the sitemap and the duplicate
/Blog (capital B).

**seo-drift.** A baseline belongs in the changelog entry when a change ships.
Use drift baselines for the 12 commercial pages before a large Webflow
publish; the re-check reads the same metrics 4 to 8 weeks later.

**seo-google.** Prefer Sitechecker for GSC and GA4 (no Google credentials in
this setup). GA4 property 297456099 is consent-exposed and last click, so it
undercounts blog to Marketplace paths.

**seo-bing.** Bing and IndexNow ownership is open (D7, STB-13). Submitting
URLs is a tier 3 change; STB-2 indexing is internal to Reliex.

**seo-plan, seo-flow, seo-sxo.** The 12-month plan exists (5 Nov 2026) and
the re-plan is due in the first week of February 2027. Use these to work
inside it, not to replace it. Structure changes stay on paper until Ostap
gives a go.

**seo-images, seo-image-gen.** Mock-ups for Ostap are built from the live
page's markup and production stylesheet; an annotated wireframe in another
style was rejected on 10 Nov 2026.

## Out of scope for this site

seo-local, seo-maps (no physical location or map pack), seo-ecommerce and
seo-shopify (sold through the Atlassian Marketplace, not a store),
seo-programmatic location pages, seo-posthog and Matomo (GA4 is the analytics
source), seo-dataforseo (Ahrefs and Sitechecker cover the same data).
