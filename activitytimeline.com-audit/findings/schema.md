# Schema / structured data: activitytimeline.com, 19 Nov 2026

**Category score: 38 / 100.** Derivation: syntax and hygiene 18/20 (every block parses, https context, no microdata or RDFa, no review markup); entity model 5/25 (no usable SoftwareApplication, two competing Organizations); URL and @id accuracy 3/20 (six commercial templates point at 404 URLs); localization 2/15 (every localized page checked serves the English graph); posts and guides 7/15 (Article + BreadcrumbList exist, dates invalid, HowTo and a customer name in the guides); fact consistency 3/5 (no rating or brand error; one `price: "0"`).

Scope: 23 saved pages (SCRATCH/live) plus 9 fetched (3 blog posts, /es/capacity-planning, /es/features, /fr/pricing, /pt/how-it-works, /pt/how-to-do-capacity-planning-in-jira, /es/blog/tempo-timesheets-alternatives) and 6 status checks. JSON-LD only: `itemscope`, `itemprop` and `typeof` counts are 0 on every page. All findings are CONFIRMED in the HTML unless marked LIKELY.

All drafts below are tier 2. Schema is written by the PM through Webflow's schema markup channel (`data_pages_tool > bulk_update_pages_schema_markup`, read back with `query_pages_schema_markup`) after Ostap approves on the ticket. Page settings did not persist on 30 Oct 2026, so do not use that route.

## What is on the pages

| Page | Head block (page schema) | Body block (site-wide) |
|---|---|---|
| /, /es, /fr, /pt | @graph: Organization "Reliex" `#organization`, WebSite, WebPage, FAQPage (6 Q) : byte-identical 4,406 B on all four | Organization "ActivityTimeline", no @id |
| /capacity-planning, /time-tracking, /resource-management, /cost-tracking, /timeline-for-jira, /reports | @graph: Organization "Reliex", WebPage, BreadcrumbList, FAQPage (6 to 10 Q) | same |
| /features | @graph: Organization "Reliex" `#org`, CollectionPage + ItemList (47), BreadcrumbList, FAQPage (5 Q) | same |
| /how-it-works | WebPage > SoftwareApplication > Offer price "0" | same |
| /schedule-demo | WebPage > SoftwareApplication + Service | same |
| /pricing, /tempo-alternative, /blog, /case-studies | none | same |
| 3 guides | @graph: WebPage, BreadcrumbList, ImageObject, Article, FAQPage; HowTo on two; VideoObject x3 on one | same |
| blog posts (3) | none in head | Organization + Article + BreadcrumbList (3 body blocks) |

## What works
- 100% of blocks are valid JSON with `https://schema.org` context; no placeholders.
- No `aggregateRating`, `Review` or rating figure in any block, so the "no review snippet" rule holds and nothing can drift from f13. (The visible "122 reviews" on /pricing is a copy issue, already known; not a schema issue.)
- "ActivityTimeline" is spelled as one word in every schema block (f02). No "Activity Timeline" in JSON-LD.
- No price in schema other than the one `"price": "0"` (finding 2). No Advanced Edition price in schema, so the open f07 question is not touched.
- English FAQPage text matches the visible FAQ word for word on all 11 English pages that carry it.
- /schedule-demo `availableLanguage` (English, Spanish, French, Portuguese) matches f12.
- Blog posts have Article with a named Person author (with URL), image, and a 3-level BreadcrumbList with absolute URLs.

## Findings

### 1. High: six commercial pages declare URLs that return 404 (CONFIRMED)
- Evidence: /capacity-planning head JSON-LD: `"url": "https://activitytimeline.com/solutions/capacity-planning"`, same in `@id` (`...#webpage`, `#breadcrumb`, `#faq`) and in BreadcrumbList position 2 `item`. Same pattern on /time-tracking (`/solutions/time-tracking`), /resource-management (`/solutions/resource-management`), /cost-tracking (`/solutions/cost-tracking`), /timeline-for-jira (`/solutions/jira-timelines`), /reports (`/product/reports`). All six targets: HTTP 404 (curl, 19 Nov). The canonicals are the short URLs.
- Effect: the page's own structured data names a different, dead URL than its canonical; the breadcrumb trail's last item is a 404. LIKELY a contributing mixed signal for pages Google has not indexed (3 of 12 on 5 Nov); causation not measured.
- Fix: replace url, every @id and the breadcrumb item with the canonical URL (draft B). /reports breadcrumb position 2 "Product" > /features is fine.
- KPI: commercial pages indexed (12 of 12). Tier 2 draft, then tier 3 (reversible) when written.
- Failed if: `query_pages_schema_markup` or a fresh curl still shows `/solutions/` or `/product/`; or URL Inspection (once Google access is back) still reports breadcrumb items it cannot crawl.

