# Apply BT SHARE's Consolidated Android App Scope Update

**Prepared:** 2026-10-14  
**Repository:** https://github.com/X10THINK/BT-SHARE  
**Connected GitHub permissions checked:** `pull: true`, `push: false`. The remote repository **has not been changed** by this update.

## Purpose

This is a **complete replacement for the previous uncommitted planning ZIPs**. It retains the **seven standalone sound utility categories**, **Android-first Flutter app**, the existing **provisional APP-F01–F12 hardware controls**, **multi-device synchronization goal**, the earlier **25 numbered feature proposals plus separately highlighted Smart Connection Recovery**, and now **12 detailed audio-workspace proposals plus 5 future concepts**. The new ideas are carefully mapped into the old ones instead of being counted as seventeen unrelated implementations.

**This package updates mobile-app scope only.** The college hardware BRD and execution plan remain controlling for the **two-receiver BM83/ESP32 proof of concept**, AUX audio path, LKR 40,000 ceiling and hardware-first engineering gates.

## Files in this package

1. `REQUIREMENTS.md` — consolidated requirements index and change boundaries.
2. `DECISIONS.md` — Android scope decision record through DEC-MOB-010.
3. `docs/mobile-app/PRODUCT_SCOPE.md` — hardware-independent app product vision and hardware boundary.
4. `docs/mobile-app/FEATURE_CATALOGUE.md` — provisional hardware functions, seven SOUND categories and expansion references.
5. `docs/mobile-app/FEATURE_EXPANSION_25.md` — the earlier 25 features plus Smart Connection Recovery.
6. `docs/mobile-app/FEATURE_EXPANSION_17.md` — all 12 detailed proposals and all five future concepts, with no-duplicate mapping.
7. `docs/mobile-app/FEASIBILITY_REGISTER.md` — Android/hardware feasibility checks for both expansions.
8. `APPLY_TO_REPOSITORY.md` — this file and README/PROJECT_STATUS insertion text below.

Upload the seven requirements/decision files under their exact repository-relative paths. This pack includes the earlier files; **do not combine it with an old ZIP by uploading duplicate copies**.

## README.md insertion (add a new section near Flutter integration)

```markdown
### Android app — expanded personal audio workspace (planning scope, 2026-10-14)

BT SHARE is **Android-first in Flutter** and is intended to be useful **without the physical BT SHARE hardware** through standalone sound utilities. The Flutter lead included all seven sound-tool categories, a multi-device synchronization goal, **25 detailed product feature concepts** plus separately highlighted **Smart Connection Recovery**, and **12 additional detailed proposals plus five future concepts**. Overlapping ideas are consolidated rather than counted as independent extra features.

See [mobile product scope](docs/mobile-app/PRODUCT_SCOPE.md), [feature catalogue](docs/mobile-app/FEATURE_CATALOGUE.md), [25-feature register](docs/mobile-app/FEATURE_EXPANSION_25.md), [audio-workspace expansion](docs/mobile-app/FEATURE_EXPANSION_17.md), [feasibility](docs/mobile-app/FEASIBILITY_REGISTER.md), [requirements](REQUIREMENTS.md), and [decisions](DECISIONS.md).

**Scope is not implementation.** Android third-party audio access, per-app volume, hardware-based visualizer, device-specific DSP/volume, more-than-two receivers and perfect synchronization have **not** been validated. The current college hardware proof remains two receivers, with hardware-first gates and the existing budget.
```

## PROJECT_STATUS.md insertion (under app planning; do not mark software complete)

```markdown
### Android Flutter mobile app — scope update (2026-10-14)

**Planning confirmed:** Android-first Flutter; standalone utilities for users without hardware; all seven SOUND categories; sync as a product goal; APP-X01–APP-X25 plus highlighted recovery APP-X26; APP-Y01–APP-Y12 (five distinct additional tool families, seven expansions) plus APP-Y13–APP-Y17 (five future concepts).

**Suggested but not finalized:** navigation (Connect / Sound Lab / Studio / Practice / My Sound) and proposed foundation / musician / advanced implementation grouping.

**Not verified or completed:** Android feature feasibility, BM83/ESP32 support for new hardware features, BLE interface freeze, sound-synchronization tolerance, Flutter source/build/tests, accessibility, privacy and audio-permission tests. All planned features require detailed acceptance criteria and prioritization.

The **two-receiver college hardware milestone, external AUX audio path and hardware-first acceptance gates remain unchanged**.
```

## GitHub application steps

1. Use an account with write access to `X10THINK/BT-SHARE`.
2. Upload the seven docs/requirements/decision files preserving directory structure, overwriting older uncommitted draft versions if needed.
3. Apply README and PROJECT_STATUS snippets above without removing hardware baseline text.
4. Review the diff in a pull request with the hardware/Flutter teams before merging.
5. Confirm the links and do not claim acceptance gates or Android feature builds passed.

Suggested commit message: `docs(android): consolidate audio workspace and future feature scope`

## Scope status labels

- **Scope confirmed:** product team has chosen the capabilities for planning.
- **Proposed:** specific navigation, release sequencing and exact interaction design.
- **Unverified:** OS permissions, supported audio routes, BM83 data/controls, audio latency/synchronization and test outcomes.
- **Not completed:** code, UI builds, integration tests and hardware qualification.
