# BT SHARE — 25 Selected Mobile App Features

**Date:** 2026-10-14  
**Platform:** Flutter/Dart, Android first  
**Decision:** All 25 feature concepts requested for inclusion in the mobile product plan.  
**Implementation:** Not yet built or independently verified.  
**Cross-team approval:** Required before changing hardware/firmware interfaces.

## Scope and acceptance interpretation

- All 25 entries are included in the **planned product scope**. The five features originally grouped under "advanced / future versions" remain future-version candidates, not first-release delivery commitments.
- This is a product feature register, **not** a promise that the listed behavior is possible on every Android device, output route, third-party app or BM83 hardware revision.
- Existing seven standalone sound-utility categories (including Audio Routing & Mixing, Per-App Volume Control, and Hearing Assistance) **remain** in the scope. Some of those categories are broader than these 25 specific feature concepts.
- The original BM83/ESP32 hardware two-receiver proof, UART/GATT control contract, procurement ceiling and test gates remain unchanged.
- Multi-device synchronization is a separate product goal (`SOUND-SYNC-01`); synchronization diagnostics `APP-X09` do not themselves prove the goal.
- **Smart Connection Recovery** appears separately below as `APP-X26` because it was highlighted outside the numbered 25 features. It is not accidentally counted as one of the 25.

## Feature register

| ID | Feature | Area | User access / dependency | Original phase |
| --- | --- | --- | --- | --- |
| APP-X01 | Smart equalizer and sound profiles | Premium sound experience | Standalone with supported audio routes | Core candidate; explicitly high priority |
| APP-X02 | Live audio visualizer | Premium sound experience | Standalone; audio-capture-dependent | Current scope |
| APP-X03 | Bass, treble and stereo controls | Premium sound experience | Standalone; processing-path-dependent | Current scope |
| APP-X04 | Automatic sound profiles | Premium sound experience | Standalone; device/event support dependent | Current scope |
| APP-X05 | Dual-device connection dashboard | Bluetooth & hardware | Requires BT SHARE hub | Signature hub screen |
| APP-X06 | Per-device volume controls | Bluetooth & hardware | Requires BT SHARE hub + supported receiver control | Current scope, feasibility gated |
| APP-X07 | One-tap pairing and reconnection | Bluetooth & hardware | Requires BT SHARE hub | Current scope |
| APP-X08 | Connection health monitor | Bluetooth & hardware | Requires BT SHARE hub | Current scope |
| APP-X09 | Audio synchronization diagnostics | Bluetooth & hardware | Requires supported device timing path | Current scope, feasibility gated |
| APP-X10 | Sound level meter | Standalone sound utilities | Standalone; microphone permission | Current scope |
| APP-X11 | Instrument tuner and metronome | Standalone sound utilities | Standalone; microphone for tuner | Current scope |
| APP-X12 | Ambient sounds and focus mixer | Standalone sound utilities | Standalone | Current scope |
| APP-X13 | Voice recorder and audio notes | Standalone sound utilities | Standalone; microphone permission | Current scope |
| APP-X14 | Speaker and headphone test suite | Standalone sound utilities | Standalone for supported outputs; hub tests require hub | Current scope |
| APP-X15 | Dynamic themes and polished dashboard | App experience | Standalone | Current scope |
| APP-X16 | Quick controls and favorites | App experience | Standalone; hardware shortcuts need hub | Current scope |
| APP-X17 | Session history and diagnostics | App experience | Standalone, plus hardware event history when connected | Current scope |
| APP-X18 | Accessibility and multilingual support | App experience | Standalone | Current scope |
| APP-X19 | Privacy-first settings | App experience | Standalone | Current scope |
| APP-X20 | Battery and performance mode | App experience | Standalone | Current scope |
| APP-X21 | Importable sound profiles | Advanced / future version | Standalone | Future-version feature |
| APP-X22 | Advanced audio analyzer | Advanced / future version | Standalone; permitted input only | Future-version feature |
| APP-X23 | Smart automation rules | Advanced / future version | Standalone; hardware actions require hub | Future-version feature |
| APP-X24 | Guided troubleshooting assistant | Advanced / future version | Standalone guidance; hub context when available | Future-version feature |
| APP-X25 | Firmware update and recovery tools | Advanced / future version | Requires BT SHARE hub and documented safe update method | Future-version feature |

## Requirements and feasibility notes by feature

### APP-X01 — Smart equalizer and sound profiles

- **Selected behavior:** 5- or 10-band EQ where supported; Bass Boost/Vocal/Classical/Movie/Gaming presets; save, rename and share custom EQ presets; output-type profiles when supported.
- **Access / dependency:** Standalone with supported audio routes.
- **Feasibility or safety gate:** Confirm processing path and Android EQ capabilities.
- **Planning phase:** Core candidate; explicitly high priority.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X02 — Live audio visualizer

