# Visual and mobile experience: activitytimeline.com, 19 Nov 2026

**Category score: not measured visually. Provisional 70/100, low confidence.**
Derived only from DOM and raw-HTML checks (hero order, CTAs, proof lines, viewport meta, menu markup, price
markup, /fr text). No styled rendering was possible, so layout, tap targets, text size, horizontal scroll, banner
overlap and image loading are NOT in this number. Do not publish or weight this score until the pages are rendered
on a machine that can reach the site's asset CDN.

## Blocker: the screenshots are unstyled and must not be used as visual evidence

The container's network policy refuses the Webflow asset host. Every stylesheet, script, image and font request
failed in Chromium (`net::ERR_TUNNEL_CONNECTION_FAILED`; proxy status: "gateway answered 403 to CONNECT" for
`cdn.prod.website-files.com:443`). Also refused: `d3e54v103j8qbb.cloudfront.net` (jQuery), `cdn.jsdelivr.net`,
`www.googletagmanager.com` (which loads the CookieYes banner), `assets.calendly.com` / `calendly.com`,
`www.google.com`, `bat.bing.com`, `files.activitytimeline.com`. I did not try to get around the policy.

The 24 PNGs in `activitytimeline.com-audit/screenshots/` (`<page>-<desktop|mobile>-<atf|full>.png`, 1440x900 and
iPhone 13, deviceScaleFactor 1) therefore show browser-default HTML: blue links, no layout, broken image icons. I
looked at them; they prove only source order and text. They take 29 MB. Recommend the lead deletes or ignores them
and re-runs the capture script from a machine with normal network access:
`/tmp/claude-0/-home-user-claude-seo-for-AT/59906b2c-085a-5d20-be69-6c6e01a02638/scratchpad/work-seo-visual/cap.js`
(`node cap.js`; it also writes tap-target, font-size, overflow, fixed-element and broken-image metrics to
`metrics.json`). The metrics.json from today's run is from the unstyled render and is not valid for those checks.

### Not checked (needs a styled render)
- What is inside the first viewport on desktop and mobile (only source order is known, see below)
- Cookie banner (CookieYes, loaded through GTM): presence, size, whether it covers the hero or the call to action
- Chat widget (Freshchat) and Hotjar overlays
- Horizontal scroll, tap-target sizes, text sizes, hamburger menu behaviour on mobile
- Layout breaks, overlapping elements, image loading, customer-logo strip rendering
- Whether the /pricing tier table is collapsed until "See prices for every team size" is clicked
- The Calendly booking widget on /schedule-demo (third-party script blocked)

## What the DOM shows (source order; all CONFIRMED in rendered DOM or saved HTML unless marked)

| Page | H1 | First calls to action after H1 | Proof lines near the hero |
|---|---|---|---|
| / | "Capacity Planning, Time Tracking and Project Costs in Jira" | "Start free trial →" or "Schedule demo"; "30-day free trial with all five modules, on your own Jira data" | "4.7 / 5 on Atlassian Marketplace", Enterprise Certified, Platinum Marketplace Partner, SOC 2 Type 2, ISO 27001:2022 |
| /pricing | "Planner, Timesheets, and Finances. One app, priced per user." | user-count chips 10 to 10,000, Monthly/Annual, two edition cards each with "Start free trial" | "4.7★ 122 reviews on Atlassian Marketplace" (f13 says 125; already known) |
| /capacity-planning | "Capacity Planning for Jira Teams in ActivityTimeline" | "Start free trial", "Schedule demo" | three benefit chips, then "Trusted by 10,000+ teams", "4.7/5 on Atlassian Marketplace", Trust Center |
| /tempo-alternative | "Timesheets, Planner and Finances in one Jira app. The Tempo alternative that costs less." | "Book a 25-min migration call →" or "Start free trial" | four certification badges, a dated price comparison block, "4.7★ 125 reviews on Atlassian Marketplace (5 Nov 2026)", "10,000+ teams" |
| /schedule-demo | "Free ActivityTimeline Product Demo" | none in HTML: booking depends on the Calendly script | six bullet points (25 minutes, up to 10 teammates, four languages) |
| /fr | "Planification de la capacité, suivi du temps et coûts des projets dans Jira" | "Démarrer l'essai gratuit →" ou "Planifier une démo" | "4,7 / 5 sur l'Atlassian Marketplace", certifications, all in French |

