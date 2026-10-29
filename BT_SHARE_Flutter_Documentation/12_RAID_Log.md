# RAID Log — Risks, Assumptions, Issues and Dependencies

> **Project:** BT SHARE — Android Flutter App  
> **Version:** 0.1.0 | **Created:** 2026-10-28 | **Status:** Draft for review  
> **Document owner:** Project lead / Risk owners | **Approval:** Pending product/Flutter/embedded review  
> **Evidence boundary:** Based on repository `main` reviewed 2026-10-28; this is a proposed, executable specification, **not proof of working code, firmware, hardware, or tests**.

## 1. Usage and status definitions
**RAID** = Risks (may occur), Assumptions (unproven dependencies), Issues (known gaps), Dependencies (prerequisite deliveries). This is a **seed log prepared from repository evidence**, not a live verified incident tracker. Owners are **roles**, not assigned individuals. Review at each milestone and record evidence link, disposition, due date and actual owner.

Severity: `Critical` blocks foundational capability/claim; `High` blocks scoped integration or release; `Medium` affects UX/quality; `Low` minor. State: `Open`, `Mitigating`, `Validated`, `Closed`, `Accepted risk`. Initially all open unless clearly identified as a documented decision, not a solved engineering item.

## 2. Risks
| ID | Risk | Probability/impact (qualitative) | Trigger / early signal | Mitigation / contingency | Owner | State |
|---|---|---|---|---|---|---|
| R-01 | BM83 AT Dual Link cannot deliver two independent concurrent audio streams | Unknown / Critical | Manufacturer docs/bench disprove G4 | Stop dual-stream claims; revise architecture with new ADR and gate | Embedded | Open |
| R-02 | Mixed-brand receiver latency creates audible echo | High/High | Playback timing differs | Measure separately, publish limits; avoid sync guarantee | Embedded/QA | Open |
| R-03 | Android forbids requested arbitrary per-app volume/capture | High/High | Feasibility spikes fail | Restrict to app-owned audio, label unsupported scope | Android | Open |
| R-04 | BLE API drift between teams | High/High | UUID/state schema mismatches | Joint contract version, fixtures, CI protocol tests | Embedded/Flutter | Open |
| R-05 | Mic/recording violates privacy expectations | Medium/High | Hidden permission/background capture | Just-in-time consent, recording indicators, redacted logs | Privacy/Flutter | Open |
| R-06 | OS audio focus or background policies interrupt sound tools | High/Medium | Music stops or unauthorized service | Device matrix and compliant media lifecycle | Android | Open |
| R-07 | Feature scope too broad for an initial release | High/High | Many incomplete surfaces | Freeze MVP and phase advanced/future work | Product | Open |
| R-08 | Local media URI invalidated, recording/export lost | Medium/High | Files moved, access revoked | Persist appropriate grants, recovery, file tests | Data lead | Open |
| R-09 | Unsafe/unverified firmware update harms hub | Unknown/Critical | OTA attempted without recovery | Keep APP-X25 future/disabled until independent firmware safety review | Embedded | Open |
| R-10 | APK signing key compromise or unverified distribution | Medium/Critical | Suspect artifact/signer | CI signing controls, signer/hash verification, revocation runbook | Release/security | Open |
| R-11 | Low-end devices overheat or drain battery with FFT/mixer | Medium/Medium | High CPU/battery in trial | Bounded buffers, pause offscreen, low-power settings | Audio/QA | Open |
| R-12 | External commercial Bluetooth-input and 3+ promise becomes conflated with college build | High/High | Public claims exceed prototype | Separate variant requirements and approval | Product/embedded | Open |
| R-13 | Audio testing creates excessive output levels | Medium/High | High tone/test volume | Conservative defaults and visible stop/mute controls | QA/audio | Open |
| R-14 | Hearing assistance mistaken for medical device function | Medium/High | Unsupported health claim | Plain disclaimers, review intended use and safety | Product/privacy | Open |

## 3. Assumptions requiring validation
| ID | Assumption | Validation method | Owner | State |
|---|---|---|---|---|
| A-01 | Team can obtain at least two different real Android devices for testing | Device inventory approval | QA | Open |
| A-02 | Target Android versions support chosen BLE/media plugins | Platform spike | Android | Open |
| A-03 | Required firmware can expose stable receiver IDs and state events | Embedded command/evidence matrix | Embedded | Open |
| A-04 | Standalone audio tools can operate offline with approved licensed assets | Offline test and rights register | Product/audio | Open |
| A-05 | Local-only data meets first-release product needs | User research and privacy review | Product | Open |
| A-06 | Website release center can validate signing/hash and securely host downloads | Website backend security proof | Release | Open |
| A-07 | User expects English and Tamil interface | Localization acceptance and human translation review | Product/UX | Open |
| A-08 | No app-owned AUX audio feed available over BLE | Validate against final hardware/protocol architecture | Embedded | Open |

