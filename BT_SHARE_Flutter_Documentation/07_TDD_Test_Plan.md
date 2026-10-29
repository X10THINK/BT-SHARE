# TDD — Test-Driven Development Strategy and Test Plan

> **Project:** BT SHARE — Android Flutter App  
> **Version:** 0.1.0 | **Created:** 2026-10-28 | **Status:** Draft for review  
> **Document owner:** QA lead / Flutter engineering | **Approval:** Pending product/Flutter/embedded review  
> **Evidence boundary:** Based on repository `main` reviewed 2026-10-28; this is a proposed, executable specification, **not proof of working code, firmware, hardware, or tests**.

## 1. Test policy
Use **Red → Green → Refactor** for domain/application logic, protocol decoding, local persistence and UI state reducers. Automated passes validate app behavior only; tests with mocked ESP32 **do not prove BM83 Bluetooth audio**, latency or external AUX capture. No tests are recorded as passed in this draft.

## 2. Test layers
| Layer | Unit under test | Tools/approach (choice TBD) | Purpose |
|---|---|---|---|
| Domain unit | receiver state transitions, two-slot invariants, profile validation | Flutter/Dart `test` | Fast, deterministic policy |
| Application unit | connect/scan/pair actions, timeout, retry coordination | Fake repositories, clocks | Logic and typed error handling |
| Widget | UI empty/loading/error, permission education, accessible labels | `flutter_test` | Correct presentation and semantics |
| Contract | JSON/binary framing, UUID mapping, version negotiation, stale/out-of-order events | Firmware fixtures + mock BLE server | Interoperability without hardware claim |
| Storage | schema, migrations, transactions, import validation | Temporary DB / test fixtures | Prevent data loss/corruption |
| Native integration | Bluetooth permissions, audio focus, background playback, file access | Real Android devices/emulators where applicable | Platform behavior |
| Hardware integration | ESP32↔app GATT commands and state reports | Real hub + test receivers | Actual interface evidence |
| Hardware acoustic | AUX→receivers with timing/compatibility capture | Embedded/bench rig, outside Flutter unit test | G3/G4, measured limitations |
| Security/privacy | invalid input, redaction, export, permissions, APK provenance | Static/dynamic review | No unintended disclosure |
| UAT | realistic end-to-end scenarios | Witnessed acceptance scripts | Product fitness |

## 3. Example TDD stories
**TDD-H01 — More than two current-prototype slots**
1. RED: test `SelectReceiver` fails with `MaxActiveReceivers` when both prototype slots occupied.
2. GREEN: implement invariant check at application/domain boundary, no BLE command emitted.
3. REFACTOR: extract capability-derived `maxActiveReceivers` policy; add tests for duplicate receiver and slot release.

**TDD-H02 — Stale state on BLE disconnect**
1. RED: simulated disconnect leaves stale `STREAMING` visible.
2. GREEN: transition view to `HubUnavailable` and mark receiver snapshots stale.
3. REFACTOR: derive UI from one immutable state reducer; test reconnect refresh and out-of-order event.

**TDD-A01 — Permission-denied recorder**
1. RED: `StartRecording` calls native recorder without mic permission.
2. GREEN: fail with typed `PermissionDenied`, surface accessible retry action.
3. REFACTOR: share permission/use-case integration; test revocation during recording.

**TDD-S01 — Corrupted preset import**
1. RED: invalid EQ bands/schema version silently overwrite stored preset.
2. GREEN: reject invalid values, leave DB unchanged.
3. REFACTOR: versioned validation/migration module, property-based edge values.

