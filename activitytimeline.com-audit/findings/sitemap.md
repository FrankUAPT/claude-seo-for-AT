# Sitemap findings: activitytimeline.com, 19 Nov 2026

**Category score: 80 / 100.** Derived from 100 minus: 8 for 36 listed URLs whose rendered canonical points to another page, 4 for 4 orphaned localized posts with broken hreflang sets, 3 for a placeholder author page in 4 locales, 5 for llms.txt links that redirect or are noindex and do not match the sitemap. Structure, validity, lastmod, hreflang reciprocity, commercial coverage and duplicates all pass.

Source: saved `sitemap.xml` (19 Nov 2026, ~11:52 UTC, 712 `<loc>`, 556 KB), `llms.txt`, 21 saved pages, plus 38 live curl fetches and 2 Chromium renders on 19 Nov 2026 (40 total, the budget). Search Console sitemap report and index coverage: not measured (no GSC or Sitechecker access today).

## What works (all CONFIRMED)

- **Valid, single file, well under limits.** One `urlset`, 712 URLs, 712 unique, 556 KB, HTTPS and apex host only, no query strings, no trailing-slash or case variants, no `priority`/`changefreq`. Referenced from robots.txt.
- **No `/Blog` duplicate and no `/design`.** Neither is in the sitemap; both return 404 live. The capital-B duplicate named in the override is gone.
- **lastmod is real, not a publish stamp.** 82 distinct values from 2025-05-20 to 2026-11-19; the most common covers 18% of URLs. The four locale copies of a path always share the English value (0 of 179 paths differ), so a localized page's lastmod reflects the English edit. One bulk value, `2025-05-28T12:09:30.917Z`, sits on 59 URLs (author, category and older posts: a CMS bulk update), which is harmless.
- **Hreflang in the sitemap is reciprocal.** 708 of 712 URLs carry the full set (`en`, `es`, `fr-FR`, `pt-BR`, `x-default`), every alternate target is itself listed, every set is self-referencing, `x-default` always equals `en`, 0 non-reciprocal pairs. Codes match the on-page tags and `<html lang>`.
- **All 12 commercial pages are listed in all 4 locales** (48 URLs): /, /capacity-planning, /tempo-alternative, /cost-tracking, /resource-management, /features, /time-tracking, /timeline-for-jira, /reports (the new home of /advanced-jira-reports), /pricing, /schedule-demo, /how-it-works. `/advanced-jira-reports` is correctly absent.
- **No redirecting or noindex URL found in the sitemap.** 27 listed URLs sampled across every section: all 200, none noindex. The noindex post `/blog/soc-2-certification` is correctly excluded.

## URL counts

| Section | en | es | fr | pt |
|---|---|---|---|---|
| Home | 1 | 1 | 1 | 1 |
| Static pages (product, guides, utility) | 29 | 29 | 29 | 29 |
| /blog/ posts | 117 | 118 | 119 | 118 |
| /blog-author/ | 6 | 6 | 6 | 6 |
| /blog-categories/ | 3 | 3 | 3 | 3 |
| /case-studies/ detail | 7 | 7 | 7 | 7 |
| /planner/ feature pages | 6 | 6 | 6 | 6 |
| /reports/ feature pages | 4 | 4 | 4 | 4 |
| /finances/ | 2 | 2 | 2 | 2 |
| /timesheets/ | 2 | 2 | 2 | 2 |
| **Total** | **177** | **178** | **179** | **178** |

179 distinct paths; 177 exist in all four locales. 75% of the sitemap (535 URLs) is localized copies; 355 are localized blog posts.

## Findings

### 1. High: 36 listed author and category URLs change their canonical to /blog in the browser (CONFIRMED)

