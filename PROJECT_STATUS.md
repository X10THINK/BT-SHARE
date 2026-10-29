# BT SHARE — Project Status and Evidence Register

**Reviewed:** 2026-10-29
**Local clone baseline:** `main` at `bc5f287d57917f3c1b5945cbcfa61f9de8bbf1be` (*Upload all 14 Flutter documentation files*)
**Scope:** The ZIP contains an updated local checkout; these edits are **not automatically pushed to GitHub**. Status is documentary, not confirmation of live devices, APKs or production releases.

> **Status terminology:** **Documented** means a specification or plan is in the repository. **Verified** needs a build/test/bench/release artifact with traceable evidence. **Unknown** means implementation evidence was not included; it does not prove the team did no work outside the repository.

## Current workstreams

| Workstream | Latest documented position | Evidence gap |
| --- | --- | --- |
| **Educational hardware prototype** | Historical October 6 BM83/ESP32 two-listener AUX prototype BRD and execution plan exist. The later owner-directed build is **fixed USB-5V only**, no battery/charger/UPS. | No native KiCad revision, reconciled live BOM, electrical sign-off, assembly or two-receiver playback test in this checkout. |
| **Commercial product R&D** | Affordable multi-listener product vision: investigate AUX **or Bluetooth source** input and ordinary mixed-brand earbuds, starting with two. | Bluetooth receive→retransmit design, 3/4+ receiver capacity, sync, codecs and cost require official specs and physical proof. |
| **Flutter Android app** | **14 Flutter technical/product documents** are regular tracked files under `BT_SHARE_Flutter_Documentation/`, in addition to prior mobile feature planning files. | No `pubspec.yaml`, `lib/`, compiled APK, tests or verified device integrations in this checkout. |
| **Website, APK releases and admin** | Angular frontend, content/docs, secure downloadable APK releases and separate admin planned in 7 website specs. | No Angular source, backend, deployed website, production security tests or signed APK in this checkout. |
| **Brand** | **X10 THINK** founded **ZAEROX** and **BT SHARE**. ZAEROX tagline: **Innovation Beyond Limits**. Six project-owner-provided logo assets included. | Legal brand registrations/certifications not independently assessed; logo assets are not evidence of released hardware. |

## Repository/documentation checkpoints

- [x] Root project requirements, decisions and scope/planning records available.
- [x] Historical original hardware BRD and execution-plan PDF + Markdown retained under `First_Documents/`.
- [x] Flutter feature-planning catalogues and feasibility register retained under `FeaturE_Scope_Documentations/mobile-app/`.
- [x] **All 14 Flutter handover documents are present and tracked** by Git in the supplied clone at `bc5f287`. The **earlier gitlink issue was already corrected in that commit**.
- [x] Website requirements, architecture, feature catalogue, sitemap, content, UI/UX and SEO docs retained.
- [x] README, brand guide, supplied logos and updated cross-workstream documentation prepared in this local checkout.
- [x] Stale internal document links corrected in this checkout; validate using `python scripts/repair_repository_links.py --check`.
- [ ] Review, commit and push the prepared changes to GitHub. No push is claimed.

## Flutter architecture — exact documented decision state

The newer files **change the prior assessment**:

| Architecture topic | Actual document evidence | Decision status |
| --- | --- | --- |
| Android-first Flutter/Dart | [`03_TRD_Technical_Requirements.md`](BT_SHARE_Flutter_Documentation/03_TRD_Technical_Requirements.md), [`11_ADR_Architecture_Decision_Records.md`](BT_SHARE_Flutter_Documentation/11_ADR_Architecture_Decision_Records.md), ADR-001 | Product direction accepted; implementation not evidenced |
| Feature-first Clean Architecture | Flutter TRD section 2; [`04_SDD_Software_Design.md`](BT_SHARE_Flutter_Documentation/04_SDD_Software_Design.md) sections 1–2; ADR-005 | **Proposed; formal team ADR sign-off pending** |
| MVVM-style presentation | Flutter TRD and SDD; ADR-005 | **Proposed** |
| Riverpod | Flutter TRD: **suggested**; SDD and ADR-005 describe a candidate | **Proposed / not approved** |
| Domain-Driven Design (DDD) | No explicit binding DDD decision in the 14 Flutter files; domain entities/layers are described | **Additional recommendation only**, see [proposal](FeaturE_Scope_Documentations/mobile-app/ARCHITECTURE_PROPOSAL.md) |

