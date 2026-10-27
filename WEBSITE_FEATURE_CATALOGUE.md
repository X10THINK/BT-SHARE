# Website Feature Catalogue

**Status:** Requested website product scope; implementation pending.

## A. Public Product Website
- `SITE-01` Responsive branded homepage with BT SHARE overview and accurate status badges.
- `SITE-02` Hardware product list and detailed hardware pages (images, supported inputs/outputs, limits, compatibility, FAQ).
- `SITE-03` Software product/application list (Flutter Android and future applications only if actually defined).
- `SITE-04` App details with features, screenshots, requirements, latest verified release link and documentation.
- `SITE-05` How-it-works overview: external AUX to BM83 to A2DP sinks, mobile BLE control separate.
- `SITE-06` Product updates/news area only if maintained by admins.
- `SITE-07` Approved about/company and contact/support details.

## B. Documentation Portal
- `DOC-01` Public documentation index, topics and search.
- `DOC-02` Product/version/category filters and stable slugs.
- `DOC-03` Rendered Markdown documentation with heading table of contents.
- `DOC-04` Public downloadable attachments/PDFs if approved.
- `DOC-05` Change history, updated date, related articles and version tags.
- `DOC-06` Draft/internal content access control, review and publishing workflow.

## C. APK Release Centre
- `APK-01` List supported applications and Android release channels.
- `APK-02` Latest stable release prominently labeled; no fabricated release.
- `APK-03` Version history, version codes, publish dates and notes.
- `APK-04` Requirements, supported CPU architectures, file size and Android version.
- `APK-05` APK SHA-256, signing certificate fingerprint and verified publication status.
- `APK-06` Controlled HTTPS download of approved immutable binary.
- `APK-07` Revocation/unpublish action and clear warnings for superseded/insecure builds.
- `APK-08` Optional server-derived download metrics (privacy reviewed; not required for launch).

## D. Secure Admin Dashboard
- `ADMIN-01` MFA-backed sign-in, logout, session state, account role view.
- `ADMIN-02` Role-based dashboard: Admin, Editor, Release Manager, Read-only Auditor.
- `ADMIN-03` Hardware product CRUD, draft preview and publish/unpublish.
- `ADMIN-04` Software application CRUD and links to versioned releases.
- `ADMIN-05` Documentation edit/version/review/publish/archive.
- `ADMIN-06` Release upload to quarantine; server validates APK content, signer and integrity.
- `ADMIN-07` Release review/approval/publish/revoke with immutable metadata.
- `ADMIN-08` Media/file management with safe uploads and access restrictions.
- `ADMIN-09` Site content management for approved static pages.
- `ADMIN-10` Admin identity/role assignment by authorized owners only.
- `ADMIN-11` Security events and tamper-resistant audit history.
- `ADMIN-12` Operational notices, error states and alerts.

## Priority
**P0:** static public site, product/app catalogue, docs reader, verified release listing and downloads, protected admin authentication and server permissions.
**P1:** draft/review/publish UI for products/docs/releases and full audit/reporting.
**P2:** advanced search, localization, additional analytics (only with explicit product/privacy approval).

**Reality check:** Features above are required/proposed, **not built**. App features from `docs/mobile-app/` are not browser capabilities merely because the website lists them.