- **Selected behavior:** Animated frequency bars, waveforms and circular visualizer; visual styles, full-screen mode and battery-friendly settings.
- **Access / dependency:** Standalone; audio-capture-dependent.
- **Feasibility or safety gate:** Audio capture rights and supported source must be verified.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X03 — Bass, treble and stereo controls

- **Selected behavior:** Bass/treble, L/R balance, mono controls; optional loudness/clarity for audio the app can process.
- **Access / dependency:** Standalone; processing-path-dependent.
- **Feasibility or safety gate:** May not apply globally to arbitrary apps or receiver routes.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X04 — Automatic sound profiles

- **Selected behavior:** Associate profiles with devices or listening contexts; allow user-approved profile switching when supported.
- **Access / dependency:** Standalone; device/event support dependent.
- **Feasibility or safety gate:** Validate connection detection and effect applicability.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X05 — Dual-device connection dashboard

- **Selected behavior:** Show both receiver names, actual states, connect/disconnect/reconnect, recent error or last connection time when available, and truthful audio-receiving status.
- **Access / dependency:** Requires BT SHARE hub.
- **Feasibility or safety gate:** ESP32 is authoritative; streaming status and timestamps must actually be exposed.
- **Planning phase:** Signature hub screen.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X06 — Per-device volume controls

- **Selected behavior:** Receiver A and B volume adjustment, plus master volume if supported; fall back to supported volume mechanisms.
- **Access / dependency:** Requires BT SHARE hub + supported receiver control.
- **Feasibility or safety gate:** Independent control for different A2DP sinks is not yet proven on BM83/firmware.
- **Planning phase:** Current scope, feasibility gated.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X07 — One-tap pairing and reconnection

- **Selected behavior:** Known receiver identities, clear pair/connect/reconnect workflow, and actionable recovery messages.
- **Access / dependency:** Requires BT SHARE hub.
- **Feasibility or safety gate:** Device persistence and pairing/reconnect mechanisms depend on BM83/ESP32.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X08 — Connection health monitor

- **Selected behavior:** Show real connection/streaming states, recent disconnections and retries; optional measured counters if provided.
- **Access / dependency:** Requires BT SHARE hub.
- **Feasibility or safety gate:** No invented RSSI percentage, signal health score or range prediction.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X09 — Audio synchronization diagnostics

- **Selected behavior:** Provide a test mode to assess audible timing difference between receivers; explore measurements and correction only after capability review.
- **Access / dependency:** Requires supported device timing path.
- **Feasibility or safety gate:** Dual A2DP links do not guarantee synchronized playback; no zero-latency promises.
- **Planning phase:** Current scope, feasibility gated.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X10 — Sound level meter

- **Selected behavior:** Display estimated live sound level and optional measurement history.
- **Access / dependency:** Standalone; microphone permission.
- **Feasibility or safety gate:** Calibrate/label estimates; avoid professional-grade accuracy claim without evidence.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X11 — Instrument tuner and metronome

- **Selected behavior:** Pitch detection, adjustable reference pitch, tempo, time signatures, tap tempo and practice presets.
- **Access / dependency:** Standalone; microphone for tuner.
- **Feasibility or safety gate:** Timing and tuner precision need real-device testing.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X12 — Ambient sounds and focus mixer

- **Selected behavior:** Offline-capable ambient tracks such as rain/ocean/wind/fan/nature; independent mix controls and sleep timer.
- **Access / dependency:** Standalone.
- **Feasibility or safety gate:** License sound assets; validate background playback constraints.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X13 — Voice recorder and audio notes

- **Selected behavior:** Record permitted phone microphone input, organize clips and add bookmarks.
- **Access / dependency:** Standalone; microphone permission.
- **Feasibility or safety gate:** Recording permissions/consent; not arbitrary third-party audio recording.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X14 — Speaker and headphone test suite

- **Selected behavior:** Left/right channel checks, conservative-level tone and sweep generation, optional BT SHARE dual-receiver playback test.
- **Access / dependency:** Standalone for supported outputs; hub tests require hub.
- **Feasibility or safety gate:** Audio safety; do not claim laboratory precision.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X15 — Dynamic themes and polished dashboard

- **Selected behavior:** Light and dark themes, accent customization, smooth animations, clean responsive home screen.
- **Access / dependency:** Standalone.
- **Feasibility or safety gate:** Final UI design and accessibility review pending.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X16 — Quick controls and favorites

- **Selected behavior:** Pin presets, device shortcuts and tools; Android widget or Quick Settings entry when supported.
- **Access / dependency:** Standalone; hardware shortcuts need hub.
- **Feasibility or safety gate:** Evaluate launcher/OS and hardware constraints.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X17 — Session history and diagnostics

- **Selected behavior:** On-device session/error history, selected profiles and exportable diagnostic report.
- **Access / dependency:** Standalone, plus hardware event history when connected.
- **Feasibility or safety gate:** Data minimization, retention controls, real event availability.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X18 — Accessibility and multilingual support