- **Evidence.** `/blog-author/*` (6 x 4 locales) and `/blog-categories/*` (3 x 4 locales) ship a self-canonical in the raw HTML, then a body script headed `<!-- Add Custom Canonical and OG:Url -->` runs on DOMContentLoaded: `existingCanon.remove()` and appends `canonical.href = url` with `url` = `https://activitytimeline.com/blog` (or `/es/blog` for /es paths). Rendered in Chromium: `/blog-categories/general` and `/fr/blog-author/user` both end with the single canonical `https://activitytimeline.com/blog` and og:url the same. The script only tests `path.startsWith("/es")`, so French and Portuguese pages canonicalize to the English blog. The category template also has `<meta name="robots" content="index">`.
- **Why it matters.** The sitemap asks Google to index 36 URLs that, once rendered, say "I am a copy of /blog". Raw and rendered canonicals disagree, which is the conflicting-signal case Google advises against, and author pages (an expertise signal for the blog) are told not to stand on their own.
- **Fix (pick one per template, Ostap decides).** (a) Blog Categories template: keep the canonical to /blog and set `includeInSitemap` off on the template page. (b) Blog Authors template: remove the canonical-rewriting script from the page's custom code so the Webflow self-canonical stands, and keep it in the sitemap; if the intent is that author pages stay out of the index, turn `includeInSitemap` off instead. If the script stays anywhere, make it locale-aware for /fr and /pt.
- **KPI.** Indirect: AI mention rate (author identity behind guides) and commercial pages indexed (cleaner signals, less crawl on duplicates). No direct click KPI; do not oversell.
- **Tier.** 3 (reversible live change: custom code and a sitemap toggle).
- **How we would know it failed.** After publish, a headless render still shows canonical `/blog` on an author page, or the 12 category URLs are still in sitemap.xml.

### 2. Medium: 4 localized blog posts are listed whose English original has been redirected away (CONFIRMED)

