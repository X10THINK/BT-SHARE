# SRS — Software Requirements Specification

> **Project:** BT SHARE — Android Flutter App  
> **Version:** 0.1.0 | **Created:** 2026-10-28 | **Status:** Draft for review  
> **Document owner:** Flutter mobile team | **Approval:** Pending product/Flutter/embedded review  
> **Evidence boundary:** Based on repository `main` reviewed 2026-10-28; this is a proposed, executable specification, **not proof of working code, firmware, hardware, or tests**.

## 1. Purpose, scope and normative language
This SRS defines testable app obligations. **SHALL** is an obligation *once the specified feature is in a signed release scope and its dependency passes the technical gate*. **MAY** is optional. Product scope selection does not mean feature is feasible, approved for MVP, implemented or validated. Original IDs from the repository are preserved for traceability.

## 2. Actor and system boundaries
- **User:** initiates consent, permissions, local playback, tools and hub commands.
- **Flutter client:** renders state; stores permitted local settings/media references; communicates over GATT to hub.
- **Android:** controls audio focus, microphone permission, file access and supported Bluetooth APIs.
- **ESP32:** authoritative hub status, receiver discovery/commands, retry policy and UART translation.
- **BM83/receivers:** external AUX audio transfer, outside Flutter's audio path.

## 3. Functional requirements — hardware-control baseline
The table below preserves original `APP-F01–APP-F12` descriptions. Actual command implementations require a frozen ESP32/Flutter protocol.
| ID | Requirement | Acceptance statement |
|---|---|---|
| APP-F01 | Connect to BT SHARE hub | Connect/disconnect BLE hub; show readiness and disconnection reasons |
| APP-F02 | Start receiver scan | Request a receiver discovery scan through ESP32, not phone A2DP APIs |
| APP-F03 | Display discovered receivers | List hub-reported name, opaque ID, and accurate state |
| APP-F04 | Select Receiver 1 | Assign selected receiver to first hardware slot |
| APP-F05 | Select Receiver 2 | Assign second slot and reject third active selection on prototype |
| APP-F06 | Pair receiver | Request pairing; show pending, success, and failure |
| APP-F07 | Connect receiver | Request connection and reflect verified hub state |
| APP-F08 | Disconnect receiver | Request disconnect without inventing resulting state |
| APP-F09 | Reconnect receiver | Request reconnect only when eligible and supported |
| APP-F10 | View connection/streaming status | Distinguish paired, connected and streaming |
| APP-F11 | View structured errors | Map protocol, timeout, maximum-links and connection failures |
| APP-F12 | Development logs | Optional redacted debug view; disable in production by default |

### Normative hub behavior
- **SRS-H01 (APP-F01):** When Bluetooth is off or required permission is denied, the app SHALL explain the condition and offer an appropriate retry/settings path without crashing.
- **SRS-H02 (APP-F02/F03):** When the hub confirms an empty scan, display an empty result with retry, distinct from a BLE connection failure. De-duplicate by hub-provided opaque ID.
- **SRS-H03 (APP-F04/F05):** Current prototype SHALL reject assigning more than two active receiver slots and SHALL prevent the same receiver occupying both slots. This is a *prototype UI gate*, not a claim of BM83 performance.
- **SRS-H04 (APP-F06..F09):** Each command SHALL expose pending, success, failure and timeout based on the firmware result; only ESP32-reported state makes it confirmed.
- **SRS-H05 (APP-F10):** A BLE-connected hub is not proof of an active receiver or streaming audio. Show `unknown` or `stale` after hub disconnect until fresh snapshot.
- **SRS-H06 (APP-F11/F12):** Errors SHALL be actionable and logs minimized/redacted; debug console SHALL NOT be required to use the product.
- **SRS-H07 (APP-X26):** Flutter SHALL display receiver-specific recovery outcomes but SHALL NOT override the ESP32 recovery algorithm with independent hidden retries.
- **SRS-H08:** The UI SHALL disable unsupported hardware commands after capability negotiation; unsupported feature must not silently emit a guessed BM83 command.