- **Selected behavior:** Scalable type, large touch targets, screen readers, contrast-safe status, English and Tamil.
- **Access / dependency:** Standalone.
- **Feasibility or safety gate:** Test translations and accessibility on Android.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X19 — Privacy-first settings

- **Selected behavior:** Just-in-time microphone/Bluetooth permission explanations; local-first diagnostics; data-erasure controls.
- **Access / dependency:** Standalone.
- **Feasibility or safety gate:** Check Android permission/API versions; avoid unnecessary location or usage collection.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X20 — Battery and performance mode

- **Selected behavior:** Reduced visual effects, appropriate scan intervals, background work limits and visualizer pause setting.
- **Access / dependency:** Standalone.
- **Feasibility or safety gate:** Battery/performance impact must be benchmarked.
- **Planning phase:** Current scope.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X21 — Importable sound profiles

- **Selected behavior:** Export/import EQ or app-owned audio settings as versioned JSON.
- **Access / dependency:** Standalone.
- **Feasibility or safety gate:** Schema validation, compatibility and secure input handling.
- **Planning phase:** Future-version feature.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X22 — Advanced audio analyzer

- **Selected behavior:** FFT spectrum, peak-frequency display and input-level history.
- **Access / dependency:** Standalone; permitted input only.
- **Feasibility or safety gate:** Only audio app may legally capture/process; measurement resolution to verify.
- **Planning phase:** Future-version feature.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X23 — Smart automation rules

- **Selected behavior:** User-approved rules for supported profile changes and scheduled ambient playback.
- **Access / dependency:** Standalone; hardware actions require hub.
- **Feasibility or safety gate:** OS background limitations and permissions apply.
- **Planning phase:** Future-version feature.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X24 — Guided troubleshooting assistant

- **Selected behavior:** Ask guided questions, use available connection details and suggest troubleshooting steps.
- **Access / dependency:** Standalone guidance; hub context when available.
- **Feasibility or safety gate:** Do not imply access to unavailable diagnostics.
- **Planning phase:** Future-version feature.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

### APP-X25 — Firmware update and recovery tools

- **Selected behavior:** Show firmware versions, verified update progress, integrity checks and recovery instructions if supported.
- **Access / dependency:** Requires BT SHARE hub and documented safe update method.
- **Feasibility or safety gate:** No OTA/update UI promised until verified bootloader, transport, fail-safe and recovery design tested.
- **Planning phase:** Future-version feature.
- **Status:** Scope confirmed by software lead; implementation, acceptance tests and applicable APIs are not yet approved.

## Additional highlighted feature (outside the 25)

### APP-X26 — Smart Connection Recovery

- **Planned behavior:** Detect hardware-reported receiver disconnects, identify the lost receiver, follow a defined reconnect policy, preserve the other receiver's visible status and report recovery success/failure.
- **Authoritative control:** The ESP32 firmware must own reconnection policy and actual device state. Flutter is the user interface, not an independent authority for the BM83 link.
- **Status:** Selected from the highlighted proposal for product planning; embedded implementation support and acceptance criteria remain to be agreed.

## Previously confirmed categories retained

| Existing ID | Category / goal | Relationship to 25 features |
| --- | --- | --- |
| SOUND-01 | Equalizers & Sound Enhancers | Related to APP-X01, X03, X04 and X21 |
| SOUND-02 | Audio Routing & Mixing | Remains a separate, broader category; not removed |
| SOUND-03 | Per-App Volume Control | Separate from APP-X06 (per-Bluetooth-receiver volume); Android feasibility unverified |
| SOUND-04 | Sound Measuring & Analysis | Includes APP-X10 and X22 |
| SOUND-05 | Tuners & Metronomes | APP-X11 |
| SOUND-06 | Ambient & Focus Sounds | APP-X12; APP-X23 may automate supported actions later |
| SOUND-07 | Hearing Assistance | Remains a separate category; no medical-grade claims |
| SOUND-SYNC-01 | Synchronized sound across devices | Product goal; APP-X09 is a diagnostic tool, not synchronization correction |

## What is not changed

- The college hardware prototype targets **two** A2DP sink devices due to budget. Larger counts are a long-term project vision requiring separate investigation.
- The AUX audio path remains external AUX → BM83 → sinks, not phone → sinks through Flutter.
- No verified per-receiver volume API, global EQ, arbitrary per-app mixer, audio capture bypass, automatic latency correction or OTA update ability is claimed.
- A BLE interface change needs joint ESP32 and Flutter review and a versioned contract.

## Next requirements work (not yet implemented)

For each feature, freeze user actions, permissions, error and unsupported-device behavior, Android API/target-device matrix, integration owner and testable acceptance cases. Do not assign "implemented" status until runnable source and test evidence exist.