### 2. High: no SoftwareApplication entity where the override requires it; the only one says price 0 (CONFIRMED)
- Evidence: home, /pricing, /features and the six product pages have no `SoftwareApplication`. The three guides reference `{"@id": "https://activitytimeline.com/#software"}` in `mentions`; that @id is defined on no page checked. The only SoftwareApplication nodes are nested, without @id, on /how-it-works (`"offers": {"price": "0", "priceCurrency": "USD", "description": "30-day free trial"}`) and /schedule-demo (no offers).
- Why it matters: f05 says Cloud starts at $10 a month for up to 10 users; "free for small teams" is open (f06). A machine reading `price: 0` reads "free". The product has no machine-readable identity, category, platform or price on the pages buyers and AI assistants land on.
- Fix: define one SoftwareApplication `#software` in the site-wide graph (draft A), reference it by @id from every page, put the confirmed starting price on /pricing only (draft C), and drop the `price: "0"` offer from /how-it-works (draft D).
- KPI: AI mention rate; cost and budget prompt mention rate; AI citations on product and pricing pages. Tier 2.
- Failed if: after 4 weeks the brand AI answers still describe the price as "free" or give no price (re-check with the STB-3 prompts); or the read-back shows more than one SoftwareApplication definition.

### 3. High: two competing Organization entities on every page (CONFIRMED)
- Evidence, e.g. home: head `{"@id": ".../#organization", "@type": "Organization", "name": "Reliex", "url": "https://activitytimeline.com"}`; body `{"@type": "Organization", "name": "ActivityTimeline", "url": "https://activitytimeline.com/"}` with no @id. Variants: /features uses `#org`; product pages drop logo and sameAs; /how-it-works and /schedule-demo give Reliex `"url": "https://reliex.com/"`; blog Article publisher is `"name": "ActivityTimeline"`. So the same domain is claimed by "Reliex" and by "ActivityTimeline", with two logos.
- Fix: one Organization node, one @id, defined once (the site-wide body block), referenced by @id elsewhere. **Decision for Ostap:** which name the Organization carries. Draft A proposes "ActivityTimeline" as the organization on this domain with Reliex as `parentOrganization` (f02: "Built by Reliex"); the alternative is Organization "Reliex" with url reliex.com and ActivityTimeline only as SoftwareApplication + Brand. Either is valid; mixing them is not.
- KPI: brand clicks/28d (site name and brand entity consistency); AI mention rate. Tier 2.
- Failed if: any page still returns two Organization nodes with different names for the same URL.

### 4. High: localized pages serve the English graph (CONFIRMED on 8 of 8 localized pages that carry page schema)
- Evidence: /es, /fr, /pt head block is byte-identical to the English home: `"inLanguage": "en"`, `"url": "https://activitytimeline.com/"`, `"name": "ActivityTimeline: Capacity Planning & Time Tracking for Jira"`, and 6 English FAQ questions, none of which is visible on the localized page (0 of 6 matched on each). /es/capacity-planning: `inLanguage en`, url `/solutions/capacity-planning`, 0 of 6 FAQ questions visible. /pt/how-it-works: `"url": "/how-it-works"`, `inLanguage en`. /pt/how-to-do-capacity-planning-in-jira: full English Article graph with English URL and @ids. /es/blog/tempo-timesheets-alternatives: `mainEntityOfPage.@id` and breadcrumb item 3 point to the English URL; no `inLanguage`. /es/features: English name and URLs, no `inLanguage`.
- Effect: each locale page tells crawlers it is the English page; FAQ markup that is not on the page breaks Google's "markup must match visible content" rule.
- Fix: per locale, set `inLanguage` (`es`, `fr-FR`, `pt-BR`, matching `<html lang>`), the locale URL in url/@id/breadcrumb, the localized name and description, and either the translated FAQ text exactly as shown or no FAQPage node. Draft E. Webflow stores schema markup per locale; the PM confirms on read-back that the secondary-locale value is independent of the primary one. Blog template: build the URL from the locale path (finding 5).
- KPI: commercial pages indexed; brand clicks/28d (es, fr, pt brand queries). Tier 2. This is schema on existing pages, not new localized content.
- Failed if: a curl of /es, /fr, /pt still shows `"inLanguage": "en"`; or a locale edit overwrote the English block (re-read the English page after every locale write: see the 6 Nov lesson on translations resetting).

