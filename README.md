# BT SHARE — Engineering Second Brain

**Central knowledge repository for the BT SHARE Multi-Bluetooth Audio Hub prototype**

BT SHARE is a hardware-first proof-of-concept designed to take **one stereo AUX/line-level audio source** and transmit the same audio program to **two independent Bluetooth Classic A2DP sink devices simultaneously**. This repository serves as the project's **engineering second brain**: a version-controlled home for requirements, approved architecture, design references, decisions, firmware, PCB files, integration contracts, test evidence, and handover material.

> **Project status:** Documentation and execution baseline established; hardware delivery was pending when the execution plan was written (06 October 2026). Update this status as work progresses. This README does **not** claim that dual-device audio has already been demonstrated.

## Project objective

Prove that a single **BM83-based audio transmitter** can deliver audio from one AUX source to **two Bluetooth receivers at once**, with reliable discovery, pairing, connection, disconnection, state reporting, and recovery. Prove the two-receiver hardware path **before** integrating the separate Flutter mobile app.

### System architecture

```text
                   CONTROL PATH
              Flutter Mobile App
                      |
                   BLE GATT
                      |
               ESP32 DevKit V1
            (control + device state)
                      |
                UART host link
                      |
                BM83SM1-00TA
               (A2DP Source/TX)
                /           \
               /             \
     Bluetooth Receiver 1   Bluetooth Receiver 2
        (A2DP Sink)           (A2DP Sink)
                      ^
                      |
             Stereo AUX / Line-In
                  AUDIO PATH
```

**Two independent paths:**

- **Audio:** Stereo AUX/line-level input → BM83 → Bluetooth Classic A2DP/SBC → two receivers.
- **Control:** Flutter app → BLE GATT → ESP32 → UART → BM83.

The **phone does not carry or relay audio**. The **ESP32** owns product-level device and connection state, while the **BM83** handles Bluetooth audio. The Flutter app presents controls and status; BM83-specific host commands are hidden behind the ESP32 integration interface.

## Prototype baseline

| Area | Agreed baseline |
| --- | --- |
| Project | BT SHARE — Multi-Bluetooth Audio Hub |
| Primary milestone | One AUX source audible on two Bluetooth A2DP sink devices simultaneously |
| Bluetooth audio engine | BM83SM1-00TA, selected AT firmware / A2DP Source / TX / SBC / Dual Link configuration |
| Controller | ESP32 DevKit V1 |
| Hardware-to-controller | UART |
| App-to-controller | BLE GATT |
| Mobile application | Flutter, developed by a separate team |
| PCB approach | Team-designed minimal BM83 carrier board; no official BM83 evaluation board in the approved prototype scope |
| Procurement ceiling | **LKR 40,000** |
| Release approach | Hardware-first, with measurable acceptance gates |

**Important:** Exact BM83 pin assignments, power limits, AT commands, firmware behavior and Dual Link support must be checked against the **approved documentation for the exact module and firmware**. Planning documents are not a substitute for this verification.

## In scope

- BM83 carrier schematic, PCB layout, fabrication and bring-up documentation.
- Safe module power, stereo line input, UART interface, control/recovery pins and test points.
- One-receiver audio proof, followed by the two-receiver Dual Link proof.
- ESP32 firmware for BM83 host communications, command parsing, device management, logging, retry/recovery and BLE GATT.
- A versioned, product-level BLE contract for the Flutter team: commands, events, device IDs, states and errors.
- Tests for compatibility, reconnection, range, long-running operation, latency observations and demonstration readiness.

## Out of scope for the first prototype

- Three to five simultaneous audio receivers.
- Auracast, LE Audio or BLE Audio Broadcast.
- Claims of perfectly synchronized receivers or zero latency.
- Production enclosure, battery product, RF certification or production-ready hardware.
- Sending audio through the Flutter phone.
- Flutter UI implementation as part of the hardware/embedded team's deliverables.

## Execution roadmap

The approved planning approach uses **gates**. Do not move to the next layer before the preceding acceptance criteria are met.

| Phase | Work | Exit gate |
| --- | --- | --- |
| P0 — Define | Freeze requirements, interfaces, references and constraints | G0: Design/baseline ready |
| P1 — Design | Carrier schematic, BOM reconciliation, PCB, RF review and manufacturing outputs | G0/G1: Reviewed design and checks |
| P2 — Build | Receive, inspect, assemble and electrically pre-check carrier | G1: Electrical ready |
| P3 — BM83 Bring-up | Verify UART response and selected firmware/host/TX/AUX configuration | G2: BM83 alive |
| P4 — One Device | Prove stable audio to one known-good receiver | G3: One-device audio |
| P5 — Two Devices | Prove same AUX program on both receivers | **G4: Two-device core proof** |
| P6 — ESP32 Host | Implement UART driver, parser, state and device-control flows | G5: ESP32 host control |
| P7 — BLE GATT | Test app-facing commands, notifications, states and errors | G6: BLE contract stable |
| P8 — Flutter | Integrate the separately developed app against the agreed contract | G7: Flutter integration |
| P9 — Validate | Run compatibility, reconnect, range, long-run, latency-observation and demo tests | G8: Validation/demo ready |

