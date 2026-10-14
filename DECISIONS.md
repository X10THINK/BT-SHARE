# BT SHARE — Decision Register

**Last updated:** 2026-10-14  
**Status:** Product-scope decisions recorded from software-workstream discussion; cross-team technical review is still required wherever existing interfaces or hardware would change.

| ID | Date | Decision | Reason / boundary | Status |
| --- | --- | --- | --- | --- |
| DEC-MOB-001 | 2026-10-14 | Target **Android first**, using **Flutter/Dart**. | iOS is not included in the initial platform target; future platform timing remains unspecified. | Scope confirmed; implementation pending |
| DEC-MOB-002 | 2026-10-14 | BT SHARE mobile app is **not hardware-only**. Non-hardware owners can use standalone sound utilities. | The physical hub remains a major app capability but is not a prerequisite to all other utilities. | Scope confirmed; implementation pending |
| DEC-MOB-003 | 2026-10-14 | Include **all seven sound utility categories** listed in `REQUIREMENTS.md`. | Product-level category inclusion does not approve every example capability or bypass Android restrictions. | Scope confirmed; details pending |
| DEC-MOB-004 | 2026-10-14 | Include **multi-device sound synchronization** as a product goal. | Achievable synchronization, device scenarios and architecture remain unverified. | Goal recorded; feasibility pending |
| DEC-MOB-005 | 2026-10-14 | Preserve the college prototype's **two-receiver BM83/ESP32 hardware baseline**, hardware-first gate sequence and **LKR 40,000** ceiling. | Long-term multi-device vision is broader; no hardware redesign or increase to receiver count has been approved here. | Existing engineering baseline unchanged |
| DEC-MOB-006 | 2026-10-14 | Include all **25** additional numbered app feature concepts, `APP-X01`–`APP-X25`, in the Android mobile app product scope. | Five items explicitly classified as advanced remain future-version candidates; platform/hardware compatibility is not proven. | Scope confirmed; delivery phases and acceptance pending |
| DEC-MOB-007 | 2026-10-14 | Track **Smart Connection Recovery** separately as `APP-X26` because it is an unnumbered, highlighted addition to the 25. | ESP32 owns recovery decisions and authoritative link state; Flutter presents user information. | Scope recorded; hardware integration pending |

| DEC-MOB-008 | 2026-10-14 | Include all **12 additional detailed audio-workspace proposals**, `APP-Y01`–`APP-Y12`, while **merging overlapping functionality** with existing features. | These refine the selected catalogue and introduce five distinct standalone capabilities; no duplicate counts or implementation claims. | Product scope confirmed; feasibility and acceptance pending |
| DEC-MOB-009 | 2026-10-14 | Include **five additional advanced concepts**, `APP-Y13`–`APP-Y17`, in the future roadmap. | Explicitly future-oriented, not MVP release promises; requires further feasibility and prioritization. | Roadmap scope confirmed; delivery timing unspecified |
| DEC-MOB-010 | 2026-10-14 | Record the proposed **five-area navigation** and **three development groupings** as UX and sequencing inputs. | Not approval of final UI screens, Figma navigation or release milestones. | Proposed; needs later UX/planning approval |

Detailed selections: [`docs/mobile-app/FEATURE_EXPANSION_25.md`](docs/mobile-app/FEATURE_EXPANSION_25.md) and [`docs/mobile-app/FEATURE_EXPANSION_17.md`](docs/mobile-app/FEATURE_EXPANSION_17.md).

## Change-control note

The 2026-10-06 BRD and execution plan document a **hardware/embedded prototype** and its provisional Flutter control interface, not the complete expanded standalone mobile product. The app scope is recorded separately in `docs/mobile-app/`. Do not silently reinterpret the old hardware-only Flutter descriptions as comprehensive requirements for every standalone utility, or use this new app scope to declare BM83 capabilities verified.

## No implementation sign-off

These decisions record what should be **considered part of product scope**. They do not constitute a passed prototype gate, an approved detailed architecture, a frozen BLE protocol, or a successful Android feasibility test.
