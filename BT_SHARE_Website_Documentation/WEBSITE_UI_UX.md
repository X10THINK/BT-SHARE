# Website UI/UX Specification — BT SHARE / ZAEROX

**Updated:** 2026-10-29
**Status:** Website design specification, not a completed UI implementation.

## Branding and visual direction

- **Product first:** BT SHARE is the primary header/hero identity, with **ZAEROX** identified as the technology brand and **X10 THINK** credited as founding company.
- ZAEROX official supplied tagline: **Innovation Beyond Limits**.
- **Approved owner-supplied visual assets** are in [`assets/branding`](../assets/branding/). Follow [Brand Identity](../BRAND_IDENTITY.md) and [Website Branding](WEBSITE_BRANDING.md).
- Product logo: supplied white icon/wordmark on blue gradient for prominent hero/artwork; white transparent logos require good contrast.
- Brand logo: ZAEROX black-background wordmark/strapline is legible in both dark/light contexts; transparent white wordmark only on a contrasting dark surface.
- Do not assume precise hex palette, typography, custom illustrations, licensed trademarks or other unseen design decisions are approved just because logo assets have been supplied.

## Public UX

- Homepage: unambiguous product overview, clear development-stage explanation, responsive layout, links to hardware/app/docs/downloads.
- Product details: distinguish **tested specifications** from **planned/under-research capabilities**, with conspicuous availability state.
- App detail: mark planned sound-tool features separately from actual downloadable releases.
- Documentation: stable search/navigation, current revisions and easy distinction between public/restricted content.
- Download pages: visible release version, Android support, signer/SHA-256 information, release notes and warnings; never imply a draft APK is published.
- Empty/error states: explain no releases, access failures, unknown hardware capability and unavailable services accurately.

## Admin UX

- Admin interface visually separate from public site; clear authorized roles and session timeout behavior.
- Publishing/revoking, destructive changes and release approvals need explicit confirmation and audit trace.
- Client route guards only guide UX; authenticated backend APIs MUST enforce authorization.
- Editorial previews must never leak unapproved/private data to public search indexes or caches.

## Accessibility / performance

- WCAG 2.2 AA target: contrast and focus visibility, keyboard/screen reader navigation, responsive tap targets, accessible dialogs, text alternatives for both product and parent-brand artwork.
- Mobile-first responsive layouts and meaningful loading, offline/error states.
- Optimize logo/image size for page performance without visually distorting original marks.
- Treat security, accessibility and performance targets as **acceptance requirements**, not verified implementation results.
