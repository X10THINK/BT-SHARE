# TRD — Technical Requirements Document

> **Project:** BT SHARE — Android Flutter App  
> **Version:** 0.1.0 | **Created:** 2026-10-28 | **Status:** Draft for review  
> **Document owner:** Flutter mobile team | **Approval:** Pending product/Flutter/embedded review  
> **Evidence boundary:** Based on repository `main` reviewed 2026-10-28; this is a proposed, executable specification, **not proof of working code, firmware, hardware, or tests**.

## 1. Technical scope and architecture boundaries
This document covers the **Android Flutter client and necessary Android-native adapters**. It does **not** design the BM83 chip, ESP32 firmware, Angular website or cloud services. Hub commands go Flutter → BLE GATT → ESP32 → UART → BM83. Hardware audio goes AUX → BM83 → A2DP sinks. App-owned audio goes Android-supported audio routes. Do not mix these data paths.

## 2. Platform and tooling
| Item | Baseline | Status |
|---|---|---|
| Platform | Android first, Flutter + Dart | Confirmed in repository |
| Android min SDK / target SDK | To select from intended device population, plugins and current Play/direct APK policies | Open, do not hardcode a guessed value |
| Architecture | Feature-first Clean Architecture + MVVM-style presentation; Riverpod suggested | **Proposed**, requires team ADR |
| Routes | Named declarative navigation; go_router or equivalent suggested | Proposed |
| Local storage | Transactional SQLite via Drift or equivalent; key-value preferences only for simple settings | Proposed |
| Bluetooth | Maintained BLE GATT library with Android-native permission integration | Library and version TBD |
| Playback | Android media session, audio focus and foreground playback where required | Required behavior; library TBD |
| Mic analysis / recording | Android permission/foreground rules + plugin/native verification | Design/tests pending |
| CI | Deterministic Flutter analyze/test/build, static analysis and artifact signing checks | Required, not present in repository |

## 3. Runtime components
- **Presentation layer:** screens, accessible UI widgets, view models / state notifiers, navigation, permission explanations.
- **Application layer:** use cases (ConnectHub, ScanReceivers, PairReceiver, PlayLocalTrack, SaveEQPreset, StartRecording, etc.) with validation and capability checks.
- **Domain:** receiver identity and state, audio sources, EQ profiles, session histories and typed failures. No Flutter or GATT imports.
- **Infrastructure:** BLE adapters, Android platform channel adapters, SQLite repositories, local media index/file handles, logging and filesystem export.
- **Shared services:** permissions, audio-focus coordinator, clock, app lifecycle, capability registry and privacy/retention controls.

## 4. Android permissions and platform constraints
- Runtime Bluetooth permissions vary by Android version; request only permissions actually needed by the implementation, with separate legacy behavior where required. Do not request location routinely if the supported BLE scan scenario does not need it; validate plugin/platform behavior.
- Use `RECORD_AUDIO` only for selected microphone features, and the relevant Android media/document picker for local audio access. Obtain persistent URI access only where supported and needed.
- Handle denied, permanently denied and revoked permissions, Bluetooth-disabled and app-resumed states.
- Background playback needs media-session/audio-focus lifecycle handling and any platform-required foreground service declarations. Microphone background behavior has tighter restrictions and must be explicitly tested rather than assumed.
- Android ordinarily cannot arbitrarily capture or independently set volume for unrelated apps or apply system-wide EQ. Guard SOUND-02/03 and APP-X features by verified support.
- Avoid accessibility APIs as an unsupported shortcut around unrelated apps' audio restrictions.

## 5. BLE requirements and firmware handshake
- On connect, read/probe protocol version and capabilities before enabling receiver commands.
- ESP32 reports authoritative receiver IDs, slot allocation and states; client caches only clearly labeled last-known data.
- Commands require correlation IDs, timeouts, deterministic error parsing, at-most-one active operation per receiver/operation class and defined retry semantics.
- Never assume GATT notifications are reliable or ordered across reconnection; request a fresh snapshot after reconnect and de-duplicate by event IDs/sequences when provided.
- BLE payload framing, MTU, characteristic UUIDs, commands and firmware-capability bits are **proposed** in [API Spec](09_API_Specification.md), not frozen. Do not implement with fabricated UUIDs.
- UI must enforce exactly two prototype slots unless the *verified hub capability* and approved commercial requirements permit more.

## 6. Audio processing rules
1. EQ/mixing/visualization applies to sources the app can decode, generate or legally receive. Device-specific firmware volume and external AUX effects are separate and unsupported until verified.
2. Local media player handles audio focus, interruptions, notifications, pause/resume, repeat and queue state consistently.
3. Recorder handles mic consent, interruption, storage exhaustion, interruption recovery, safe file finalization and export.
4. DSP processing must declare latency, channel strategy, supported sample rates and floating/fixed-point clipping protections once chosen.
5. Visualization FFT must use bounded input buffers, pause when invisible and never silently use microphone if source changes.
6. Sound-level estimation requires calibration/limitations; hearing tools must avoid medical or measured-at-ear claims without evidence.

## 7. Proposed quality requirements — targets for sign-off, not verified performance
| NFR ID | Requirement | Proposed measurable gate |
|---|---|---|
| NFR-M01 | Graceful offline/hub-free operation | Standalone release subset works with Wi-Fi/cellular off and no connected hub |
| NFR-M02 | Accessibility | Screen-reader usable; semantic labels; dynamic text; keyboard/switch access tested on target devices |
| NFR-M03 | State integrity | Unknown/stale receiver states cannot be displayed as current streaming; reconnection refresh works |
| NFR-M04 | Crash resilience | No unhandled exception in specified permission denial, disconnect and low-storage tests |
| NFR-M05 | Privacy | No network upload of recordings/receiver identifiers by default; local erase verified |
| NFR-M06 | Maintainability | Analysis/lint, unit tests, feature isolation and CI checks required |
| NFR-M07 | Performance | Startup, scroll, DSP CPU/battery, audio glitches and BLE command latency measured against a target device matrix; numeric budgets TBD |
| NFR-M08 | Storage integrity | Transactional migrations, corruption handling and record/file cleanup tests pass |
| NFR-M09 | Protocol compatibility | Unsupported protocol versions produce actionable, safe UI; no command guessed |
| NFR-M10 | Security | No secrets embedded in APK; exported data redacted; release APK signed and checksummed |

## 8. Compatibility/test matrix to select
At least: Android low/mid/high performance tiers available to team, two or more supported OS versions, Bluetooth-enabled and disabled, headset and phone-speaker route, permission grant/denial, app background/restart, dark/light, English/Tamil, accessibility text sizes, low storage, offline operation. Actual models/API versions must be recorded before claiming coverage.

## 9. Dependency and security management
Lockfile committed; review plugin permissions/licenses; use maintained plugins with native Android test coverage; secure signing key outside source; dependency scanning; static analysis; release build reproducibility; minimize export/open-file intents. No backend secrets or service credentials inside Flutter bundles.

## 10. Open technical decisions
Select Android SDK versions, BLE library, codec support and native DSP strategy, storage package/encryption policy, foreground services, performance budgets, firmware protocol version and test hardware matrix. Record outcomes in [ADR](11_ADR_Architecture_Decision_Records.md).

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