### 5. Medium: blog Article dates are not ISO 8601, and the template ignores locale (CONFIRMED on 3 of 3 posts)
- Evidence: /blog/atlassian-enterprise-certified: `"datePublished": "Oct 30, 2026T10:00:15+02:00"`; same pattern on /blog/tempo-timesheets-alternatives (`"Jul 07, 2026T..."`) and /blog/best-tools-for-capacity-management (`"May 27, 2026T..."`). The time is the same constant on every post, so it is hard-coded after a display-format date. No `dateModified`. Publisher is an inline Organization, not the @id. Blocks sit in `<body>` (valid, but late).
- Fix: in the Blog Posts template embed, bind the date field with the `YYYY-MM-DD` format and delete the hard-coded `T10:00:15+02:00`; add `dateModified` from the CMS "updated" field; point `publisher` to `{"@id": "https://activitytimeline.com/#organization"}`; add `inLanguage` and build `mainEntityOfPage` and the breadcrumb from the current locale URL. Draft F. LIKELY: this block is template custom code or an embed, not the page schema field, so the PM checks which channel holds it before writing.
- KPI: buyer-segment clicks/28d (dated posts); AI mention rate (freshness of cited posts). Tier 2.
- Failed if: a published post still shows a month name in `datePublished`.

### 6. Medium: guides carry HowTo, a customer name, and @ids that resolve to nothing (CONFIRMED)
- Evidence: /how-to-do-capacity-planning-in-jira: 1 `HowTo` (`#howto-planned-vs-actual`); /how-to-do-time-tracking-in-jira: 2 `HowTo` (`#howto-setup`, `#howto-report`), whose step text says "(for Server)" and "for the Server version" (f10: do not mention Server). The capacity guide's Article `mentions` contains `{"@type": "Organization", "name": "<a customer>"}` (f26: no customer names). All three guides reference `#organization`, `#website` and `#software` by @id but define none of them in the page; the only Organization on the page is the body block with no @id, so author and publisher resolve to an empty node. `dateModified` equals `datePublished` on all three.
- Fix: delete the HowTo nodes (retired; do not replace), delete the customer `mentions` entry, and let the site-wide block (draft A) define the three @ids. Set `dateModified` only when the guide really changes. The guide v2/v3 drafts built on 4 Nov should be checked against the same list before publish.
- KPI: buyer-segment clicks/28d; AI citations on product pages. Tier 2.
- Failed if: read-back still contains `"HowTo"` or an Organization in `mentions` other than Atlassian.

### 7. Medium: /pricing, /tempo-alternative, /blog and /case-studies have no page-level schema (CONFIRMED)
- Evidence: one JSON-LD block each, the 248-byte site-wide Organization. /fr/pricing: the same.
- Fix: WebPage + BreadcrumbList on each, referencing `#software`; the starting-price Offer on /pricing (draft C); `CollectionPage` on /blog and /case-studies (no customer names in schema). /tempo-alternative: WebPage with `about: #software` only; no competitor prices in schema. Do not add FAQPage to /pricing or /tempo-alternative for a SERP feature: the FAQ rich result was retired on 7 May 2026.
- KPI: AI citations on pricing and comparison pages; cost and budget prompt mention rate. Tier 2.
- Failed if: the /pricing schema price and the visible "flat $10 a month" line ever differ (add to the monthly f13/f05 re-check).

### 8. Low: hygiene (CONFIRMED)
- Relative URLs: /how-it-works `"url": "/how-it-works"`; /schedule-demo `"@id": "/schedule-demo"`, `"url": "/schedule-demo"`. Use absolute URLs.
- /schedule-demo sameAs `"https://twitter.com/@ReliexSolutions"` (malformed; home uses `https://twitter.com/ReliexSolutions`).
- WebSite node differs by page: full on home, partial inline copies on product pages, missing `@id` on /resource-management and /timeline-for-jira.
- Home `WebPage.mentions` is a bare Brand; replace with `about: {"@id": "...#software"}`.
- Two different logos (Reliex white SVG, ActivityTimeline dark SVG) for what is presented as one organization.
- /features FAQPage has no @id; ItemList items that point to `#g-...` fragments are fine.

### 9. Info: FAQPage on 11 English pages
Home, /features, six product pages, three guides. Valid and matches visible text. No Google SERP feature since 7 May 2026; any AI benefit is unconfirmed. Keep as is on English pages; do not add more for SERP reasons; on localized pages it is currently wrong (finding 4). No action otherwise.

