# UAT Plan — User Acceptance Testing

> **Project:** BT SHARE — Android Flutter App  
> **Version:** 0.1.0 | **Created:** 2026-10-28 | **Status:** Draft for review  
> **Document owner:** QA/UAT lead / Product owner | **Approval:** Pending product/Flutter/embedded review  
> **Evidence boundary:** Based on repository `main` reviewed 2026-10-28; this is a proposed, executable specification, **not proof of working code, firmware, hardware, or tests**.

## 1. Purpose and user groups
UAT checks whether users can accomplish the **approved release scope**, not whether mocks demonstrate hardware capability. Participants: novice sound-utility user, hardware owner, accessibility/large-text user, Tamil/English user where available, and a support/QA observer. Record participant consent and privacy of any user recordings.

## 2. Entry criteria
- Frozen PRD/SRS release requirements with named approvers and known exclusions.
- Signed APK candidate build, version/commit, test devices, release notes, no known blocker bugs.
- Approved BLE protocol and real hub if hardware-control claims are under UAT; hardware G3/G4 evidence available for simultaneous listening claim.
- Licensed sample media, safe test audio, headphone pair(s), hub firmware/board identifiers, recovery scripts, permission-denial test setup.
- Accessible test instructions and relevant approved localization.

## 3. UAT scenarios and expected outcomes
| UAT ID | Scenario / steps | Expected result | Linked requirements | Hardware? |
|---|---|---|---|---|
| UAT-01 | Install app → launch without hub or account → use standalone tools | No forced account/hub pairing; tools accessible | BIZ-02/SRS-A01 | No |
| UAT-02 | Turn Bluetooth off → open Connect → follow guidance | Honest Bluetooth-off state, no crash; other tools usable | APP-F01 | No |
| UAT-03 | Deny Bluetooth permission then re-enable via OS | Explains denial and recovers on return | APP-F01/X19 | Hub for complete flow |
| UAT-04 | Scan for hub → connect → open receiver control | Displays firmware-confirmed readiness and snapshot | APP-F01/F10 | Yes |
| UAT-05 | Scan sinks → select first/second receiver → pair and connect | Hub-reported statuses accurate; both slots distinct | APP-F02..F07 | Yes |
| UAT-06 | Try to select a third active receiver | Clear two-slot limit; no unsupported GATT action | APP-F05 | Yes/mock validation |
| UAT-07 | Disconnect one receiver → request reconnect | Receiver-specific status and errors; other status not fabricated | APP-F08/F09/X26 | Yes |
| UAT-08 | Turn hub power off while receiver card says streaming | UI changes to hub disconnected/receiver status stale | APP-F10/X05 | Yes |
| UAT-09 | Attempt unsupported per-receiver volume on hub lacking capability | Control absent/disabled with explanation | APP-X06 | Yes/fake hub |
| UAT-10 | Play local user-selected track; pause/seek/restart | Playback stable and route correctly indicated | APP-Y10 | No |
| UAT-11 | Apply EQ preset on app-owned track and disable it | Audible/parameter effect only on permitted source | APP-X01/Y08 | No |
| UAT-12 | Mix two licensed ambient tracks, set timer, background app | Expected volume/timer/interrupt behavior | APP-X12/Y06 | No |
| UAT-13 | Refuse mic permission, then grant and make recording | No hidden recording; clip saved locally only after consent | APP-X13/Y02/X19 | No |
| UAT-14 | Delete local recording and selected history | Confirmation; data removed or partial failure reported | APP-X19/Y17 | No |
| UAT-15 | Activate large text, TalkBack and dark theme | Navigation/readouts/tap targets usable; no state only via color | APP-X15/X18 | No |
| UAT-16 | Switch to Tamil and back (if localized in release) | Reviewed labels usable and not clipped | APP-X18 | No |
| UAT-17 | Remove local media permission/file while in playlist | Graceful unavailable state; reselect flow | APP-Y10 | No |
| UAT-18 | Test hub audio on mixed headphones and capture observer notes | Separate bench result for actual dual output; no false sync claim | AUD-004/SOUND-SYNC-01 | Yes + embedded test |
| UAT-19 | Open diagnostics, export with consent, inspect artifact | Clear useful message, no secrets/private audio export | APP-X17/F12 | Optional hub |
| UAT-20 | Use airplane/offline mode with approved standalone functions | Functions documented offline still operate | APP-Y17/SRS-A01 | No |

## 4. Execution instructions
1. Tester receives a fresh install or documented upgrade setup, known device/firmware versions, and scenario card **without hidden developer intervention**.
2. Observe taps, confusion, permission prompts, failures and recovery; record duration only if measuring a defined usability target.
3. Record `pass/fail/blocked/not applicable`, app version/commit, phone OS/model, firmware, receiver models, actual vs expected and attachments.
4. Blocked or N/A is **not** a pass. Rescope or resolve each release-blocking failure with documented owner and re-test.
5. If hardware is unavailable, do **not** mark hardware test cases passed based on simulator alone.

## 5. Proposed defect severities
- **Blocker:** app unusable in approved core function, unauthorized recording, corrupt data/unsafe sound, misleading hardware audio claim or bad APK signature.
- **Critical:** core hub command wrong receiver, recurrent crash, unfixable access denial, leakage of sensitive diagnostics.
- **Major:** feature fails common intended journey but safe workaround exists.
- **Minor:** polish/accessibility issue not preventing agreed critical task; scope by severity and user impact.

## 6. Exit/signoff criteria
All **included release-blocking** UAT cases pass on the approved matrix; no blocker/critical open issue; major defects have documented disposition and product-owner acceptance; privacy/security/accessibility gate passed; installation and upgrade verified; hardware-dependent claims backed by real tested hardware. Completion requires sign-off by product owner, QA lead, Flutter lead and embedded lead for hub-related content. Signature/date fields intentionally left blank.

| Approver | Name | Date | Outcome / evidence |
|---|---|---|---|
| Product owner | TBD | TBD | Pending |
| Flutter lead | TBD | TBD | Pending |
| QA lead | TBD | TBD | Pending |
| Embedded lead (hub only) | TBD | TBD | Pending |
| Privacy/security reviewer | TBD | TBD | Pending |

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
