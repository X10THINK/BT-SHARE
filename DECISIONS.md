# BT SHARE — Decision and Change Register

**Reviewed:** 2026-10-29
**Rule:** Preserve earlier decisions, distinguish newer owner information from independently signed engineering evidence, and mark recommendations **PROPOSED** until approved.

## Company and product identity (owner supplied 2026-10-29)

| ID | Decision | Evidence/source | Status |
| --- | --- | --- | --- |
| DEC-BRAND-001 | **X10 THINK** is the founding company of the **ZAEROX** brand and **BT SHARE** product. | Owner statement in project conversation, 2026-10-29 | **Owner confirmed** |
| DEC-BRAND-002 | **ZAEROX** is the technology brand; its tagline is **Innovation Beyond Limits**. | Owner statement and supplied two logo variations | **Owner confirmed** |
| DEC-BRAND-003 | **BT SHARE** is the product name; owner supplied four product-logo variations. | Owner-provided visual identity | **Owner confirmed** |
| DEC-BRAND-004 | README and public website should credit all three entities without presenting product R&D as commercial availability. | Scope-control editorial policy | **Documentation rule** |

See [BRAND_IDENTITY.md](BRAND_IDENTITY.md). These decisions are not independent proof of legal registration or rights certification.

## Mobile app scope decisions recorded on 2026-10-14

| ID | Original decision (preserved) | Boundary / status |
| --- | --- | --- |
| DEC-MOB-001 | Target **Flutter + Dart, Android first**. | Confirmed direction; Android versions and implementation pending |
| DEC-MOB-002 | Include standalone sound utilities for users who do not own the hub. | Scope confirmed, behavior/OS limits not finalized |
| DEC-MOB-003 | Include all **seven** sound utility categories. | Category inclusion is not blanket implementation feasibility |
| DEC-MOB-004 | Include multi-device sound synchronization as a product goal. | Achievable timing/architecture not verified |
| DEC-MOB-005 | Preserve historical two-receiver BM83/ESP32 college prototype and original LKR 40,000 envelope. | Applies to original October 6 baseline; later hardware changes must be imported/reconciled |
| DEC-MOB-006 | Include 25 additional numbered feature concepts APP-X01–APP-X25. | Advanced X21–X25 remain future candidates; no delivery promise |
| DEC-MOB-007 | Track Smart Connection Recovery as APP-X26. | Hub-state and recovery ownership remains with ESP32 |
| DEC-MOB-008 | Include 12 detailed audio workspace proposals APP-Y01–APP-Y12 while merging overlaps. | Five distinct new tool families; acceptance still pending |
| DEC-MOB-009 | Include five future concepts APP-Y13–APP-Y17. | Roadmap, not MVP |
| DEC-MOB-010 | Record five-area navigation and three development groupings. | Proposal / UX sequencing, not finalized design |

Full prior scope: [Mobile Product Scope](FeaturE_Scope_Documentations/mobile-app/PRODUCT_SCOPE.md) · [25-feature expansion](FeaturE_Scope_Documentations/mobile-app/FEATURE_EXPANSION_25.md) · [17-proposal expansion](FeaturE_Scope_Documentations/mobile-app/FEATURE_EXPANSION_17.md).

## New scope/context recorded, not falsely verified

| ID | Statement | Status |
| --- | --- | --- |
| DEC-HW-CONTEXT-001 | Current college prototype power direction is fixed protected **USB-5V only**, without battery/charge-while-playing. This later change is not represented in the original October 6 BRD. | **Owner-reported change; exact authoritative native design/electrical evidence must be imported** |
| DEC-PROD-RD-001 | Investigate a commercially affordable product accepting **AUX or Bluetooth source input** and targeting multiple ordinary headphones. Two listeners first; analyze 3, 4+ with evidence. | **Commercial R&D goal; not a verified design decision or prototype result** |
| DEC-WEB-001 | Use **Angular** for the planned website frontend, including products, docs, APK releases and an admin dashboard. | **Website planning direction documented** in 2026-10-27 specs; implementation pending |
| DEC-WEB-002 | Choose a secure backend/hosting/identity/release solution separately; enforce admin permissions server-side. | **Architecture requirement; provider/stack not selected** |
| DEC-REPO-001 | Keep the **14 Flutter documents already committed as ordinary files in local clone `bc5f287`**, and repair legacy references to renamed folders. | **Flutter gitlink resolved in supplied clone; doc link repairs prepared locally, not pushed** |

## Outstanding decisions — do not label as approved

| Proposed ID | Candidate decision | Approval required from |
| --- | --- | --- |
| ADR-APP-001 | **Approve/revise existing Flutter ADR-005:** Feature-first Clean Architecture, MVVM presentation and Riverpod state management; review **DDD principles** as a separate enhancement. | Mobile lead; TRD/SDD/ADR exist but are explicitly draft/proposed |
| ADR-APP-002 | Android minimum SDK, media architecture, persistence, plugin/native boundaries and MVP scope. | Mobile technical owner |
| ADR-INTEGRATION-001 | Versioned Flutter ↔ ESP32 BLE GATT commands, states, errors, UUIDs and recovery policies. | Embedded + mobile owners |
| ADR-WEB-001 | Production backend, storage, auth/roles, CI/CD, signing and release hosting provider. | Website/backend owners |
| ADR-PRODUCT-001 | Commercial architecture, chipsets, Bluetooth input, target number of listeners, timing/price criteria. | Product and engineering owners based on official specs and tests |

Existing architecture candidates: [Flutter TRD](BT_SHARE_Flutter_Documentation/03_TRD_Technical_Requirements.md) · [SDD](BT_SHARE_Flutter_Documentation/04_SDD_Software_Design.md) · [ADR-005](BT_SHARE_Flutter_Documentation/11_ADR_Architecture_Decision_Records.md). DDD extension: [ARCHITECTURE_PROPOSAL.md](FeaturE_Scope_Documentations/mobile-app/ARCHITECTURE_PROPOSAL.md).

## Engineering change controls

1. New decisions must identify **source, owner, approval date, impact, revision and verification**.
2. A plan does not prove **physical prototype functionality**, safe power or release readiness.
3. Keep **ordered, paid, received and missing** components distinct. Do not treat the LKR 40,000 historical ceiling as the current cash balance or purchasing authority.
4. Do not convert the historical two-receiver educational limit into a permanent commercial product limit; do not claim 3+ or dual audio paths are feasible without separate evidence.
5. Any change to the AUX/BM83/ESP32 firmware/BLE contract or to public product claims requires cross-team review.
6. No unverified architecture suggestion, including DDD/MVVM, becomes an implementation requirement merely because it appears in a README.

See [REQUIREMENTS.md](REQUIREMENTS.md), [PROJECT_WORKFLOW.md](PROJECT_WORKFLOW.md) and [PROJECT_STATUS.md](PROJECT_STATUS.md).