### Not schema, passed to the lead
- /pt/how-to-do-capacity-planning-in-jira has two `rel="canonical"` tags that disagree (the /pt URL and the English URL). The English capacity and time tracking guides have the canonical twice (same value).
- /es/features shows the five FAQ questions in English (schema FAQ text matched visible text 5 of 5 on the Spanish page). LIKELY untranslated FAQ block.
- /pricing footer links say "Admin Guide - Server/DC" (f10, visible copy).

## Drafts (tier 2; JSON-LD)

### A. Site-wide block (replaces the 248-byte body Organization; one definition of each entity)
Needs Ostap's decision on the Organization name (finding 3). No rating, no install count, no customer count. `sameAs` reuses only profiles already in the live schema; add the Marketplace listing URL once someone can open it (host blocked today).
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://activitytimeline.com/#organization",
      "name": "ActivityTimeline",
      "url": "https://activitytimeline.com/",
      "logo": {
        "@type": "ImageObject",
        "url": "https://cdn.prod.website-files.com/60b67fe41fdcf019c5266a3a/6141dba8ea34267e6ed2d54a_at_new_logo_dark.svg"
      },
      "parentOrganization": { "@type": "Organization", "name": "Reliex", "url": "https://reliex.com/" },
      "sameAs": [
        "https://www.facebook.com/activitytimeline",
        "https://www.linkedin.com/company/reliex.solutions",
        "https://twitter.com/ReliexSolutions",
        "https://www.youtube.com/@reliex"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://activitytimeline.com/#website",
      "name": "ActivityTimeline",
      "url": "https://activitytimeline.com/",
      "publisher": { "@id": "https://activitytimeline.com/#organization" },
      "inLanguage": ["en", "es", "fr-FR", "pt-BR"]
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://activitytimeline.com/#software",
      "name": "ActivityTimeline",
      "description": "ActivityTimeline is a resource planning, capacity management and time tracking app for Jira Cloud and Data Center.",
      "url": "https://activitytimeline.com/",
      "applicationCategory": "BusinessApplication",
      "applicationSubCategory": "Resource planning and time tracking for Jira",
      "operatingSystem": "Jira Cloud, Jira Data Center",
      "publisher": { "@id": "https://activitytimeline.com/#organization" },
      "featureList": ["Planner", "Workspace", "Timesheets", "Reports", "Finances"]
    }
  ]
}
```
Description is f01; modules are f03. No `offers` here: the price lives on /pricing only (draft C), so there is one place to keep in step with the page.

### B. Product page (example: /capacity-planning; same pattern for the other five with their canonical URL)
Keep the existing FAQPage node, changing only its @id to `https://activitytimeline.com/capacity-planning#faq`. Remove the inline Organization "Reliex" node.
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://activitytimeline.com/capacity-planning#webpage",
      "url": "https://activitytimeline.com/capacity-planning",
      "name": "Capacity Planning for Jira Teams | ActivityTimeline",
      "description": "Plan capacity in Jira with ActivityTimeline: real hours per person after schedules and time off, work from every project, and overload spotted weeks ahead.",
      "inLanguage": "en",
      "dateModified": "2026-11-13",
      "isPartOf": { "@id": "https://activitytimeline.com/#website" },
      "about": { "@id": "https://activitytimeline.com/#software" },
      "publisher": { "@id": "https://activitytimeline.com/#organization" },
      "breadcrumb": { "@id": "https://activitytimeline.com/capacity-planning#breadcrumb" }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://activitytimeline.com/capacity-planning#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://activitytimeline.com/" },
        { "@type": "ListItem", "position": 2, "name": "Capacity planning", "item": "https://activitytimeline.com/capacity-planning" }
      ]
    }
  ]
}
```
URL map: `/solutions/time-tracking` > `/time-tracking`; `/solutions/resource-management` > `/resource-management`; `/solutions/cost-tracking` > `/cost-tracking`; `/solutions/jira-timelines` > `/timeline-for-jira`; `/product/reports` > `/reports`.

### C. /pricing
Only the figure that is both confirmed (f05) and visible on the page ("Up to 10 users is a flat $10 a month on Standard"). No Advanced price (f07 covers one figure only; showing Advanced prices on /pricing is an open question for Ostap). No price 0 and no "free" offer (f06 open). The PM reads the live line again on the day of writing.
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://activitytimeline.com/pricing#webpage",
      "url": "https://activitytimeline.com/pricing",
      "name": "<the live title tag of /pricing>",
      "inLanguage": "en",
      "isPartOf": { "@id": "https://activitytimeline.com/#website" },
      "about": { "@id": "https://activitytimeline.com/#software" },
      "breadcrumb": { "@id": "https://activitytimeline.com/pricing#breadcrumb" },
      "mainEntity": { "@id": "https://activitytimeline.com/pricing#offer-standard-cloud" }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://activitytimeline.com/pricing#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://activitytimeline.com/" },
        { "@type": "ListItem", "position": 2, "name": "Pricing", "item": "https://activitytimeline.com/pricing" }
      ]
    },
    {
      "@type": "Offer",
      "@id": "https://activitytimeline.com/pricing#offer-standard-cloud",
      "name": "ActivityTimeline Standard Edition, Jira Cloud, up to 10 users",
      "itemOffered": { "@id": "https://activitytimeline.com/#software" },
      "url": "https://activitytimeline.com/pricing",
      "priceSpecification": {
        "@type": "UnitPriceSpecification",
        "price": "10.00",
        "priceCurrency": "USD",
        "billingDuration": "P1M",
        "description": "Flat monthly price for up to 10 Jira users; graduated per-user pricing above 10. 30-day trial through the Atlassian Marketplace."
      }
    }
  ]
}
```
The `name` placeholder is deliberate: copy the live title at write time; do not ship the placeholder.