## 4. Functional requirements — standalone categories
| ID | Category / goal | Boundary |
|---|---|---|
| SOUND-01 | Equalizers and Sound Enhancers | App-owned/allowed audio processing only |
| SOUND-02 | Audio Routing and Mixing | Permitted app-owned/microphone routes only; investigate any wider claim |
| SOUND-03 | Per-App Volume Control | Arbitrary third-party-app volume control not assured on Android |
| SOUND-04 | Sound Measuring and Analysis | Mic calibration and capture rights |
| SOUND-05 | Tuners and Metronomes | Pitch and timing accuracy on real devices |
| SOUND-06 | Ambient and Focus Sounds | Licensed assets, timer/background playback |
| SOUND-07 | Hearing Assistance | Latency, device compatibility and no medical claims |
| SOUND-SYNC-01 | Cross-device sound synchronization | Unverified goal; diagnostics ≠ correction |

### Normative standalone behavior
- **SRS-A01:** App SHALL provide launch/navigation to its enabled standalone features without BLE hub, account or Internet.
- **SRS-A02:** Local player SHALL accept user-authorized media references, report unsupported files and manage pause/resume/audio focus.
- **SRS-A03:** EQ SHALL indicate the supported input/output context and only apply to app-controlled processing paths.
- **SRS-A04:** Visualizers SHALL describe and respect actual audio input; no hidden mic capture and no assumed access to external AUX.
- **SRS-A05:** Microphone features SHALL obtain permission at use, stop on user request and protect partial recording files after interruption.
- **SRS-A06:** Time-based features (sleep timer, metronome, practice timer) SHALL define background behavior and persist only supported state.
- **SRS-A07:** Profiles/favorites SHALL save locally with input validation and withstand app process restart.
- **SRS-A08:** SOUND-03 arbitrary per-app volume control and SOUND-07 hearing assistance SHALL NOT be shipped with unsupported/medical-grade claims.
- **SRS-A09:** Sound test generator SHALL use conservative startup levels and clear warnings; no safety/accuracy claims without measured evidence.
- **SRS-A10:** A feature that depends on media or mic permissions SHALL still offer a functioning hub-free remainder of the app when permission is denied.

## 5. Feature-to-requirement register: additional 26 concepts
For each selected release feature the Flutter team SHALL define at least one scenario for happy path, unsupported/denied path, persistence (if any), accessibility and lifecycle behavior. Future features remain in the backlog until explicitly scheduled.
| ID | Feature | Intended behavior | Status / gate |
|---|---|---|---|
| APP-X01 | Smart equalizer and sound profiles | 5/10-band EQ and presets on permitted paths | Core candidate |
| APP-X02 | Live audio visualizer | Bars/waves/circle from allowed source | Current scope |
| APP-X03 | Bass, treble and stereo controls | Balance/mono and source-specific adjustments | Current scope |
| APP-X04 | Automatic sound profiles | User-approved context/device associations | Current scope |
| APP-X05 | Dual-device connection dashboard | Two receiver cards with actual status | Core candidate |
| APP-X06 | Per-device volume controls | A/B controls only if firmware and sinks support | Feasibility gated |
| APP-X07 | One-tap pairing and reconnection | Known device flow mediated by hub | Core candidate |
| APP-X08 | Connection health monitor | Actual states, retries and supplied counters only | Current scope |
| APP-X09 | Audio synchronization diagnostics | Measured acoustic comparison only with verified rig | Feasibility gated |
| APP-X10 | Sound level meter | Estimated microphone sound level; no precision claim | Current scope |
| APP-X11 | Instrument tuner and metronome | Pitch detection, time signatures and tap tempo | Current scope |
| APP-X12 | Ambient sounds and focus mixer | Licensed loops, mix and sleep timer | Current scope |
| APP-X13 | Voice recorder and audio notes | User-consented mic recordings and bookmarks | Current scope |
| APP-X14 | Speaker and headphone test suite | Safe channel/tone/sweep tests | Current scope |
| APP-X15 | Dynamic themes and dashboard | Light/dark/accent/responsive UI | Current scope |
| APP-X16 | Quick controls and favorites | Pinned tools/presets; widgets OS-gated | Current scope |
| APP-X17 | Session history and diagnostics | Local history and redacted export | Current scope |
| APP-X18 | Accessibility and multilingual support | Screen readers, scaling, English/Tamil | Current scope |
| APP-X19 | Privacy-first settings | Just-in-time permissions and erase/export | Current scope |
| APP-X20 | Battery and performance mode | Reduced animation, scanning and background work | Current scope |
| APP-X21 | Importable sound profiles | Versioned JSON import/export | Future candidate |
| APP-X22 | Advanced audio analyzer | FFT and level histories from permitted input | Future candidate |
| APP-X23 | Smart automation rules | Explicit user-approved and OS-supported rules | Future candidate |
| APP-X24 | Guided troubleshooting assistant | Guided help based on available evidence | Future candidate |
| APP-X25 | Firmware update and recovery tools | Only with authenticated fail-safe firmware update | Future candidate |
| APP-X26 | Smart Connection Recovery | ESP32-owned reconnect policy; app reports outcome | Integration gated |

