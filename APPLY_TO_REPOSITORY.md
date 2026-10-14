# How to Add This Scope Pack to X10THINK/BT-SHARE

**Why this pack exists:** The GitHub connection used to prepare it has **read-only permission** (`push: false`), so it could not commit to the source repository. Files are prepared for manual upload or a commit by a collaborator with write access.

## Files to upload at repository root (preserve paths)

- `REQUIREMENTS.md` (new)
- `DECISIONS.md` (new)
- `docs/mobile-app/PRODUCT_SCOPE.md` (new)
- `docs/mobile-app/FEATURE_CATALOGUE.md` (new)
- `docs/mobile-app/FEASIBILITY_REGISTER.md` (new)

The existing `README.md`, `PROJECT_STATUS.md`, `BT_SHARE_BRD.md` and `BT_SHARE_Execution_Plan.md` are **not overwritten** by this package.

## Recommended README.md addition

Insert near the beginning of the README after the project-vision introduction:

```markdown
## Android mobile app — expanded product scope (2026-10-14)

BT SHARE is also planned as an **Android-first Flutter sound utility app**, useful **with or without BT SHARE hardware**. The hardware mode remains a major function, while standalone categories include Equalizers & Sound Enhancers; Audio Routing & Mixing; Per-App Volume Control; Sound Measuring & Analysis; Tuners & Metronomes; Ambient & Focus Sounds; and Hearing Assistance. **Cross-device sound synchronization** is also a product goal, subject to technical feasibility and measured results.

See [mobile app product scope](docs/mobile-app/PRODUCT_SCOPE.md), [feature catalogue](docs/mobile-app/FEATURE_CATALOGUE.md), [requirements index](REQUIREMENTS.md) and [decisions](DECISIONS.md). These are planned features, not evidence of implementation or OS-level permissions. The current **two-receiver BM83/ESP32, AUX-fed hardware prototype**, its budget and its acceptance gates remain unchanged.
```

## Recommended PROJECT_STATUS.md addition

Add to a product-planning subsection (do **not** mark any feature as coded/tested):

```markdown
### Android Flutter app product-scope update — 2026-10-14

- [x] Android-first Flutter platform direction confirmed for scope planning.
- [x] Hardware-independent sound utilities included at category level: EQ/Enhancers, Routing/Mixing, Per-App Volume, Measuring/Analysis, Tuners/Metronomes, Ambient/Focus, Hearing Assistance.
- [x] Cross-device synchronization included as a product goal, **not** as a proven working behavior.
- [ ] Detailed utility behaviors, Android feasibility and acceptance criteria reviewed.
- [ ] Final Flutter feature catalogue, screens and hardware BLE interface approved.
- [ ] App source code and runnable tests supplied and verified.

See `docs/mobile-app/PRODUCT_SCOPE.md`. The project's current hardware stage and two-device gate status remain unverified.
```

## Apply using GitHub web interface

1. Open `https://github.com/X10THINK/BT-SHARE` as a collaborator with write access.
2. Use **Add file → Upload files** (preserving the relative paths) or a local clone and Git commit.
3. Prefer a branch / pull request so the software and hardware leads can review the scope change separately from the frozen hardware BRD.
4. Add the two README/status notes, review the resulting diff and merge when authorized.
5. Do **not** rewrite the 2026-10-06 BRD or execution plan to imply that audio synchronization or Android system-wide processing has been verified.

## Status terminology

- **Scope confirmed:** product direction/category selected by software project lead.
- **Feasibility pending:** platform/hardware ability has not been demonstrated.
- **Implementation complete:** only claim after source/tests exist.
