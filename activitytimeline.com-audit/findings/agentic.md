# Agent readiness: activitytimeline.com (19 Nov 2026)

**Category score: 68 / 100.** Derived from an eight-part rubric of my own (not the Lighthouse fraction, not the
toolkit's Agent-UX heuristic, both unavailable today): access policy 16/20, server-rendered content and real 404s
15/15, discovery files 8/10, Markdown delivery 1/5, accessibility tree on /, /pricing, /schedule-demo 14/25, task
"price for N users" 8/10, task "book a demo" 4/10, WebMCP 2/5.

## Summary

- **Lighthouse Agentic Browsing: not measured.** `lighthouse_agentic.py` (one try, mobile and desktop) got
  `PSI returned HTTP 429: Quota exceeded ... 'Queries per day'`. No fraction is reported and none is estimated.
- **Agent-UX heuristic (toolkit, 0-100): unavailable.** `agent_ux_check.py` and `agentic_check.py` both stop at the
  SSRF guard in this container (`Refusing configured HTTP proxy '127.0.0.1'`); neither has a saved-file mode. The same
  checks were done by hand with curl (21 requests) and system Chromium + Playwright (`ariaSnapshot`, DOM probes,
  scripted calculator run).
- **Measured P0 failures: 0.** Content is server-rendered, robots.txt is reachable and blocks no agent, unknown URLs
  return a real 404. Two P0 items were not tested: CLS (needs Lighthouse) and WAF behaviour toward agent user agents
  (`--ua-matrix` not authorized for this run).
- **What most limits agents today:** booking a demo. The only booking path is a third-party Calendly iframe injected
  by JavaScript, with no plain link behind it, and on /pricing and /tempo-alternative every "Book a demo" control is
  `<a href="#">`.

### Render caveat (read before trusting the tree findings)

The proxy blocks `cdn.prod.website-files.com` (Webflow CSS and JS), `d3e54v103j8qbb.cloudfront.net` (jQuery),
`assets.calendly.com`, `calendly.com`, `cdn.jsdelivr.net` and GTM. The pages were rendered **without the Webflow
stylesheet, without Webflow's interaction script and without Calendly**. Inline page scripts ran (the /pricing
calculator works). So: anything that depends on CSS visibility (mobile nav duplicate, target sizes, overlays, FAQ
collapse), on Webflow interactions (modal open, dropdown ARIA) or on the inside of the Calendly iframe is marked
LIKELY or "not checked". Findings marked CONFIRMED were seen in the raw HTML or in a script-driven run.

## What works (CONFIRMED)

- **Server-rendered.** /, /pricing, /schedule-demo return full HTML (568 KB, 226 KB, 164 KB) with the H1, copy, nav
  and footer links present without JavaScript. One H1 per page.