Prior `PROJECT_STATUS.md` marked app architecture selection pending when the 14 handover files were absent from that assessment. These files now supply a **proposal**, not a signed final architecture choice.

## Prototype hardware gates (do not mark passed without evidence)

| Gate | Acceptance evidence | Checkout status |
| --- | --- | --- |
| G0 — Design ready | Reviewed native KiCad files, correct electrical/RF design, exact BM83 references, BOM/DRC/ERC | **Unknown / no native files here** |
| G1 — Electrical ready | Inspection and safe power rails on assembled prototype | **No bench evidence** |
| G2 — BM83 alive | Reproducible module configuration and UART logs | **No bench evidence** |
| G3 — One-device audio | AUX source audible on a known compatible A2DP sink | **No audio test evidence** |
| G4 — Two-device simultaneous audio | Same source audible on two independent sinks, recorded proof | **No dual-audio test evidence** |
| G5 — ESP32 host control | Versioned firmware build and UART/device-state tests | **No source/test evidence** |
| G6 — BLE GATT contract | Jointly approved protocol + independent tests | **No approved contract evidence** |
| G7 — Flutter integration | End-to-end app/hub evidence | **No integration evidence** |
| G8 — Validation/demo | Compatibility, recovery, latency observations, long run and demo report | **No validation evidence** |

**Hardware scope controls:** The **LKR 40,000** figure in the original BRD is a **historical cap**, not proof of present funds or purchase authorization. Later changes in battery removal, procurement, power input and native PCB must be reconciled against actual updated hardware evidence before claiming completion or ordering anything. Do not assume two BM83 connections prove two active audio streams or synchronization.

## Software and website requirements — what remains open

- [ ] Flutter team approves or revises its proposed feature-first Clean/MVVM/Riverpod design, explicitly deciding whether/how to adopt DDD principles.
- [ ] Choose supported Android SDK levels, plugin versions, mobile storage, native audio integration and release MVP.
- [ ] Freeze versioned ESP32 ↔ Flutter BLE characteristics, messages, errors, capabilities and test fixtures.
- [ ] Implement and verify Flutter application source and supported Android audio/permission behaviors.
- [ ] Select and build website backend/auth/release storage; implement Angular site and security/a11y testing.
- [ ] Ship only signed, integrity-checked, approved APKs and verified product claims.
- [ ] Import outside-repository hardware/procurement revisions **only after evidence review**, without repeating or overwriting completed engineering.

## Navigate source documents

- [README](README.md) · [Requirements](REQUIREMENTS.md) · [Decisions](DECISIONS.md) · [Project workflow](PROJECT_WORKFLOW.md)
- [Flutter TRD](BT_SHARE_Flutter_Documentation/03_TRD_Technical_Requirements.md) · [Flutter SDD](BT_SHARE_Flutter_Documentation/04_SDD_Software_Design.md) · [Flutter ADRs](BT_SHARE_Flutter_Documentation/11_ADR_Architecture_Decision_Records.md)
- [Mobile scope](FeaturE_Scope_Documentations/mobile-app/PRODUCT_SCOPE.md) · [Architecture extension proposal](FeaturE_Scope_Documentations/mobile-app/ARCHITECTURE_PROPOSAL.md)
- [Website requirements](BT_SHARE_Website_Documentation/WEBSITE_REQUIREMENTS.md) · [Website architecture](BT_SHARE_Website_Documentation/WEBSITE_ARCHITECTURE.md)
- [Original hardware BRD](First_Documents/MD/BT_SHARE_BRD.md) · [Execution plan](First_Documents/MD/BT_SHARE_Execution_Plan.md)
- [Brand identity](BRAND_IDENTITY.md)
