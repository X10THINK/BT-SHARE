# BT SHARE — Requirements Index

**Reviewed:** 2026-10-29
**Type:** Cross-workstream requirements navigation and scope control.
**Rule:** Distinguish historical educational hardware, commercial product R&D, Android software, website and brand requirements. This index does not replace official technical source documents or test evidence.

## A. Origin, ownership and branding

| ID | Requirement / identification | Status |
| --- | --- | --- |
| BRAND-01 | **X10 THINK** is the company that founded **ZAEROX** and **BT SHARE**. | Owner-provided identity, 2026-10-29 |
| BRAND-02 | **ZAEROX** is the technology brand. Tagline: **Innovation Beyond Limits**. | Owner-provided identity |
| BRAND-03 | **BT SHARE** is a ZAEROX product initiative. | Owner-provided identity |
| BRAND-04 | Use the owner-provided six logo variations in product documentation/website without distorting marks or implying certifications. | Assets supplied; website implementation pending |

See [Brand Identity](BRAND_IDENTITY.md) and [Website Branding](BT_SHARE_Website_Documentation/WEBSITE_BRANDING.md).

## B. Original college prototype — historical hardware scope

Original authority: [BT SHARE Hardware BRD](First_Documents/MD/BT_SHARE_BRD.md) and [Execution Plan](First_Documents/MD/BT_SHARE_Execution_Plan.md), dated 2026-10-06. Treat these as **historical baseline**; later changes and native engineering records are not included in this repository snapshot.

| ID | Historical requirement | Verification needed |
| --- | --- | --- |
| BR-001 / AUD-004 | One stereo external AUX source is heard simultaneously on two independent Bluetooth Classic A2DP sink devices. | Actual hardware G4 two-receiver playback evidence |
| BR-002 | Prove the hardware audio function before Flutter integration. | G2 BM83, G3 one-device, G4 two-device tests |
| BR-003 | Original prototype procurement ceiling **LKR 40,000**. | Reconcile later approved change records, purchases, receipts and balances; no purchase authorization here |
| HW-001–HW-005 | Correct carrier/power/AUX/UART/RF keepout/testpoint interfaces. | Approved native KiCad project, ERC/DRC, review and power checks |
| BT-001–BT-003 | Scan, pair, manage receiver slots under the first prototype's two-receiver target. | Verified exact module/firmware and bench data |
| FW-001–FW-007 | ESP32 UART host, parser, state, recovery and independent control. | Versioned source, build and functional tests |
| APP-F01–APP-F12 | Provisional Flutter BLE control and state catalogue. | Versioned jointly accepted GATT contract; hardware-independent app mocks |

**Later owner-reported scope correction (not backported into the original BRD):** Current college hardware direction is **protected fixed USB-5V input only**, no battery, battery charger, UPS or charge-while-playing circuit. Before fabrication, reconcile this with the latest authoritative native KiCad and approved electrical change records. Do **not** treat the October 6 procurement list as an up-to-date remaining-parts list.

**Unverified:** exact BM83 AT firmware's dual-active-audio behavior, audio synchronization, current KiCad completion, physical build, approval gates and actual expenditure.

## C. Commercial multi-listener product — research track

| ID | Desired outcome | Status |
| --- | --- | --- |
| PROD-R01 | Affordable, broadly compatible audio sharing for price-sensitive users. | Product goal; pricing validation pending |
| PROD-R02 | Accept **either AUX analog input or compatible Bluetooth audio input** from phone/computer. | Commercial architecture research; not a prototype capability claim |
| PROD-R03 | Send the same audio program to multiple ordinary Bluetooth headsets/earbuds, including mixed brands. | Two-listener baseline to verify; research 3, 4 and more independently |
| PROD-R04 | Measure realistic codec, buffering, latency/synchronization, RF scheduling, battery/power and regulatory constraints. | Research and empirical testing needed |
| PROD-R05 | Do not present Bluetooth input, third/fourth link, low latency or precise synchronization as available until supported by verified implementation evidence. | Mandatory claim boundary |

Commercial scope cannot silently amend the original educational prototype's validated limits, budget or PCB architecture.

## D. Flutter Android app — planned product scope

Current planning sources:

- [Product Scope](FeaturE_Scope_Documentations/mobile-app/PRODUCT_SCOPE.md)
- [Feature Catalogue](FeaturE_Scope_Documentations/mobile-app/FEATURE_CATALOGUE.md)
- [25-feature expansion](FeaturE_Scope_Documentations/mobile-app/FEATURE_EXPANSION_25.md)
- [12 detailed proposals + 5 future concepts](FeaturE_Scope_Documentations/mobile-app/FEATURE_EXPANSION_17.md)
- [Feasibility register](FeaturE_Scope_Documentations/mobile-app/FEASIBILITY_REGISTER.md)
- [Architecture proposal](FeaturE_Scope_Documentations/mobile-app/ARCHITECTURE_PROPOSAL.md)