### D. /how-it-works and /schedule-demo
Replace the nested SoftwareApplication (and its `price: "0"` offer on /how-it-works) with a reference, and make URLs absolute:
```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "https://activitytimeline.com/how-it-works#webpage",
  "url": "https://activitytimeline.com/how-it-works",
  "name": "How ActivityTimeline Works | Jira Planning & Time Tracking",
  "inLanguage": "en",
  "isPartOf": { "@id": "https://activitytimeline.com/#website" },
  "about": { "@id": "https://activitytimeline.com/#software" }
}
```
/schedule-demo: same shape with its URL; keep the `Service` node (demo, four languages, f12) with `"provider": {"@id": "https://activitytimeline.com/#organization"}`.

### E. Locale variant (example: /es home WebPage node; same rule for every localized page)
```json
{
  "@type": "WebPage",
  "@id": "https://activitytimeline.com/es#webpage",
  "url": "https://activitytimeline.com/es",
  "name": "<the live Spanish title tag>",
  "description": "<the live Spanish meta description>",
  "inLanguage": "es",
  "isPartOf": { "@id": "https://activitytimeline.com/#website" },
  "about": { "@id": "https://activitytimeline.com/#software" }
}
```
Use `fr-FR` on /fr and `pt-BR` on /pt. FAQPage on a localized page only with the question and answer text exactly as displayed in that language; otherwise leave it out. Entity @ids (`#organization`, `#website`, `#software`) stay the same in every locale.

### F. Blog Posts template Article (Webflow field bindings shown as {{...}})
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "https://activitytimeline.com/{{locale-prefix}}blog/{{slug}}#article",
  "mainEntityOfPage": "https://activitytimeline.com/{{locale-prefix}}blog/{{slug}}",
  "headline": "{{name}}",
  "description": "{{meta description}}",
  "image": ["{{main image}}"],
  "inLanguage": "{{locale tag}}",
  "datePublished": "{{published date, format YYYY-MM-DD}}",
  "dateModified": "{{updated date, format YYYY-MM-DD}}",
  "author": { "@type": "Person", "name": "{{author name}}", "url": "https://activitytimeline.com/blog-author/{{author slug}}" },
  "publisher": { "@id": "https://activitytimeline.com/#organization" }
}
```
LIKELY: Webflow embeds have no locale variable, so the locale prefix and tag may need one embed per locale or a small conditional; the PM confirms in the Designer. The BreadcrumbList on posts needs the same locale-aware URLs for items 1 to 3.

## Could not check
- Google Rich Results Test and Search Console enhancement reports (no Google access; Sitechecker unreachable).
- The Marketplace listing (host blocked): rating not re-verified today, and the listing URL for `sameAs` not confirmed.
- Whether Webflow's schema markup field holds independent values per locale (needs `query_pages_schema_markup` per locale; read-only audit, Webflow not queried).
- The other ~700 URLs: only 3 blog posts and 6 localized pages were sampled; findings 4 and 5 are template-level, so they are LIKELY site-wide.
- JS-injected schema: not rendered; all blocks found are in the raw HTML.
