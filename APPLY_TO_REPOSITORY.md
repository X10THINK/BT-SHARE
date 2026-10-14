# Apply BT SHARE's 25-feature Android App Scope Update

**Prepared:** 2026-10-14  
**Repository:** https://github.com/X10THINK/BT-SHARE  
**GitHub permission observed:** `pull: true`, `push: false` — **no remote files were changed**.

## Purpose

This package extends the prior Android-first BT SHARE sound app planning pack with **all 25 numbered features** selected by the Flutter workstream lead, plus the separately highlighted **Smart Connection Recovery** (`APP-X26`). It **does not** overwrite or weaken the original two-receiver BM83/ESP32 hardware proof-of-concept requirements.

## Files to upload or replace (keep directory paths)

- `REQUIREMENTS.md` — root requirements index, updated with APP-X01–X26.
- `DECISIONS.md` — includes feature-selection decisions.
- `docs/mobile-app/PRODUCT_SCOPE.md` — product boundary and expansion summary.
- `docs/mobile-app/FEATURE_CATALOGUE.md` — existing APP-F01–F12 and seven SOUND categories, plus the new expansion link.
- `docs/mobile-app/FEATURE_EXPANSION_25.md` — **new** comprehensive list of all 25, key dependencies, and recovery feature.
- `docs/mobile-app/FEASIBILITY_REGISTER.md` — expanded risk and validation questions.

If the previous Android scope pack was **not** uploaded yet, upload all six files here. If it was uploaded, replace the existing five and add the new `FEATURE_EXPANSION_25.md`.

## README.md addition

Add a short paragraph near the Android app scope section (or create that section if absent):

```markdown
### Android sound app — 25-feature expansion (2026-10-14)

The Flutter software-workstream lead selected **all 25** additional sound-app feature concepts for the **planned Android app scope**, plus **Smart Connection Recovery** as a separately highlighted requirement. These cover premium sound tools, hub management, standalone utilities, usability/privacy and future-version features. The seven previously selected standalone sound-tool categories remain included. **Selected for product scope does not mean implemented or universally supported by Android or BM83 hardware.**

See [feature expansion](docs/mobile-app/FEATURE_EXPANSION_25.md), [feature catalogue](docs/mobile-app/FEATURE_CATALOGUE.md), [requirements](REQUIREMENTS.md) and [decisions](DECISIONS.md). The college hardware prototype still targets two A2DP receivers with its existing budget and acceptance gates.
```

## PROJECT_STATUS.md addition

Add under planning status without claiming code completion:

```markdown
### Flutter Android app scope — 2026-10-14

- [x] Android-first Flutter app, hardware-independent utilities and the seven sound-tool categories selected.
- [x] All 25 additional sound-app feature concepts APP-X01–APP-X25 selected for the product roadmap.
- [x] Smart Connection Recovery tracked as separate highlighted feature APP-X26.
- [ ] Final Android feasibility, supported target versions/devices and native-API access checked.
- [ ] App/hardware BLE command and event contract approved by both teams.
- [ ] Detailed feature acceptance tests and release prioritization approved.
- [ ] Flutter implementation and real-device testing evidenced.

**Note:** APP-X21–APP-X25 remain advanced/future-version candidates. The two-receiver hardware prototype baseline and status are unchanged.
```

## GitHub upload steps

1. Sign into GitHub using an account with **write permission** to `X10THINK/BT-SHARE`.
2. Upload the six files preserving their repository-relative paths (or copy them into a clone).
3. Apply the two text additions to README.md and PROJECT_STATUS.md.
4. Use a pull request for cross-team review if available; check the diff carefully before merging.
5. Do not rewrite `BT_SHARE_BRD.md` and `BT_SHARE_Execution_Plan.md`, since they are the governing college hardware baseline.

**Suggested commit message:** `docs(android): record 25 feature concepts and recovery requirement`

## Scope confidence

- **Confirmed:** feature ideas included in mobile product requirements planning.
- **Provisional:** exact functionality, screen flow, implementation order, OS / hardware support and acceptance tests.
- **Not established:** deployed or tested code, hardware/receiver latency correction, system-wide third-party volume or EQ access, OTA update capability.
