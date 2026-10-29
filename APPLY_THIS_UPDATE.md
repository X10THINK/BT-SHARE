# BT SHARE — Final Updated Clone: How to Use

**Prepared:** 2026-10-29
**Based on uploaded local Git clone:** `bc5f287d57917f3c1b5945cbcfa61f9de8bbf1be` (`main`)
**Repository:** https://github.com/X10THINK/BT-SHARE

This archive is a **complete updated copy of the user's cloned repository**, not a documentation-only patch. It includes the original `.git` directory, all 14 tracked Flutter specification documents, website documents, hardware planning PDFs/Markdown and images, plus the new brand assets and refreshed documentation. The new edits are deliberately **uncommitted and not pushed**; the user retains control over publishing.

## What's been changed

- New GitHub README with genuine BT SHARE and ZAEROX logo images; **X10 THINK** is clearly credited as the founding company, **ZAEROX** as the technology brand, and **BT SHARE** as the product.
- Added `BRAND_IDENTITY.md`, `PROJECT_WORKFLOW.md`, website branding guide, mobile architecture extension proposal and six original logo variants.
- Updated `PROJECT_STATUS.md`, `REQUIREMENTS.md`, `DECISIONS.md`, website content and website UI/UX planning to separate completed documentation from unverified hardware/software milestones.
- Preserved and **read all 14 Flutter documents** already in the uploaded clone: `03_TRD`, `04_SDD` and `11_ADR` propose feature-first Clean Architecture, MVVM-style presentation and Riverpod. DDD is an additional recommendation pending approval, **not** an existing official architectural decision.
- Repaired outdated document references to renamed directories, including the 14 Flutter specs' GitHub links to old paths. `python scripts/repair_repository_links.py --check` verified **325 local Markdown/HTML links with zero broken** in the final checkout.
- Verified all six PNG images are readable, replacing a truncated draft asset with the actual original upload.

**Preserved:** original hardware BRD/execution plans, existing Flutter/website planning docs, commit history, user-supplied images and existing repository structure. Historical technical limitations and approval gates are not rewritten as completed work. The 14 Flutter documents in this clone are **ordinary Git-tracked files**, not the earlier problematic gitlink.

## Update your GitHub repository (Windows PowerShell or Terminal)

1. Extract the ZIP. Open the included `BT-SHARE` folder. It already includes `.git`, so **do not clone again or copy it into another nested BT-SHARE folder**. Keep your existing checkout backed up if it has other unpushed changes.
2. Open a terminal in this extracted `BT-SHARE` folder.
3. Review the proposed edits and run checks:

```powershell
git status --short
python scripts/repair_repository_links.py --check
git diff --check
git diff --stat
```

4. To make a reviewable branch and push it:

```powershell
git switch -c docs/zaerox-btshare-2026-10-29
git add -A
git diff --cached --check
git commit -m "docs: complete BT SHARE ZAEROX branding and project documentation"
git push -u origin docs/zaerox-btshare-2026-10-29
```

5. Open a pull request on GitHub from that branch to `main`, inspect the diff, then merge when the team approves. **No purchase, PCB fabrication, software release or deploy is authorized by this document update.**

If Git asks for login, authenticate with your own GitHub account. If the remote branch has advanced since the uploaded clone, fetch and reconcile changes rather than force-pushing. The linked account in the earlier conversation had read-only permissions; the local archive can be pushed with a GitHub account having permission.

## Architecture: what the documents actually say

| Concept | Source | Status |
| --- | --- | --- |
| Flutter/Dart Android first | Existing app scope and Flutter ADR-001 | Recorded product choice |
| Feature-first Clean Architecture | `BT_SHARE_Flutter_Documentation/03_TRD_Technical_Requirements.md`, `04_SDD_Software_Design.md`, ADR-005 | Proposed, not signed off |
| MVVM | Same TRD/SDD/ADR-005 | Proposed |
| Riverpod | TRD "suggested", SDD/ADR-005 candidate | Proposed |
| DDD principles | `FeaturE_Scope_Documentations/mobile-app/ARCHITECTURE_PROPOSAL.md` (added in this update) | Recommended addition, **not approved** |

The Flutter team should ratify the existing ADR-005 instead of blindly replacing it with an asserted decision.

## Important limitations

- **No executable Flutter, Angular, ESP32 firmware or native KiCad engineering source** is present in this uploaded clone. The repository mostly contains planning/specification materials and assets.
- No source-backed claim is made that simultaneous two-receiver audio, Bluetooth input, 3+ listeners, synchronization, hardware manufacturing, APK release or live website deployment has been demonstrated.
- The historical **LKR 40,000** figure is not a verified spending balance; this update does not authorize orders or payments.
- No other repo folders or source PDFs were intentionally deleted.

For the details see [Project status](PROJECT_STATUS.md), [Decision register](DECISIONS.md), [Requirements](REQUIREMENTS.md) and [Project workflow](PROJECT_WORKFLOW.md).
