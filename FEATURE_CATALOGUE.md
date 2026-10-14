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

## D. Explicitly unresolved decisions

- Detailed sub-features, priority and acceptance criteria for each sound utility category.
- Minimum supported Android OS version, device types and required permissions.
- Extent of sound control across third-party apps under Android restrictions.
- Supported combinations for synchronization, including whether multiple phones can participate.
- The jointly agreed BLE service/characteristic UUIDs, commands, events, messages and error codes for the hub.
- Individual device volume, music metadata controls and "play on phone" were illustrated/discussed but **not confirmed as separate build requirements**.

**Implementation status:** Catalogue only; no working feature is asserted.