## 6. Expansion and future mappings
An “Expansion” adds requirements to an existing feature; it is not counted as unrelated new software. All five `APP-Y13..17` remain roadmap items.
| ID | Feature | Type | Existing mapping | Phase |
|---|---|---|---|---|
| APP-Y01 | Live Audio Visualizer Studio | Expansion | APP-X02/APP-X22 | Current candidate |
| APP-Y02 | Voice Recorder and Audio Lab | Expansion | APP-X13 | Current candidate |
| APP-Y03 | Rhythm and Drum Studio | New family | SOUND-05/APP-X11 | Later candidate |
| APP-Y04 | Mini Audio Mixer | Expansion | SOUND-02/APP-X03 | Feasibility gated |
| APP-Y05 | Smart Practice Room | New family | SOUND-05/APP-X11 | Later candidate |
| APP-Y06 | Ambient Sound Mixer | Expansion | SOUND-06/APP-X12 | Current candidate |
| APP-Y07 | BT SHARE Device Control Center | Expansion | APP-F01..F12/APP-X05 | Hardware gated |
| APP-Y08 | Personal Audio Profiles | Expansion | APP-X01/APP-X04 | Current candidate |
| APP-Y09 | Audio Sync and Diagnostics Lab | Expansion | APP-X09/SOUND-SYNC-01 | Research gated |
| APP-Y10 | Local Audio Player | New family | APP-X01/SOUND-01 | Core candidate |
| APP-Y11 | Custom Soundboard | New family | SOUND-02 | Later candidate |
| APP-Y12 | Customizable Sound Dashboard | New family | APP-X15/APP-X16 | Current candidate |
| APP-Y13 | AI Sound Assistant | Future | APP-X24 | Future |
| APP-Y14 | Audio Spectrum History | Future | APP-X22/APP-X17 | Future |
| APP-Y15 | Multi-Listener Session Manager | Future | APP-F04/APP-F05 | Future; hardware gated |
| APP-Y16 | Safe Listening Tools | Future | SOUND-07 | Future |
| APP-Y17 | Offline-First Experience | Future quality attribute | APP-X19 | Future |

