# Visual and mobile experience: activitytimeline.com, 19 Nov 2026

**Category score: 78/100.**
Derived from 24 styled screenshots (6 pages x desktop 1440x900 and iPhone 13, above the fold and full page) plus
measured layout data: desktop 90 (clear hero, call to action and proof in the first viewport on every page, no
overflow, no broken images), mobile 70 (same strengths, minus 9-10px text on three pages, the booking widget
placed above the headline on /schedule-demo, a clipped hero label and a product tour too small to read), weighted
towards mobile, then minus points for the /pricing default state and English strings on /fr.

## How it was captured, and what could not be checked

System Playwright Chromium in Node, deviceScaleFactor 1, taken about 12:01 UTC after the asset host was allowed.
Files: `activitytimeline.com-audit/screenshots/<page>-<desktop|mobile>-<atf|full>.png` for home, pricing,
capacity-planning, tempo-alternative, schedule-demo, fr. The earlier unstyled set was deleted. Every page returned
200, styles and images loaded, 0 broken images on all 12 renders, and no page scrolls sideways (document width
equals viewport width at 1440 and 390).

Still blocked in this container, so **not checked**:
- Cookie banner (CookieYes loads through googletagmanager.com): whether it shows, how big it is, what it covers
- Chat overlay (Freshchat) and Hotjar
- Calendly widget: the booking areas on /schedule-demo and the home page render as empty white cards here
- Mobile menu: the menu button did nothing because jQuery (cloudfront host) and Webflow's script did not load; this
  is a limit of the test, not a site defect
- Webflow interactions in general. I saw no content left invisible by an entrance animation that never fired. FAQ
  answers showed expanded on /pricing and the home page, which may be the same script limit; not reported
- reCAPTCHA (google.com), real-device behaviour, tablet and 1366 widths

## What a buyer sees above the fold (CONFIRMED in screenshots)

| Page | Desktop 1440x900 | iPhone 13 |
|---|---|---|
| / | H1 "Capacity Planning, Time Tracking and Project Costs in Jira", one-sentence value line, "Start free trial →" or "Schedule demo", trial note, proof row (4.7 / 5 on Atlassian Marketplace, Enterprise Certified, Platinum Marketplace Partner, SOC 2 Type 2, ISO 27001:2022), start of the product tour | H1, value line, both calls to action, all four proof lines. Complete |
| /pricing | H1, user-count chips, Monthly/Annual, both edition cards with "$10 / month" and "$15 / month" and "Start free trial" | H1 and the user-count control only. First price is at about 800px, in the second screen |
| /capacity-planning | H1, value line, "Start free trial" + "Schedule demo", three benefit ticks, start of the three-step demo | Same, plus the step tabs. Complete. Rating and logo strip come in the second and third screen |
| /tempo-alternative | H1, sub-line, "Book a 25-min migration call →" or "Start free trial", four certification badges, the dated 500-user price comparison ("You keep $26,500 / year"), and a proof row with "4.7★ 125 reviews on Atlassian Marketplace (5 Nov 2026)", 10,000+ teams | H1, value line, both calls to action. Price comparison and proof are in the second screen. A sticky "Book a 25-min migration call" bar appears after scrolling |
| /schedule-demo | Booking card (empty here) on the left, H1 "Free ActivityTimeline Product Demo", four bullets, hosts, languages on the right. No proof line | **Only the empty booking card.** H1 starts at about 700px |
| /fr | Same layout as /, fully in French above the fold | Same as / in French |

What works: the hero pattern is consistent and strong; primary call to action is green and unmistakable; proof sits
directly under the call to action; customer logos (unnamed here) and all images load; the main nav and header
fit; prices on /pricing and /tempo-alternative are visible without any interaction on desktop; mobile primary
buttons are 42px high and full or half width.

## Findings

### 1. /schedule-demo on mobile opens on the booking widget, not the headline
- Severity: High. CONFIRMED (`schedule-demo-mobile-atf.png`; H1 measured at y 698-778 on a 664px viewport).
- Evidence: on iPhone 13 the first screen is the header and the widget card; "Free ActivityTimeline Product Demo",
  the description and the bullets come after it. With Calendly loaded the card holds a calendar, so the visitor
  still gets no headline, no "25 minutes, up to 10 teammates" and no reassurance before being asked to pick a
  slot. The four bullets under the H1 render at 9px.
