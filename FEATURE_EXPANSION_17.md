# BT SHARE — Audio Workspace Expansion: 12 Detailed Proposals + 5 Future Concepts

**Date:** 2026-10-14  
**Status:** Included in the Android app product requirements **for planning** by the Flutter workstream lead; not verified as implementable or completed  
**Platform:** Flutter/Dart, **Android first**  
**Relation:** Extends (does not replace) `FEATURE_EXPANSION_25.md`, the seven SOUND categories, the BRD APP-F01–F12 hub functions, and `SOUND-SYNC-01`.

## How to read this register

- **APP-Y01–APP-Y12** reproduce the twelve more detailed proposals. A feature marked **Expansion** should be merged into the previously selected feature; it is **not counted as an unrelated new feature**. A **New** entry establishes a genuinely additional feature family.
- **APP-Y13–APP-Y17** reproduce the five later/future concepts. They are included in the roadmap scope, **not** committed to the first Android release.
- These IDs record requirements intent; Android permission limits, hardware command support, UX details, performance and pass/fail criteria remain open.
- The original two-receiver BM83/ESP32 college prototype, AUX audio path, hardware-first acceptance gates and LKR 40,000 ceiling remain unchanged.

## 12 selected detailed proposals

| ID | Feature | Type | Existing scope mapping | Intended rollout |
| --- | --- | --- | --- | --- |
| APP-Y01 | Live Audio Visualizer Studio | Expansion | APP-X02, APP-X22, SOUND-04 | Foundation candidate |
| APP-Y02 | Voice Recorder & Audio Lab | Expansion | APP-X13 | Foundation candidate |
| APP-Y03 | Rhythm & Drum Studio | **New** | Complements SOUND-05 / APP-X11 | Musician toolkit candidate |
| APP-Y04 | Mini Audio Mixer | Expansion | SOUND-02; related APP-X03 | Foundation/advanced feasibility needed |
| APP-Y05 | Smart Practice Room | **New** | Complements SOUND-05 / APP-X11 | Musician toolkit candidate |
| APP-Y06 | Ambient Sound Mixer | Expansion | SOUND-06 / APP-X12 | Musician toolkit candidate |
| APP-Y07 | BT SHARE Device Control Center | Expansion | APP-F01–F12, APP-X05, X07, X08, X26 | Hardware control candidate |
| APP-Y08 | Personal Audio Profiles | Expansion | APP-X01, X04, X21 | Foundation candidate |
| APP-Y09 | Audio Sync & Diagnostics Lab | Expansion | SOUND-SYNC-01, APP-X09, X17, X22 | Advanced engineering candidate |
| APP-Y10 | Local Audio Player | **New** | Supports app-owned audio playback and EQ/visualization | Foundation candidate |
| APP-Y11 | Custom Soundboard | **New** | Related to app-owned sound playback/mixing | Musician toolkit candidate |
| APP-Y12 | Customizable Sound Dashboard | **New** | Extends APP-X15/X16 | UX foundation candidate |

### APP-Y01 — Live Audio Visualizer Studio

**Planned experience:** Real-time waveform, spectrum/frequency bars, circular visualizer, bass-reactive and full-screen styles, user-selected colors/themes, saved visualizer presets and battery-conscious animations.

**Hardware-dependent stretch requirement:** A visualizer reacting to music passing through the external BT SHARE AUX → BM83 system is proposed **only if a valid audio-level/FFT data path is designed and verified**. The Flutter control connection alone does **not** expose AUX audio samples.

**Feasibility gate:** Define app-owned audio vs permitted capture sources; verify Android capture permissions, low-latency graphics and any hardware telemetry interface before promising hardware-mode visualization.

### APP-Y02 — Voice Recorder & Audio Lab

**Planned experience:** Record voice, singing, instruments and rehearsals; pause/resume; waveform editing and trim; export supported formats; organize folders; place markers; perform A/B comparison of two recordings.

**Feasibility gate:** Microphone permission, recording consent, supported codecs/export formats, playback behavior, storage scope, and reliable edit/undo semantics. No blanket recording of other apps' audio is implied.

### APP-Y03 — Rhythm & Drum Studio — new

**Planned experience:** Drum pads, basic rhythm patterns, adjustable tempo, subdivisions/time signatures, tap tempo, count-in, practice timer, tempo presets and a loopable rhythm pattern builder for instrument practice.

**Feasibility gate:** Define sequencer accuracy, sample asset licensing, playback latency and background/audio focus behavior. This expands the existing metronome category but is a new composition/workspace capability.

### APP-Y04 — Mini Audio Mixer

**Planned experience:** Mix audio sources the application is legitimately able to receive/process, with separate source levels, mute/solo, master level, stereo balance, saved mixer presets, clipping indicators and output meters.

**Feasibility gate:** Precisely enumerate permitted sources/routes, including app-owned tracks and any user-authorized microphone inputs. **Do not promise arbitrary third-party-app capture, system-wide routing or a virtual audio cable** under standard Android app privileges.

### APP-Y05 — Smart Practice Room — new

**Planned experience:** Create musical practice sessions with goals and durations, retain tuner/metronome settings, add notes, review prior sessions, define personal routines and view local progress without requiring an account.

**Feasibility gate:** Local data model, privacy, backup/export policy and whether timers remain valid during lifecycle/background changes.

### APP-Y06 — Ambient Sound Mixer

**Planned experience:** Mix licensed rain, ocean, wind, forest and similar layers with independent volumes; save favorites; use a sleep timer, fades and supported background audio.

**Feasibility gate:** Licensed sound assets, audio focus, Android background playback and battery consumption.

### APP-Y07 — BT SHARE Device Control Center

**Planned experience:** Show device names and live ESP32-reported states; connect/disconnect/reconnect; show any actually available signal information; assign an **in-app alias**; remember devices where supported; make recovery problems understandable.