## 7. Selected detailed acceptance rules by area
| SRS ID | Linked source ID | Testable acceptance criterion | Gate |
|---|---|---|---|
| SRS-EQ-01 | APP-X01 | For app-owned track on supported route, enabling a saved preset changes the specified DSP parameters and survives restart | Audio engine verified |
| SRS-EQ-02 | APP-X03 | Balance/mono option never claims to alter unrelated third-party streams or external AUX | Route limitations documented |
| SRS-VIZ-01 | APP-X02/Y01 | Visualizer ceases sampling when dismissed/paused and indicates its actual input | Mic/capture rights tested |
| SRS-HUB-01 | APP-X05/Y07 | Both cards accurately represent hub-provided slot/name/state, or show stale/unknown | Frozen firmware state mapping |
| SRS-VOL-01 | APP-X06 | Independent volume controls are absent/disabled if verified hardware flag missing | BM83/ESP32 capability evidence |
| SRS-SYNC-01 | APP-X09/Y09 | If shown, any numerical delay has rig/method, units, uncertainty and test log; BLE status alone yields no latency estimate | Acoustic test design |
| SRS-REC-01 | APP-X13/Y02 | Denied mic permission yields clear message; no recording starts; user can reattempt later | Android device test |
| SRS-AMB-01 | APP-X12/Y06 | Two licensed ambient layers can play with independent levels; configured sleep timer stops them | Licensed assets, background test |
| SRS-PLY-01 | APP-Y10 | App lists/selects authorized local file, displays metadata, plays/pauses/seeks and gracefully handles revoked URI | File/codec tests |
| SRS-PRA-01 | APP-X11/Y03/Y05 | Tuner and practice timer handle pause/resume; measured timing error meets approved device-specific tolerance | Accuracy threshold TBD |
| SRS-PRO-01 | APP-X04/Y08 | App will not auto-switch EQ unless user consented; routing applicability is explicit | Capability check |
| SRS-LOC-01 | APP-X18 | English/Tamil strings are reviewed; screen readers announce connection state without reliance on color | Locale/a11y review |
| SRS-PRIV-01 | APP-X19 | Clear-local-data option removes selected local metadata/recordings per explicit scope; explains irreversible deletion | Privacy signoff |
| SRS-PERF-01 | APP-X20 | Reduced-motion/power mode pauses unnecessary animation/FFT and prevents uncontrolled scanning | Device perf test |
| SRS-FUT-01 | APP-X25 | OTA UI cannot appear unless authenticated update path, integrity and recovery are independently verified | Future only |

## 8. Non-functional requirements (release-blocking where scoped)
| ID | Requirement | Verification |
|---|---|---|
| SRS-N01 | No unauthorized background recording or raw audio upload | Permission/log/network inspection |
| SRS-N02 | A user can exit all live mic/audio activities | Lifecycle and stop controls tests |
| SRS-N03 | Wrong/missing/stale BLE values do not become definitive UI claims | Fake protocol and reconnect tests |
| SRS-N04 | Local data migrations are loss-minimizing and fail safely | Migration suite |
| SRS-N05 | Resilient to permission denial, Bluetooth off, empty scan, corrupted preset and low disk | Negative test suite |
| SRS-N06 | Flutter analysis/static checks and automated tests pass | CI |
| SRS-N07 | Target-device accessibility, localization and battery/latency budgets pass once frozen | Device matrix |
| SRS-N08 | Signed release artifact, provenance, SHA-256 and rollback metadata | Release verification |
| SRS-N09 | User data retention/deletion and recording export follow reviewed privacy policy | Privacy UAT |

## 9. Requirement statuses and governance
Each requirement must have `source_id`, `priority`, `owner`, `dependency`, `release`, `implementation_state` (planned/in-progress/implemented), `test_id`, `test_result` and `approval`. **Default state for all app functionality is planned/unverified** in this pack. No test result is fabricated.

## 10. Traceability / cross-doc rules
- Business rationale → [BRD](01_BRD_Business_Requirements.md); user value and release priority → [PRD](02_PRD_Product_Requirements.md).
- Design and technologies → [TRD](03_TRD_Technical_Requirements.md), [SDD](04_SDD_Software_Design.md).
- BLE operations → [API](09_API_Specification.md); persistence → [DB](10_DB_Design.md).
- Verification → [TDD](07_TDD_Test_Plan.md) and [UAT](13_UAT_Plan.md).
- All `APP-F` dependencies must cite the **versioned firmware capability/command contract** at approval time.

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