- Fix: on mobile put the H1, one line and the bullets before the widget (reverse the column order), and set the
  bullets to at least 14px.
- KPI: demos and 50+ user trials. Tier: 3. Failed if: mobile demo bookings from this page drop in the four weeks
  after the change (GA4, Calendly).

### 2. Body text at 9-10px on mobile on three pages
- Severity: High. CONFIRMED (computed font sizes on the iPhone 13 render, and visible in the full-page shots).
- Evidence: /pricing mobile: "/ month", "Flat price for up to 10 users", every module description, the
  procurement paragraph and the trial and billing note are 10px (about 2,100 characters). /schedule-demo mobile:
  the bullets and the language line are 9px. / and /fr mobile: testimonial quotes are 9px. Body copy elsewhere is
  14-17px, so this is a class that scales down too far, not a design choice. /capacity-planning and
  /tempo-alternative mobile are fine (12px minimum, body 14-18px).
- Fix: set a floor of 14px for body text and 12px for captions at the mobile breakpoint on the classes used in
  these blocks (likely `text-size-small` and the testimonial card text).
- KPI: demos and 50+ user trials; buyer-segment clicks (mobile usability). Tier: 3. Failed if: a re-run of
  `cap.js` still reports text under 12px on these pages.

### 3. /pricing opens on 10 users; a 50+ user buyer sees "$10 / month" and must interact to see their price
- Severity: Medium. CONFIRMED.
- Evidence: default state shows Standard "$10 / month" and Advanced "$15 / month", "Flat price for up to 10
  users". The full table (10 to 10,000 users, both editions, monthly and annual) is `display: none` until "See
  prices for every team size" is clicked; I clicked it on mobile and it opens and fits the screen (358px, 12px
  text). The "Compare with Tempo" block and the calculator on /tempo-alternative also default to 10 users, while
  that page's hero argues the 500-user case. On mobile the first price is in the second screen.
- Fix: draft for Ostap: default the selector to a mid-size team (100 or 500), or show the table open. Showing
  Advanced prices at all is an open question for Ostap (f07), not judged here.
- KPI: demos and 50+ user trials. Tier: 3. Failed if: trial starts or "Talk to us" clicks from /pricing fall in
  the four weeks after the change.

### 4. /pricing raw HTML says "$1,000 / month" for both editions until the script runs
- Severity: Medium for visitors, High for machine readers. CONFIRMED in saved HTML.
- Evidence: `<span data-pr="std-amt" ...>$1,000</span> / month` and the same in `data-pr="adv-amt"`, next to
  "≈ $2.08 per user per month · 51–100 user tier". Rendered with JavaScript it is $10 and $15. The same page's raw
  footer reads "© 2011 - 2021" (`id="currentYear"`; / and /schedule-demo have 2026).
- Fix: make the server-rendered placeholders true values (the default state) and set the year.
- KPI: AI citations on product, pricing or comparison pages. Tier: 3. Failed if: `curl` of /pricing still returns
  "$1,000" in `std-amt`.