What works: every page has one H1 that states the product and Jira; a trial and a demo call to action follow the
H1 directly in source order; proof (rating, certifications) sits next to the hero rather than far down the page;
`<meta name="viewport" content="width=device-width, initial-scale=1">` on all six; the main nav collapses to a
menu button at tablet width (`data-collapse="medium"`); /tempo-alternative uses a reduced landing header (logo,
About, two calls to action) and shows dated, sourced Tempo prices in the hero; /fr sets `lang="fr-FR"` and its
hero, nav labels and proof line are translated.

## Findings

### 1. /pricing raw HTML shows "$1,000 / month" for both editions; the real figures exist only after JavaScript runs
- Severity: High. CONFIRMED.
- Evidence: saved HTML of https://activitytimeline.com/pricing:
  `<span data-pr="std-amt" class="text-weight-medium pricing">$1,000</span> ... / month` with
  `≈ $2.08 per user per month · 51–100 user tier`, and the same `$1,000` in `data-pr="adv-amt"` (Advanced).
  $2.08 x 100 users is about $208, not $1,000 a month, so the placeholder contradicts itself. With JavaScript the
  cards read "$10 / month, Flat price for up to 10 users" (Standard) and "$15 / month" (Advanced).
- Why it matters: fetchers that do not run JavaScript (most AI assistants' fetchers, some crawlers, link previews)
  read a wrong price, identical for both editions. A buyer with a slow or blocked script sees it too.
- Fix: make the server-rendered placeholder a true state (the 10-user default: $10 and $15 a month, with the
  matching sub-line), so the page is right before the script runs. Whether Advanced prices should be on /pricing
  at all is an open question for Ostap (f07 covers one figure only); this finding is about the placeholder, not
  about the Advanced prices being right or wrong.
- KPI: AI citations on product, pricing or comparison pages; cost and budget prompt mention rate.
- Tier: 3 (reversible live change, Ostap approves on the ticket).
- Failed if: `curl` of /pricing still returns "$1,000" in `data-pr="std-amt"` after publishing, or an AI answer
  quoting the page gives $1,000 a month.

### 2. /pricing opens on the 10-user state, so a 50+ user buyer first sees "$10 / month"
- Severity: Medium. CONFIRMED in the rendered DOM (default state); what is in the first viewport is not checked.
- Evidence: after load the cards read "$10 / month · Flat price for up to 10 users" and "$15 / month". The full
  tier table sits in `<div data-pr-panel="price-table" class="pricing-table">` behind the link
  `<a data-pr-toggle="price-table">See prices for every team size</a>` (LIKELY collapsed until clicked; needs a
  styled render). The enterprise line "at 5,000 users, Advanced is about $0.79 per user per month" comes after
  both cards.
- Fix: draft two options for Ostap: open on a mid-size default (for example 100 or 500 users) or show the tier
  table open by default. Prices then show for the charter's target buyer without a click.
- KPI: demos and 50+ user trials.
- Tier: 3.
- Failed if: trial starts or "Talk to us" clicks from /pricing fall in the four weeks after the change (GA4).

### 3. /fr still carries English strings
- Severity: Medium. CONFIRMED in the rendered DOM of https://activitytimeline.com/fr.
- Evidence: (a) a case-study card title in English, "How [customer] Improved Resource Planning for Multiple
  Projects with ActivityTimeline" (customer name withheld); (b) product-tour captions injected by script: "The
  team total looks fine, but" and "from Wednesday after two days of vacation. Emma has free days."; (c)
  `aria-label` values in English: "Why teams trust ActivityTimeline", "ActivityTimeline product tour",
  "ActivityTimeline modules", "Replay step 1: Connect Tempo", "Replay step 2: Choose what to import", "Replay
  step 3: Check the result". Only /fr was checked; /es and /pt probably share (b) and (c) (LIKELY).
- Fix: translate the tour strings and aria-labels in the embed; for the case-study card either translate the
  title or label the card as English content. This is a fix to existing page text, not a new localized post.
- KPI: buyer-segment clicks per 28 days (localized pages); commercial pages indexed.
- Tier: 3.
- Failed if: the same strings are still in the rendered DOM of /fr after publishing.

### 4. /schedule-demo has no way to book if the Calendly script does not load
- Severity: Medium. CONFIRMED (in this container the page rendered with zero iframes and no booking link in the
  hero); how often real visitors hit it is not measured.
- Evidence: the hero contains only the H1, a paragraph and six bullets; booking is
  `calendly-inline-widget` + `calendly.com/assets/external/widget.js`. The only `<noscript>` on the page is the
  GTM one. Corporate networks and content blockers that refuse third-party schedulers leave an empty area.
- Fix: add a plain fallback under the widget: a link to the Calendly page and a contact address ("Can't see the
  calendar? Book here").
- KPI: demos and 50+ user trials.
- Tier: 3.
- Failed if: the fallback link gets no clicks in eight weeks (then the problem is rare and the link is harmless).

### 5. Review count differs between pages a buyer compares
- Severity: Low. CONFIRMED. Already known to the lead; listed because it is visible proof text.
- Evidence: /pricing "4.7★ 122 reviews on Atlassian Marketplace"; /tempo-alternative "4.7★ 125 reviews on
  Atlassian Marketplace (5 Nov 2026)". Fact f13: 125 (5 Nov 2026).
- Fix: set /pricing to the f13 figure with its date. KPI: AI mention rate (consistent facts). Tier: 3.
- Failed if: `/seo activitytimeline facts` on /pricing still flags f13.

### 6. Images have no width and height attributes (Info, hand to the performance specialist)
- CONFIRMED in saved HTML: / 56 of 61 `<img>` without `width`; /capacity-planning 20 of 25; /pricing 11 of 16;
  /tempo-alternative 21 of 22. Every content image is `loading="lazy"`. Layout shift from this is not measured
  here (no styled render). One `<img>` without `alt` per page is a hidden tracking pixel, not a content image.

## Structured summary (for audit-data.json)

```json
{"category": "visual", "score": null, "provisional_score": 70, "confidence": "low",
 "blocked": "asset CDN cdn.prod.website-files.com refused by network policy; screenshots unstyled",
 "screenshots_valid": false,
 "findings": [
  {"id": "V1", "severity": "High", "status": "CONFIRMED", "page": "/pricing", "title": "Raw HTML price placeholder $1,000 / month for both editions", "tier": 3},
  {"id": "V2", "severity": "Medium", "status": "CONFIRMED", "page": "/pricing", "title": "Default state is 10 users; tier table behind a toggle", "tier": 3},
  {"id": "V3", "severity": "Medium", "status": "CONFIRMED", "page": "/fr", "title": "English strings in tour captions, aria-labels and one case-study title", "tier": 3},
  {"id": "V4", "severity": "Medium", "status": "CONFIRMED", "page": "/schedule-demo", "title": "No booking fallback when Calendly script is blocked", "tier": 3},
  {"id": "V5", "severity": "Low", "status": "CONFIRMED", "page": "/pricing", "title": "122 vs 125 reviews", "tier": 3},
  {"id": "V6", "severity": "Info", "status": "CONFIRMED", "page": "site", "title": "Images without width/height", "tier": 3}
 ]}
```
