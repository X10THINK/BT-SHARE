# Project Plan — Development Roadmap

> **Project:** BT SHARE — Android Flutter App  
> **Version:** 0.1.0 | **Created:** 2026-10-28 | **Status:** Draft for review  
> **Document owner:** Product lead / Engineering lead | **Approval:** Pending product/Flutter/embedded review  
> **Evidence boundary:** Based on repository `main` reviewed 2026-10-28; this is a proposed, executable specification, **not proof of working code, firmware, hardware, or tests**.

## 1. Planning premise
This is a dependency-based roadmap, **not a promise of calendar dates**. The repository documents scope but no verified Flutter source. A separate embedded team owns BM83/ESP32 and a separate website team owns Angular releases. Parallelize standalone app functionality with hardware feasibility; keep BLE-dependent acceptance behind contract and hardware gates.

## 2. Phases and release gates
| Phase | Outcome / tasks | Evidence to close | Ownership | Depends on |
|---|---|---|---|---|
| M0 — Baseline | Reconcile repo revisions, confirm standalone vs commercial scope, confirm team owners | Signed MVP/backlog, scope trace, open decision log | Product + leads | None |
| M1 — Feasibility | Android API tests for local player/EQ, mic, routing, BLE scan; BM83 dual-stream feasibility reviewed by embedded | Device experiment notes; manufacturer evidence from embedded | Flutter + embedded | M0 |
| M2 — Foundation | Flutter project, architecture, lint/CI, navigation, themes, localization skeleton, permission UX and local storage | Runnable app, automated tests, initial accessibility smoke | Flutter | M0 |
| M3 — Standalone core | Local player, app-owned EQ/profiles, ambient playback, recorder/tuner where validated | Feature demo, device tests, persisted data | Flutter | M1/M2 |
| M4 — Hub integration contract | Firmware handshake, capabilities, event model, UUIDs, errors, snapshots, mock hub | Contract v1, fake-server tests and cross-team sign-off | Embedded + Flutter | M1 |
| M5 — Hub app slices | Connect/scan/select/pair/connect/status/errors/reconnect UI | BLE mock pass + physical device integration evidence | Flutter + embedded | M2/M4 and hardware G3/G4 for core audio claims |
| M6 — Hardening / candidate | Privacy deletion, interruption, battery, offline, a11y, migration, diagnostics, negative cases | Test plan, UAT sign-off, security and performance report | QA + leads | M3/M5 for included features |
| M7 — Release | Signed Android artifact, release notes, checksum, website publication handoff | Reproducible CI and release checklist | Flutter + release team | M6 |
| M8 — Later / research | Rhythm/soundboard, extended tools, sync diagnostics, OTA, AI, 3+ commercial receivers | Individual PRD addenda and feasibility gates | Product + owning teams | Explicit new approvals |

## 3. Suggested work streams (no fixed durations)
- **Product/UX:** personas, workflows, first-release scope, design tokens, bilingual content, prototype UAT.
- **Flutter platform:** repo scaffolding, permissions, audio focus, storage, testing infrastructure, app lifecycle.
- **Standalone audio:** file playback/EQ, microphone tools, ambience, practice utilities, profiling.
- **Hub integration:** protocol negotiation, BLE state reducer, firmware fakes, structured errors and real-device verification.
- **QA/security:** test automation, test phones, permission matrix, privacy review, release checks.
- **Release/website liaison:** APK metadata and signing, no draft release public exposure, release notes/rollback.

## 4. Backlog prioritization method
For each feature record `user impact`, `dependency confidence`, `Android feasibility`, `hardware feasibility`, `effort`, `testability`, `risk`, `release candidate`. Recommend delivering a small, reliable vertical slice before expanding feature variety. This prioritization is **proposed** and must be signed off by product owner.

