# BT SHARE Android — Feasibility Questions

**Date:** 2026-10-14  
**Status:** Unverified questions, **not** implementation blockers confirmed by testing.

| Scope | Question requiring research/test | Evidence needed before promising behavior |
| --- | --- | --- |
| Equalizers & Sound Enhancers | Can the desired EQ apply to the app's own playback, Bluetooth output, or third-party audio on target Android versions? | Scoped APIs, permission evaluation, device tests |
| Audio Routing & Mixing | Which input/output routing and capture scenarios are actually available without privileged OS control? | Android API/permissions matrix and demonstration |
| Per-App Volume Control | Can independent volume be controlled for unrelated third-party apps, or only for app-owned streams? | Supported OS/API paths and real-device validation |
| Sound Measuring & Analysis | What precision/calibration is achievable with phone microphones? | Device testing and measurement limitations |
| Tuners & Metronomes | What pitch/tempo accuracy is achievable across supported devices? | Microphone and timing tests |
| Ambient & Focus Sounds | Which licensed sounds and playback rules will be specified? | Content/licensing plan and functional acceptance criteria |
| Hearing Assistance | What microphone-to-output latency and safety limitations apply? | Permission/routing tests, clearly defined intended-use boundary |
| Multi-device synchronization | Which receiver/device combinations can be synchronized, and to what measurable tolerance? | Timing measurements and actual device-pair tests |
| Hardware control | Does the intended BM83 firmware support the approved dual-device operations, exposed through ESP32 BLE? | Firmware evidence, serial logs and frozen GATT contract |

No claim of system-wide Android capability, guaranteed low latency or medical-grade hearing functionality should be made until supported by evidence.

## Expanded-feature feasibility gates (APP-X01–APP-X26)

| Feature IDs | Key dependency to research/test before implementation approval |
| --- | --- |
| APP-X01 / X03 / X04 / X21 | EQ path scope, output/device compatibility, Android effects APIs, preset portability and versioned import validation |
| APP-X02 / X22 | Which input stream can legally/technically be visualized; audio-capture restrictions, FFT performance and animation energy use |
| APP-X05 / X07 / X08 / X26 | Actual ESP32/BM83 statuses, saved pairing data, reconnect policy ownership and available connection diagnostics |
| APP-X06 | Whether BM83 + receiver firmware supports per-sink absolute/relative volume control and a meaningful master gain |
| APP-X09 | Real timing/latency measurement method and achievable results; diagnosis must not imply automatic sync correction |
| APP-X10 / X11 | Microphone permission, calibration/accuracy limitations, input latency and stable tuner/metronome timing |
| APP-X12 / X13 | Sound content rights, background audio, recording consent, local file management and data retention |
| APP-X14 | Safe default levels and supported device-routing scenarios for test sounds |
| APP-X15 / X16 / X18 / X20 | Android adaptive layouts, locale/RTL needs, accessibility, widgets/Quick Settings constraints and power testing |
| APP-X17 / X19 | Diagnostic log availability, minimization/consent, local deletion and safe export |
| APP-X23 | Android background/task restrictions, scheduling reliability and explicit user rule approvals |
| APP-X24 | Truthful separation of available device evidence vs generic guided checks |
| APP-X25 | Existence of a safe firmware-update transport, authentication/integrity, fail-safe recovery and hardware approval |

**No new feasibility test has been run by merely selecting these features.** Every item remains in planned scope until verified on an agreed Android target-device matrix and, where applicable, BM83/ESP32 hardware.


## Audio workspace expansion — new feasibility questions (APP-Y01–APP-Y17)

| IDs | Question / required evidence | Status |
| --- | --- | --- |
| APP-Y01 | Which visualizer inputs are app-owned or permitted? Could hardware-mode AUX spectrum data be obtained from a **new verified telemetry path**? No AUX samples are available merely by connecting over BLE. | Unverified |
| APP-Y02 | Mic permission, pause/resume reliability, nondestructive trim/editing, A/B playback, export codec compatibility and local storage/consent policy. | Unverified |
| APP-Y03 | Rhythm sequencer/metronome timing under audio focus, sample asset licensing, beat-loop timing and latency. | Unverified |
| APP-Y04 | Identify permitted input sources, app-owned stream mixing, Android capture restrictions, metering and clipping behavior. | Unverified |
| APP-Y05 | Offline practice session persistence, timer lifecycle behavior and personal activity data privacy. | Unverified |
| APP-Y06 | Layered playback, license rights, sleep/fade/background audio behavior and power consumption. | Unverified |
| APP-Y07 | Product-level BLE field inventory; signal/diagnostic telemetry availability; saved paired devices; distinguish in-app alias from hardware Bluetooth name. | Unverified |
| APP-Y08 | Preset schema compatibility, allowed application EQ paths, saved device associations and **no presumed DSP influence on external AUX hardware audio**. | Unverified |
| APP-Y09 | Acoustic sync measurement test rig, reference clocks, data capture, telemetry and uncertainty. Do not infer measured acoustic delay from BLE connection events. | Unverified |
| APP-Y10 | Android user-granted audio file access, codecs, playlists, audio focus/routing; local phone audio is not automatically the external hardware AUX source. | Unverified |
| APP-Y11 | Imported sound-file formats, concurrency/overlap, storage, looping response time and playback routing. | Unverified |
| APP-Y12 | Customizable home layout, accessibility, compact views, device-size adaptation and persistence. | Unverified |
| APP-Y13 | Rule-based vs optional AI assistant, knowledge boundaries, data processing consent, network needs and accuracy disclaimers. | Future validation |
| APP-Y14 | Spectrum history retention, microphone calibration limitations, storage/export and comparability across phones. | Future validation |
| APP-Y15 | Saved receiver-group persistence, currently supported maximum two active BM83 links, and future hardware/protocol gates for larger groups. | Future validation |
| APP-Y16 | Listening reminders/duration estimation, unclear actual acoustic ear-level output, safety wording and no medical claims. | Future validation |
| APP-Y17 | Offline-first local data strategy, permissions, optional backups, capacity limits and behavior without network/account. | Future validation |

**Selection does not prove viability.** Prior APP-X dependencies still apply. This register is not evidence of a failed test or completed test.
