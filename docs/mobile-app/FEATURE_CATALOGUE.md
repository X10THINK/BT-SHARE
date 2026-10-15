# BT SHARE — Flutter Feature Catalogue

**Date:** 2026-10-14  
**Status:** Product-scope catalogue. Detailed feature design, technical feasibility, priorities inside categories and acceptance tests remain to be agreed.

## A. BT SHARE hub: provisional BRD app functions

| BRD ID | Planned function | Meaning | Scope classification |
| --- | --- | --- | --- |
| APP-F01 | Connect to BT SHARE hub | Connect the Flutter app to ESP32 over BLE and show hub readiness | Hardware-dependent core |
| APP-F02 | Start receiver scan | Ask ESP32/BM83 to discover compatible Bluetooth audio sinks | Hardware-dependent core |
| APP-F03 | Display discovered devices | Show ESP32-reported device name, ID and state | Hardware-dependent core |
| APP-F04 | Select Device 1 | Assign receiver to prototype slot 1 | Hardware-dependent core |
| APP-F05 | Select Device 2 | Assign receiver to slot 2; enforce prototype maximum-two rule | Hardware-dependent core |
| APP-F06 | Pair device | Request pairing and show progress/result | Hardware-dependent core |
| APP-F07 | Connect device | Request connection and show status | Hardware-dependent core |
| APP-F08 | Disconnect device | Request receiver disconnection | Hardware-dependent core |
| APP-F09 | Reconnect request | Request reconnection for eligible disconnected receiver | Hardware-dependent core |
| APP-F10 | View status | Show state of hub and each receiver (paired/connected/streaming as available) | Hardware-dependent core |
| APP-F11 | View errors | Show structured pairing, connection, maximum-links, BM83 comms and timeout errors | Hardware-dependent core |
| APP-F12 | Development log/status view | Developer-facing protocol and diagnostic information | Hardware-dependent **optional** |

These IDs and descriptions come from `BT_SHARE_BRD.md` section 11.1. The BRD itself says the **final Flutter function catalogue and BLE contract are not yet frozen**. The phone does not scan/pair sinks through normal mobile audio Bluetooth APIs in this flow: **ESP32/BM83** does so and reports results to Flutter.

## B. Standalone sound utilities: seven included categories

| Tracking ID | Category | Confirmed at category level | Detailed functionality |
| --- | --- | --- | --- |
| SOUND-01 | Equalizers & Sound Enhancers | Included | Needs specification and Android feasibility verification |
| SOUND-02 | Audio Routing & Mixing | Included | Needs specification and Android feasibility verification |
| SOUND-03 | Per-App Volume Control | Included | Needs specification and Android feasibility verification |
| SOUND-04 | Sound Measuring & Analysis | Included | Needs specification and Android feasibility verification |
| SOUND-05 | Tuners & Metronomes | Included | Needs specification and Android feasibility verification |
| SOUND-06 | Ambient & Focus Sounds | Included | Needs specification and Android feasibility verification |
| SOUND-07 | Hearing Assistance | Included | Needs specification and Android feasibility verification |

All seven are **intended to be usable by people who do not own the hardware**, subject to device-level permissions, Android support and detailed requirements. Competitor app examples mentioned during brainstorming are **references**, not a guaranteed feature-by-feature parity commitment.

## C. Cross-device synchronization

| ID | Goal | Status |
| --- | --- | --- |
| SOUND-SYNC-01 | Keep sound playback synchronized across devices with minimal noticeable timing difference | In product scope; scenarios and method not specified, effectiveness unverified |

Do not equate the first prototype's two A2DP connections with proven synchronized output. No zero-latency claim is approved.

## D. Additional 25 selected features and highlighted recovery flow

The software lead has now selected **all 25** entries `APP-X01`–`APP-X25` for the planned Android app product scope, including the five explicitly labelled **advanced/future-version** features. **Smart Connection Recovery** is separately tracked as `APP-X26` (highlighted outside the numbered 25).

See **[`FEATURE_EXPANSION_25.md`](FEATURE_EXPANSION_25.md)** for the complete indexed list, user-facing behaviors, feature-to-category mapping, dependencies and validation cautions. These decisions supersede the earlier uncertainty about whether independent receiver volume, profile saving and visualizers should be in the *planned feature set*; they do **not** establish technical ability.

## E. Audio workspace expansion: 12 detailed proposals + 5 future concepts

All twelve further proposals (`APP-Y01`–`APP-Y12`) and all five future concepts (`APP-Y13`–`APP-Y17`) are included in the **planned Android product scope**. This is a **merge into the existing catalogue**, not seventeen unique new implementations.

- **Five distinct added tool families:** Rhythm & Drum Studio (`APP-Y03`), Smart Practice Room (`APP-Y05`), Local Audio Player (`APP-Y10`), Custom Soundboard (`APP-Y11`) and Customizable Sound Dashboard (`APP-Y12`).
- **Seven detailed refinements:** Live Audio Visualizer Studio (`APP-Y01`), Voice Recorder & Audio Lab (`APP-Y02`), Mini Audio Mixer (`APP-Y04`), Ambient Sound Mixer (`APP-Y06`), BT SHARE Device Control Center (`APP-Y07`), Personal Audio Profiles (`APP-Y08`), Audio Sync & Diagnostics Lab (`APP-Y09`).
- **Five future concepts:** AI Sound Assistant (`APP-Y13`), Audio Spectrum History (`APP-Y14`), Multi-Listener Session Manager (`APP-Y15`), Safe Listening Tools (`APP-Y16`), Offline-First Experience (`APP-Y17`).

**Complete requirement details, existing-ID mappings and feasibility gates:** [`FEATURE_EXPANSION_17.md`](FEATURE_EXPANSION_17.md).

**Proposed (not approved) information architecture:** Connect, Sound Lab, Studio, Practice, My Sound. No screens or component designs are finalized by this selection.

## F. Explicitly unresolved decisions

- Detailed acceptance criteria and first-release priority for all selected features; APP-X01–X26 plus APP-Y01–Y17 are product scope, not an approved delivery schedule.
- Minimum supported Android OS version, device types and required permissions.
- Extent of sound control across third-party apps under Android restrictions.
- Supported combinations for synchronization, including whether multiple phones can participate.
- The jointly agreed BLE service/characteristic UUIDs, commands, events, messages and error codes for the hub.
- **Per-device volume is now selected as APP-X06, feasibility pending.** "Now Playing" metadata and playing hardware AUX audio on the phone have **not** been separately approved as additional requirements.

**Implementation status:** Catalogue only; no working feature is asserted.
