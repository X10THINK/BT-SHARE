# UI/UX Specification — Flutter Android

> **Project:** BT SHARE — Android Flutter App  
> **Version:** 0.1.0 | **Created:** 2026-10-28 | **Status:** Draft for review  
> **Document owner:** UX lead / Flutter lead | **Approval:** Pending product/Flutter/embedded review  
> **Evidence boundary:** Based on repository `main` reviewed 2026-10-28; this is a proposed, executable specification, **not proof of working code, firmware, hardware, or tests**.

## 1. Status and guiding principles
**Draft UI/UX specification, not an approved visual design or Figma artifact.** Design for: hardware optionality, clear distinction between actual and desired receiver state, simple beginner-friendly flows, Android accessibility, English/Tamil localization, privacy by design and consistent application-owned audio source labeling.

## 2. Navigation — candidate information architecture
| Destination | Main screens | Primary action | Hardware dependent? |
|---|---|---|---|
| Connect | Hub discovery, hub detail, receiver scan, slots 1/2, connection diagnostics | Connect hub, manage receiver | Yes |
| Sound Lab | EQ, balance, visualizer, permitted audio analyzer | Select source, apply supported DSP | No hub required; source limits |
| Studio | Local player, ambient mixer, voice recorder, later soundboard | Play/record/mix app-owned media | No |
| Practice | Tuner, metronome, later rhythm/practice sessions | Practice, save settings | No |
| My Sound | Presets, favorites, session history, dashboard, settings, privacy | Manage settings and data | No |

The proposal uses five bottom-navigation destinations, with large-form tablet alternatives only after UX review. Avoid requiring a BLE scan/onboarding before standalone access.

## 3. Information hierarchy and screen inventory
| Screen ID | Screen | Required elements and states |
|---|---|---|
| UX-01 | First launch | Value explanation, "Use sound tools" and "Connect hub"; no mandatory login |
| UX-02 | Home/dashboard | Pinned tools, resume supported activity; reorder only if APP-Y12 included |
| UX-03 | Hub discovery | Bluetooth status, permission rationale, scanning, empty/error/retry |
| UX-04 | Hub control | Hub readiness/firmware if provided, 2 receiver cards, scan action |
| UX-05 | Receiver selection | Receiver name + opaque identifier/alias, slot select, confirmation, third-slot limit |
| UX-06 | Receiver detail | Pair/connect/stop/reconnect, factual state, last event and error advice |
| UX-07 | Local player | File picker/library, transport, progress, output route, queue/favorites |
| UX-08 | EQ profiles | Supported source indicator, bands, presets, reset/save, unsupported routes |
| UX-09 | Visualizer | Explicit capture source, styles, pause, battery mode, mic disclosure if needed |
| UX-10 | Ambient mixer | Layer rows with volume, sleep timer, fade, background playback state |
| UX-11 | Recorder | Mic request rationale, record/pause/stop, elapsed time, save/discard, local clips |
| UX-12 | Tuner/metronome | Mic indicator, note/offset, tempo/time signatures, tap tempo, stop |
| UX-13 | History/diagnostics | Local event list, privacy-safe export, erase action |
| UX-14 | Settings | English/Tamil, theme, motion, permissions, privacy, data retention, about/support |
| UX-15 | Optional advanced screens | Soundboard, rhythm, practice, sync rig, AI and OTA only with separate approvals |

## 4. Detailed hub-state presentation
Use a **single source-of-truth banner**: `Hub disconnected`, `Connecting`, `Connected/Ready`, `Protocol incompatible`, `Permission denied`, `Bluetooth off`. Receiver chips distinguish `Discovered`, `Selected`, `Pairing`, `Paired`, `Connecting`, `Connected`, `Streaming`, `Disconnected`, `Failed`, `Unknown/Stale` only when the underlying protocol supports them. Color alone must not communicate state; use text and accessible icons.

When BLE disconnects mid-session, show `Connection to BT SHARE hub lost. Receiver states are not currently verified.` Do not claim receivers disconnected or audio stopped unless firmware/safe test evidence supports it. A recovery button re-establishes hub link, re-subscribes and refreshes snapshot.

## 5. Critical flows, including errors
**A. Connect:** User taps Connect → rationale (if needed) → OS permission → nearby hub list → handshake → ready / incompatible firmware / no hub / permission denied. Retry requires user action or documented safe policy.

**B. Select second headset:** Scan → select receiver 1 → select receiver 2 → app validates distinct IDs and available slots → pair/connect commands through hub → progress and authoritative status. Third active selection produces an explanatory boundary, not a crash.

**C. Standalone listening:** Pick local file → confirm audio route → play → optionally choose EQ if supported; local file deletion or revoked URI shows reselect prompt without corrupting playlist.

**D. Recording:** Tap Record → explain mic permission/consent → OS grant/deny → recording visible indicator → Pause/Stop → save/discard. App background restrictions and errors must not leave hidden recording active.

## 6. Design system — initial constraints, not approved colors/fonts
- Create reusable primitives: app header, five-destination navigation, feature tile, state badge, device card, permission panel, inline alert, empty state, media transport, slider, EQ band, sheet/dialog and diagnostic row.
- Theme modes light/dark, user-selected accent within accessible contrast boundaries. Exact colors, typography family, illustration style and logo require brand approval.
- Adaptive layout targets small phones (~320dp and up), common phones, tablets in portrait/landscape; prevent clipping at large font scaling.
- Touch targets and focus order should follow current Android/Material accessibility guidance; visually show active focus.
- Animation must honor reduced-motion settings and optional low-power mode; pause visualizers when not visible.
- Audio controls require meaningful labels/values (e.g., `Receiver 1 volume 50 percent`) rather than unlabeled sliders.

## 7. Copy and localization policy
- Strings externalized in ARB or equivalent; English and **human-reviewed Tamil**; no hardcoded state labels in widgets.
- Explain unfamiliar terms: `Hub (BT SHARE device)`, `Headphones`, `Pair`, `Connected`, `Playing` with consistent glossary.
- Differentiate `Unsupported`, `Permission needed`, `Not connected`, `Unavailable due to firmware` and `Coming later`.
- Show clear recording/privacy disclosures; do not assert exact medical hearing or synchronized milliseconds without validated evidence.

## 8. Permission and privacy UX
Use just-in-time prompts; do not bundle microphone and BLE permissions into one initial wall of text. Offer a non-blocking hub-free route if Bluetooth is denied. Provide local history/export and erase controls where implemented. For any audio visualization/capture, show source and stop mechanism.

## 9. Accessibility acceptance
Navigation usable with TalkBack and large text, correct traversal and announced state updates (throttled for noisy real-time data); sliders usable with accessible actions; no critical meaning conveyed only by color; focus remains sensible after dialogs; inputs clearly labeled; reduce motion honored; translated strings reviewed for truncation.

## 10. Design deliverables for sign-off
User flow diagrams, low-fidelity wireframes for UX-01..UX-14, token list, error/empty/permission states, accessibility checklist, Tamil/English strings, interaction prototype and annotated handoff with APP requirement IDs. No mockup should imply BM83 volume, live AUX waveform or sync correction capability without a verified protocol.

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
