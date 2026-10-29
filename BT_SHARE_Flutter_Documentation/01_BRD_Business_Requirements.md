# BRD — Business Requirements Document

> **Project:** BT SHARE — Android Flutter App  
> **Version:** 0.1.0 | **Created:** 2026-10-28 | **Status:** Draft for review  
> **Document owner:** Product owner | **Approval:** Pending product/Flutter/embedded review  
> **Evidence boundary:** Based on repository `main` reviewed 2026-10-28; this is a proposed, executable specification, **not proof of working code, firmware, hardware, or tests**.

## 1. Business context and problem
BT SHARE targets the inconvenience of sharing one audio program between independent Bluetooth listening devices, while also offering an Android audio toolbox to people who do not own a hub. Existing college-prototype documents define **external stereo AUX → BM83 → two Bluetooth Classic A2DP sinks**. A future affordable commercial product may accept Bluetooth audio input and investigate more simultaneous listeners; those are **separate unapproved architecture requirements**, not prototype facts.

## 2. Business objectives
| ID | Objective | Proposed evidence / exit criterion | Commitment |
|---|---|---|---|
| BIZ-01 | Give hardware owners a comprehensible remote control | User can discover a hub, initiate supported receiver operations and understand errors in UAT | Must for hardware-control MVP, subject to tested hub |
| BIZ-02 | Serve people without the hub | User can launch and use approved standalone audio tools without pairing or creating an account | Must for initial standalone release |
| BIZ-03 | Maintain truthful capability claims | UI never labels a receiver streaming unless ESP32 supplies validated evidence; unsupported features are hidden/disabled with reasons | Must |
| BIZ-04 | Protect trust and privacy | Contextual microphone/Bluetooth permissions, local-first data, meaningful erase controls, no fabricated analytics | Must |
| BIZ-05 | Support economical Sri Lankan distribution | Android-first, low-end device testing and a verifiable APK publication path | Direction; device ranges and commercial price TBD |
| BIZ-06 | Reduce delivery risk | Separate app-owned audio from hub external AUX audio, and track hardware/Android feasibility independently | Must |

## 3. Intended users and stakeholders
- **Hardware owner:** wants to connect an ESP32 hub, choose up to two receivers for the *current prototype*, reconnect safely and see real status.
- **Standalone user:** wants local music playback, EQ, ambient sounds and supported recording/practice tools without hub or account.
- **Technical tester / support:** needs diagnostic errors, reproducible session logs and a way to distinguish mobile permission, BLE, firmware and audio failures.
- **Product owner:** owns priorities, scope freeze, release approval and truthful marketing language.
- **Flutter team:** implements application and Android-native integration. **Embedded/hardware team:** owns ESP32 BLE protocol, receiver state, BM83 control and audio path.
- **Website/release team:** owns the separate Angular portal and signed APK distribution pipeline; this document does not authorize a new mobile cloud backend.

## 4. Business scope
**Included in planned product scope:** Android Flutter client; hub control over BLE; seven sound categories; 25 selected APP-X features plus APP-X26; 12 APP-Y expansions and five APP-Y future concepts. See [PRD](02_PRD_Product_Requirements.md) and [SRS](05_SRS_Software_Requirements_Specification.md). Planned inclusion is not an MVP commitment.

**Out of scope by current decision:** iOS first release; cloud account requirement; phone relaying the existing external AUX feed; guaranteed arbitrary third-party app capture/control; medical-grade hearing claims; production-ready Bluetooth-input mode; proven 3+ receiver output; automatic synchronization correction; unverified OTA updates.

## 5. Business rules
1. Hardware is optional for standalone tools; lack of BLE must not block them.
2. The *existing prototype* supports a maximum UI selection of two active receivers; expanding that number requires a new, tested hardware capability contract.
3. ESP32 is the authoritative source of pairing, connection, streaming, link error and recovery state. UI must not infer acoustic streaming from a successful BLE connection.
4. App EQ and visualizer behavior only affects audio streams that Android legally provides to the app. No automatic DSP control of external AUX.
5. User recording and microphone analysis require explicit user action, permission and clear data handling.
6. Draft/future features must remain identified as unavailable until build, device test and sign-off.

## 6. Business success measures — proposed, not approved targets
| Measure | Baseline | Definition / review decision |
|---|---|---|
| UAT completion | Not measured | 100% of release-blocking acceptance cases pass on chosen Android and hardware matrix |
| Hub operation completion | Not measured | Observe median / failure distribution for scan → select → connect; target to be set after hardware telemetry |
| Crash-free sessions | Not measured | Choose numerical SLO after pilot, not invented now |
| Support comprehension | Not measured | UAT participants can identify disconnect/failure and appropriate next action |
| Offline utility access | Not measured | Tested tools function without account, network or hub where specified |
| Privacy controls | Not measured | Erase/export tests pass; permissions requested only when needed |

## 7. Constraints, dependencies and approvals
- Actual official BM83 AT firmware support for simultaneous active audio remains unverified within the repository; this blocks any commercial dual-stream guarantee.
- Hardware BRD/Execution Plan date **2026-10-06** and Android scope dates **2026-10-14/15**. The current repository does not prove later native engineering status.
- The documented college procurement ceiling is LKR 40,000 **for that prototype**, not an approved commercial selling price or Flutter budget.
- Minimum Android API, hosting/CDN for APK, storage library, analytics policy and exact first release feature subset are undecided.

## 8. Approval gates
**BRD sign-off requires:** product owner accepts business objectives; embedded owner confirms hub capability boundary; Flutter lead accepts independent application responsibility; tester accepts measurable MVP outcomes; legal/privacy owner reviews microphone/hearing and release claims. Status remains **Draft** until those approvals are recorded.

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
