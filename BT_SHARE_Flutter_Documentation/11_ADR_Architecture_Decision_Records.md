# ADR — Architecture Decision Records

> **Project:** BT SHARE — Android Flutter App  
> **Version:** 0.1.0 | **Created:** 2026-10-28 | **Status:** Draft for review  
> **Document owner:** Engineering leads / Product owner | **Approval:** Pending product/Flutter/embedded review  
> **Evidence boundary:** Based on repository `main` reviewed 2026-10-28; this is a proposed, executable specification, **not proof of working code, firmware, hardware, or tests**.

## 1. ADR policy
Record decisions with `ID`, `date`, `status` (`Accepted`, `Proposed`, `Superseded`, `Rejected`), context, options, tradeoffs, evidence, approvers and consequences. **Accepted below** refers to choices already recorded in source documents, not evidence that their hardware works. **Proposed below** is not implementation authorization. New commercial hardware scope gets its own separate ADRs rather than rewriting college prototype history.

## ADR-001 — Android-first Flutter/Dart
- **Status:** Accepted product direction (source DEC-MOB-001, 2026-10-14).
- **Decision:** Build Android mobile client using Flutter/Dart first; iOS not part of initial deliverable.
- **Consequences:** Android-specific permission/audio features may require Kotlin/native plugins. Minimum SDK and versions unresolved.

## ADR-002 — Hub control and audio path separation
- **Status:** Accepted college-prototype baseline (source hardware BRD 2026-10-06).
- **Decision:** Flutter ↔ BLE GATT ↔ ESP32 ↔ UART ↔ BM83 for control; external AUX ↔ BM83 ↔ A2DP receivers for audio.
- **Consequences:** Flutter does not automatically equalize, record, visualize or route the external AUX signal. Any commercial Bluetooth-input variant requires fresh architecture evaluation.

## ADR-003 — Prototype two-receiver limit / long-term vision
- **Status:** Accepted prototype scope, technical capability not independently verified.
- **Decision:** First college build targets exactly two A2DP sink receivers; 3+ remains research. Hardware proof G4 is prerequisite to claims of success.
- **Consequences:** UI prototype max slots two; app must not imply same BM83 supports larger sessions. Contract-driven future extensibility may be designed without promising it works.

## ADR-004 — Standalone app functionality without hub
- **Status:** Accepted product scope (DEC-MOB-002/003).
- **Decision:** Standalone sound utility categories can be used without connected BT SHARE hardware.
- **Consequences:** No mandatory BLE/account onboarding; independent audio-stack testing, privacy and lifecycle requirements.

## ADR-005 — Feature-first Clean Architecture + MVVM/Riverpod
- **Status:** **Proposed** (not recorded as approved for BT SHARE in source repo).
- **Context:** Multiple sound utilities and hardware integration require testable boundaries.
- **Decision candidate:** Feature folders with domain/application/data/presentation, reactive Riverpod-style state and clear ownership.
- **Alternatives:** BLoC/Cubit, plain Flutter ValueNotifier, other DI/state solutions.
- **Sign-off needed:** Lead compares package footprint, team familiarity, device performance and testing.

## ADR-006 — On-device SQLite/Drift persistence
- **Status:** **Proposed**.
- **Context:** Local presets, playlists, session/recording metadata and history need offline storage and migrations.
- **Decision candidate:** SQLite with typed repository and migration layer; simple preferences for non-relational settings.
- **Alternatives:** Isar/ObjectBox/Hive-like key-value stores or custom files; consider licensing, migration and maintenance.
- **Caveat:** No selected cloud database or mobile backend currently.

## ADR-007 — Capability-negotiated BLE contract
- **Status:** **Proposed**, based on accepted ESP32 authoritative-state principle.
- **Decision candidate:** Version handshake, explicit receiver capabilities, product-level errors, snapshots, correlation/sequence and safe unsupported behavior.
- **Alternatives:** Fixed minimal commands or binary-specific protocol.
- **Prerequisite:** Embedded owner approves UUIDs, transport security, events and exact firmware behavior.

## ADR-008 — EQ, mixing and visualizer scoped to permitted sources
- **Status:** Accepted product boundary; exact DSP implementation **Proposed**.
- **Decision:** Never assume privileged system-wide capture/control; start with app-owned playback and user-authorized mic sources.
- **Consequence:** Some requested broad features are technically gated or deferred; UI must disclose source scope.

## ADR-009 — Local-first privacy and no mandatory accounts
- **Status:** Product direction recorded; data retention/encryption details **Proposed**.
- **Decision candidate:** Offline default, least permissions, no raw audio upload by default, explicit file export and erase.
- **Open:** backup, permission policy, diagnostics retention, optional future cloud sync.

## ADR-010 — Direct APK distribution supported by website release center
- **Status:** Website scope documented; channel operational choice **Proposed**.
- **Decision candidate:** Controlled signed APK publication with SHA-256, signer fingerprint, immutable release metadata and revocation.
- **Alternatives:** Google Play, internal enterprise distribution or combination.
- **Consequence:** Website release backend separate from mobile BLE, and needs secure key custody/approval process.

## ADR-011 — Sync diagnostics are not audio synchronization
- **Status:** Accepted limitation in README/requirements.
- **Decision:** Never use GATT link timestamps as proof of headphone acoustic delay; any numeric sync assessment needs calibrated test rig, uncertainty and independent evidence.
- **Consequence:** Sync correction remains a future research track.

## ADR-012 — Receiver volume / firmware OTA must be capability gated
- **Status:** Accepted requirement boundary, unverified technical feasibility.
- **Decision:** Disable or exclude per-sink volume and OTA UI until hardware ownership, command support, authentication and recovery verification are complete.
- **Consequence:** MVP must still function without those features.

## 2. Decision backlog
| Open ADR | Options to compare | Needed evidence | Owner |
|---|---|---|---|
| ADR-TBD-01 | BLE plugin + native permission approach | Supported OS/API matrix, connection/device tests | Flutter/Android |
| ADR-TBD-02 | Playback/DSP plugins or custom native engine | EQ quality, latency, audio focus and licensing | Audio lead |
| ADR-TBD-03 | App minimum/target SDK | Device population and policy | Product/Android |
| ADR-TBD-04 | Theme/navigation system | UX research and accessibility | UX |
| ADR-TBD-05 | Diagnostic retention/encryption and backups | Threat/privacy assessment | Privacy/data |
| ADR-TBD-06 | Hardware architecture for Bluetooth input and 3+ receivers | Official chipset evidence and experiments | Embedded/commercial hardware |

## 3. Decision change process
Do not overwrite prior accepted entries. Add a new ADR with rationale and links to superseded IDs; update impact map for BRD, PRD, SRS, API, DB, test plans and actual firmware. Every final ADR requires named reviewers and decision date; no such sign-offs are fabricated here.

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
