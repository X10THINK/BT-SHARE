# BT SHARE — Repository and Development Workflow

**Drafted:** 2026-10-29
**Scope:** Project documentation, hardware, Flutter mobile app, and Angular website
**Approval status:** Proposed coordination workflow; engineering constraints and procurement require separate project-owner approval.

## 1. Separate project workstreams

**HARDWARE-PROTOTYPE:** The historical college two-receiver AUX → BM83 → A2DP experiment, ESP32/UART/BLE control and its G0–G8 verification gates.

**PRODUCT-RESEARCH:** Broader affordable multi-listener audio sharing. Treat additional receiver counts, Bluetooth audio input, alternate transmitter architectures, pricing and certification as unverified until independently demonstrated or formally approved. Never silently copy prototype capabilities to the commercial specification.

**MOBILE-APP:** Flutter/Dart Android application: BLE hub controls and standalone sound tools. The app team owns app source, UI, native Android integrations and its own tests; the hardware team owns the verifiable device-side BLE contract and mock data.

**WEBSITE:** Angular public product pages, documentation, secure APK releases and separate admin UI. Backend/service/platform choices require explicit decision and enforce authorization on the server.

**BRAND:** The owner has supplied identity **X10 THINK → ZAEROX → BT SHARE**, tagline **Innovation Beyond Limits**, and six product/brand logo variants (2026-10-29). Use [BRAND_IDENTITY.md](BRAND_IDENTITY.md) as documentation. Artwork is not evidence of implementation or legal certification.

## 2. Task lifecycle

Use these states for issues, decisions, requirements, milestones and releases:

`PROPOSED → APPROVED → IN_PROGRESS → IN_REVIEW → VERIFIED`
`BLOCKED` and `ON_HOLD` are explicit alternatives. `VERIFIED` requires linked acceptance evidence. `DOCUMENTED` means only that text exists; it is not a completed implementation status.

Every work item should contain:

- Identifier and workstream (`HW-`, `PROD-`, `APP-`, `WEB-`, `DOC-`, `BRAND-`).
- Goal, owner, scope/in-scope and out-of-scope.
- Authoritative document/version, dependency or approved decision.
- Acceptance criteria that another person can check.
- Relevant branch/commit/PR, source artifacts, test logs and reviewer.
- Explicit unknowns, blocked items and next action.

## 3. Authority and change control

1. Consult the latest approved workstream-specific requirement and actual engineering evidence, not the most attractively written summary.
2. Treat the October 6 hardware BRD and execution plan as historical base documents. Later approved electrical, budget, component, procurement or commercial-product decisions must be imported as dated changes and reconciled before use.
3. Use `DECISIONS.md` for approved cross-team decisions. Proposed architecture decisions are labelled `PROPOSED` until ratified.
4. Distinguish **ordered**, **paid**, **received**, **verified stock**, **new missing**, **estimate** and **quote**. No workstream may treat document existence as authorization to purchase or fabricate.
5. Include a short change-impact review if requirements affect firmware ↔ BLE ↔ Flutter, website ↔ backend/API, product claims, safety or budget.

## 4. Git workflow

- Work on focused branches (`docs/...`, `app/...`, `web/...`, `hw/...`); keep `main` reviewable.
- Before opening a PR: check tracked-file modes, relative links, accidental nested repositories, large/binary files, secrets and obsolete paths.
- Include changed requirement IDs, effect on other teams, test/evidence links and any unresolved risks in the PR description.
- Require an owner/reviewer for scope-changing decisions, new public claims and hardware acceptance status.
- Do not check in secrets, private signing keys, production credentials or unlicensed proprietary firmware/specification bundles.

## 5. Mobile architecture decision and handover

**Found in the 14 tracked Flutter specifications:** [TRD](BT_SHARE_Flutter_Documentation/03_TRD_Technical_Requirements.md), [SDD](BT_SHARE_Flutter_Documentation/04_SDD_Software_Design.md) and [ADR-005](BT_SHARE_Flutter_Documentation/11_ADR_Architecture_Decision_Records.md) **propose** feature-first Clean Architecture, MVVM-style presentation and Riverpod. The additional **DDD principles** are recommended but not explicitly decided in those source documents. Ask the Flutter lead to accept/revise the existing ADR, rather than adding a duplicate accepted decision.

Suggested responsibilities *if approved*:

- `features/<feature>/presentation/`: Flutter screens, MVVM view models, UI state and Riverpod providers.
- `features/<feature>/domain/`: entities/value objects, business rules, repository contracts and use cases as justified by complexity.
- `features/<feature>/data/`: API/BLE/local persistence adapters, DTOs, mappings and repository implementations.
- `core/` and `shared/`: narrowly scoped cross-feature infrastructure and reusable UI; avoid a general dumping ground.
- Dependencies should point inward to domain contracts rather than UI-to-BM83 command internals.

Before app/hardware integration, agree on BLE contract version, GATT services/characteristics, commands, events, states, error codes, max-links rules, timeouts, reconnection ownership and mock fixtures. Do not assume user-facing standalone phone-audio functions can process external AUX audio.

## 6. Website / APK release workflow

`Source reviewed → CI build → signing and provenance checks → quarantine upload → authorization/security review → authorized publish → checksums + release notes → monitoring / revoke or rollback`.

- Android files must be signed and validated; record SHA-256, signing identity, app ID/version, min SDK and release channel.
- Public visitors can view only published products, documentation and releases. Draft/admin records stay private server-side.
- Administrative approvals and audit trails cannot be implemented solely in Angular route guards.
- No APK or website should be labelled released before the relevant artifact, tests and deployment exist.

## 7. Hardware gate evidence

| Gate | Minimum meaningful proof |
| --- | --- |
| G0 | Controlled native schematic/PCB, BOM, design review and exact manufacturer references |
| G1 | Assembly and safe electrical-check record |
| G2 | Reproducible BM83 firmware/config and UART response log |
| G3 | One known-good receiver playing the external AUX audio |
| G4 | Two independently identifiable A2DP sinks playing the same source simultaneously |
| G5 | Compiling ESP32 firmware with tested host command/state paths |
| G6 | Versioned tested BLE contract with Flutter-team acceptance |
| G7 | End-to-end Flutter ↔ ESP32 ↔ BM83 integration test |
| G8 | Compatibility/reconnect/range/latency-observation/long-run evidence |

A simulated test, design completion or statement of intent cannot substitute for physical playback and measurement evidence.

## 8. Documentation maintenance cadence

- Update `PROJECT_STATUS.md` only when an evidence link or repository state changes; include an exact review date and commit.
- Keep `README.md` concise, branded, accurate and navigable; place fine-grained inventories and gates in linked docs.
- Repair renamed/moved document links in the same PR as the move.
- Preserve source document revisions and archive outdated instructions as historical context.
- Keep each product requirement tagged `proposed / approved / implemented / tested / released` so public-site language never overclaims functionality.

## 9. Immediate repository cleanup

1. Preserve all **14 Flutter specifications already tracked as normal files** in this supplied clone (`bc5f287`). Do not undo the earlier Gitlink fix.
2. Repair relative references to `First_Documents/` and `FeaturE_Scope_Documentations/mobile-app/`.
3. Reconcile `README.md`, `REQUIREMENTS.md`, `DECISIONS.md` and `PROJECT_STATUS.md` with the website docs, without inventing completed implementations.
4. Review and commit the provided README, brand identity, website branding and logo assets after confirming the git diff.
5. Record a formal mobile architecture decision; only afterward create/assess Flutter code structure against it.
6. Use the included link-repair script to correct residual moved-folder Markdown paths and re-verify links.