- **Real 404s.** `/this-page-does-not-exist-zz19`, `/pricing.md`, `/index.md`, `/llms-full.txt` and every
  `/.well-known/*` probe return `HTTP/2 404` (the well-known ones with the 88-byte body "Invalid .well-known
  request"). No catch-all 200, so nothing false-fails `llms-txt` or `ard-schema` in Lighthouse.
- **llms.txt is valid.** `HTTP/2 200`, `text/plain; charset=utf-8`, `x-robots-tag: noindex`, H1 `# ActivityTimeline`,
  a `>` summary, 53 Markdown links (32 on activitytimeline.com), 8.7 KB. It meets the three Lighthouse `llms-txt`
  rules (H1, a link, 50+ characters). It lists /pricing and /schedule-demo. No text in it addresses an agent with
  instructions.
- **Names and alt text.** 0 links without an accessible name and 0 images without `alt` on all three pages
  (267, 148 and 117 links).
- **Home page widgets are built properly.** Two `role="tablist"` groups with `role="tab"`, `aria-selected` and
  `tabindex="0"`; the pause and "Replay step N" controls are `role="button"` with `tabindex="0"` and names. Nav
  dropdowns are click-open (`data-hover="false"`), not hover-only.
- **The price calculator answers "price for N users".** Scripted run on /pricing: typing `250` in the textbox gives
  Standard `$520 / month` and Advanced `$770 / month`; "Annual" gives `$5,850 / year` and `$8,650 / year`; preset
  `500` + Annual gives `$8,450` and `$12,450`. Presets and the billing toggle carry `aria-pressed`; the table toggle
  carries `aria-expanded`. The full nine-row price table ("See prices for every team size") is in the raw HTML, so a
  fetch-only agent can read prices for 10 to 10,000 users without JavaScript. The calculator and the table agree
  (500 users annual: $8,450 in both; the $8,250 mismatch noted in lessons.md is gone).
- **No WAF challenge or CAPTCHA** was served to curl or headless Chromium on any request
  (`cf-cache-status: HIT`, no `cf-mitigated`).

## Access policy (three lines, never merged)

robots.txt, read 19 Nov 2026: one group, `User-agent: *`, `Allow: /`, `Disallow: /order`, `Disallow: /order?`,
`Sitemap:`. No group names any AI token. No `Content-Signal` line and no `content-signal` response header.

- **Training** (GPTBot, ClaudeBot, Google-Extended control token): allowed by default through the `*` group. No
  stated preference either way.
- **Search and answer indexes** (OAI-SearchBot, Claude-SearchBot, PerplexityBot): allowed by default through `*`.
- **User-triggered agents** (ChatGPT-User, Claude-User, Perplexity-User, Google-Agent): allowed; several of these do
  not treat robots.txt as binding anyway (vendor docs, checked 2026-09-23).

Behaviour of the Cloudflare WAF toward requests that carry these tokens: **not tested** (no authorization for
`--ua-matrix`). `/order` is disallowed but answers `HTTP/2 200` with a public "Order" page: it is not private data,
so the P1 "protect private paths with authentication" item does not apply.

## Findings by priority

Skill priority in brackets; severity is the audit severity asked for in the brief.

### 1. /schedule-demo offers no booking path to an agent that does not run the Calendly iframe [P1] — High, CONFIRMED (markup) / LIKELY (effect)

- **Evidence.** https://activitytimeline.com/schedule-demo raw HTML: the whole booking UI is
  `<div class="calendly-inline-widget" data-url="https://calendly.com/reliex/activitytimeline-product-demo-session?hide_event_type_details=1&hide_gdpr_banner=1" ...></div>`
  plus `<script src="https://assets.calendly.com/assets/external/widget.js" async>`. There is no `<a href>` to the
  Calendly page, no `<noscript>` fallback (the only `<noscript>` is GTM), no `<form>`, no email or phone alternative.
  Rendered accessibility tree of the page body (Calendly blocked here): H1, four bullet texts, three "what happens
  after you book" texts, then the footer. Nothing actionable. The page also has no `<main>` and no H2.
- **Why it matters.** A fetch-only agent (ChatGPT-User, Claude-User, Perplexity-User) asked "book me a demo with
  ActivityTimeline" finds a URL only inside a `data-url` attribute. A browsing agent must work inside a cross-origin
  iframe that appears after an async script; the inside of that iframe was not checked (host blocked).
- **Fix.** Under the widget add one visible line with a real link, for example "Calendar not loading? Open the
  booking page" pointing to the same Calendly URL (`target="_blank"`), and wrap the page content in `<main>`. Give
  the three "What happens after you book" items an H2. No change to the Calendly flow itself.
- **KPI.** Demos and 50+ user trials.
- **Tier.** 3 (reversible live change, Ostap's approval on the ticket). Draft is tier 2.
- **How we would know it failed.** Re-run `curl -s https://activitytimeline.com/schedule-demo | grep -c 'href="https://calendly.com/reliex'`:
  0 means it is not live. Calendly "scheduled events" by source over 28 days shows no bookings from the fallback
  link (add `utm_content=fallback-link`), which would mean nobody, human or agent, uses it and it can come out.

### 2. On /pricing and /tempo-alternative, "Book a demo" and "Talk to us" are `<a href="#">` [P0 class: interactive element semantics] — High, CONFIRMED (markup) / LIKELY (modal behaviour)

- **Evidence.** /pricing raw HTML: 14 anchors with `href="#"`. Three are
  `<a ... href="#" class="button is-primary with-shadow w-button">Book a 25-min demo →</a>` and one is
  `<a ... href="#" class="button is-secondary with-shadow w-button">Talk to us</a>`; they open a Webflow-interaction
  modal (`<div class="modal-wrapper"><div class="modal-card demo-session">`) that holds
  `<iframe id="demo-calendar" title="Book a demo" src="https://calendly.com/reliex/activitytimeline-product-demo-land?...">`.
  The modal has no `role="dialog"`, no `aria-modal`, no `aria-label`; its close control is
  `<div data-modal-close="true" class="icon-24px with-cursor w-embed">` (an icon-only `<div>`, no role, no name, no
  tabindex). /tempo-alternative: 12 `href="#"` anchors, **0** links to /schedule-demo, the same Calendly "-land"
  event, no `<main>`. /pricing links to /schedule-demo only twice (navigation).
- **Why it matters.** In the accessibility tree these are links whose URL is `#`: an agent that follows links goes
  nowhere, and one that clicks depends on a JavaScript interaction opening an unlabelled layer. The pricing page is
  where the charter wants the demo to start.
- **Fix.** Point each demo CTA's `href` at `/schedule-demo` and keep the modal as an enhancement (the interaction
  can still intercept the click). Add `role="dialog" aria-modal="true" aria-label="Book a demo"` to
  `.modal-card.demo-session` and make the close control a `<button aria-label="Close">`.
- **KPI.** Demos and 50+ user trials.
- **Tier.** 3. Note for the ticket: two Calendly events are in use (`...-demo-session` on / and /schedule-demo,
  `...-demo-land` on /pricing and /tempo-alternative). That may be deliberate attribution; the fix must not merge
  them.
- **How we would know it failed.** `grep -c 'href="#"' ` on the saved /pricing HTML is still 14; or Calendly
  bookings for the "-land" event drop in the 28 days after the change (then revert the href and keep only the ARIA).

### 3. Pricing calculator: the − and + steppers, the users field and the result are weak in the accessibility tree [P0 class] — Medium, CONFIRMED

- **Evidence** (https://activitytimeline.com/pricing, DOM probe after load):
  - Steppers: `<div data-pr-step="-1" class="button-with-icon">` and `<div data-pr-step="1" ...>`: `role` null,
    `tabindex` null (`tabIndex -1`), no `aria-label`, empty text (SVG only). In the snapshot they appear as two bare
    `img` nodes next to the textbox. They do work on click (500 → 550).
  - Users field: `<input data-pr-input="users" ... name="name" data-name="Name" placeholder="Users" type="text"/>`,
    two of them, no `<label>`, no `aria-label`; the visible text "Jira users" is a sibling `<div>`. The accessible
    name "Users" comes from the placeholder only. `type="text"` with no `inputmode`. Each sits in
    `<form name="email-form" data-name="Email Form" method="get">`.
  - Result: prices change in `[data-pr="std-amt"]` / `[data-pr="adv-amt"]` with no `aria-live` region (0 on page).
  - Price table: nine rows built from `<div class="pricing-table-row">` / `pricing-table-header-cell`; no `<table>`,
    no row or column roles, so the snapshot is one flat text run
    ("250 users $520 $5,850 201–300 tier $770 $8,650 201–300 tier ...").
  - Toggle: `<a data-pr-toggle="price-table" href="#">` has `aria-expanded` but no `aria-controls`.
  - FAQ: nine `<div data-w-id="..." class="faq-header">` question rows: no role, `tabIndex -1`. The answers are in
    the DOM text, so reading works; expanding by keyboard or by role does not.
- **Why it matters.** The task still completes (see "What works"), so this is not a blocker. The risk is a wrong
  reading: with a flat table an agent has to guess which of four dollar figures is "Advanced, annual", and the
  unlabelled field is named `name` inside a form called "Email Form".
- **Fix.** `aria-label="Jira users"` (or a real `<label for>`), `inputmode="numeric"`, and `name="users"` on both
  inputs; turn the steppers into `<button type="button" aria-label="Fewer users">` / `"More users"`; add
  `aria-live="polite"` on the two edition price blocks; rebuild the price table as a real `<table>` with `<th
  scope="col">` and `<th scope="row">` (an HTML embed, same nine rows); make FAQ headers `<button aria-expanded>`.
  The calculator script finds elements by `data-pr-*`, so the attributes survive a tag change.
- **KPI.** AI citations on product, pricing or comparison pages; demos and 50+ user trials.
- **Tier.** 3. Any price text that moves must pass `/seo activitytimeline facts` first; Advanced Edition prices are
  an open question for Ostap (f07) and this finding takes no position on them.
- **How we would know it failed.** Re-run the DOM probe in
  `SCRATCH/work-seo-agentic/scripts/task.js`: `steps[].role` still null, `live` still 0, or the calculator stops
  returning `$520` for 250 users monthly (a regression from the tag change, revert at once).

### 4. Landmarks: no `contentinfo` anywhere, no `main` on /schedule-demo and /tempo-alternative, nested `banner` [P0 class, small] — Medium, CONFIRMED

- **Evidence.** Raw HTML of /, /pricing, /schedule-demo: 0 `<footer>` and 0 `role="contentinfo"` (the footer is
  `<div class="footer v2 section-4">`). /schedule-demo and /tempo-alternative: 0 `<main>`. All three pages:
  `<header class="header-nav">` containing `<div ... role="banner" class="nav-bar w-nav">` and a second
  `role="banner"` on `nav-bar-mobile` (snapshot: `banner > banner`, plus a duplicate banner). Each nav column in the
  mega menu is its own unnamed `navigation` (14 `nav` elements, none with `aria-label`).
- **Why it matters.** Landmarks are how DOM- and tree-reading agents skip 100+ navigation links to reach the page
  body. On /schedule-demo there is no `main` to jump to.
- **Fix.** In Webflow set the footer wrapper's tag to `footer`, the content wrapper on /schedule-demo and
  /tempo-alternative to `main`, remove `role="banner"` from the inner nav bars (the `<header>` already supplies it),
  and add `aria-label` ("Product", "Solutions", "Resources", "Footer") to the nav elements. Shared components: one
  change covers every page and all four locales.
- **KPI.** Demos and 50+ user trials (demo page); AI citations on product, pricing or comparison pages.
- **Tier.** 3.
- **How we would know it failed.** `grep -c '<footer\|<main'` on the live HTML of the three pages stays at 0/1; or a
  visual regression in header or footer after the tag change (check all four locales before and after).

### 5. llms.txt points at a redirecting URL and omits two commercial pages [P1] — Low, CONFIRMED

- **Evidence.** https://activitytimeline.com/llms.txt line 17:
  `- [Jira reports](https://activitytimeline.com/advanced-jira-reports): ...` (that URL now 301s to /reports).
  `grep` for `tempo-alternative` and `how-it-works`: no match. Content quality and citability of the file belong to
  the geo specialist; this is the discovery side only.
- **Fix.** Change the link to `/reports`; add /tempo-alternative and /how-it-works under "Product overview and
  evaluation".
- **KPI.** AI citations on product, pricing or comparison pages. No ranking or citation effect is promised: no
  vendor confirms that a consumer agent reads llms.txt, and Google Search ignores it.
- **Tier.** 3.
- **How we would know it failed.** `curl -s .../llms.txt | grep -c advanced-jira-reports` is not 0.

### 6. Footer on /pricing and /features says "© 2011 - 2021" [P3] — Low, CONFIRMED

- **Evidence.** Raw HTML footer on /pricing and /features:
  `© 2011 - </div><div id="currentYear" class="text-body _13px">2021</div>`. / and /schedule-demo carry `2026` in the
  same element, so two footer variants are live. A script may correct the year in a browser (not confirmed: the
  Webflow script was blocked here and /pricing rendered 2021); a fetch-only agent reads 2021 either way.
- **Fix.** Type the current year into the static element of the older footer variant, or replace that variant with
  the shared footer component used on /.
- **KPI.** AI mention rate (a stale date is a small freshness signal in a fetched copy of the pricing page).
- **Tier.** 3.
- **How we would know it failed.** `curl -s https://activitytimeline.com/pricing | grep -o 'currentYear[^<]*>[0-9]*'`
  still prints 2021.

### Opportunities (absence is not a defect)

- **Content-Signal** [P1, info]: not present. Cloudflare CC0 policy; the IETF individual draft expired 2026-04-04;
  no Google statement found (checked 2026-09-23). If Ostap wants a stated preference, one line in the `*` group is
  enough because there are no named groups. Whether `ai-train` is yes or no is his decision; I do not recommend
  one. No confirmed effect on any KPI.
- **Markdown delivery** [P1, info]: none. `Accept: text/markdown` on / and /pricing returns `text/html`;
  `vary: accept-encoding` only; `/pricing.md` is 404; no `<link rel="alternate" type="text/markdown">`. No primary
  source shows a consumer agent sending that header. Webflow cannot do this natively; it would need a Cloudflare
  feature in front. Not recommended now. If it is ever switched on, apply the help-centre lesson of 9 Nov: `.md`
  responses need `X-Robots-Tag: noindex`.
- **ai-catalog.json and /.well-known documents** [P3]: all 404, correctly. There is no MCP server, public API or
  A2A agent to list, so publishing one would only add a counted Lighthouse failure risk.
- **WebMCP** [P2]: none (`document.modelContext` absent, 0 `registerTool`, 0 forms with `toolname`). The site has no
  first-party form to bind a tool to: the calculator is client-side text and the booking is Calendly's. Not
  recommended now.

## Not found (checked, clean)

- No interactive element with an empty accessible name; no `aria-hidden` wrapper around focusable elements.
- No cookie or consent layer in the DOM of the three pages (GTM was blocked here, so a GTM-injected banner is not
  ruled out: not checked).
- No text in robots.txt, llms.txt or the three pages that addresses an AI agent with instructions.

## Standards status (dates from references/vendor-matrix.md, last full check 2026-09-23, 57 days old)

- Lighthouse Agentic Browsing category: Lighthouse 13.5.0 at the last check; version today not confirmed (PSI 429).
- Content-Signal: Cloudflare policy, not an IETF standard; individual draft expired 2026-04-04.
- llms.txt: community proposal (llmstxt.org); counted by Lighthouse, ignored by Google Search.
- ai-catalog.json (ARD 1.0): proposal, validated by Lighthouse 13.5.
- MCP Server Card (SEP-2127): open and unmerged at 2026-09-12.
- WebMCP: draft. Chrome origin trial M149 to M156 with a secondary-sourced end date of 2026-11-17, which has now
  passed; current status is **unverified**. WebKit opposes, Mozilla is not implementing.
- Web Bot Auth: `draft-ietf-webbotauth-httpsig-protocol-00` (2026-09-01). Site owners verify at the edge; nothing
  to publish here.

## Not checked

- Lighthouse Agentic Browsing fraction and CLS: PSI quota (HTTP 429). Local alternative:
  `npx lighthouse@latest https://activitytimeline.com/ --only-categories=agentic-browsing --output=json`, then
  `lighthouse_agentic.py --from-json`.
- Toolkit Agent-UX heuristic and `agentic_check.py`: blocked by the SSRF guard behind this proxy.
- Inside of the Calendly iframe (field labels, time-slot buttons, confirmation state): calendly.com blocked.
- CSS-dependent items: target sizes (24 x 24 px), overlays, hover states, whether the mobile nav copy is hidden
  from the tree: Webflow CDN blocked.
- Whether the Webflow interaction script adds ARIA to FAQ headers or the modal at runtime: script blocked.
- WAF treatment of AI user agents: not authorized. www host: blocked.
- /es, /fr, /pt versions of /pricing and /schedule-demo: not rendered (shared components, so findings 2 to 4 very
  likely apply: LIKELY).

## Structured findings (for audit-data.json, AI Search Readiness)

```json
[
  {"title": "Demo page has no booking link outside the Calendly iframe", "severity": "High",
   "description": "/schedule-demo exposes the booking only as a JS-injected Calendly widget (URL in a data-url attribute); no <a href>, no noscript, no <main>.",
   "recommendation": "Add a visible fallback link to the Calendly booking page under the widget and wrap the content in <main>."},
  {"title": "Demo CTAs on /pricing and /tempo-alternative are href=\"#\"", "severity": "High",
   "description": "14 href=\"#\" anchors on /pricing (3 'Book a 25-min demo', 1 'Talk to us') and 12 on /tempo-alternative open an unlabelled modal; /tempo-alternative has no link to /schedule-demo.",
   "recommendation": "Point the CTAs at /schedule-demo, keep the modal as an enhancement, add role=dialog, aria-modal and a named close button."},
  {"title": "Pricing calculator controls are weak in the accessibility tree", "severity": "Medium",
   "description": "Stepper buttons are unnamed non-focusable divs, the users field has no label (placeholder only, name=\"name\"), no aria-live on results, price table and FAQ headers are plain divs. The task still completes.",
   "recommendation": "Use real buttons with aria-labels, label the input, add aria-live, rebuild the price table as a <table>, make FAQ headers buttons."},
  {"title": "Missing landmarks", "severity": "Medium",
   "description": "No footer/contentinfo on any page, no <main> on /schedule-demo and /tempo-alternative, nested role=banner, 14 unnamed nav elements.",
   "recommendation": "Set the footer and main tags in Webflow, drop the inner role=banner, label the nav elements."},
  {"title": "llms.txt has a redirecting link and omits two commercial pages", "severity": "Low",
   "description": "Line 17 links /advanced-jira-reports (301 to /reports); /tempo-alternative and /how-it-works are absent.",
   "recommendation": "Update the link and add the two pages."},
  {"title": "Footer year is 2021 on /pricing and /features", "severity": "Low",
   "description": "Raw HTML of /pricing and /features carries '© 2011 - 2021'; / and /schedule-demo carry 2026.",
   "recommendation": "Set the current year in the static element."}
]
```

Evidence files: `/tmp/claude-0/-home-user-claude-seo-for-AT/59906b2c-085a-5d20-be69-6c6e01a02638/scratchpad/work-seo-agentic/`
(`fetch/*.hdr`, `out/*.aria.yml`, `out/*.stats.json`, `out/task.log`, `scripts/snap.js`, `scripts/task.js`).