- **Evidence.** `/es|fr|pt/blog/how-to-do-resource-planning-in-jira-using-apps`: 200, self-canonical, sitemap and on-page hreflang list only `es`, `fr-FR`, `pt-BR` (no `en`, no `x-default`); the English URL 301s to `/how-to-do-resource-management-in-jira`. `/fr/blog/jira-workload-management-tips-with-activitytimeline`: 200, the only sitemap entry with 0 alternates; the English URL 301s to `/blog/workload-management`. lastmod 2025-05-28 and 2025-08-29.
- **Why it matters.** The English versions were consolidated; the translations were left live and compete in their languages with the localized pillar (`/es/how-to-do-resource-management-in-jira`) and `/fr/blog/workload-management`, both of which are in the sitemap.
- **Fix.** Finish the consolidation: 301 each of the 4 to the localized equivalent of the English target. That is tier 4. The reversible interim step is `includeInSitemap` off (Webflow sets this per CMS item per locale only if the locale item can be drafted separately; if not, the redirect is the only clean route).
- **KPI.** Buyer-segment clicks/28d (the localized pillar stops sharing its topic with a stale post). Small.
- **Tier.** 4 for the 301s (needs Ostap + devil's advocate); 3 for the sitemap toggle.
- **How we would know it failed.** The 4 URLs still return 200 or are still in sitemap.xml after the next publish; or clicks on the localized pillar fall in the 4 to 8 weeks after.

### 3. Medium: llms.txt and the sitemap disagree on 3 links, and llms.txt omits the newest commercial pages (CONFIRMED)

- **Evidence.** Of 32 activitytimeline.com links in llms.txt, 29 are in the sitemap. The other three: `/advanced-jira-reports` ("Jira reports") 301 -> `/reports`; `/how-to-create-jira-project-reports` 301 -> `/blog/how-to-create-jira-project-reports` (the target is not in the sitemap; its status and robots tag were not checked, budget spent); `/blog/soc-2-certification` 200 but `<meta name="robots" content="noindex"/>`, listed under "Security, trust and support". In the sitemap but absent from llms.txt: `/tempo-alternative`, `/how-it-works` (already known), and also `/reports`, `/budget-planning`, `/resource-utilization`, the four module hubs (`/planner`, `/workspace`, `/timesheets`, `/finances`) and their 14 feature pages.
- **Fix.** Draft a corrected llms.txt: point "Jira reports" at `/reports`, replace or drop the project-reports link after checking its target, either drop the SOC 2 post or remove its noindex (a noindex page is a poor trust citation), and add `/tempo-alternative`, `/how-it-works`, `/budget-planning` and the module hubs. Run the fact lint on the new descriptions first.
- **KPI.** AI mention rate; cost and budget prompt mention rate (/budget-planning, /finances, /cost-tracking are the cost pages); AI citations on product, pricing or comparison pages.
- **Tier.** 2 to draft, 3 to publish.
- **How we would know it failed.** A re-fetch of llms.txt still contains a link that returns 301 or noindex; no change in cost-prompt mention rate at the 4 to 8 week re-check.

### 4. Low: a placeholder author page, "User", is listed in 4 locales (CONFIRMED)

- **Evidence.** `/blog-author/user` and `/es|fr|pt/blog-author/user`: 200, title `User | ActivityTimeline's Blog Author`, in the sitemap with a full hreflang set.
- **Fix.** Reassign that author's posts to a named author and archive the CMS item, or turn `includeInSitemap` off for it. Deleting the item removes a URL: tier 4 if it has links or impressions (not measured).
- **KPI.** AI mention rate (named, real authors on guides). Small.
- **Tier.** 3 (reassign, sitemap off); 4 if the item is deleted.
- **How we would know it failed.** The URL is still in sitemap.xml, or posts still show "User" as author.

### 5. Info: the toolkit profile still lists /advanced-jira-reports as a commercial path (CONFIRMED)

- **Evidence.** `data/activitytimeline/profile.json` > `site.commercial_paths` contains `"/advanced-jira-reports"`, which now 301s to `/reports` (also `/es/advanced-jira-reports` -> `/es/reports`). The commercial gate and the "12 of 12 indexed" KPI would test a redirect.
- **Fix.** Replace it with `/reports` in the profile and wherever the memory lists the 12 pages. Tier 2 (repository change, not the site).
- **KPI.** Commercial pages indexed (keeps the measure honest).
- **How we would know it failed.** The next gate run still reports /advanced-jira-reports.

### 6. Info: observations passed on, not scored here

- `/become-a-partner`, `/activitytimeline-basic-concepts`, `/activitytimeline-quick-start-guide`, `/how-to-create-utilization-reports-in-jira` and two saved guides show a second `rel="canonical"` string in the body. It sits inside an HTML comment (`<!--<link href=... rel="canonical">`) and the script beside it only writes og:url, so it is inert. On `/become-a-partner` the commented value is `/partners`. Leftover custom code worth deleting; no effect today. (CONFIRMED)
- `/pt/reports` has an English title, "ActivityTimeline Reports: Workload, Availability and Planned vs Actual..." (CONFIRMED on that one URL; /es and /fr not fetched). For the hreflang specialist.
- `/reports/planned-vs-actual` and `/reports/planned-vs-actual-chart` are both listed, both 200 and self-canonical, with near-identical titles. Possible overlap for the content or cluster specialist. (LIKELY)
- Thin utility pages: none found. The smallest sampled listed page is `/become-a-partner` (about 490 words in `<main>`), which is a legitimate page.

## Sample checked live (19 Nov 2026)

| Group | URLs | Result |
|---|---|---|
| Old and case-variant paths | /advanced-jira-reports, /es/advanced-jira-reports, /Blog, /design | 301, 301, 404, 404; none in sitemap |
| llms.txt-only links | /how-to-create-jira-project-reports, /blog/soc-2-certification | 301; 200 noindex |
| Author and category | /blog-author/user, /es/blog-author/user, /blog-author/(a named author), /blog-categories/general, /blog-categories/features, plus 2 renders | 200; rendered canonical /blog |
| Utility and guides | /educational-videos, /activitytimeline-basic-concepts, /activitytimeline-quick-start-guide, /become-a-partner, /partners, /how-to-setup-jira-start-end-date-custom-fields, /how-to-create-utilization-reports-in-jira | 200, self-canonical, no robots tag |
| Product and module pages | /budget-planning, /resource-utilization, /finances, /planner, /workspace, /timesheets, /planner/bookings, /reports/planned-vs-actual, /reports/planned-vs-actual-chart, /finances/expenses | 200, self-canonical, no robots tag |
| Localized | /es/pricing, /fr/capacity-planning, /pt/tempo-alternative, /pt/reports, /pt/blog/jira-timesheets | 200, self-canonical, 5 hreflang tags, correct lang |
| Orphan locale posts and their English URLs | 2 localized + 2 English | 200 and 200; English 301 and 301 |
| Blog | /blog/jira-capacity-planning | 200, self-canonical |

## Not checked

- Search Console sitemap status, submitted versus indexed counts, and which listed URLs are excluded: not measured (no GSC, Sitechecker unreachable).
- Crawl versus sitemap coverage (pages live but unlisted beyond the llms.txt comparison): no crawl available today.
- The other 672 sitemap URLs' status, robots and canonical; the 7 case-study detail pages; the target of the project-reports redirect.
- www host and help.activitytimeline.com links in llms.txt: not checked (host blocked).
