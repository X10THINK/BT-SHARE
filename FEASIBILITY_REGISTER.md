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