## 5. Initial milestones as usable tasks
| Task ID | Action | Deliverable | Exit test |
|---|---|---|---|
| TASK-001 | Sign off supported Android/phone matrix | Device/OS list | Product + QA approval |
| TASK-002 | Freeze MVP list from APP-F/APP-X/APP-Y/SOUND | Versioned prioritized feature register | No conflicting requirements |
| TASK-003 | Create Flutter repository structure | `lib`, `test`, `integration_test`, lockfile and CI | Analyze + sample tests green |
| TASK-004 | Prototype source-owned local playback and EQ | Working audio demo | Audibly verified behavior on target route |
| TASK-005 | Prototype BLE GATT with simulator | Version handshake, notifications, failures | Mock tests |
| TASK-006 | Finalize protocol contract | UUIDs, schema, states, seq/acks, capability flags | Joint signatures |
| TASK-007 | Create local schema + migrations | DB v1 and migrations | Unit/integration tests |
| TASK-008 | Create complete UX flows | Screen map + component states | UX approval and accessibility review |
| TASK-009 | Integrate supported receiver operations | Hub-controlled flows | Verified firmware and device test |
| TASK-010 | Conduct release UAT | Signed result matrix | 0 open blocker/critical failures |
| TASK-011 | Produce signed APK and metadata | Binary, hash, version, signer, notes | Independent download/install verification |

## 6. Governance and acceptance
Use one issue per implementable requirement with reference ID, dependency, positive/negative acceptance, test ID and acceptance evidence. Weekly status can show `planned → ready → implementing → review → tested → accepted → released`, not assumed completion percentages. Gate M5 cannot be declared passed by Flutter mocks alone; physical hub evidence is required for hardware behavior.

## 7. Critical path and response to blocking items
The dual-audio feasibility challenge may block the **hardware product** but need not block standalone player/EQ/ambient/recording development. If BM83 cannot meet G4, freeze hub marketing claims and return to architecture review; do not disguise blocked audio by app UI. If Android system-wide features fail feasibility, scope them to app-owned media or defer explicitly.

## 8. Deliverable acceptance checklist
- BRD/PRD/SRS consistent and reviewed; ADR decisions recorded.
- Buildable source and deterministic tests present; API / DB versioned.
- UI designs cover loading/error/permission/unsupported/empty states.
- Hardware operations signed off by embedded owner; QA has test logs.
- Signed APK validated, provenance retained and published via approved channel.
- RAID risks closed/accepted with owners; no hidden assumptions remain release blockers.

## Source references and document control

- [overview](https://github.com/X10THINK/BT-SHARE/blob/main/README.md)
- [status](https://github.com/X10THINK/BT-SHARE/blob/main/PROJECT_STATUS.md)
- [requirements](https://github.com/X10THINK/BT-SHARE/blob/main/REQUIREMENTS.md)
- [decisions](https://github.com/X10THINK/BT-SHARE/blob/main/DECISIONS.md)
- [brd](https://github.com/X10THINK/BT-SHARE/blob/main/Basic%20Documents/MD/BT_SHARE_BRD.md)
- [plan](https://github.com/X10THINK/BT-SHARE/blob/main/Basic%20Documents/MD/BT_SHARE_Execution_Plan.md)
- [catalogue](https://github.com/X10THINK/BT-SHARE/blob/main/docs/mobile-app/FEATURE_CATALOGUE.md)
- [x25](https://github.com/X10THINK/BT-SHARE/blob/main/docs/mobile-app/FEATURE_EXPANSION_25.md)
- [y17](https://github.com/X10THINK/BT-SHARE/blob/main/docs/mobile-app/FEATURE_EXPANSION_17.md)
- [feasibility](https://github.com/X10THINK/BT-SHARE/blob/main/docs/mobile-app/FEASIBILITY_REGISTER.md)
- [product](https://github.com/X10THINK/BT-SHARE/blob/main/docs/mobile-app/PRODUCT_SCOPE.md)

**Change control:** Before implementation, confirm current source commit, product scope, prototype firmware capabilities, Android device matrix, ownership and acceptance criteria. Revisions must log approver, date and affected requirement IDs. The existing repository baseline remains authoritative for recorded historical decisions; this new pack does not silently supersede it.
