# Content quality and on-page SEO: activitytimeline.com, 19 Nov 2026

**Content Quality: 66 / 100.** Derived from page-type scores weighted by business role: commercial pages 85 (weight 40%), home 80 (10%), three pillar guides 42 (25%), blog sample 66 (20%), /how-it-works and /case-studies 50 (5%), minus 2 for fact contradictions between pages.

**On-Page SEO: 79 / 100.** Derived from 20 saved pages plus 8 blog posts: titles 90, meta descriptions 70 (commercial pages comply with the 10 Nov decision, guides and blog do not yet), H1 and heading structure 80, duplication 95, cross-page fact consistency 60.

Scope: saved HTML of 19 Nov ~11:52 UTC (home, 11 commercial pages, /case-studies, /blog index, three guides), gate JSON for 12 pages, and 8 blog posts fetched with curl on 19 Nov (4 buyer posts, 4 how-tos). English only. Working files: `/tmp/claude-0/-home-user-claude-seo-for-AT/59906b2c-085a-5d20-be69-6c6e01a02638/scratchpad/work-seo-content/`.

## E-E-A-T breakdown (toolkit's internal weights, not Google's)

| Factor | Score | Why |
|---|---|---|
| Experience (20%) | 62 | Commercial pages show worked examples with real numbers (a team of five at 105% of real capacity, a margin walk-through). Guides have none; they define "capacity planning" for factories. |
| Expertise (25%) | 68 | Blog posts carry a named author with a role and an author page. Guides credit the Organization in JSON-LD but show no visible "by the ActivityTimeline team" line. Guide copy has errors a product expert would not make. |
| Authoritativeness (25%) | 66 | Atlassian Enterprise Certified, Platinum Partner, SOC 2, ISO 27001 shown consistently. Marketplace rating shown, with two different review counts. |
| Trustworthiness (30%) | 62 | Prices dated and sourced on /pricing and /tempo-alternative (good). Pulled down by: contradicting facts between blog and /pricing, uncited statistics in guides, footer "© 2011 - 2021" on 8 pages, placeholder prices in /pricing static HTML. |
| **Weighted** | **64** | |

AI citation readiness: 68 (commercial pages 80: definition block, question H2s, FAQ in HTML; guides 45; blog 65).

## Page scores by Visibility Scale page type

| Page | Type | Words (main, no footer) | Content | Note |
|---|---|---|---|---|
| / | Product (home) | 4,885, of which about 2,600 are the review carousel repeated 4 times | 80 | Clear definition block and FAQ |
| /capacity-planning | Paid landing page | 1,746 | 88 | Worked example, 4-step method, FAQ |
| /time-tracking | Product | 2,341 | 87 | |
| /resource-management | Product | 2,373 | 86 | |
| /cost-tracking | Product | 1,985 | 90 | Highest information density (0.77) |
| /timeline-for-jira | Product | 2,416 | 85 | |
| /reports | Product | 2,274 | 85 | 10 H2, no H3 |
| /features | Product | 2,284 | 82 | |
| /pricing | Pricing | 1,223 | 78 | G3 fail; placeholder prices in static HTML |
| /tempo-alternative | Comparison | 1,650 | 84 | Only page that passes G3 |
| /how-it-works | Product | 613 | 50 | Pre-redesign copy |
| /schedule-demo | Paid landing page | 106 | 60 | Thin but a booking page; acceptable |
| /case-studies | Blog/hub | 634 | 50 | |
| /how-to-do-capacity-planning-in-jira | Pillar guide | 2,800 | 40 | |
| /how-to-do-time-tracking-in-jira | Pillar guide | 2,414 | 55 | |
| /how-to-do-resource-management-in-jira | Pillar guide | 1,308 | 30 | |
| 8 blog posts | Blog post / Comparison | 2,161 to 3,325 | 55 to 80 | See finding 4 |

`content_quality.py` information density: commercial pages 0.49 to 0.77; guides 0.22 (capacity), 0.29 (resource), 0.32 (time tracking).