### 5. /fr: English left in the page
- Severity: Medium. CONFIRMED (`fr-mobile-full.png`, `fr-desktop-atf.png`, rendered DOM).
- Evidence: the hero, nav, calls to action, proof row, section headings and FAQ are French. English remains in:
  the product tour mock-ups ("Team with Users", "Week", "Today", "Platform team, week 48", "4 people"); the Tempo
  import mock-up ("Choose the data to import", "Start import", "Ready to import", "Results appear here after the
  import", "Same hours, same attributes. Approvals, reports and project costs now run on this history."); two
  tour captions; one case-study card title (customer unnamed); six `aria-label` values ("ActivityTimeline product
  tour", "Replay step 1: Connect Tempo" and others).
- Fix: translate the captions, the Tempo mock-up sentence and the aria-labels. If the product screens themselves
  are English-only, keep the mock-ups and add one French line saying so. Existing page text only, no new post.
- KPI: buyer-segment clicks per 28 days. Tier: 3. Failed if: the strings are still in the rendered /fr.

### 6. Home and /fr mobile: hero label clipped, product tour too small to read
- Severity: Medium. CONFIRMED.
- Evidence: the label above the H1 ("Planner · Workspace · Timesheets · Reports · Finances") measures x -25 to
  415 on a 390px screen and is cut on both sides ("Finance" in English; on /fr it runs to 475px and starts
  mid-word). The Planner mock-up in the tour is scaled to the screen width, so its text is about 3-4px high. The
  ratings row above the testimonials is also cut at the left edge on /fr mobile.
- Fix: let the label wrap or shorten it on mobile; on mobile show the simplified card version of the tour step
  (the page already has one further down: "Platform team, Week 48") instead of the scaled desktop mock-up.
- KPI: demos and 50+ user trials. Tier: 3. Failed if: the label still measures wider than the viewport.

### 7. Small tap targets in secondary links (Low)
- CONFIRMED. Primary buttons are 42px high (fine). Text links are 20-24px high: "Schedule demo" beside the hero
  button (119x24), "See prices for every team size" (231x24), footer links (20px high, 26px apart), /pricing user
  chips 38px. Fix: add vertical padding to reach 44px on text links that carry a conversion. KPI: demos and 50+
  user trials. Tier: 3. Failed if: re-measure shows them under 44px.

### 8. Proof details that differ between pages (Low)
- CONFIRMED. /pricing "122 reviews on Atlassian Marketplace" against /tempo-alternative "125 reviews ... (5 Nov
  2026)" (f13 is 125). /pricing shows a "Bestseller on Atlassian Marketplace" badge where the other pages show
  "Atlassian Enterprise Certified". In the /pricing Tempo comparison both rows are titled "Planning and time
  tracking", though the second compares the set with Financial Manager and Advanced (LIKELY a label slip).
- Fix: use the f13 figure with its date; one badge set; relabel the second row. KPI: AI mention rate. Tier: 3.
  Failed if: the fact lint still flags f13 on /pricing.

### 9. /schedule-demo has no fallback if Calendly is blocked (Low)
- CONFIRMED in HTML (only the widget script; no link or form); how often visitors hit it is not measured. Here
  the page showed an empty card and no way to book. Fix: a plain "Can't see the calendar? Book here" link under
  the widget. KPI: demos and 50+ user trials. Tier: 3. Failed if: the link gets no clicks in eight weeks.

## Structured summary (for audit-data.json)

```json
{"category": "visual", "score": 78, "desktop": 90, "mobile": 70, "screenshots_valid": true,
 "not_checked": ["cookie banner", "chat overlay", "Calendly widget", "mobile menu", "Webflow interactions"],
 "horizontal_scroll": false, "broken_images": 0,
 "findings": [
  {"id": "V1", "severity": "High", "status": "CONFIRMED", "page": "/schedule-demo", "title": "Mobile: booking widget before the H1; bullets at 9px", "tier": 3},
  {"id": "V2", "severity": "High", "status": "CONFIRMED", "page": "/pricing, /schedule-demo, /, /fr", "title": "9-10px body text on mobile", "tier": 3},
  {"id": "V3", "severity": "Medium", "status": "CONFIRMED", "page": "/pricing", "title": "Default state 10 users; tier table hidden until clicked", "tier": 3},
  {"id": "V4", "severity": "Medium", "status": "CONFIRMED", "page": "/pricing", "title": "Raw HTML placeholder $1,000 / month and footer year 2021", "tier": 3},
  {"id": "V5", "severity": "Medium", "status": "CONFIRMED", "page": "/fr", "title": "English strings in mock-ups, captions, aria-labels", "tier": 3},
  {"id": "V6", "severity": "Medium", "status": "CONFIRMED", "page": "/, /fr", "title": "Mobile hero label clipped; tour mock-up unreadable", "tier": 3},
  {"id": "V7", "severity": "Low", "status": "CONFIRMED", "page": "site", "title": "Secondary links under 44px tall", "tier": 3},
  {"id": "V8", "severity": "Low", "status": "CONFIRMED", "page": "/pricing", "title": "122 vs 125 reviews, badge set, duplicate comparison label", "tier": 3},
  {"id": "V9", "severity": "Low", "status": "CONFIRMED", "page": "/schedule-demo", "title": "No booking fallback without Calendly", "tier": 3}
 ]}
```
