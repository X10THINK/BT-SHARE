# Website Requirements — BT SHARE

**Version:** draft 0.1 | **Date:** 2026-10-27 | **Status:** Proposed requirements, not implemented

## Scope
Build an Angular website with four sections: **(1) products & applications**, **(2) public documentation**, **(3) Android APK releases/downloads**, **(4) access-controlled admin dashboard**. Public visitors should not be forced to register. Admin login is separate from public browsing.

## Functional requirements
| ID | Requirement | Acceptance expectation |
|---|---|---|
| WEB-F01 | Homepage and company/product overview | Responsive, correct product claims and clear navigation |
| WEB-F02 | Hardware product catalogue | Product pages show verified capabilities, status, compatibility, specifications and images |
| WEB-F03 | Software application catalogue | Each application has overview, platform, status, features and supported version info |
| WEB-F04 | Product detail and cross-links | Each product/app links to relevant documentation and releases only when applicable |
| WEB-F05 | Documentation library | Public category navigation, search, versions, last updated, readable pages and optional PDFs |
| WEB-F06 | Documentation release policy | Draft/restricted docs never accessible through public APIs, URLs or search index |
| WEB-F07 | Android release listing | App name, version name/code, publish date, min Android version, release notes, file size |
| WEB-F08 | Secure APK download | Only published, server-approved artifacts; SHA-256 displayed; file delivered over HTTPS |
| WEB-F09 | APK authenticity | Verified signer provenance/fingerprint and CI-calculated checksum kept with each release |
| WEB-F10 | Prior releases and status | Stable/beta distinctions, rollback/revoke and explicit compatibility warnings |
| WEB-F11 | Admin authentication | Identity provider login, MFA, short-lived sessions and server-enforced authorization |
| WEB-F12 | Admin product/app editor | Create, edit, preview, archive; approval before public publish |
| WEB-F13 | Admin documentation editor | Version content, preview, stage, approve, publish and unpublish |
| WEB-F14 | Admin release manager | Upload to quarantine, validate, verify APK, stage, approve, publish/revoke |
| WEB-F15 | Admin dashboard | Counts and recent activity from authorized API, no fabricated analytics |
| WEB-F16 | Roles/permissions | Admin/editor/release manager/viewer; enforce least privilege on every backend endpoint |
| WEB-F17 | Audit trail | Record who performed each privileged action, when, affected entity, before/after identifiers |
| WEB-F18 | Error/empty states | Clear behavior for no publications, invalid versions, service outages and access failures |
| WEB-F19 | Contact/support information | Show approved support information only; secure form if contact workflow approved |
| WEB-F20 | Responsive accessibility | Keyboard usable, mobile-first, screen-reader labels, English initially; Tamil only when reviewed |

## Nonfunctional requirements and security acceptance
- `WEB-N01` **Data boundary:** Angular is a frontend. All admin operations require independent server-side authentication and authorization. Never trust a frontend route guard, hidden button or client role claim.
- `WEB-N02` **Authentication:** MFA for privileged users; no default credentials; rate limits and lockout/risk controls; secure, HttpOnly, SameSite session cookies, with CSRF protection and secure logout/session rotation.
- `WEB-N03` **Backend validation:** Validate all inputs/ids; parameterized queries; restrictive CORS; object-level authorization; secrets only in protected server configuration.
- `WEB-N04` **Web security:** HTTPS/HSTS, CSP with appropriate nonce strategy, Angular AOT, safe templating, dependency scans and security headers.
- `WEB-N05` **Upload safety:** Extension/MIME/magic checks, file-size limits, malware scanning/quarantine, SHA-256 verification, APK signing certificate validation, restricted write privileges.
- `WEB-N06` **Release integrity:** Two-stage or two-person approval for production releases where possible; published release metadata immutable; revocation available; retain audit and provenance.
- `WEB-N07` **Storage:** Prevent public listing/unapproved direct access to draft binaries and documents; give downloads time-limited URLs or controlled server responses.
- `WEB-N08` **Reliability:** backups, restore testing, incident/revocation procedure, monitoring without exposure of private secrets, availability and performance targets to be decided.
- `WEB-N09` **Privacy:** publish approved privacy/contact notices before analytics or collection; minimize IP/user logs; set retention and deletion procedures.
- `WEB-N10` **Verification:** security tests (including auth bypass/IDOR, upload abuse, XSS, CSRF), accessibility, mobile testing and prelaunch security review must pass before public launch.

## Exclusions / non-assumptions
No e-commerce/payment, web-browser Bluetooth controller, user accounts, cloud music streaming, Android-to-browser audio relay or download tracking is approved by this request. Those require separate decisions. No production deployment or APK artifact is present or verified by this document.