## What works

- Every saved page has exactly one H1, one canonical (self), no noindex.
- No duplicated copy between commercial pages: the highest 6-word shingle overlap between any two is 5% (/pricing and /tempo-alternative, the shared Tempo price lines). Each page owns its own examples.
- All 11 commercial titles are unique, 37 to 70 characters, carry the brand, and none has a year stamp.
- Meta descriptions on home and all 11 commercial pages name ActivityTimeline and a capability (decision of 10 Nov). /pricing left as is. `metadata_template.py` on 25 title/description pairs: site_risk low, 0 templated. Its "brand-suffix-in-description" flag on 5 product pages contradicts the 10 Nov decision: ignore it.
- "10,000+ teams" is now the only team count on all saved pages (f15), including es/fr/pt home pages. No install counts anywhere (f14 policy). No "5,000".
- /tempo-alternative dates and sources every Tempo price and says "like for like" (f25). Its arithmetic checks out ($17,280 + $12,575 + $9,095 = $38,950; $12,450 is 68% less).
- /blog/jira-bulk-update (refreshed 5 Nov) is the model how-to: direct answer first, a hard limit, a "what you can't do" section, product mentioned only where it adds something.

## Findings

### 1. High · CONFIRMED · The three pillar guides are the weakest content on the site and sit on the biggest buyer queries
- Evidence, /how-to-do-resource-management-in-jira (dated 25 Nov 2025, 1,308 words): generic textbook copy ("all businesses are limited in the resources they have"); H2 "Benefits of Jira Resource Management Plugin" describes a product that does not exist under that name; typos "work uder-, or overload", "boost your improve resource management"; FAQ "Does Jira have a project management tool? Jira provides a wide range of add-ons".
- Evidence, /how-to-do-capacity-planning-in-jira (27 Feb 2026): TL;DR opens with "Resource allocation is the discipline of allocating resources" (wrong topic); "53% of burnt-out employees" attributed to "Recent reports" with no source; "What is a Capacity Planning?"; "an significant aspect"; "ActivityTimeline is a resource capacity planning."; unsupported "one of the most popular add-ons", "a leading Jira capacity planning plugin"; the title promises "(Native vs App)" but the body has no native-versus-app comparison.
- Evidence, /how-to-do-time-tracking-in-jira (13 Feb 2026): H2 "How to enable time tracking in Jira" is followed by two paragraphs on why estimates matter, the steps come three sections later; the on-page contents list names sections that are not on the page ("What is Time Tracking?", "Why is Time Tracking important for Jira?"); missing spaces in the body ("cancompare", "athird-party", "RemainingEstimate", "movesthat"); "boost revenue by up to 61% and reduce team stress by 25%" with no source; FAQ still says "More → Log Work".
- All three call the product a "plugin" or "add-on" 4 to 10 times each; commercial pages say "app".
- Fix: interim hygiene pass on the live guides without waiting for the structure decision: fix the TL;DR, typos, missing spaces, wrong H2, contents list; cite or delete the three statistics; delete the superlatives; replace the two nonsense FAQ answers. The capacity v2 draft stays the blueprint for the full rebuild (STB-7, still waiting for Ostap; structure is "keep on paper"). No redirect is proposed here; any guide-to-blog move is tier 4.
- KPI: buyer-segment clicks; AI citations on product, pricing or comparison pages (the guides are the pages AI Overviews already consider: 36 AIO citations on the time tracking guide in the Oct baseline).
- Tier: 2 for the draft, 3 to apply.
- Failed if: 4 to 8 weeks after publish the guides' positions (22.0, 23.2, 11.3 on 10 Nov) and AIO citation counts have not moved, or citations drop.

