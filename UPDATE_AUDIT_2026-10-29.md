# Final Clone Update — Verification Notes

**Date:** 2026-10-29
**Uploaded source:** `BT-SHARE.zip`, local Git HEAD `bc5f287d57917f3c1b5945cbcfa61f9de8bbf1be`.

## Scope of the update

This is a **reconciled full repository clone**, using the clone supplied by the owner rather than assuming the earlier GitHub snapshot contains the newest files. The previous README update overlay was merged and corrected against the newer source documents.

## Evidence corrections

1. **Flutter folder:** The earlier `c6d7cf6` GitHub snapshot held `BT_SHARE_Flutter_Documentation` as a gitlink. The owner-provided clone has newer commit `bc5f287` with **14 ordinary Git-tracked Markdown files** in that folder. The final update preserves all 14 and does not fabricate a missing-folder problem.
2. **Mobile architecture:** The Flutter TRD, SDD and ADR-005 explicitly **propose** Feature-first Clean Architecture with MVVM and Riverpod. **DDD** is absent as an explicit approved architecture decision; the new extension is clearly labeled PROPOSED.
3. **Documentation links:** Legacy paths referencing `Basic Documents` and `docs/mobile-app`, plus absolute GitHub links in the Flutter specs, have been fixed in the local checkout. The link check result is recorded below.
4. **Logos:** One previous draft `bt-share-logo-blue.png` was truncated. All six new brand-asset files were copied from the owner's original uploads and verified using an image decoder.
5. **Engineering progress:** No native KiCad source or reproducible BM83/ESP32/Flutter/Angular build and physical test evidence appears in the supplied archive. Completion/availability claims are therefore not inferred.

## Non-destructive policy

The original project source PDFs, historical engineering plans, feature catalogues and current Flutter handover specs remain included. Changes to original spec files are limited to correcting outdated link destinations. No paid receipts, approvals, hardware test results or source code were invented. No remote Git operation was performed.

## Validation results

- **14** Flutter handover documents preserved.
- **6** provided logo variants verified readable.
- **325** local Markdown and HTML references checked; **0** unresolved targets.
- Git checks, ZIP integrity and final file counts are validated when producing the release artifact.

To repeat the document-link check, run `python scripts/repair_repository_links.py --check` from the repository root.
