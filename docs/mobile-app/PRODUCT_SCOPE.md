# BT SHARE Android App — Product Scope

**Version:** Draft 0.1  
**Date:** 2026-10-14  
**Owner workstream:** Flutter mobile application  
**Status:** Feature categories and Android-first direction confirmed in product discussion; detailed behavior and feasibility not yet frozen.

## 1. Product identity

BT SHARE is planned as a **Flutter-based, Android-first sound utility application** that can be useful with or without the BT SHARE physical hardware.

Two distinct areas are in scope:

- **BT SHARE hardware mode:** control and observe a BM83/ESP32-based audio-sharing hub. The **current college prototype** supports a maximum of two simultaneous Bluetooth Classic A2DP receivers.
- **Standalone sound utilities:** user-accessible sound tools that do **not** require the BT SHARE hub. All seven product categories below are included for detailed specification and feasibility review.

The project's wider audio-sharing vision is **multiple** receivers; two is a constrained first hardware milestone. The long-term receiver count and hardware architecture have not been chosen.

## 2. Confirmed standalone feature categories

| Ref | Category | What has been selected | What is not yet specified or proven |
| --- | --- | --- | --- |
| SOUND-01 | Equalizers & Sound Enhancers | Equalization and sound-enhancement utility category | Which effects, supported audio sources, system-wide control, presets and Android APIs |
| SOUND-02 | Audio Routing & Mixing | Audio routing/mixing utility category | Exact input/output routes, cross-app capture rights, virtual routes and limitations |
| SOUND-03 | Per-App Volume Control | Per-application sound-volume management category | Whether/how arbitrary third-party app audio streams can be controlled on Android |
| SOUND-04 | Sound Measuring & Analysis | Sound-level and frequency-analysis category | Measurement calibration, accuracy claims, microphone access and exact displays |
| SOUND-05 | Tuners & Metronomes | Instrument tuning and beat/tempo tools category | Instrument selection, tuning algorithms and timing/accuracy criteria |
| SOUND-06 | Ambient & Focus Sounds | Generated/recorded ambient and focus-audio category | Sound library, licensing, playback/mixing UI and audio asset management |
| SOUND-07 | Hearing Assistance | Hearing-related audio assistance category | Routing latency, compatible outputs, permission model, safety boundaries and test criteria |

**Scope interpretation:** Inclusion of a category is a product decision, **not** a claim that every listed competitor-app function is approved or technically possible. Individual behaviors still need precise product requirements and feasibility checks.

## 2A. Confirmed 25-feature expansion (2026-10-14)

The software-workstream lead requested that **all 25** additional feature concepts be included in BT SHARE's Android app product scope. They cover premium sound experiences (`APP-X01`–`APP-X04`), hub-oriented controls and monitoring (`APP-X05`–`APP-X09`), standalone utilities (`APP-X10`–`APP-X14`), product experience (`APP-X15`–`APP-X20`), and originally labelled advanced/future features (`APP-X21`–`APP-X25`). A highlighted **Smart Connection Recovery** requirement is tracked separately as `APP-X26`.

The full feature list and precise wording are in [`FEATURE_EXPANSION_25.md`](FEATURE_EXPANSION_25.md). These are requirements-planning commitments, **not** claims of Android system access or available BM83/ESP32 firmware support. The pre-existing seven categories, including Audio Routing & Mixing, Per-App Volume Control and Hearing Assistance, remain included even where they are not exactly matched by a numbered new feature.

**Phasing rule:** Features `APP-X21`–`APP-X25` remain identified as advanced/future, not first-version deliveries. No definitive release date, UI layout or final acceptance test has been approved.

## 2B. Audio workspace expansion: 12 detailed proposals and 5 future concepts

The Flutter lead subsequently selected all **12 detailed audio-workspace proposals** and **five additional future concepts** for requirements planning. These are mapped in [`FEATURE_EXPANSION_17.md`](FEATURE_EXPANSION_17.md), with explicit references to existing APP-X/SOUND/APP-F features so overlapping ideas are treated as **refinements**, not unrelated duplicate capabilities.

