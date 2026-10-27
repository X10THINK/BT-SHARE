# Website UI/UX Specification — Draft

- Angular standalone, responsive mobile-first design; maintain desktop/touch parity.
- Brand assets, colors and typography require explicit approval; do not reuse prototype branding as final without review.
- Public header: Product, Applications, Documentation, Downloads, About. Footer: privacy, support and confirmed official links.
- Public home: one hero, honest product introduction, two paths (Explore Products / Download App), feature overview, docs access.
- Product pages: specifications separated from planned capabilities; visually obvious availability status.
- Docs portal: sidebar tree on desktop; collapsible contents on mobile; persistent version indicator, clear anchors, keyboard search.
- Downloads: version + date + compatibility + size + SHA-256 + signing information adjacent to each download; warn on prerelease/revoked artifacts. Never auto-trigger unknown downloads.
- Admin shell visually separate from public website; session expiry and role-denied states explicit; destructive operations require confirmation.
- Admin editors show Draft → Review → Published and timestamped activity; use accessible forms, inline validation, previews.
- WCAG 2.2 AA target: sufficient contrast, keyboard focus, touch size, accessible dialog handling, meaningful status not color-only.
- English copy initially; Tamil when translators review content. No placeholder copy goes live.
- Empty states: no APK releases, docs not published, products not ready. Never show fake counters or hard-coded security promises.
- Test responsive widths 320px, 375px, 768px, 1024px, 1440px, with real devices and accessibility checks.
