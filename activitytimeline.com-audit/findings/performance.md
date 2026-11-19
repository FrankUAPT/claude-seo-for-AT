# Performance and images: activitytimeline.com, 19 Nov 2026

**Performance score: 60 / 100 (low confidence).** Derived from what could be measured (document delivery, HTML weight, DOM size, script and iframe loading order) and not from Core Web Vitals: LCP, CLS, TBT, CSS/JS/image/font weight could not be measured today (see "Not measured"). Start 100; minus 12 render-blocking third-party script on every page, minus 10 hidden Calendly iframe on /pricing and /tempo-alternative, minus 10 HTML and DOM weight, minus 8 for missing measurement of the vitals themselves (unknown is not a pass).

**Images score: 55 / 100 (medium confidence, attributes only).** Start 100; minus 20 no `height` on any image on any of 21 pages, minus 10 `loading="lazy"` on above-the-fold header images, minus 10 PNG/JPG without modern format on blog and home, minus 5 no `fetchpriority` on hero images. Image byte sizes were not measured.

All numbers below are **lab data from a cloud container in the US, not field data**. None of them is a Core Web Vitals pass or fail.

## Not measured (and why)

| Item | Status |
|---|---|
| CrUX field data (LCP, INP, CLS at p75) | Not measured. Keyless PageSpeed Insights API returned HTTP 429 for /, /pricing and /capacity-planning, and again on one retry ("Quota exceeded ... Queries per day"). No Google credentials. |
| Lab LCP and its element, CLS, TBT (INP proxy) | Not measured. System Playwright Chromium 157 loaded the HTML document, but the container proxy refuses every asset host: `cdn.prod.website-files.com` (CSS, JS, all images), `d3e54v103j8qbb.cloudfront.net` (jQuery), `www.google.com` (reCAPTCHA), `www.googletagmanager.com`, `cdn.jsdelivr.net`, `calendly.com`, `bat.bing.com` all failed with `ERR_TUNNEL_CONNECTION_FAILED` (gateway 403). An unstyled, script-less render gives meaningless LCP/CLS/TBT, so none is reported. |
| Transfer size of CSS, JS, images, fonts; third-party weight | Not measured (same block). Only the HTML document weight is real. |
| Font loading (`font-display`, formats, preload) | Not measured: `@font-face` rules live in the blocked stylesheet. The HTML has no font `preload` link; font family is Inter. |
| Which element is the LCP, and whether it is lazy or lacks dimensions | Not measured. Static reading only: see finding 4. |
| www host | Not checked (host blocked). |

To close the gap: run PageSpeed Insights from a browser (or tomorrow, when the shared quota resets), or start the session in an environment that allows the asset hosts. The measurement script is ready: `/tmp/claude-0/-home-user-claude-seo-for-AT/59906b2c-085a-5d20-be69-6c6e01a02638/scratchpad/work-seo-performance/measure.js` (mobile with CPU 4x, mobile with slow 4G, desktop).

## What was measured (lab, cloud container in the US, 19 Nov 2026 ~12:10 UTC)

| Page | TTFB, curl x3 | HTML compressed / raw | Elements in HTML | `<img>` | Inline SVG | Inline JS | Inline CSS |
|---|---|---|---|---|---|---|---|
| / | 132-164 ms | 126 KB / 568 KB | 3,694 | 60 | 317 (242 KB) | 98 KB | 57 KB |
| /pricing | 120-154 ms | 57 KB / 226 KB | 1,859 | 15 | 118 (109 KB) | 23 KB | 0.2 KB |
| /capacity-planning | 125-148 ms | 76 KB / 271 KB | 1,486 | 24 | 128 (116 KB) | 90 KB | 0.2 KB |

Requests the parser starts at load (before scroll, same on all three): 1 stylesheet, 4 synchronous scripts at the end of `<body>` (jQuery 3.5.1 from cloudfront + 3 Webflow chunks), 1 synchronous script in `<head>` (reCAPTCHA), GTM (async), Finsweet Attributes (async module, jsdelivr), 4 images; on desktop also `bat.bing.com`. /pricing adds 4 eager badge images and the Calendly iframe.

## What works

- Delivery: Cloudflare cache HIT, HTTP/2 with h3 advertised, TTFB 120-164 ms in the lab (well under the 800 ms guide value, lab only), compressed HTML, 103 Early Hints with `preconnect` to the asset CDN and a `preload` of the one stylesheet.
- One stylesheet, no web-font or CSS third parties in the HTML, no base64 images.
- Freshchat loads only after the first user interaction and never on mobile (inline script, footer). Home-page Calendly loads through an IntersectionObserver with a 600 px margin. Both are the right pattern.
- Commercial pages use SVG icons and code-drawn product visuals in place of screenshots: 14 of 15 images on /pricing and 23 of 24 on /capacity-planning are SVG. Images default to `loading="lazy"`.
- Guides: the hero image is `loading="eager"` with `srcset`; 11-14 WebP images per guide.

