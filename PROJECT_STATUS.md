# Project Status

## Project Name
BT SHARE — Multi-Bluetooth Audio Hub (Hardware & Embedded Prototype)

## Project Goal
The ultimate goal of BT SHARE is to develop a multi-device Bluetooth audio-sharing system that allows multiple receiving devices to play audio from one source simultaneously.

The current college prototype is limited to two simultaneous Bluetooth receivers because of budget constraints.

This prototype serves as an initial proof of concept for the broader multi-device vision. Supporting additional receivers will require further hardware and protocol research.

## Current Stage
**Planning / pre-build engineering (last documented baseline; current execution progress unverified).**

The execution plan dated **2026-10-06** records: BRD ready, final purchase list ready, procurement ready/submitted, hardware delivery pending, and pre-arrival engineering work to start immediately. No later completion evidence was provided with the source documents. This file does **not** assert that a design, firmware, hardware, or test gate has passed.

## Completed Work
*Documented planning deliverables only; completion does not imply physical implementation:*
- [x] Hardware and Embedded Prototype BRD prepared (working baseline, 2026-10-06).
- [x] Hardware & Embedded Execution Plan prepared (working baseline, 2026-10-06).
- [x] Initial architecture, exactly-two-receiver prototype target, hardware/Flutter responsibility split, and LKR 40,000 procurement ceiling documented.
- [x] Final procurement list recorded as ready/submitted **in the execution plan** (delivery and purchase fulfillment not verified).

## Work in Progress

## Flutter Android Application — Product Scope Status

**Last scope review:** 2026-10-15

**Current Stage:** Requirements planning and feasibility review.

### Completed Planning

- [x] Android-first development with Flutter and Dart confirmed.
- [x] Standalone sound utilities for users without BT SHARE hardware included.
- [x] Seven sound utility categories selected.
- [x] Original BT SHARE hardware-control feature catalogue documented.
- [x] 25 additional sound application features selected.
- [x] Smart Connection Recovery recorded.
- [x] 12 additional audio-workspace proposals included.
- [x] 5 future feature concepts included in the roadmap.
- [x] Multi-device sound synchronization recorded as a product goal.

### Pending Software Work

- [ ] Select Android minimum SDK and supported devices.
- [ ] Finalize first-release (MVP) requirements.
- [ ] Validate Android audio APIs, permissions, and limitations.
- [ ] Define Flutter application architecture.
- [ ] Finalize app navigation and user journeys.
- [ ] Design and approve the UI/UX.
- [ ] Finalize the ESP32–Flutter BLE GATT contract.
- [ ] Define acceptance criteria and testing plans.
- [ ] Implement the Flutter application.
- [ ] Complete Android device testing and hardware integration.

**Important:** Planned features are not yet implemented or verified. The current college hardware prototype still targets two receivers, and no hardware acceptance gate is marked complete without test evidence.


*Planned or instructed to start in the execution baseline; actual progress needs team confirmation:*
- Pre-arrival hardware design: official BM83 document register, carrier interfaces, KiCad schematic, PCB layout and BOM reconciliation.
- ESP32 firmware planning: UART driver/protocol, command shell, state model, logging and mock testing.
- BLE GATT command/event contract definition with the parallel Flutter team.

## Pending Work
*Not verified as complete from the supplied documents:*
- [ ] Approve exact BM83SM1-00TA documentation, firmware capabilities, pinout, voltage requirements and supported commands.
- [ ] Review and release BM83 carrier schematic, PCB, antenna keep-out, ERC/DRC reports, Gerbers and assembly files.
- [ ] Receive, inspect and assemble parts; complete safe power/electrical checks.
- [ ] Verify BM83 UART control and documented transmitter/AUX configuration.
- [ ] Demonstrate stable AUX audio on one Bluetooth A2DP sink (G3).
- [ ] Demonstrate the same AUX audio simultaneously on two independent sinks (G4; primary hardware milestone).
- [ ] Implement and test ESP32 serial-controlled scan, pair, connect, disconnect, reconnect, state and error handling (G5).
- [ ] Validate the product-level BLE GATT contract independently of Flutter (G6).
- [ ] Integrate Flutter control/status after hardware proof (G7).
- [ ] Complete compatibility, reconnect, range, long-run, latency-observation and demo acceptance evidence (G8).

## Known Issues and Blockers
- **Hardware delivery:** Listed as pending on 2026-10-06; current delivery status unknown.
- **Flutter function catalogue:** Final function catalogue had not been issued at the BRD baseline; integration contract remains provisional until agreed.
- **BM83 technical feasibility:** Exact selected firmware support, Dual Link behavior, commands and electrical details must be confirmed against approved manufacturer documentation and actual tests; do not assume these are already verified.
- **No verified gate evidence supplied:** Current schematic, firmware build logs, procurement receipts and test results have not been provided for this status update.
- **Technical limitation:** Two active receivers are not a guarantee of synchronized playback; any latency differences and compatibility constraints must be observed and documented.

## Technology Stack
- **Frontend:** Android-first Flutter/Dart application, including hardware control and standalone sound utilities (planned).
- **Backend:** ESP32 embedded firmware: BM83 UART host control, device/state management and BLE GATT server. No cloud/server backend specified.
- **Database:** None specified or required by the approved prototype baseline; optional on-device persistence is only a future firmware interface consideration.
- **Deployment:** ESP32 firmware flashed to the development controller; BM83 configured with approved firmware; custom KiCad-designed BM83 carrier PCB; Flutter app integration after hardware gates. No hosted/cloud deployment specified.
- **Hardware / interfaces:** BM83SM1-00TA, ESP32 DevKit V1, stereo 3.5 mm AUX/line-level input, UART, BLE GATT and Bluetooth Classic A2DP Source/SBC.
- **Engineering tools:** KiCad for schematic/PCB design; structured serial logs and documented hardware/protocol testing.

## Important Requirements
- Long-term vision: Support multiple simultaneous wireless audio receivers.
- Current prototype: Support two simultaneous Bluetooth Classic A2DP receivers.
- Reason for current limitation: College project budget constraints.
- Future expansion: Research hardware and protocols capable of supporting more than two receivers.
- The existing BM83-based design must not be assumed to support additional receivers without technical validation.
  
## Next Recommended Tasks
1. **Confirm the live status:** Ask workstream owners for current procurement delivery, KiCad schematic/PCB revisions, firmware commits and evidence of any passed gates. Update this file with verified facts.
2. **Complete the pre-arrival engineering pack:** Official BM83 document register and capability verification, carrier interface spec, reviewed schematic/PCB and schematic-to-BOM mapping.
3. **Prepare independent bring-up:** Compile/test the ESP32 mock firmware components, document the BM83 command/event matrix, and draft BLE interface + acceptance test sheets. Once parts arrive, progress strictly from electrical checks to BM83, one-device audio and two-device proof.

## Source of Truth
- See [`README.md`](README.md) for the project overview.
- **Primary supplied sources:** *BT SHARE — Hardware & Embedded Prototype BRD* (2026-10-06) and *BT SHARE — Hardware & Embedded Execution Planning* (2026-10-06).
- The execution plan also identifies the *Final Company Procurement Submission* as the purchasing authority; it was **not supplied for this update**.
- Refer to actual source code, KiCad design revisions, approval records, receipts and tests to verify implementation status. A plan is not evidence of completion.

## Last Updated
2026-10-14

> **Status confidence:** Document-based baseline only. Request an owner-verified update before using this file as a live execution dashboard.