**Feasibility gate:** Freeze the ESP32 BLE commands/events, persistence ownership and available telemetry. Renaming an in-app label **does not** necessarily rename the Bluetooth receiver itself. The first physical prototype still supports **two simultaneous receiver links**.

### APP-Y08 — Personal Audio Profiles

**Planned experience:** Presets such as Bass Boost, Vocal Clarity, Balanced and Custom; one-tap switching; supported device associations; import/export; optional user-approved profile selection for the active BT SHARE configuration.

**Feasibility gate:** Versioned preset schema and clear separation of effects applied to app-owned audio from the **external AUX → BM83** hardware audio path. A Flutter-selected preset does not change external AUX audio unless a verified hardware effect interface exists.

### APP-Y09 — Audio Sync & Diagnostics Lab

**Planned experience:** Display actual receiver connection/streaming state; run controlled test-signal measurements with suitable equipment/setup; compare recorded output timing; log disconnect/reconnect attempts; expose measurable buffer/error data; export useful reports.

**Feasibility gate:** Specify test signal, reference clock, capture arrangement, measurement uncertainty, permissions and documented telemetry. Connection status alone is **not** an acoustic-latency measurement. No perfect sync or automatic correction is promised.

### APP-Y10 — Local Audio Player — new

**Planned experience:** Select/browse permitted local audio files, play/pause/seek/repeat, playlists/favorites, progress and metadata, supported playback-speed adjustments, and playback using phone-available audio routes.

**Feasibility gate:** Android media access, audio focus, codec support and platform routing. The local player is **not automatically an audio source feeding the existing external AUX hardware**; that would require a separately specified and validated physical/audio integration path.

### APP-Y11 — Custom Soundboard — new

**Planned experience:** User-named/color-coded/icon-based audio buttons, imported sound clips, categorized boards, supported looping/playback options, and saved boards for different activities.

**Feasibility gate:** Storage permissions, supported file types, concurrent audio mixing and response latency.

### APP-Y12 — Customizable Sound Dashboard — new

**Planned experience:** Reorderable in-app cards for tuner, metronome, visualizer and audio controls; pinned tools and recent presets; custom saved layouts; compact and full-screen layouts.

**Feasibility gate:** Responsive layout, accessibility labels, state persistence and clear navigation. These are **in-app dashboard elements**, not a commitment to Android home-screen widgets.

## Five additional future concepts — included, not committed to MVP

| ID | Future concept | Relation to existing scope | Requested behavior / boundary |
| --- | --- | --- | --- |
| APP-Y13 | AI Sound Assistant | Extends APP-X24 troubleshooting | Explain analysis results, help pick EQ settings and guide diagnosis based only on available data; first consider rule-based help; AI provider, privacy and cost unspecified |
| APP-Y14 | Audio Spectrum History | Extends APP-X22 analyzer and APP-X17 local history | Save and compare permitted, microphone-based or app-owned spectral sessions with uncalibrated-device disclaimers |
| APP-Y15 | Multi-Listener Session Manager | **New future feature** relating to APP-F04/F05 and SOUND-SYNC-01 | Save/restore supported receiver groups and sessions; **never** imply more than two simultaneous BM83 links on current hardware |
| APP-Y16 | Safe Listening Tools | **New future feature** connected to hearing-related SOUND-07 | User-configured listening reminders, duration tracking and conservative guidance; no uncalibrated claims about actual sound pressure at the ear |
| APP-Y17 | Offline-First Experience | **New cross-cutting quality requirement** | Where technically practical, local-first settings, presets, audio files, practice data, recordings and diagnostics; cloud/account sync remains optional and unapproved |

## Proposed navigation framework — not a finalized UI decision

The supplied concept describes five destinations; they are recorded for later UX validation, **not** as approved Figma screens:

1. **Connect** — hub, receivers, sessions.
2. **Sound Lab** — EQ, visualizer and analysis.
3. **Studio** — local player, recorder and soundboard.
4. **Practice** — tuner, metronome, rhythms and practice room.
5. **My Sound** — presets, saved sessions, appearance and preferences.

Hardware-free users must be able to reach standalone tools without a BT SHARE device connection or mandatory account.

## Proposed development grouping — sequencing subject to team review

- **Foundation candidate:** Visualizer, local audio player, voice recorder, profiles, hardware device control, offline settings/diagnostics. Hardware-control *integration* remains gated by BLE/ESP32 and the existing hardware-first roadmap.
- **Musician toolkit candidate:** Rhythm and drums, smart practice, enhanced EQ, ambient mixer, soundboard, spectrum history.
- **Advanced audio engineering candidate:** Sync/diagnostics, multi-listener sessions, advanced routing/mixing, AI-assisted help and more sophisticated analysis.

These are **proposals from the supplied concept**, not approved release commitments. Some features overlap phases, and feasibility may change sequencing.

## Scope preservation / open decisions

- **No duplicate feature inflation:** APP-Y expansions refine prior APP-X/SOUND/APP-F items; they do not imply seventeen unrelated implementations.
- **No unverified OS access:** An ordinary Android app cannot be assumed to control arbitrary other apps' volume, capture their protected audio or change system-wide processing/routing.
- **No implied medical function:** Hearing assistance and safe listening tools require safety and product-claim review.
- **No implied hardware upgrades:** BM83/ESP32 firmware commands, acoustic sync correction, additional receivers, hardware-side EQ and hardware AUX visualizer data require independent engineering approval.
- **No false completion claims:** All requirements in this file remain design/planning scope with **zero validated implementation evidence supplied**.
- **Detailed release priorities, target Android versions, acceptance tests, telemetry definitions, GATT contract and Figma UX** remain to be agreed.