## Findings

### 1. High. reCAPTCHA script blocks rendering on every page, including pages with no form. CONFIRMED (tag), LIKELY (cost)
- Evidence: `<script src="https://www.google.com/recaptcha/api.js" type="text/javascript"></script>` in `<head>` with no `async` or `defer`, on 21 of 21 saved pages. `/`, `/capacity-planning`, `/features` and `/schedule-demo` contain 0 `<form>` elements; no page checked has a `g-recaptcha` element. In the lab run the browser requested it at priority High before first paint.
- Why it matters: a synchronous third-party script in the head stops HTML parsing until google.com answers, on a new connection (the Early Hints preconnect covers only the asset CDN). It then pulls the main reCAPTCHA bundle from gstatic (size not measured here). It is the only render-blocking third party on the site.
- Fix: in Webflow Site settings > Apps and integrations > reCAPTCHA, turn validation off if the two live forms (pricing and tempo-alternative modals) can use Webflow's own spam protection or a honeypot; if reCAPTCHA must stay, Webflow injects it site-wide, so move the forms to an embedded form tool that loads its own check on submit. Ask Ostap which forms need it.
- KPI: demos and 50+ user trials (faster first paint on the pricing and demo path); buyer-segment clicks (CWV is a tiebreaker only).
- Tier 3 (reversible site setting; needs a publish by Ostap).
- Failed if: form spam rises in the two weeks after the change, or PSI still lists `recaptcha/api.js` under render-blocking requests.

### 2. High. /pricing and /tempo-alternative load the Calendly booking iframe inside a closed modal on every visit, and request it twice. CONFIRMED
- Evidence: `/pricing` line 287, inside `<div class="modal-background not-active">` before the `<h1>`: `<iframe id="demo-calendar" title="Book a demo" src="https://calendly.com/reliex/activitytimeline-product-demo-land?hide_gdpr_banner=1&...">`, no `loading="lazy"`. The inline script right after it calls `render()` at once and sets `frame.src` again with UTM parameters. Lab request log for /pricing: two `calendly.com` Document requests at priority VeryHigh, the first `ERR_ABORTED`. `/tempo-alternative` line 68 has the same iframe in `#ts-modal`.
- Why it matters: the whole Calendly app (document, scripts, fonts; weight not measured here) competes with the page's own CSS, scripts and hero for bandwidth and main thread on the two pages closest to a purchase decision, for a modal most visitors never open.
- Fix: ship the iframe without `src` (keep the URL in `data-src`) and set it in `render()` only when the modal opens; call `render()` from the open handler in place of the page-load call. The consent/UTM logic stays the same. The home page already does the equivalent with an IntersectionObserver.
- KPI: demos and 50+ user trials; AI citations on pricing or comparison pages is not affected.
- Tier 3 (custom-code edit, reversible).
- Failed if: the calendar shows blank for more than about a second after "Schedule demo" is clicked, or demo bookings from /pricing drop week on week (Calendly `utm_campaign=/pricing`).

### 3. Medium. Every page ships a 130 KB header and a DOM far above 1,500 elements on the home and features pages. CONFIRMED
- Evidence: `<header>...</header>` is 130.5 KB raw (about 30 KB gzip, 870 elements, 79 inline SVGs, 83 links) on every page: 23% of the home HTML, 58% of /pricing. Total elements: `/` 3,694, `/features` 3,273, `/es` 3,636, `/pricing` 1,859, `/capacity-planning` 1,486. Home HTML is 568 KB raw, 126 KB compressed, with 317 inline SVGs (242 KB), 98 KB inline JS and 57 KB inline CSS.
- Why it matters: large DOM raises style and layout cost on every interaction (an INP risk on mid-range phones; not measured) and the mega menu is parsed before the hero on every page. The inline home-page widgets are not cacheable across pages or locales.
- Fix: (a) header: replace repeated inline SVG icons with one external SVG sprite or `<img>` icons, and drop the blog-card image block from the mega menu; target under 40 KB raw. (b) home: move the four `:host{...}` widget style blocks and the 37 KB/15 KB widget scripts into one hosted, cached file loaded with `defer`, and mount below-the-fold widgets on IntersectionObserver as the Calendly block already does.
- KPI: buyer-segment clicks (weak, tiebreaker); commercial pages indexed (lighter HTML is cheaper to crawl and render; weak).
- Tier 2 for the draft, tier 3 to ship (shared component: read back all four locales after the edit, per lessons.md).
- Failed if: the header HTML is not under about 60 KB after the change, or PSI "Optimize DOM size" still reports more than 1,500 elements on /pricing and the product pages.