### 2. High · CONFIRMED · /pricing static HTML shows "$1,000 / month" for both editions; the real figures are filled by script
- Evidence: `<span data-pr="std-amt" class="text-weight-medium pricing">$1,000</span> / month` and the same for `data-pr="adv-amt"`, followed by "≈ $2.08 per user per month · 51–100 user tier". Rendered in Chromium the same elements read "$10" and "$15" (10 users, monthly). The "Compare with Tempo" block has "0" in all four price cells in static HTML. The full price table and the FAQ are in static HTML and are correct, so this is partial, not total.
- Why it matters: crawlers and assistants that do not run scripts read Standard = Advanced = $1,000 a month, which contradicts the table 300 words below (100 users: $250 and $350). This is Visibility Scale gate G2 on the page that should be cited for price prompts.
- Fix: set the static defaults to the values the script shows on load ($10 and $15, "up to 10 users, flat price") and put real 100-user figures in the comparison cells, or leave the cells empty.
- KPI: AI citations on product, pricing or comparison pages; cost and budget prompt mention rate.
- Tier: 3 (after the Advanced-price question below is answered).
- Failed if: a no-JavaScript fetch still shows "$1,000" after publish, or an assistant quotes $1,000 a month for ActivityTimeline.

### 3. High · CONFIRMED · Facts disagree between pages (G3), beyond what the gate patterns catch
Gate result: 11 of 12 commercial pages fail G3; on 10 of them the only hit is "Activity Timeline" twice in the shared header (lead already has it). What reading the copy adds:

| Where | Text | Against |
|---|---|---|
| /blog/tempo-timesheets-alternatives, closing CTA | "free for up to 10 users on Jira Cloud, no credit card required" | f06 open; /pricing says "Up to 10 users is a flat $10 a month on Standard and $15 on Advanced" |
| same post, comparison table | "Activity Timeline"; "$845/mo, Advanced version (including Finances module) - $1245/mo"; "from $2.50/user to $0.13/user" | f02; f07 (open question for Ostap); /blog/jira-time-tracking says "drops to $0.10" |
| same post | "only Timesheets costs $1,522.50/mo for a team of 500 users", no date or source | f25 (date and source every Tempo price); /tempo-alternative has $17,280 a year, dated 1 Oct 2026 |
| /pricing hero proof line | "4.7 ★ 122 reviews" | /tempo-alternative "125 reviews … (5 Nov 2026)", /time-tracking "from 125 reviews" (f13) |
| /pricing edition card and FAQ | Advanced adds "Security Log" and "Premium Support" | f04 lists only Finances and Alignment; Premium Support is marked unverified in facts.md. Open question, not called wrong. |
| / "Data residency" card | "Keep ActivityTimeline data in the EU, the United States or Australia" | f19 open (docs say Frankfurt or Ohio) |
| / integrations block | "Structure", "eazyBI" listed next to BigPicture and BigGantt | f22 open for Structure; eazyBI is not in f21 |
| /how-to-do-time-tracking-in-jira | "(for Server)", "for the Server version" | f10: do not mention Server |
| /how-it-works | "Cloud / Server / Data Center" guide links | f10 |
| Shared footer, 15 pages | "Admin Guide Server/DC", "User Guide Server/DC" | f10 |
| /how-to-do-capacity-planning-in-jira | "changes sync every 10 minutes" | not in the register; check against the help centre |
| /tempo-alternative | Enterprise Certified described as "third-party penetration tests, independent audits, data residency and a 24-hour response on critical issues" | not in the register (f18 covers the badge only) |
| /tempo-alternative FAQ vs /pricing FAQ | "ActivityTimeline runs on Data Center too … we scope the Tempo migration for your instance" vs "the Advanced edition and the Tempo import are on Jira Cloud" | each other; f09 asks for "existing Data Center customers" wording |

- Fix: one fact pass. (a) Live now, already decided: 122 → 125 with the date on /pricing; "Activity Timeline" → "ActivityTimeline" in the post table; remove "(for Server)" from the guide; rename footer labels to "Data Center". (b) One question to Ostap per open item: is the Advanced column, Security Log and Premium Support confirmed (then f04 and f07 get the figures); f06 free or $10; f19; f22. Until answered, soften the blog CTA to "30-day free trial, no credit card" (f11, confirmed).
- KPI: AI mention rate; cost and budget prompt mention rate (assistants repeat whichever figure they find first).
- Tier: 3.
- Failed if: `activitytimeline_gate.py` still reports G3 on /pricing after publish, or the re-fetched blog post still contains "free for up to 10 users".

