# Website Architecture & Secure Operations

**Status: architecture recommendation, not chosen deployed stack.** Angular is confirmed by founder request. Other infrastructure remains to be selected.

## Frontend
- Angular latest supported stable release at implementation time; TypeScript strict mode, standalone components, lazy-loaded route groups, Angular Router.
- Prerender/SSR/hybrid for public discoverable pages if hosting allows; client-side rendering for private admin shell.
- Strong route-level code splitting; typed API models, interceptors for handling errors (not secret injection), feature folders `core/`, `shared/`, `features/public/`, `features/docs/`, `features/downloads/`, `features/admin/`.
- Avoid sensitive secrets in Angular environment files, compiled bundles or browser local storage.

## Backend / trust boundaries
- Separate authenticated API for product catalogue, docs, releases and administrator mutations. Backend platform to be chosen after reviewing team operations and pricing.
- API validates sessions and role+resource permissions for **every** admin request; Angular `canActivate` is UX, not authorization.
- Managed identity service recommended with phishing-resistant MFA for privileged users, revocable short-lived sessions, account recovery process.
- Public queries only return explicit `published` records; draft records inaccessible even with guessed IDs.

## Data model (conceptual)
- `products`: id, slug, type(hardware/software), status, approved content, timestamps.
- `applications`: id, slug, platform, app_id/package_name, release channel config.
- `documents`: id, product_id, version, slug, visibility, draft/published status, body, approver, revision.
- `releases`: id, app_id, version_name, version_code, channel, min_sdk, abi, object_key, sha256, signer_fingerprint, size, state, notes, published_at.
- `release_approvals`: release_id, actor_id, action, timestamp.
- `admin_roles`: identity_id, role, managed_by, timestamps.
- `audit_events`: event_id, actor_id, action, target_type/id, request_id, time, redacted details.

## Secure APK release pipeline
1. Build Android artifact in controlled CI from reviewed source; use protected signing credentials.
2. Compute SHA-256, artifact size, Android metadata; verify signing certificate with platform tooling.
3. Upload server-side into private quarantine/staging storage; inspect file type, enforce size caps and malware scanning.
4. Require authorized release-manager approval and optionally a second approver, then atomically publish immutable release metadata and a read-only artifact.
5. Serve via HTTPS using controlled download API or short-lived storage URL; enforce revocation, never expose direct staging paths.
6. Log publish/revoke events; preserve artifact provenance; rehearse rollback/revocation.

## Security design requirements
- Enforce MFA for all admins, least-privilege RBAC and server-side object checks; require reauthentication for critical role/release actions.
- Use HttpOnly Secure SameSite cookies for server sessions; CSRF protections on state-changing requests, appropriate CORS, strict input validation and output encoding.
- Set HTTPS/HSTS, CSP (with nonce/Trusted Types where practical), frame restrictions, content-type protection and safe cache rules.
- Use Angular AOT template compilation, template escaping and no unsafe bypass of sanitizer; dependency/license/vulnerability checks in CI.
- Deny anonymous writes; public storage for approved published assets only; private service credentials inaccessible to browsers.
- Rate-limit login, content mutation, API calls and download abuse; record security audit events without leaking tokens or personal information.
- Upload allowlists and malware scanning are mandatory, not optional UI checks.
- Backups, retention, restore rehearsal, monitoring, error alerting and incident procedures required for launch.
- Third-party penetration testing or independent security review before go-live. No software can honestly be guaranteed "100% secure".

## Delivery / release conditions (embedded; no standalone deployment document)
- Environments: local, staging, production with different secrets and controlled promotions.
- Branch protection, review, CI tests, signed/traceable release artifacts and dependency scanning.
- Choose host, DNS, domain, storage and backend separately; no provider or price presumed.
- Required checks: unit/integration/e2e, authorization/IDOR, CSRF, XSS, uploads, release tampering, accessibility and mobile browsers.
- Configure origin restrictions, security headers, TLS certificates, custom domain and backups before launch.
- Do not declare website/API/admin production-ready until the stack is implemented and security acceptance is evidenced.

## References
- Angular security: https://angular.dev/best-practices/security
- Angular rendering: https://angular.dev/guide/ssr
- Angular routing: https://angular.dev/guide/routing