**Distinct new tool families introduced:** Rhythm & Drum Studio; Smart Practice Room; Local Audio Player; Custom Soundboard; Customizable Sound Dashboard. Other proposals deepen existing visualizer, recorder, mixer, ambient, profiles, hardware control and synchronization/diagnostic plans.

**Future scope added:** AI Sound Assistant; Audio Spectrum History; Multi-Listener Session Manager; Safe Listening Tools; Offline-First Experience. The first four introduce or deepen features, while offline-first is a cross-cutting quality direction. These are **future roadmap inclusions**, not first-release commitments.

The source also outlines five candidate navigation destinations and foundation/musician/advanced sequencing. They are **recorded as proposals only**, without UI/UX sign-off or release schedule.

## 3. Multi-device synchronization goal

**SOUND-SYNC-01 — Maintain synchronized sound across devices** is in the planned product scope. The user experience goal is to minimize perceptible inter-device timing differences.

- This does **not** authorize a claim of perfect synchronization or zero latency.
- Supported device combinations, whether other smartphones are participants, how timing would be measured, and the synchronization mechanism remain unspecified.
- Existing hardware documentation warns that different A2DP receivers may introduce different delays; **dual connection** and **synchronized playback** are different acceptance outcomes.

## 4. Hardware-dependent mobile feature baseline

The BRD's **provisional** APP-F01–APP-F12 set covers: connect to hub; request receiver scan; display discoveries; select receiver slots 1 and 2; pair; connect; disconnect; reconnect; view state/errors; and optional developer diagnostics. The full register appears in [`FEATURE_CATALOGUE.md`](FEATURE_CATALOGUE.md).

**Hardware-mode architecture:** Flutter → BLE GATT → ESP32 → UART → BM83 for control; AUX/line-in → BM83 → two A2DP sinks for audio. The Flutter phone is **not** the AUX audio relay for this prototype. This architectural rule does not forbid local playback or microphone access by separate standalone utilities where technically permitted.

## 5. User journeys (high level, pending UI approval)

### A. Hardware-owner journey

1. Open BT SHARE.
2. Access hub connection flow and connect to ESP32 via BLE.
3. Request discovery of compatible audio receivers via ESP32/BM83.
4. Select receiver 1 and receiver 2, pairing when required.
5. Connect both receivers and play the **external AUX source**.
6. Observe their actual states; disconnect or request reconnect as needed.
7. Receive actionable errors if connection, pairing, timeout, or maximum-two conditions occur.

### B. Standalone-user journey

1. Open BT SHARE **without a hardware connection**.
2. Choose one of the seven available sound utility categories.
3. Use the functions that are ultimately specified and supported on that Android device.

The screen navigation, onboarding steps, permission flow and specific tool controls have **not** been approved by this document.

## 6. Platform and engineering cautions

- **First target:** Flutter/Dart for Android. Specific minimum Android version is not selected.
- Native Android code or system APIs **may be necessary** for some audio operations; Flutter by itself does not confer system-level permissions.
- Android restricts a number of arbitrary third-party app capture, per-app volume, audio routing and global processing scenarios. Feature breadth cannot be promised before scoped Android feasibility tests.
- Sound-level measurements need calibration/limitations recorded; hearing-related tools need careful latency and safety evaluation. No medical-grade performance claim is approved.
- Hardware features depend on the approved BLE command/event protocol and validated ESP32/BM83 behavior.

## 7. Current state

**Requirements planning only, now including 25 selected feature concepts, separately highlighted Smart Connection Recovery, twelve detailed audio-workspace proposals and five future roadmap concepts.** No Flutter implementation, Android permission/device compatibility result, synchronized playback measurement or hardware app integration is claimed as complete in this scope document.

## 8. Existing engineering sources

- [`../../BT_SHARE_BRD.md`](../../BT_SHARE_BRD.md) — hardware prototype requirements and provisional mobile app functions.
- [`../../BT_SHARE_Execution_Plan.md`](../../BT_SHARE_Execution_Plan.md) — hardware-first gates and Flutter integration sequencing.
- [`../../PROJECT_STATUS.md`](../../PROJECT_STATUS.md) — overall engineering status (update separately when merging this scope).
- [`../../DECISIONS.md`](../../DECISIONS.md) — app scope decision log.
