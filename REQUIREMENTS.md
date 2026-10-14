# BT SHARE — Requirements Index

**Date:** 2026-10-14  
**Status:** Scope recorded; implementation and detailed acceptance criteria not yet validated  
**Document purpose:** Keep the existing hardware prototype baseline distinct from the expanded Android mobile-app product scope.

## Requirements sources and authority

1. **Current college hardware prototype:** [`BT_SHARE_BRD.md`](BT_SHARE_BRD.md) and [`BT_SHARE_Execution_Plan.md`](BT_SHARE_Execution_Plan.md) remain the source documents for the BM83/ESP32 two-receiver prototype, LKR 40,000 procurement ceiling and hardware-first test gates. This file does not revise or supersede them.
2. **Android mobile application:** [`docs/mobile-app/PRODUCT_SCOPE.md`](docs/mobile-app/PRODUCT_SCOPE.md) records product-level scope confirmed during feature planning on 2026-10-14. Detailed acceptance criteria, Android technical feasibility and BLE integration contracts require further review.
3. **Feature list:** [`docs/mobile-app/FEATURE_CATALOGUE.md`](docs/mobile-app/FEATURE_CATALOGUE.md) records the proposed app functions and separate standalone sound-tool categories.
4. **Selected 25 feature concepts:** [`docs/mobile-app/FEATURE_EXPANSION_25.md`](docs/mobile-app/FEATURE_EXPANSION_25.md) records all 25 explicitly selected feature ideas and the separate Smart Connection Recovery flow; selected means included in product planning, not technically validated.
5. **Audio workspace expansion (12 detailed proposals + 5 future concepts):** [`docs/mobile-app/FEATURE_EXPANSION_17.md`](docs/mobile-app/FEATURE_EXPANSION_17.md) maps new detail into existing requirements, records genuinely new tools and future candidates, and prevents double-counting.
6. **Decisions and limitations:** [`DECISIONS.md`](DECISIONS.md) logs the recent scope decisions. These are not proof of implementation or hardware capability.

## Product-level requirements recorded

| Reference | Requirement | Scope / status |
| --- | --- | --- |
| APP-PLATFORM-01 | Develop the mobile application with Flutter/Dart for **Android first**. | Direction confirmed; Android versions / device support TBD. |
| APP-USABILITY-01 | Permit users without BT SHARE hardware to access the app's standalone sound utilities. | Direction confirmed; feature-level constraints TBD. |
| SOUND-01 | Equalizers & Sound Enhancers | Category included; functions and OS support to validate. |
| SOUND-02 | Audio Routing & Mixing | Category included; Android limitations to validate. |
| SOUND-03 | Per-App Volume Control | Category included; Android limitations to validate. |
| SOUND-04 | Sound Measuring & Analysis | Category included; calibration / permissions to validate. |
| SOUND-05 | Tuners & Metronomes | Category included; precision and UI behavior to specify. |
| SOUND-06 | Ambient & Focus Sounds | Category included; sound assets and exact functionality to specify. |
| SOUND-07 | Hearing Assistance | Category included; latency, permissions and safety considerations to validate. |
| SOUND-SYNC-01 | Keep sound synchronized across devices. | Product goal recorded; supported device scenarios, achievable latency and technical approach **not confirmed**. |
| HUB-APP-01 | Support BT SHARE hub control/status over BLE as specified in the BRD's provisional APP-F01–APP-F12 catalogue. | Hardware-dependent app capability; contract remains provisional. |
| HUB-LIMIT-01 | Respect the **two simultaneous A2DP receiver** limit of the current college prototype. | Existing hardware baseline, not a permanent product limit. |

## Additional mobile requirements — expanded feature selection (2026-10-14)

- **APP-X01–APP-X25:** All 25 feature concepts in [`FEATURE_EXPANSION_25.md`](docs/mobile-app/FEATURE_EXPANSION_25.md) are included in the **planned app scope**.
- **APP-X26:** Smart Connection Recovery is separately recorded from the highlighted proposal, bringing the enumerated feature ideas to **25 plus one separately highlighted recovery feature**.
- **APP-ROADMAP-01:** APP-X21–APP-X25 are **future-version candidates**, consistent with the originally supplied categorization; inclusion is not a commitment to first-release delivery.
- **APP-COMPAT-01:** Actual Android APIs, permissions, native integration, battery impact, supported devices and receiver control limitations must be established before declaring specific features implementable.
- **APP-PRIVACY-01:** Microphone access, local history, stored recordings, hearing-related processing and any export/firmware controls require appropriate permissions, safety boundaries, and user-visible privacy behavior.
- **APP-GATT-01:** Any new hub-dependent actions require a reviewed, versioned ESP32/Flutter interface contract. No ESP32 commands or BM83 behaviors are assumed to exist yet.

## Audio workspace expansion selected for planning (2026-10-14)

- **APP-Y01–APP-Y12:** All twelve detailed app proposals in [`FEATURE_EXPANSION_17.md`](docs/mobile-app/FEATURE_EXPANSION_17.md) are included for requirements planning. Seven refine already-selected features; the five distinct additional capabilities are **Rhythm & Drum Studio**, **Smart Practice Room**, **Local Audio Player**, **Custom Soundboard** and **Customizable Sound Dashboard**.
- **APP-Y13–APP-Y17:** All five future concepts are included in the roadmap/backlog, **not** as first-release commitments: AI Sound Assistant, Audio Spectrum History, Multi-Listener Session Manager, Safe Listening Tools and Offline-First Experience.
- **APP-NAV-01:** A five-destination concept (Connect / Sound Lab / Studio / Practice / My Sound) is recorded as a **UX proposal**, not an approved navigation design.
- **APP-ROADMAP-02:** The source's foundation / musician / advanced-engineering groups are **suggested sequencing only**, subject to feature feasibility and team approval.
- **APP-AUDIOPATH-01:** Audio generated/played by standalone utilities is app-owned phone audio; it is **not automatically injected** into the current hardware prototype's external AUX audio input.
- **APP-DIAGNOSTICS-01:** Accurate receiver-latency measurement needs a validated signal/capture setup; BLE connection state alone cannot prove acoustic synchronization.

## Boundaries that remain unchanged

- **Current hardware audio path:** external stereo AUX/line-in → BM83 → two Bluetooth Classic A2DP sinks. The Flutter phone controls the hub; it does not relay this hardware-mode AUX audio.
- **Current hardware control path:** Flutter Android app → BLE GATT → ESP32 → UART → BM83.
- A broader **multi-device** goal does not establish that the present BM83, firmware or hardware supports more than two sinks.
- No claim of zero-latency or guaranteed perfectly synchronized playback.
- No newly approved backend, account system, iOS deliverable, Android OS bypass or production medical feature is implied here.

## Requirements still to be frozen

- Testable detailed actions, screens, inputs/outputs and acceptance criteria for all SOUND categories, APP-X01–APP-X26, APP-Y01–APP-Y17 and synchronization.
- Android API level/device support, permissions and native-platform feasibility for sound-system controls.
- BM83 technical evidence and the jointly reviewed versioned BLE GATT contract for APP-F01–APP-F12.
- Whether phone-to-phone synchronization or phone-speaker participation are in scope; these have **not** been confirmed as specific capabilities.

## Implementation evidence

**None supplied for the expanded app scope.** These records describe feature intentions, not working software.
