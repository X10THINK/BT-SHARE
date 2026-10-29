# BT SHARE Android App — Proposed Architecture

**Date:** 2026-10-29
**Decision status:** **PROPOSED — NOT APPROVED**
**Context:** This clone contains the 14 Flutter handover documents as ordinary Git-tracked files. Its [TRD](../../BT_SHARE_Flutter_Documentation/03_TRD_Technical_Requirements.md), [SDD](../../BT_SHARE_Flutter_Documentation/04_SDD_Software_Design.md) and [ADR-005](../../BT_SHARE_Flutter_Documentation/11_ADR_Architecture_Decision_Records.md) already **propose** feature-first Clean Architecture, MVVM-style presentation and Riverpod; **DDD** is a compatible *additional* recommendation, not an explicitly accepted requirement. Do not duplicate the existing ADR or represent a proposal as approval.

## Proposed standard

**Feature-First + Clean Architecture + Domain-Driven Design (DDD) principles + Model–View–ViewModel (MVVM) + Riverpod**.

These concepts serve different purposes and are compatible:

- **Feature-first:** group source code around user capabilities (hub control, device discovery, local player, presets, sound measurement, etc.).
- **Clean Architecture:** isolate business rules/domain interfaces from Flutter widgets, BLE plugins, Android services and databases.
- **DDD principles:** use meaningful entities, value objects, aggregates and bounded contexts for complex device/session/audio rules; **avoid forcing ceremonial DDD patterns on simple screens**.
- **MVVM:** screens/widgets render state and delegate user intent to presentation ViewModels/Notifiers.
- **Riverpod:** state and dependency composition; use consistent provider lifecycles and test overrides.

### Illustrative layout (not code already committed)

```text
lib/
  app/                         # Bootstrap, router, app-wide dependency wiring
  core/                        # Cross-cutting errors, logging, permissions, BLE abstractions
  features/
    hub_control/
      presentation/            # Pages, widgets, view models, UI state
      domain/                  # Entities, use cases, repository interfaces
      data/                    # BLE adapters, DTOs, mapping, implementations
    standalone_audio/
      presentation/
      domain/
      data/
  shared/                      # Truly reusable widgets and primitives only
```

## Critical integration boundary

- **Flutter ↔ ESP32:** BLE GATT *control* with a versioned contract, IDs, commands, events, states, timeouts and errors.
- **ESP32 ↔ BM83:** UART, controlled by embedded firmware. Flutter should **not** depend on BM83 raw AT commands.
- **AUX audio:** external audio follows the hub's physical audio path; Flutter-only equalization/visualization does not automatically alter it.
- **Standalone Android utilities:** depend on actually available Android audio routes/APIs/permissions; platform-specific implementations may be required.
- **State ownership:** ESP32 is authoritative for hub connection/device state; app ViewModels reflect the reported state, with explicit optimistic action handling where justified.

## Proposed approval checklist

- [x] Inspect the 14 tracked Flutter specs: TRD, SDD and ADR-005 identify the proposed feature-first Clean/MVVM/Riverpod combination; sign-off still pending.
- [ ] Obtain mobile-team approval for existing ADR-005 and separately determine whether DDD modeling is appropriate.
- [ ] Identify accepted state management patterns and a chosen Flutter/package version.
- [ ] Freeze MVP feature set, target minimum Android SDK, routing, storage and native audio integration constraints.
- [ ] Sign off the BLE GATT protocol between mobile and hardware teams; supply mocks and compatibility tests.
- [ ] Update Flutter ADR-005 and the main `DECISIONS.md` with actual reviewer approval, date and decision; avoid fabricated sign-off.

Until those items are complete, **do not claim this architecture is approved, in production, or implemented**.

Related documents: [Product Scope](PRODUCT_SCOPE.md) · [Feature Catalogue](FEATURE_CATALOGUE.md) · [Feasibility Register](FEASIBILITY_REGISTER.md) · [Decision Register](../../DECISIONS.md).