## 4. Test case matrix — proposed IDs
| Test ID | Source IDs | Scenario | Expected result | Level |
|---|---|---|---|---|
| TC-H001 | APP-F01 | BLE permission denied / Bluetooth off | Clear state and recovery; no crash | Widget/device |
| TC-H002 | APP-F01 | Protocol version unknown | Commands blocked; upgrade guidance | Contract |
| TC-H003 | APP-F02/F03 | Empty/duplicate receiver scan | Empty view and unique stable ID list | Contract/widget |
| TC-H004 | APP-F04/F05 | Third slot or duplicate receiver | Rejected, no unauthorized command | Unit |
| TC-H005 | APP-F06/F07 | Pair/connect timeout | Pending clears; typed error appears | Contract/widget |
| TC-H006 | APP-F08/F09 | Disconnect and reconnect request | State follows ESP32 events only | Contract/device |
| TC-H007 | APP-F10/X05 | BLE lost while streaming | Receiver state stale/unknown, not falsely active | Unit/widget |
| TC-H008 | APP-F11/F12 | Malformed/unknown event | Event rejected/logged safely; no crash | Contract |
| TC-H009 | APP-X26 | One receiver loses link | Receiver-specific recovery, other state preserved | Contract/device |
| TC-H010 | APP-X06 | No volume capability | Volume UI absent/unsupported, no GATT command | Unit/widget |
| TC-A001 | APP-Y10 | Authorized local file playback | Play/pause/seek and focus behaviors | Device |
| TC-A002 | APP-X01 | App-owned EQ enabled | Preset applies and disables correctly | Device |
| TC-A003 | APP-X02/Y01 | Visualizer source withdrawn | Sampling stops and UI explains unavailable input | Unit/device |
| TC-A004 | APP-X12/Y06 | Ambient mixing + timer | Independent layers; stop at timer | Device |
| TC-A005 | APP-X13/Y02 | Mic denied, revoked mid-recording | Clear denial, safe cleanup, no silent capture | Device |
| TC-A006 | APP-X10 | Uncalibrated sound meter | “Estimate” label/no false calibrated dB claim | UAT/device |
| TC-A007 | APP-X11 | Tuner/metronome timing | Meets agreed tolerance once measured | Device |
| TC-A008 | APP-X03/SOUND-03 | Third-party-app stream | No unsupported global-volume claim | UX/negative |
| TC-A009 | APP-X14 | Headphone test startup | Conservative safe level, clear stop | Device |
| TC-P001 | APP-X15/X18 | Large text/Tamil/dark mode | No clipping; screen reader labels correct | A11y |
| TC-P002 | APP-X19 | Local data deletion | User-confirmed selected records/files removed | Storage/UAT |
| TC-P003 | APP-X17 | Log export | No raw Bluetooth identifiers, tokens, or private audio | Privacy |
| TC-P004 | APP-X20 | Background/low-power mode | Unnecessary FFT/scanning suspended | Performance |
| TC-D001 | DB-01 | Database upgrade from schema v1 | Deterministic migration, no lost presets | Storage |
| TC-R001 | RELEASE-01 | APK install/hash/signature | Trusted signed artifact, matching published checksum | Release |
| TC-U001 | SOUND-SYNC-01 | Two headphones simultaneous playback | **Bench test only**; separately note latency and compatibility | Hardware gate |

## 5. Environment, fixtures and evidence
Use seeded fake hub fixture, invalid/old/new protocol versions, a negative permission harness, synthetic local audio clips with usage rights, low-storage emulator, real Android test phones, a known-good/cheap mixed brand headphone pair and documented firmware/board versions. Record `build_sha`, APK version, Android OS/model, hub firmware, receiver firmware/model, test steps, result, measured output, log/photos and tester.

## 6. Entry/exit criteria
**Entry:** approved release scope, APIs and source versions; devices available; feature flagged supported. **Exit:** all release-blocking tests pass, critical security/privacy issues closed, no unexplained stale status, crashes or audio-recording leaks; hardware claims have real audio evidence; UAT sign-off completed. Numeric coverage threshold must be chosen and maintained, not retroactively invented.

## 7. CI pipeline gates
Format/lint/static analysis → dependency audit → unit/widget tests → storage/contract tests → integration smoke → build artifact → signing/provenance checks. Android device-lab, performance and accessibility runs may be gated per candidate/release. An automated mock pass can never promote unverified BM83 dual-stream capability into “verified.”

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
