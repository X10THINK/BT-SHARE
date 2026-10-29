# BT SHARE — Website Content Register

**Updated:** 2026-10-29
**Status:** Draft content specification. Approved company/brand names and logo files supplied; actual website copy, legal claims, backend, deployment and product features still require review.

## Identity and editorial hierarchy

- **Founding company:** X10 THINK.
- **Parent technology brand:** ZAEROX — **Innovation Beyond Limits**.
- **Product:** BT SHARE — audio-sharing hardware initiative and Android sound workspace.
- Required brand reference: [Website Branding](WEBSITE_BRANDING.md) / [Brand Identity](../BRAND_IDENTITY.md).
- Use supplied assets from [`assets/branding`](../assets/branding/) and product-first visual emphasis.

## Homepage

- Branded BT SHARE logo and name, with explicit ZAEROX / X10 THINK attribution.
- Concise mission and product overview without suggesting that planned features are shipped.
- Clear development-stage indicators and links to documentation/product/app detail.
- Explain the distinction between **educational two-listener prototype** and **future commercial research**.

## Hardware product detail

- Product name, prototype/commercial-track label, current version/status and source type (AUX prototype vs proposed AUX/Bluetooth commercial R&D).
- Only verified hardware capabilities presented as specifications; proposed or experimental capabilities in a visibly separate section.
- Describe supported Bluetooth profiles, receiver counts, latency and mixed-brand compatibility only from verifiable testing and manufacturer evidence.
- Do not present 3/4+ receivers, Bluetooth input or synchronization accuracy as available before verification.

## Mobile application detail

- Flutter Android app is **planned** as BLE hardware control plus standalone sound utilities.
- Feature catalogue and requirements link to the mobile docs, and explicitly distinguish planned, tested and released functionality.
- App availability, release notes, images, Android support and APK URL appear only when the real deliverable exists.

## Documentation

- Each published document shows workstream, owner, revision, approval/publication status, last update and links to related source/evidence.
- Do not accidentally expose internal-only drafts, engineering secrets, receipts, signing keys or unapproved schematics.

## APK downloads

- Release fields: application, version name/code, release channel, minimum Android version, architectures, size, signature provenance, SHA-256 and publish timestamp.
- Draft/staging releases are inaccessible without appropriate authorization. No invented download links or placeholder production badges.
- Publication/revocation is controlled by audited backend workflows, not Angular UI-only protection.

## Admin-managed content

- Approved products, applications, brand media, documentation, release metadata and publishing activity.
- Separate admin authentication, roles, approval flow and immutable audit trail.
- Contact/legal/privacy claims require explicit editorial and legal approval.

See [Website Requirements](WEBSITE_REQUIREMENTS.md), [Website Architecture](WEBSITE_ARCHITECTURE.md), and [Website Branding](WEBSITE_BRANDING.md).