### 4. High · CONFIRMED · Blog and guide meta descriptions do not yet follow the 10 Nov decision
- Evidence (live `<meta name="description">`, 19 Nov): 7 of 8 sampled posts do not name ActivityTimeline, including three buyer posts: /blog/tempo-timesheets-alternatives ("Compare the top Tempo Timesheets alternatives side by side…"), /blog/tempo-planner-vs-activitytimeline ("Tempo Planner is now Capacity Planner. Features, 2026 prices…"), /blog/track-billable-hours. /blog/jira-capacity-planning's description is a broken excerpt: "Capacity planning answers whether it can be done. So, to move beyond this, teams need something…". /blog/jira-story-points ends "Read more!".
- Guides: the time tracking guide's description is 108 characters ("How to do Jira time tracking? Use ActivityTimeline to generate time tracking reports and timesheets in Jira."); the resource guide's is generic ("Our guide explores how to optimize…"); the capacity guide's is 172 characters and will be cut.
- The rewrite list of 10 Nov (85 descriptions, 82 naming ActivityTimeline) has no change-log entry: it is not live.
- Fix: publish the approved list, buyer posts and the three guides first. Do not write new text; the list exists.
- KPI: buyer-segment clicks (CTR at existing positions: the three guides had 25,801 impressions and 52 clicks in the list's 90-day window).
- Tier: 3.
- Failed if: CTR on the changed URLs is not above their own previous 28 days after 4 to 6 weeks at the same average position.

### 5. Medium · CONFIRMED · Blog posts ship template placeholders and broken title text in static HTML
- Evidence, all 8 sampled posts: "0 min read" (`fs-readtime-element="time"` holds `0`) and a contents list reading "Example H2 / Example H3" (`fs-toc-element="link"`). Both are filled by script.
- /blog/tempo-timesheets-alternatives `<title>` is cut by the 80-character field: "…5 Jira Apps to Track Time and Plan Resources in 2" (known since 10 Nov, still live). /blog/tempo-planner-vs-activitytimeline is 78 characters, 2 from the limit.
- Related-post cards are H2s and "Related Articles" appears twice as an H2, so a post has 15 to 21 H2s of which 6 to 8 are other posts' titles. The /blog index has 101 H2s.
- Article JSON-LD `datePublished` is not a valid date ("Jul 07, 2026T10:00:15+02:00") and there is no `dateModified`, so the 5 Nov refresh of /blog/jira-bulk-update is invisible as a date. (For the schema specialist; listed here because it hides freshness.)
- Fix: template change in the Blog Posts collection page: empty the two placeholders in the static markup, make card titles a non-heading element or H3, one "Related Articles" block. Shorten the truncated title to 60 characters or fewer.
- KPI: AI citations (extractable headings and dates); buyer-segment clicks for the truncated title.
- Tier: 3 (template is one change for all posts; test on one post first).
- Failed if: a curl of any post still contains "Example H2" or the live title still ends "in 2".

### 6. Medium · CONFIRMED · Year stamps: 19 blog titles say 2026, six weeks before 2027
- Evidence: /blog index H2s: 19 contain "2026", 1 contains "2025" ("Jira Custom Reports: A Full Guide for 2025"). Related cards also show "Jira Task Management: A Full Guide for 2025". /blog/jira-bulk-update has "(2026)" in the H1 but not in the title.
- The 9 Nov draft that removes "(2027)" from 10 titles and "2025" from 13 is still unpublished.
- Fix: publish the 9 Nov draft; for the 2026 stamps, remove the year from titles and H1s where the post is not about a year (keep it on price comparisons, where the year is information). Do not roll them to 2027 without updating the content.
- KPI: buyer-segment clicks.
- Tier: 3.
- Failed if: any live title carries a year older than the current one on 15 Jan 2027.

### 7. Medium · CONFIRMED · Legacy pages left out of the redesign: /how-it-works, /case-studies, /schedule-demo
- /how-it-works: 613 words of pre-redesign copy ("Jira Resource Management with Ease", "Discover the best features", "Your team is your greatest asset"), H1 "Learn how ActivityTimeline works", H2s without the brand, links labelled "Learn more ↗" four times. It is one of the 12 commercial pages and the only one that does not say what happens to Jira data in plain terms, which its own description promises ("syncs with Jira to schedule issues…").
- /case-studies: H1 "Be inspired by our clients" (no topic); meta description spells the brand "Activity Timeline" and says "our plugin".
- /schedule-demo: title "ActivityTimeline Product Demo session" (37 characters, no "Jira", lower-case "session"); 106 words. Thin is acceptable for a booking page; the title is not.
- /blog index description: "…with our plugin."
- Fix: rewrite /how-it-works on the product-page pattern (what it reads from Jira, what it writes back, the five modules, setup time) using only confirmed facts; retitle /schedule-demo ("Book a Live Demo of ActivityTimeline for Jira"); fix the two descriptions and the /case-studies H1.
- KPI: commercial pages indexed (12 of 12: on 9 Nov /how-it-works and /schedule-demo were still not in Sitechecker's found_at list; Google index state not measured today); demos booked.
- Tier: 2 draft, 3 to apply.
- Failed if: /how-it-works is still "crawled, not indexed" 4 weeks after the rewrite and an indexing request.

### 8. Low · CONFIRMED · Smaller on-page items
- /tempo-alternative meta description is 194 characters; it is cut after about "…migrate in hours". Move "Book a 25-min migration call" forward or drop it. Tier 3.
- /timeline-for-jira description 168 characters; title 69. /reports title 70. Both display in full on desktop most of the time; trim only when next edited.
- H1s without the search term: /pricing ("Planner, Timesheets, and Finances. One app, priced per user." has neither "pricing" nor "ActivityTimeline"). The title covers it; consider "ActivityTimeline pricing" as the eyebrow line inside the H1. Tier 3.
- Guide titles and H1s differ on purpose (title keyword-led, H1 a question) and that is fine. The capacity guide's JSON-LD WebPage name ("Jira Capacity Planning: A Detailed Guide") is a third variant.
- Footer copyright: "© 2011 - 2021 Reliex" on 8 saved pages (/pricing, /features, /cost-tracking, /how-it-works, /case-studies and the three guides), "© 2011 - 2026" on 7. Two footer variants; fix the old one. Tier 3. KPI: none directly (trust hygiene); bundle with the footer "Server/DC" label fix.
- Home: the review carousel is in the HTML four times (about 1,750 repeated words of 4,885). Harmless for ranking; it dilutes the page for extractors. Also the home carousel and two guides name customers. f26 covers new material only, so no change is proposed; do not copy these into new pages.
- Guides have no visible author or team line and no visible "updated" date. Per the override: add "By the ActivityTimeline team at Reliex" and an updated date when the guides are next edited, not a personal author.

## Not checked

- Marketplace review count today (marketplace.atlassian.com blocked); f13's 125 is from 5 Nov.
- Product claims against the help centre (help.activitytimeline.com blocked; docs export not in this session): "sync every 10 minutes", Security Log, Premium Support.
- Search Console and AI citation data per page (Sitechecker unreachable): every CTR and position figure above is quoted from memory files of 10 Nov, not measured today.
- G4 (one owner per question). From the sitemap alone: /blog/jira-time-tracking, /blog/jira-configure-time-tracking and the time tracking guide target the same head term, as do /blog/jira-capacity-planning and the capacity guide (D1, open).
- es/fr/pt body copy beyond the home-page fact line; the other English blog posts; author pages.
- Sitemap note for the sitemap specialist: /blog/best-time-tracking-apps-for-jira is in sitemap.xml and returns 301 to /blog/track-billable-hours.