### 4. Medium. No image on any page has a `height` attribute; the header logo is lazy-loaded. CONFIRMED (attributes), LIKELY (layout shift)
- Evidence: 21 of 21 saved pages: every `<img>` lacks `height` (4 per page have `width` only), e.g. `<img src=".../6141dba8ea34267e6ed2d54a_at_new_logo_dark.svg" loading="lazy" width="116" alt="ActivityTimeline App logo" class="img__at-logo">`: the first image in the document, above the fold, and lazy. On the home page the customer-logo strip under the hero (`class="logo-item_logo"`, `loading="lazy"`, no dimensions) is the first content image, which is what the gate flagged (60 of 60 without dimensions, lazy first image). No image on the 12 commercial pages has `fetchpriority`.
- LCP element (static reading, LIKELY): on `/`, `/pricing` and `/capacity-planning` the hero is text plus code-drawn visuals, with no hero `<img>`, so the LCP is probably the `<h1>` or a lead paragraph and the "lazy LCP image" problem probably does not apply to these three pages. It can apply to the guides and blog posts, whose hero is a real image (the guides already set it `eager`).
- Why it matters: without both dimensions the browser cannot reserve space unless the CSS fixes the size (CSS not readable today), so logos and icons can shift content as they arrive (CLS risk). A lazy header logo is fetched late for no saving.
- Fix: in the Webflow header component set the two logo images to `loading="eager"`; add width and height (Webflow writes both when the image element has explicit size set from the asset; for images in embeds, add the attributes by hand). Set the hero image of guide and blog templates to `fetchpriority="high"`.
- KPI: buyer-segment clicks (weak, tiebreaker); demos and trials (visual stability on pricing).
- Tier 3 (reversible, shared component).
- Failed if: a field or PSI run still shows layout shifts attributed to `img.img__at-logo` or `.logo-item_logo`, or the gate check `images-missing-dimensions` still reports all images.

### 5. Medium. Blog index and home still serve PNG/JPG where WebP or AVIF would do. CONFIRMED (formats), sizes not measured
- Evidence: `/blog`: 214 images, 104 PNG, 24 JPG, 76 WebP, 0 AVIF; 92 with `srcset`, 122 without. `/`: 12 reviewer photos are PNG with no `srcset` (3 files, each repeated 4 times in the review marquee). The mega-menu blog card PNG is on every page of the site. Guides: 5-8 PNG each next to 11-14 WebP.
- Fix: convert in Webflow Assets (the built-in "Compress" to WebP/AVIF) starting with the mega-menu card image (site-wide), the 3 reviewer photos and blog thumbnails; reviewer photos should be exported at their display size (avatars).
- KPI: buyer-segment clicks (weak); mostly a page-weight gain on /blog.
- Tier 3 (asset replacement, reversible).
- Failed if: `/blog` still has more than 20 PNG/JPG images after the pass.

### 6. Low. jQuery and three Webflow scripts load synchronously; HTML came back gzip, not Brotli. CONFIRMED / LIKELY
- Evidence: end of `<body>`: `jquery-3.5.1.min...js` (cloudfront, a second origin with no preconnect) and three `webflow.*.js` files with no `defer`. Standard Webflow output, not render-blocking for first paint, but it delays interactivity; sizes not measured. `curl -H 'Accept-Encoding: br, gzip'` returned `content-encoding: gzip` (through the container proxy, so check in a browser before acting).
- Fix: none needed now; if Brotli is really off, it is a Webflow hosting setting to raise with Webflow support. Adding `<link rel="preconnect" href="https://d3e54v103j8qbb.cloudfront.net">` in site head code is a cheap tier 3 change.
- KPI: none directly; do not ticket this alone.

### 7. Info. Third parties present (weight not measured)
Google Tag Manager `GTM-N7ZQ2HH` (async, in head; whatever it injects, including CookieYes and Bing UET `bat.bing.com`, was not inspectable), reCAPTCHA (finding 1), Finsweet Attributes from jsdelivr (async module, `fs-autovideo`), Calendly (finding 2), Freshchat (deferred to first interaction, desktop only), YouTube via a Webflow lightbox (loads on click). A footer script appends `og:url` after DOMContentLoaded: no performance cost, passed to the technical specialist.

## Priority order
1. Finding 2 (one custom-code edit, two money pages).
2. Finding 1 (one site setting, every page; needs Ostap's answer on spam protection).
3. Finding 4 header logo eager + dimensions (one shared component).
4. Get real numbers: PSI for /, /pricing, /capacity-planning (field + lab) before spending effort on findings 3 and 5.