## 4. Issues / known specification gaps
| ID | Issue (confirmed documentation gap, not claimed runtime defect) | Impact | Next action | Owner | State |
|---|---|---|---|---|---|
| I-01 | Current `PROJECT_STATUS.md` dated 2026-10-15, later web docs dated 2026-10-27 | High | Reconcile current physical/code work and update status | Product | Open |
| I-02 | Repository `main` contains planning docs but no Flutter/ESP32/KiCad implementation tree | High | Locate authoritative native artifacts and commits | Leads | Open |
| I-03 | BLE UUIDs/transport/security not frozen | High | Joint API Spec sign-off | Embedded/Flutter | Open |
| I-04 | Minimum Android SDK and device matrix unspecified | High | Research/scope supported devices | Android/QA | Open |
| I-05 | Current MVP features and prioritization unspecified | High | PRD approval | Product | Open |
| I-06 | Native DSP/audio engine not selected | Medium | Benchmark options | Audio lead | Open |
| I-07 | Data retention, backup and encryption undecided | Medium | Privacy/security review | Data/privacy | Open |
| I-08 | Official BM83 AT firmware dual-stream proof not attached | Critical | Manufacturer matrix + G4 bench evidence | Embedded | Open |
| I-09 | Exact target hardware commercial architecture unapproved | High | Separate V1.1 research and ADR | Product/embedded | Open |
| I-10 | No signed APK/build/test evidence linked | High | Establish CI/release procedure | Release/QA | Open |

## 5. Dependencies
| ID | Dependent deliverable | Required prerequisite | Provider / consumer | Gate |
|---|---|---|---|---|
| D-01 | Hub control build | Versioned command/event/capability GATT contract | Embedded → Flutter | M4 |
| D-02 | Hardware listening demonstration | BM83 source mode + G3/G4 physical audio proof | Embedded → Product/QA | G3/G4 |
| D-03 | Flutter standalone audio release | Android library/device feasibility, licensed assets | Android/audio → Flutter | M1/M3 |
| D-04 | Local data release | Storage ADR, migrations, privacy rules | Product/data → Flutter | M2/M6 |
| D-05 | UI implementation | Approved navigation, visual language, bilingual glossary | Product/UX → Flutter | M2 |
| D-06 | APK publication | Signing, CI, website publish/approval interface | Flutter/release → Website | M7 |
| D-07 | Sync feature | Validated reference signal/capture/clock and measured uncertainty | Hardware/QA → Product | Future |
| D-08 | Firmware update feature | Secure updater, recovery, authorized integrity validation | Embedded → Flutter | Future |

## 6. Review cadence and controls
At each milestone review `new/changed risks`, `due assumptions`, `open blockers`, `dependency status`; assign actual individuals and evidence URLs. A risk is not closed merely because code or a planning document exists. Critical issues require an explicit stop/go decision and no misleading public claims. If BM83 capability fails, product owner must approve redesign or narrowed prototype scope.

## Source references and document control

- [overview](../README.md)
- [status](../PROJECT_STATUS.md)
- [requirements](../REQUIREMENTS.md)
- [decisions](../DECISIONS.md)
- [brd](../First_Documents/MD/BT_SHARE_BRD.md)
- [plan](../First_Documents/MD/BT_SHARE_Execution_Plan.md)
- [catalogue](../FeaturE_Scope_Documentations/mobile-app/FEATURE_CATALOGUE.md)
- [x25](../FeaturE_Scope_Documentations/mobile-app/FEATURE_EXPANSION_25.md)
- [y17](../FeaturE_Scope_Documentations/mobile-app/FEATURE_EXPANSION_17.md)
- [feasibility](../FeaturE_Scope_Documentations/mobile-app/FEASIBILITY_REGISTER.md)
- [product](../FeaturE_Scope_Documentations/mobile-app/PRODUCT_SCOPE.md)

**Change control:** Before implementation, confirm current source commit, product scope, prototype firmware capabilities, Android device matrix, ownership and acceptance criteria. Revisions must log approver, date and affected requirement IDs. The existing repository baseline remains authoritative for recorded historical decisions; this new pack does not silently supersede it.