| ID | Requirement | Status / constraint |
| --- | --- | --- |
| APP-PLATFORM-01 | Flutter/Dart, Android first. | Direction confirmed; Android target version TBD |
| APP-USABILITY-01 | Standalone utility features must not require a BT SHARE hardware hub. | Product direction; feature acceptance/OS limits pending |
| SOUND-01 | Equalizers & Sound Enhancers. | Planned; audio routes/OS support to verify |
| SOUND-02 | Audio Routing & Mixing. | Planned; permissions and OS support to verify |
| SOUND-03 | Per-App Volume Control. | Planned; Android third-party control not guaranteed |
| SOUND-04 | Sound Measuring & Analysis. | Planned; mic calibration/permissions to verify |
| SOUND-05 | Tuners & Metronomes. | Planned; precision/UX to specify |
| SOUND-06 | Ambient & Focus Sounds. | Planned; sound rights/background rules to verify |
| SOUND-07 | Hearing Assistance. | Planned; safety/latency/claim review needed |
| SOUND-SYNC-01 | Minimize timing variation across supported devices. | Goal only; scenarios/measurement/sync method unverified |
| HUB-APP-01 | BLE control/status through ESP32. | GATT contract not frozen; APP-F01–F12 provisional |
| HUB-LIMIT-01 | Respect two-receiver target of original college prototype. | Prototype-only limit, not commercial product ceiling |
| APP-X01–APP-X25 | Include 25 additional feature concepts in the backlog. | Selected scope, not implemented; APP-X21–X25 future candidates |
| APP-X26 | Smart Connection Recovery tracked separately. | Planned; ESP32 remains authoritative on hub states |
| APP-Y01–APP-Y12 | Twelve detailed audio workspace proposals (five introduce distinct new tool families; seven refine overlapping scope). | Planned; deduplicate implementation and keep feasibility gates |
| APP-Y13–APP-Y17 | Five future audio concepts. | Roadmap, not MVP promise |
| APP-NAV-01 | Five-destination Connect / Sound Lab / Studio / Practice / My Sound concept. | UX proposal only |
| APP-GATT-01 | Hub-dependent functions use a reviewed versioned BLE contract. | Contract pending |
| APP-PRIVACY-01 | Appropriate permission, privacy and safety controls for recordings, microphone and hearing-related functions. | Detailed acceptance pending |
| APP-AUDIOPATH-01 | Phone-owned audio utilities do not automatically process externally supplied AUX audio. | Architectural boundary documented |
| APP-ARCH-01 | Flutter TRD/SDD/ADR-005 propose **Feature-first Clean Architecture + MVVM-style presentation**, with **Riverpod** suggested. DDD principles are an additional proposal. | **NOT APPROVED / NOT IMPLEMENTED IN SUPPLIED CHECKOUT** |

**Architecture evidence:** The supplied clone contains **14 normal tracked Flutter specification documents**. See the [TRD](BT_SHARE_Flutter_Documentation/03_TRD_Technical_Requirements.md), [SDD](BT_SHARE_Flutter_Documentation/04_SDD_Software_Design.md) and [ADR-005](BT_SHARE_Flutter_Documentation/11_ADR_Architecture_Decision_Records.md). Clean Architecture/MVVM/Riverpod are **proposed**, while explicit DDD adoption requires additional approval.

## E. Angular website / secure admin / APK release planning

Source: [Website Requirements](BT_SHARE_Website_Documentation/WEBSITE_REQUIREMENTS.md), [Website Feature Catalogue](BT_SHARE_Website_Documentation/WEBSITE_FEATURE_CATALOGUE.md), [Website Architecture](BT_SHARE_Website_Documentation/WEBSITE_ARCHITECTURE.md).

| ID | Requirement | Status |
| --- | --- | --- |
| WEB-F01–WEB-F04 | Angular homepage, product and app catalogue with truthful published status. | Planned, not implemented |
| WEB-F05–WEB-F06 | Public controlled documentation with draft/publish distinction. | Planned |
| WEB-F07–WEB-F10 | Signed APK release centre, SHA-256, provenance, versions, approval/revoke. | Planned; no APK evidenced |
| WEB-F11–WEB-F17 | Separate secure admin, server-verified roles, editors, approvals and audit log. | Planned; backend/provider TBD |
| WEB-F18–WEB-F20 | Errors/empty states, contact/support and responsive accessible experiences. | Planned |
| WEB-N01–WEB-N10 | Security, privacy, accessibility, testing and deployment controls from the website spec. | Must be proven before production |
| WEB-BRAND-01 | Present the X10 THINK → ZAEROX → BT SHARE hierarchy and owner-supplied brand artwork. | Documentation ready; website implementation pending |

**Explicitly not inferred:** deployed Angular/Flutter software, working backend, public APK, production device, approved prices, regulation/trademark clearance or an available full multi-listener architecture.

## F. Requirements that still need freeze / objective evidence

- Current native KiCad revisions, BOM and power corrections, manufacturer BM83 documents and hardware test gates.
- Commercial Bluetooth input and receiver-count feasibility through engineering analysis and real tests.
- Sign off Flutter ADR-005 (feature-first Clean Architecture/MVVM and state management), separately resolve DDD, MVP priority, Android SDK, BLE contract, UI journeys and OS capabilities.
- Website backend/identity/storage, release signing and CI provenance, privacy/accessibility/security testing.
- Owners and reviewers for every approved change; link progress to evidence, not a document claim.

See [Project Status](PROJECT_STATUS.md), [Decision Register](DECISIONS.md) and [Project Workflow](PROJECT_WORKFLOW.md).
