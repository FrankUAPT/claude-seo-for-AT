# Topical architecture (cluster drift check), activitytimeline.com, 19 Nov 2026

**Score: 46 / 100.** Derived from six weighted checks of the live site against the Lab's own map
(`seo-strategy/ownership-map-2026-11-07.csv`, `page-action-map-2026-11-07.csv`): one clear owner per hub on the
live site 8/25; map still describes the site 5/15; owner pages link to each other 12/20; competing posts link to
their owner with a descriptive anchor 10/20; titles differ from the owner's head term 3/10; URL hygiene (dead
URLs, redirects, orphans) 8/10.

Scope: drift check only. No new cluster plan, no SERP overlap run. English only. Cannibalisation **by query is
not measured** today (no Search Console, Sitechecker unreachable); every count below is URLs and titles.
D1 (capacity owner) and D3 (redirect list) are still open: no 301 is recommended here as an action. Every merge
in the map stays "waiting on Ostap" (tier 4, needs his approval and a devil's advocate comment).

Sources: saved `sitemap.xml` (712 `<loc>`; 177 English, 178 es, 179 fr, 178 pt), the 23 saved pages, 37 pages
fetched by curl on 19 Nov (20 new pages, 10 competing posts, the utilization guide, 6 status checks) plus 2
status-only requests. Working files: `SCRATCH/work-seo-cluster/` (`en.txt`, `hubs.txt`, `mat.txt`, `links.json`,
`fetchlog.txt`).

## The headline

Between 7 and 19 Nov the site gained **21 English URLs that the map does not have**: five module pages
(/planner, /workspace, /timesheets, /reports, /finances), fourteen module sub-pages, and two new job pages
(/budget-planning, /resource-utilization). All are 200, indexable, self-canonical, in the sitemap, in the main
menu and linked from the home page and /features. The memory records the structure as "not a go yet, keep on
paper" (decision 10 Nov) and the change log has no entry for the launch. Nothing was merged or redirected at the
same time (only /advanced-jira-reports → /reports), so every hub now has more live URLs on its head term than on
7 Nov, not fewer. The map said "5 module pages go live, the job pages change role, posts merge" as one phase-2
move; the first third shipped alone.

## What works

- No dead URLs. Every content URL the inventory called live still answers 200 or redirects on purpose.
- The new pages are not orphans: menu, home and /features link all 21; module pages link their sub-pages and the
  matching job page in body copy with descriptive anchors ("Capacity planning in Jira with ActivityTimeline",
  "How cost tracking works in Jira", "See every report in ActivityTimeline Reports").
- The four root guides cross-link each other and link down to their job page and module ("Jira capacity
  planning" → /capacity-planning, "running time tracking across a team" → /time-tracking).
- Sampled posts do link to a commercial page in body copy: 8 of 10 (see table in finding 5).
- The second canonical tag reported on 10 Nov on /capacity-planning and /time-tracking is gone: each now carries
  one self-canonical (open question 1 in `decisions/open/2026-11-10-meta-list-questions.md` can be closed after
  Ostap confirms it was removed on purpose).

## Hubs: live English URLs and the mapped owner

"Topic URLs" = English sitemap URLs whose slug, title or H1 is about the hub (home, /blog, /features, /pricing
excluded). "Head term in title" = the owner's head term is in the title or H1. "New" = not in the 7 Nov inventory.

| Hub | Topic URLs | Head term in title | New since 7 Nov | Mapped owner (map, 7 Nov) | Owner state today |
|---|---|---|---|---|---|
| Capacity and workload | 22 | 11 | 7 | Learn: /how-to-do-capacity-planning-in-jira (D1 open; 10 Nov proposal says /blog/jira-capacity-planning). Buy: /capacity-planning | Not decided. Live site behaves as if the blog post won (finding 2) |
| Time tracking and timesheets | 28 | 20 | 4 | Learn: /how-to-do-time-tracking-in-jira. Buy: /time-tracking. "jira timesheets": /timesheets (new) | /timesheets is live; /blog/jira-timesheets still live with the same lead title |
| Resource planning | 12 | 8 | 2 | Learn: /how-to-do-resource-management-in-jira. Buy: /resource-management | Unchanged; /planner title now also says "Resource and Capacity Planning" |
| Cost and finances | 11 | 8 | 4 | Learn: /how-to-track-project-costs-in-jira (new, not live). Buy: /cost-tracking. Module: /finances | Three commercial pages on cost/budget; still no guide |
| Planned vs actual and reports | 27 | 21 | 6 | Learn: /how-to-create-utilization-reports-in-jira (retarget). Module: /reports. Listicle: /blog/jira-reporting-plugins | /reports live (took over /advanced-jira-reports); /resource-utilization and two planned-vs-actual sub-pages are unmapped |
| Timeline | 7 | 5 | 0 | Learn: /blog/jira-timeline. /timeline-for-jira was to fold into /planner | Both /planner and /timeline-for-jira live, cross-linked |
| Tempo comparison | 6 | 6 | 0 | /tempo-alternative (+ 5 named posts kept) | Unchanged |

The 7 Nov map counted "9 to 16 URLs per head query" from Search Console. Whether the new pages already rank for
those queries is not measured.

Full per-hub URL lists with titles and map action: `SCRATCH/work-seo-cluster/hubs.txt`.

## Drift: sitemap against the 7 Nov inventory

**In the sitemap, not in the inventory (37).** 21 are new pages:
/planner, /planner/bookings, /planner/holidays-and-time-off, /planner/placeholders, /planner/sprints,
/planner/story-points-to-hours, /planner/workload-indicator, /workspace, /timesheets,
/timesheets/billable-hours, /timesheets/timesheet-approval, /finances, /finances/cost-and-billing-rates,
/finances/expenses, /reports, /reports/planned-vs-actual, /reports/planned-vs-actual-chart,
/reports/project-resources-forecast, /reports/team-capacity-chart, /budget-planning, /resource-utilization.
All 21 fetched: 200, one self-canonical, no robots meta, 8 hreflang tags.
The other 16 are collection items the inventory listed only as templates (7 case-study pages, 6 author pages,
3 category pages): not new, an inventory gap.

**In the sitemap, inventory said not live (1).** /blog/skills-gap-analysis (inventory: live "no", draft "True").
Today 200, self-canonical, indexable. Either republished after 7 Nov or the inventory read a staged draft flag.

**Inventory live, not in the sitemap (36).**

| URL | Status 19 Nov | Note |
|---|---|---|
| /advanced-jira-reports | 301 → /reports | Not in the change log; page-action-map still names it as the reporting solution page |
| /faq | 301 → activitytimeline.atlassian.net wiki "Customer Q A" | Target not checked (host blocked). Inventory row is the Blog FAQs template |
| /blog/atlassian-events-tour | 200, `noindex` | Known since 5 Nov; still linked from related-post cards (seen on /blog/jira-financial-management) |
| /blog/soc-2-certification | 200, `noindex` | Known since 5 Nov ("confirm intent" never answered); map says keep as proof, P1 |
| /start-trial | 200, `noindex`, two canonical tags (self and home), two robots tags | System page, in every menu as "Start Free Trial" |
| /schedule-online-session | 200, `noindex` | System page |
| 30 system, template and portal URLs (/401, /404, /order*, /partner-portal/*, /search, templates) | not fetched | Out of scope in the map; correctly absent from the sitemap |

## Findings

### 1. High · CONFIRMED · 21 pages went live that the map and the decisions say are still on paper
- Evidence: sitemap.xml lists the 21 URLs above; e.g. `/planner` title "ActivityTimeline Planner: Resource and
  Capacity Planning", `/timesheets` H1 "Jira Timesheets: Log, Approve and Report Time in Jira". Memory:
  `decisions/README.md` 10 Nov "Site structure: not a go yet, keep on paper"; `changes/CHANGELOG.md` has no
  entry; `page-action-map` has no row for 16 of them and "(new)" placeholders for 5.
- Why it matters: the map's merges were sized against a site without these pages. Every hub gained 2 to 7 URLs
  on the owner's topic and lost none. Re-checks and baselines for a launch this size do not exist.
- Fix: (a) change-log entry with the publish date and today's baseline; (b) add the 21 rows to the page-action
  map with layer, cluster, owner and role; (c) ask Ostap one question: is the structure now a go, and do the job
  pages (/capacity-planning, /time-tracking, /resource-management, /cost-tracking, /timeline-for-jira) stay as
  lighter pages next to the modules or fold in. Until answered, treat module = "what the product part is",
  job page = "which Jira app does X", guide = "how do I do X in Jira".
- KPI: commercial pages indexed (the commercial list grows from 12 to about 19 with the modules and two job
  pages); AI citations on product pages.
- Tier: 2 (memory and map only).
- Failed if: at the next weekly run the commercial list, llms.txt and the map still disagree on which URLs exist.

### 2. High · CONFIRMED · Capacity: the site now points at the blog post as "the guide" while D1 is open
- Evidence: `/capacity-planning` links `/blog/jira-capacity-planning` twice ("Guide Jira capacity planning: the
  complete guide…", "Quarterly planning guide →") and `/how-to-do-capacity-planning-in-jira` zero times.
  `/planner/bookings` ("capacity planning in Jira") and `/reports/team-capacity-chart` ("Guide: capacity planning
  in Jira") also link the post. Across 56 pages read, the root guide gets links from only four: the three other
  guides and `/resource-utilization` (anchor "Read the guide"). The post itself links neither the guide nor the
  reverse. D1 recommendation of 9 Nov: guide URL; 10 Nov proposal: blog URL; Ostap: not decided.
- Why it matters: internal links are the strongest owner signal the site controls. They now back the post, the
  inbound links from other sites (14 live / 10 domains, Ahrefs 5 Nov) back the guide. The split D1 was meant to
  end is wider than on 7 Nov.
- Fix: put D1 back in front of Ostap with this fact: "the live site already links the post as the guide from
  three product pages; confirm post or guide". After his answer, point all three links (and the guide's or
  post's own body) at the chosen URL. No redirect now; the loser's 301 stays in D3, waiting on Ostap (tier 4).
- KPI: buyer-segment clicks (capacity is the largest buyer hub, 300 US searches on the head term); AI mention rate.
- Tier: 3 for the link changes after the decision.
- Failed if: six weeks after the links are aligned, Search Console still shows both URLs taking impressions on
  "jira capacity planning" at similar positions.

### 3. High · CONFIRMED · New module sub-pages repeat the head term of posts the map names as owners
- Evidence (title or H1 against the mapped owner):

| New page | Its title / H1 | Mapped owner for that question | Owner's title |
|---|---|---|---|
| /planner/sprints | "Jira Sprint Capacity Planning" | /blog/sprint-capacity-planning-in-jira | "Sprint Capacity Planning in Jira: Why Green Workloads…" |
| /timesheets | H1 "Jira Timesheets: Log, Approve and Report Time in Jira" | /timesheets (new) with /blog/jira-timesheets to merge | post: "Jira Timesheets: What's Native, What's Missing…" |
| /timesheets/timesheet-approval | H1 "Timesheet Approval in Jira: Review, Approve and Lock Worklogs" | /blog/timesheet-approval | "Timesheet Approval in Jira: Key Steps, Benefits…" |
| /timesheets/billable-hours | "Track Billable Hours in Jira" | /blog/track-billable-hours | "How to Track Billable Hours Using Jira Add-ons" |
| /reports/planned-vs-actual and /reports/planned-vs-actual-chart | "Planned vs Actual Report for Jira", "Planned vs Actual Chart for Jira" | /how-to-create-utilization-reports-in-jira (retarget) | guide title has no "planned vs actual"; two posts do |
| /resource-utilization | "Resource Utilization Reports for Jira" | /how-to-create-utilization-reports-in-jira | "Resource Utilization in Jira: Formula, Benchmarks & Reports" |
| /reports/team-capacity-chart | "Jira Capacity Report: Team Capacity Chart" | /blog/capacity-planning-kpis ("capacity report" intent) | "10 KPIs That Separate Real Capacity Planning…" |
| /planner/workload-indicator | "Jira Team Workload Indicator" | /capacity-planning workload section + /blog/workload-management | "Team Workload Management: Strategies and How to Track It in Jira" |
| /budget-planning, /finances, /cost-tracking | "Project Budgeting Software for Jira", "…Project Cost and Budget in Jira", "Project Cost Management Software for Jira" | /cost-tracking (buy), /finances (module) | three commercial pages share "project cost/budget … Jira" |

- Mitigation already live: each sub-page links its post as "Guide: …" or "Read the guide →" (e.g.
  `/timesheets/timesheet-approval` → "Guide: timesheet approval process in Jira"), which is the right direction.
  The posts do not link back yet (they predate the pages; 0 of 10 sampled posts link a sub-page).
- Fix: update the map so each pair has one role each: sub-page owns "ActivityTimeline does X" (product/buy),
  post owns "how to do X in Jira" (learn). Retitle the sub-page where it reads as a how-to (start with the
  ActivityTimeline feature name, as `/planner/placeholders` already does: "Placeholders: Tentative Planning for
  Jira"). Add one body link from each post to its sub-page with the feature as anchor. For planned vs actual,
  decide between the guide and /reports/planned-vs-actual as owner and record it; the two posts stay as they are
  until D3-style review. For cost, give /cost-tracking, /budget-planning and /finances three different head
  terms in the map before any copy work (cost tracking, budget tracking, the Finances module).
- KPI: buyer-segment clicks; cost and budget prompt mention rate (7.9%); AI citations on product pages.
- Tier: 2 (map, titles as drafts), 3 (titles and links live after approval).
- Failed if: after 4 to 8 weeks Search Console shows the post and its sub-page alternating on the same query
  with neither inside the top 10, or the sub-pages are "crawled, not indexed".

### 4. High · CONFIRMED · The four root guides fell out of the site template
- Evidence: the 28 links shared by at least 80% of pages (menu and footer) contain no `/how-to-…` URL. On 10 Nov
  the footer's Product column linked the four guides (`site-structure-proposal-2026-11-10.md`). Inbound today
  within the 56 pages read: capacity guide 4 pages, time guide 5, resource guide 5, utilization guide 10. The
  home page and /blog link none of them. None of the 10 sampled posts links the capacity or time guide.
- Why it matters: these are the mapped learn-layer owners for four hubs, the time guide held 32 AI citations
  (10 Nov memo) and the capacity guide holds the hub's external links. The map's whole capacity and time plan
  merges posts into URLs that now sit three clicks from the home page.
- Fix: restore one template link to each guide (a "Guides" footer column is already in the 10 Nov proposal), or
  link each from its job page and module page in body copy (/time-tracking and /resource-management already do;
  /capacity-planning, /planner, /timesheets, /cost-tracking do not). This is independent of D1: if the post wins
  capacity, the footer link for capacity goes to the post.
- KPI: AI citations on product, pricing or comparison pages (guides feed them); buyer-segment clicks.
- Tier: 3.
- Failed if: guide clicks and citations keep falling at the 4-week re-check while the linked job pages rise
  (then the guides are simply being replaced, and the merge direction in the map should flip).

### 5. Medium · CONFIRMED · Posts link to a commercial page, rarely to the mapped owner; two link to nothing
Sample of 10 competing posts, body links only (menu and related-post cards excluded):

| Post | Mapped owner | Links mapped owner? | Best body link to a hub page (anchor) |
|---|---|---|---|
| /blog/jira-capacity-planning | capacity guide | no | /capacity-planning "capacity planning"; /planner "Planner module" |
| /blog/resource-capacity-planning | capacity guide | no | /capacity-planning "capacity planning" |
| /blog/jira-time-tracking | time guide | no | /time-tracking "time tracking"; /timesheets "3 types (views) of Timesheet Reports" |
| /blog/jira-timesheets | /timesheets | yes, weak anchor "approval workflow" | /workspace "Workspace" |
| /blog/effective-resource-management | resource guide | yes: "resource management", "resource planning" | none to /resource-management |
| /blog/jira-cost-management | cost guide (not live) | n/a | **none** (only /blog/capex-vs-opex…) |
| /blog/jira-financial-management | cost guide (not live) | n/a | /cost-tracking "tracking costs"; /finances "ActivityTimeline Finances" |
| /blog/planned-vs-actual | utilization guide | yes: "utilization reports" | none to /reports or /reports/planned-vs-actual |
| /blog/tempo-timesheets-alternatives | /tempo-alternative (hub) | **no** | /timesheets "Timesheets module"; migrate CTA goes to /blog/tempo-timesheets-for-jira |
| /blog/jira-timeline | itself | n/a | /timeline-for-jira "plan across several projects"; /planner "Team Panel" |

Mapped owner linked: 3 of 7 where a live owner other than the post exists. Descriptive anchors where links
exist: good (no "click here"; one weak, "approval workflow"). Generic anchors are on the product side instead:
`/resource-utilization` links three guides with the same "Read the guide"; `/cost-tracking` → post "Read the guide".
- Fix (in order): `/blog/jira-cost-management` gets a body link to /cost-tracking and /finances;
  `/blog/tempo-timesheets-alternatives` links /tempo-alternative from its migrate sentence ("Learn how to migrate
  from Tempo to ActivityTimeline" currently goes to a sibling post); `/blog/planned-vs-actual` links
  /reports/planned-vs-actual; the three capacity and time posts wait for D1 and then link the chosen owner.
  Replace the three "Read the guide" anchors on /resource-utilization with the guide topic.
- KPI: cost and budget prompt mention rate; AI citations on comparison pages; buyer-segment clicks.
- Tier: 3 (primary-locale inline links need the paragraph-swap method in `lessons.md`; read back all locales).
- Failed if: the owner's internal inbound count has not risen at the next crawl, or a locale lost its translation.

### 6. Medium · CONFIRMED · /tempo-alternative is isolated from its own cluster
- Evidence: body links on `/tempo-alternative` go only to /finances ("Finances.") and /pricing ("See pricing").
  It links none of the five Tempo posts, including `/blog/tempo-planner-vs-activitytimeline` (the most AI-cited
  ActivityTimeline URL per the map). In the other direction, the one Tempo post sampled reaches it only through
  the menu item "Migrate from Tempo"; the other four Tempo posts were not fetched (LIKELY the same). Product
  pages do link it in body copy (/time-tracking, /resource-management, /timesheets, /pricing,
  /resource-utilization).
- Fix: on the hub, a short "Compare by product" block linking the three alternatives posts and the two versus
  posts by name; in each of the five posts, one body link to /tempo-alternative with "Tempo alternative for Jira"
  or "switch from Tempo" as anchor.
- KPI: AI citations on comparison pages (0 today); demos (Tempo is the strongest commercial intent).
- Tier: 3.
- Failed if: at the 25 Dec re-check /tempo-alternative still has no impressions inside the top 20 for
  "tempo alternative" variants while the posts keep theirs.

### 7. Medium · CONFIRMED · Titles of competing posts still lead with the owner's head term
No merge has shipped, so the 7 Nov title collisions all stand. Worst by hub (title, map action):
- Capacity (owner head term "jira capacity planning"): `/blog/jira-capacity-planning` "Jira Capacity Planning: A
  Complete Guide for 2026" (merge, D1); `/blog/jira-planner` "Jira Planner: Capacity Planning Guide" (merge →
  /planner, which is now live); `/blog/resource-capacity-planning` "What is Resource Capacity Planning…";
  `/blog/jira-workforce-management` "…A Guide to Efficient Capacity Planning";
  `/blog/jira-project-planning-and-capacity-management-best-practices`.
- Time ("jira time tracking"): `/blog/jira-time-tracking` "Jira time tracking guide: Best 5 tools" against the
  guide's "Jira Time Tracking: How to Add Time Tracking in Jira"; `/blog/time-tracking-best-practices`;
  `/blog/jira-configure-time-tracking`; `/blog/jira-time-tracking-report`; `/blog/jira-timesheets` against the
  new /timesheets H1 (both start "Jira Timesheets:").
- Resource ("jira resource management"): `/blog/effective-resource-management`,
  `/blog/top-resource-management-plan-mistakes-and-how-to-avoid-them`,
  `/blog/how-to-create-resource-planner-for-jira-best-tips`.
- Cost: `/blog/jira-cost-management`, `/blog/jira-financial-management` ("Complete Guide to…"),
  `/blog/jira-budget-tracking-bridging-operations-and-finance`: three "guides" and no guide owner live.
- Reports: `/blog/planned-vs-actual` and `/blog/how-to-create-planned-vs-actual-chart-for-jira` against the two
  new /reports sub-pages; five utilization posts against the guide and /resource-utilization.
- Timeline: `/timeline-for-jira` title "Jira Timeline for People and Teams Across Projects" against
  `/blog/jira-timeline` "Jira Timeline: How to Create and Use It" (both lead "Jira Timeline").
- Tempo: fine. Each post names a different Tempo product; the hub owns the generic term.
- Fix: no retitling of posts that are on the merge list (wasted work if D3 passes). Two cheap moves that do not
  depend on D1 or D3: (a) `/timeline-for-jira` title back to a product lead ("Timeline for Jira: …", as its H1
  already reads); (b) the map note for `/blog/jira-planner`: its target /planner now exists, so its row can move
  into the D3 list for Ostap's review. Everything else: waiting on Ostap (D1, D3).
- KPI: buyer-segment clicks.
- Tier: 3 for (a); 2 for (b); tier 4 for any merge, not proposed here.
- Failed if: /timeline-for-jira loses its position on "timeline for jira" (2.3 on 7 Nov) after the title change.

### 8. Low · CONFIRMED · Map and memory housekeeping from the status checks
- `/advanced-jira-reports` 301 → `/reports`: update the page-action-map row (the reporting solution page is now
  /reports, which the map had as the *module* page; the role of "Reports job page" is now empty or merged, say which).
- `/blog/skills-gap-analysis` is live and indexable but the inventory says not live: add it to the map
  (cluster resource, likely "keep" or "retire"; 0 clicks in 90 days, position 65.5 on 7 Nov).
- `/blog/soc-2-certification` is noindex while the map keeps it as P1 proof for the security intent; the intent
  question from 5 Nov is still open. Ask once more or drop it from the proof list.
- `/blog/atlassian-events-tour` (noindex) still receives related-post card links.
- Blog posts ship a table-of-contents stub in the raw HTML: `<a href="#" class="toc_link">Example H2</a>` and
  "Example H3" (seen in every sampled post). Scripts replace it in the browser; a crawler that does not run
  scripts reads "Example H2". Fix in the blog template (hide or empty the stub).
- KPI: commercial pages indexed (map accuracy); AI mention rate (clean raw HTML). Tier 2 for the map, 3 for the
  template. Failed if: the next inventory run still disagrees with the sitemap on these rows.

## Waiting on Ostap (listed, not recommended as actions)

- D1 (STB-7): capacity owner, guide or post. New evidence for the ticket: finding 2.
- D3 (STB-9): redirect list v2, 12 rows in 4 batches. None shipped. Capacity rows stay held behind D1.
- The 52 merges and 5 retirements in the page-action map (D2 item-by-item list): none shipped; all tier 4.
- New: is the structure a go, now that the module pages are live (finding 1); and the 19 Nov gate question on
  /advanced-jira-reports → /reports.

## Not checked

- Cannibalisation by query, positions, clicks and impressions for any URL: not measured (no Search Console).
- Whether Google has indexed the 21 new pages: not measured.
- AI citations and backlinks per URL: not re-pulled (5 Nov figures quoted where used).
- es/fr/pt copies of the new pages and of every finding above: out of scope (English drift check); the sitemap
  holds 178, 179 and 178 localized URLs.
- The other 107 blog posts' body links: only 10 posts sampled (fetch budget 40, 39 used).
- The /faq redirect target (activitytimeline.atlassian.net): host blocked.
- help.activitytimeline.com pages that rank for planned vs actual and team capacity chart: host blocked.
- Side note for the hreflang specialist: `/tempo-alternative` has 0 hreflang tags in the saved HTML; every other
  page read has 8.
