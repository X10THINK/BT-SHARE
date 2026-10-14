# Project Status

## Project Name
BT SHARE — Multi-Bluetooth Audio Hub (Hardware & Embedded Prototype)

## Project Goal
Build and validate a hardware-first proof-of-concept that accepts one stereo AUX/line-level audio source and transmits the same audio program simultaneously to **two independent Bluetooth Classic A2DP sink devices**. A BM83-based audio engine handles Bluetooth audio, an ESP32 manages host control and authoritative device state, and a separately developed Flutter application later provides control/status over BLE GATT. **Audio must never pass through the Flutter phone.**

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
- **Frontend:** Flutter mobile application (separate team; control and status only).
- **Backend:** ESP32 embedded firmware: BM83 UART host control, device/state management and BLE GATT server. No cloud/server backend specified.
- **Database:** None specified or required by the approved prototype baseline; optional on-device persistence is only a future firmware interface consideration.
- **Deployment:** ESP32 firmware flashed to the development controller; BM83 configured with approved firmware; custom KiCad-designed BM83 carrier PCB; Flutter app integration after hardware gates. No hosted/cloud deployment specified.
- **Hardware / interfaces:** BM83SM1-00TA, ESP32 DevKit V1, stereo 3.5 mm AUX/line-level input, UART, BLE GATT and Bluetooth Classic A2DP Source/SBC.
- **Engineering tools:** KiCad for schematic/PCB design; structured serial logs and documented hardware/protocol testing.

## Important Requirements
- Exactly **two simultaneous Bluetooth Classic A2DP sink receivers** in the first prototype, receiving the same stereo AUX program.
- **LKR 40,000** prototype procurement ceiling; budget changes require approval.
- **Hardware-first proof:** core two-device audio must work independently before Flutter integration.
- Strict paths: **Audio:** AUX → BM83 → two A2DP sinks. **Control:** Flutter → BLE GATT → ESP32 → UART → BM83.
- ESP32 is the product-level source of truth for discovered/selected/paired/connected/streaming device state; Flutter must not expose raw BM83 commands.
- Support discovery, pairing, connecting, disconnecting, reconnect policy, maximum-two limit, state/error reporting and structured diagnostics.
- Use only verified BM83 documentation for pins, voltage, firmware capabilities and protocol syntax.
- Do not claim zero latency or perfect synchronization; capture observed limitations.
- Out of scope: 3–5 simultaneous receivers, Auracast/LE Audio, battery/enclosure productization, production RF certification, and routing audio through Flutter.
- Every stage must pass an evidence-backed gate before proceeding; retain test logs, design reviews and artifacts.

## Next Recommended Tasks
1. **Confirm the live status:** Ask workstream owners for current procurement delivery, KiCad schematic/PCB revisions, firmware commits and evidence of any passed gates. Update this file with verified facts.
2. **Complete the pre-arrival engineering pack:** Official BM83 document register and capability verification, carrier interface spec, reviewed schematic/PCB and schematic-to-BOM mapping.
3. **Prepare independent bring-up:** Compile/test the ESP32 mock firmware components, document the BM83 command/event matrix, and draft BLE interface + acceptance test sheets. Once parts arrive, progress strictly from electrical checks to BM83, one-device audio and two-device proof.

## Source of Truth
- See [`README.md`](README.md) for the project overview.
- See [`REQUIREMENTS.md`](REQUIREMENTS.md) for approved requirements **when that file has been created and reviewed**.
- See [`DECISIONS.md`](DECISIONS.md) for technical decisions **when that file has been created and reviewed**.
- **Primary supplied sources:** *BT SHARE — Hardware & Embedded Prototype BRD* (2026-10-06) and *BT SHARE — Hardware & Embedded Execution Planning* (2026-10-06).
- The execution plan also identifies the *Final Company Procurement Submission* as the purchasing authority; it was **not supplied for this update**.
- Refer to actual source code, KiCad design revisions, approval records, receipts and tests to verify implementation status. A plan is not evidence of completion.

## Last Updated
2026-10-14

> **Status confidence:** Document-based baseline only. Request an owner-verified update before using this file as a live execution dashboard.