**Primary hardware success gate (G4):** Both receivers play the same input source simultaneously **without relying on Flutter**. Passing this gate must be backed by recorded evidence, not just a status label.

## Flutter integration boundary

The provisional app-facing feature baseline includes:

1. Connect to the BT SHARE hub and view hub readiness.
2. Scan and list discovered Bluetooth receivers.
3. Assign receivers to Device 1 and Device 2 slots; reject a third active selection/link.
4. Pair, connect, disconnect and request reconnection.
5. Display per-device pairing, connection, streaming and error states.
6. Optionally expose diagnostics for development.

The **final Flutter function catalogue and interface contract are not yet frozen** in the supplied BRD. Do not treat draft UUIDs, message formats or UI behaviors as approved until the teams sign off on the versioned contract.

### State and event principles

- **ESP32 is the source of truth** for discovered, selected, paired, connected and streaming state.
- Pairing and active connection are **different states**.
- Commands need validation, timeouts and structured errors.
- Important transitions and failures need traceable logs.
- An error or disconnect must lead to a known state rather than a silently frozen interface.

## Suggested repository organization

The following layout is a **proposal for organizing the second brain**, not a claim that these folders or files already exist:

```text
bt-share-second-brain/
├── README.md
├── docs/
│   ├── 00-source-documents/       # Approved BRD, execution plan, procurement documents
│   ├── 01-requirements/           # Requirement IDs, scope, acceptance matrix
│   ├── 02-architecture/           # Control/audio separation, interfaces, diagrams
│   ├── 03-bm83-reference/         # Verified datasheets, firmware capability notes, command matrix
│   ├── 04-hardware/               # Carrier interface, BOM, assembly guidance
│   ├── 05-firmware/               # ESP32 modules, state machine, UART/BM83 protocol
│   ├── 06-ble-flutter-contract/    # Versioned GATT API and team handover
│   ├── 07-tests/                  # Test protocols, logs, evidence, acceptance results
│   ├── 08-decisions/              # Engineering decisions, assumptions, change records
│   └── 09-progress/               # Milestones, blockers, open issues, meeting notes
├── hardware/
│   └── kicad/                     # KiCad source projects and manufacturing artifacts
├── firmware/
│   └── esp32/                     # ESP32 source code and tests
└── templates/                     # Reusable issue, experiment and test-record templates
```

Add only the directories you actually need, and preserve clear revision labels for controlled engineering material.

## How to use this second brain

1. **Start with the approved baseline.** Read the BRD and execution plan before interpreting supporting documents.
2. **Separate facts from hypotheses.** Mark unverified BM83 capabilities, assumptions and possible approaches explicitly.
3. **Track every requirement.** Reference IDs such as `BR-001`, `AUD-004`, `FW-003` and the corresponding tests.
4. **Record decisions and changes.** Include rationale, evidence, revision, reviewer and approval status; do not silently overwrite approved constraints.
5. **Keep engineering outputs reproducible.** Version schematic/PCB revisions, firmware, interface contracts and test conditions.
6. **Use evidence for gate completion.** Link logs, measurements, photos, test sheets and sign-off records.
7. **Distinguish planned vs completed.** A document describing a test is not proof the test passed.

### Guidance for AI assistants

This repository may be used as project context by AI coding and research assistants. Assistants should:

- Prefer the **latest approved BRD + Master Plan + Final Company Procurement Submission** when they conflict with older drafts.
- Ask for missing specifications rather than inventing BM83 pins, electrical limits, commands or firmware capabilities.
- Preserve the **two-receiver, hardware-first, LKR 40,000** prototype baseline unless a documented change is approved.
- Keep the UART/BM83 implementation separate from the Flutter-facing BLE contract.
- Cite the exact source file, revision and requirement ID when proposing a design or code change.
- Identify what is **verified**, **proposed**, **untested** or **blocked**.

## Source documents

Initial project materials provided for this repository:

- `final brd.pdf` — **BT SHARE: Multi-Bluetooth Audio Hub, Business Requirements Document**, hardware & embedded two-device prototype baseline, dated **06 October 2026**.
- `plan.pdf` — **BT SHARE: Hardware & Embedded Execution Planning**, working baseline dated **06 October 2026**.

The supplied documents also reference a **Final Company Procurement Submission** and original architecture material. Those references should be imported and checked separately before they are described as present in this repository.

## Definition of success

The prototype succeeds when the evidence shows that:

- The approved carrier and power interfaces are reviewed and safe for the selected hardware.
- Stereo AUX input is transmitted to **two** compatible Bluetooth A2DP receivers at the same time.
- The hardware works independently before the Flutter app is integrated.
- ESP32 can manage discovery, pairing, two-device connections, disconnection, recovery and authoritative state.
- Flutter can control and observe the hub over the agreed BLE GATT contract.
- Limitations, particularly device compatibility and audible latency differences, are honestly documented.
- Procurement remains within the approved prototype ceiling unless a change is approved.

---

**BT SHARE** · Hardware-first prototyping · Evidence-driven engineering · One source, two receivers
