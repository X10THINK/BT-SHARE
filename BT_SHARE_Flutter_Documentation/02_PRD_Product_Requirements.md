# PRD — Product Requirements Document

> **Project:** BT SHARE — Android Flutter App  
> **Version:** 0.1.0 | **Created:** 2026-10-28 | **Status:** Draft for review  
> **Document owner:** Product owner / Flutter lead | **Approval:** Pending product/Flutter/embedded review  
> **Evidence boundary:** Based on repository `main` reviewed 2026-10-28; this is a proposed, executable specification, **not proof of working code, firmware, hardware, or tests**.

## 1. Product definition
**Working product:** BT SHARE for Android (Flutter/Dart). Two independent experiences: (A) hub-connected control of the BM83/ESP32 prototype and (B) standalone phone-owned sound workspace. First app distribution is not yet approved; the planned product website describes an official APK download center. No cloud login is required by present product decisions.

## 2. Audience, jobs and journeys
| Persona | Primary job | Success / failure behavior |
|---|---|---|
| Hub owner | Select/operate supported receivers | Can see states, recover from lost link and distinguish hub unavailable from headphones unavailable |
| Music listener | Listen to local files and customize permitted output | Can import/select file, play, pause, use supported EQ and retain presets offline |
| Creator / musician | Record, tune, practice and compose | Can create an authorized recording and reuse locally saved routines |
| Accessibility-first user | Use tools confidently | Scalable text, screen reader status, accessible controls and Tamil/English labels once reviewed |

**Journey H1 — hub:** Open → Connect → request Android BLE permission → discover hub → connect → display actual hub readiness → request receiver scan → select 1/2 → pair/connect → display actual states → error/retry → disconnect. The app never performs receiver A2DP pairing itself in this design.

**Journey S1 — standalone:** Launch offline → no account/hub prompt required → select Sound Lab / Studio / Practice → handle microphone/media permission only at first relevant action → perform task → save/export local result → reopen later.

## 3. Product information architecture — proposal pending UX approval
1. **Connect:** hubs, devices, receiver slots and truthful diagnostics.
2. **Sound Lab:** permitted EQ, balance, visualization, analysis.
3. **Studio:** local player, recorder, ambient mixer, optional soundboard.
4. **Practice:** tuner, metronome, rhythm studio, practice sessions.
5. **My Sound:** presets, saved sessions, favorites, privacy and appearance.
See [UI/UX Spec](08_UI_UX_Specification.md); these are candidate destinations, not final screens.

## 4. Release scope — recommended phasing, not a previously approved commitment
| Group | Proposed minimum behavior | Release gate |
|---|---|---|
| Foundation standalone | Navigation, settings/theme, local file playback, accessible controls, local presets, privacy/permission handling | Local test without hardware/internet |
| Core sound | EQ on app-owned playback, basic visualizer of permitted source, licensed ambient mixer, tuner/metronome and recorder if validated | Native Android feasibility and device tests |
| Hub control | BLE hub connect, actual device discovery and two-slot operation, structured states/errors, recovery UI | Verified firmware and versioned BLE API; ideally physical G3/G4 evidence before claims |
| Later tools | Drum practice, advanced mixer, soundboard, health diagnostics, optional widgets | Each separately scoped and accepted |
| Future research | AI helper, multi-listener groups, sync diagnostics/correction, firmware update, advanced cross-app controls | No implied initial release promise |

## 5. Consolidated feature catalogue
The 25 additional concepts are planning inclusions; the 26th is a highlighted recovery feature. “Current scope” is not “implemented”.
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

### Audio-workspace additions and mapping
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

### Existing hub and sound categories
See [SRS](05_SRS_Software_Requirements_Specification.md) for the complete APP-F01–F12 and SOUND-01–07 requirement tables; those **remain in scope even where APP-X/APP-Y overlap**.

## 6. Key product interaction rules
- Show hub-free experience without upsell/blocked onboarding; clearly identify “Requires BT SHARE hub” actions.
- Pairing, connected and streaming are separate states; avoid green “Playing” on a mere connection event.
- No generic “low-latency sync” promise: actual cross-brand earbud delays may differ and must be measured externally.
- Per-device hardware volume appears only behind a verified capability flag; normal Android media volume is not equivalent.
- Any visualizer or EQ must identify its **audio source**; live AUX visualizer is not supported merely through BLE control.
- Use explicit consent for recording, clearly explain source and retention, and make local erase work reliably.
- Background audio playback should use compliant Android media lifecycle/focus controls; no guarantee of background microphone capture without validated requirements.

## 7. Feature acceptance examples
| Feature | Release acceptance example | Blocking prerequisite |
|---|---|---|
| APP-F01/F10 | Hub connection loss shows “Disconnected” and receiver status becomes unknown/stale rather than silently “Connected” | Firmware event contract |
| APP-F02/F03 | Empty scan shows “No receivers found” and retry; duplicates use stable identifiers | BM83 discovery availability |
| APP-X01/APP-Y10 | Local supported audio plays; EQ change audibly affects only the supported app-owned path; disabling returns original processing | Playback/codec matrix |
| APP-X12/APP-Y06 | Two approved ambient tracks play/mix offline; sleep timer stops playback | Asset licensing and background audio test |
| APP-X13 | Rejecting microphone permission does not crash; recording is blocked with explanation | Android permissions |
| APP-X26 | Receiver-specific disconnect error does not falsely clear second receiver; status is from ESP32 | Firmware recovery policy |

## 8. Edge cases and unsupported scenarios
BLE turned off; permissions denied permanently; hub drops connection mid-operation; app process restarted; receiver unknown; two slots full; user tries unsupported independent volume; audio focus taken by call; media file revoked/deleted; low disk space; microphone denied; no network; device language changes; theme and reduced-motion settings; mismatched protocol version; firmware reports unsupported capabilities.

## 9. Analytics and privacy policy
**No analytics service is selected.** If analytics is later approved, collect aggregate non-sensitive usage only under a privacy review; do not upload raw microphone input, user audio files, Bluetooth identities or diagnostic secrets by default. Local operational logs are separate from telemetry.

## 10. Product open decisions
- MVP feature subset, Android min/target SDK, supported phones, app brand assets and final navigation.
- Bluetooth-input commercial hardware variant and 3+ receivers require separate hardware feasibility work.
- Whether standalone audio playback can ever be fed to an external hub is not part of the current phone↔hub BLE control contract.
- User research, pricing, app store vs direct APK distribution, optional cloud, accessibility/localization signoff and release acceptance thresholds remain unresolved.

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
