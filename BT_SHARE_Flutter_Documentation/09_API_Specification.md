# API Specification — Flutter ↔ ESP32 BLE GATT (Provisional)

> **Project:** BT SHARE — Android Flutter App  
> **Version:** 0.1.0 | **Created:** 2026-10-28 | **Status:** Draft for review  
> **Document owner:** Embedded protocol owner / Flutter lead | **Approval:** Pending product/Flutter/embedded review  
> **Evidence boundary:** Based on repository `main` reviewed 2026-10-28; this is a proposed, executable specification, **not proof of working code, firmware, hardware, or tests**.

## 1. API boundary and approval status
**This is a design proposal, not a frozen or implemented BLE contract.** Bluetooth service/characteristic UUIDs, ESP32 command/event opcodes, firmware protocol bytes and BM83 host commands have **not been validated** in the source repository. All examples below are **illustrative application-level shapes**, not instructions to transmit unsupported messages to real hardware. A signed firmware/app contract replaces this document's proposals before coding to hardware.

**Transport:** Flutter Android acts as BLE GATT **client**; ESP32 acts as GATT **server**; ESP32 translates product-level operations to BM83 UART. Only approved product messages are visible in Flutter. External AUX audio is **not** carried via this BLE API.

## 2. Required GATT discovery information
| Field | Description | Current status |
|---|---|---|
| `SERVICE_UUID` | BT SHARE service UUID | **TBD by embedded team** |
| `COMMAND_CHARACTERISTIC_UUID` | Client-to-hub write path | **TBD** |
| `RESPONSE_CHARACTERISTIC_UUID` | Hub ack/error path | **TBD** |
| `EVENT_CHARACTERISTIC_UUID` | Hub state/scan notifications | **TBD** |
| `INFO_CHARACTERISTIC_UUID` | Protocol/capabilities/version | **TBD** |
| Write mode / notification behavior | Write-with-response vs without, notify/indicate, CCCD handling | **TBD and experimentally verified** |
| Security | Pairing/bonding, GATT auth/encryption, authorization model | **TBD; threat review required** |
| Frame format / MTU | JSON vs binary, fragmentation, max payload and retry policy | **TBD; do not assume 512-byte messages** |

## 3. Negotiation and compatibility
After BLE link establishment: discover approved service → subscribe to events/response channels → obtain `protocol_major.minor` and `capabilities` → validate supported revision → request complete state snapshot → permit supported commands. If major revision incompatible, disable controls and show meaningful firmware update guidance; never guess commands or assume all features.

### Proposed capability keys (contract candidates, not reported facts)
`can_scan_receivers`, `max_active_receivers`, `can_pair`, `can_connect`, `can_report_streaming`, `can_set_per_receiver_volume`, `can_report_link_metrics`, `can_report_fw_version`, `can_update_firmware`, `can_report_audio_timing`. Default for absent/unknown capability is **unsupported**, not `true`. For college prototype UI, `max_active_receivers` cannot bypass an approved two-slot restriction merely because an unverified field says a larger number.

## 4. Illustrative envelope (not executable wire specification)
```json
{
  "schema": "btshare.gatt.proposal.v0",
  "request_id": "2b4c64b2-illustrative-id",
  "type": "command",
  "operation": "receiver.scan",
  "target_id": null,
  "args": {}
}
```
A hypothetical reply:
```json
{
  "schema": "btshare.gatt.proposal.v0",
  "request_id": "2b4c64b2-illustrative-id",
  "type": "response",
  "result": "accepted",
  "error": null
}
```
**IMPORTANT:** The string `btshare.gatt.proposal.v0` and operation names are examples only; firmware has not committed to JSON, request IDs or these values. Receiving `accepted` is **not** the same as receiver successfully connecting or streaming. An authoritative later event/snapshot must confirm the state.

## 5. Proposed command catalogue — firmware approval required
| App operation | Related IDs | Request concept | Expected response/event concept |
|---|---|---|---|
| `hub.get_info` | APP-F01 | Read protocol, firmware and supported flags | Version + capability snapshot |
| `hub.get_state` | APP-F10 | Refresh state after connection/reconnect | Hub + receiver states with freshness |
| `receiver.scan` | APP-F02/F03 | Start bounded discovery | scan progress/results/end/error |
| `receiver.select` | APP-F04/F05 | Assign unique receiver to slot 1/2 | authoritative assignment event or rejection |
| `receiver.pair` | APP-F06 | Request pairing of selected ID | pending/success/failure event |
| `receiver.connect` | APP-F07 | Request A2DP sink connection | connection events |
| `receiver.disconnect` | APP-F08 | Request specific link disconnection | disconnect event |
| `receiver.reconnect` | APP-F09/X26 | Request eligible reconnect | retry/connection outcome |
| `receiver.set_volume` | APP-X06 | Receiver-specific volume | **Only if hardware flag verified** |
| `diagnostics.get` | APP-F12/X08 | Bounded status/counters | Only data firmware actually supplies |
| `firmware.update` | APP-X25 | Firmware update flow | **Future only: never enable without safe/authenticated OTA design** |

No `audio.stream`, `audio.capture_aux`, `latency.auto_correct` or `receiver.3plus` command is accepted in this prototype without separate technical approval.

## 6. Receiver object and state semantics — candidate normalized fields
```json
{
  "receiver_id": "opaque-from-esp32",
  "display_name": "Receiver A",
  "slot": 1,
  "pairing_state": "paired",
  "link_state": "connected",
  "stream_state": "unknown",
  "last_reported_utc": "2026-10-28T12:00:00Z"
}
```
The client may store a local alias separately; alias is **not** the Bluetooth device name. State enum candidates: `UNKNOWN, DISCOVERED, SELECTED, PAIRING, PAIRED, CONNECTING, CONNECTED, STREAMING, DISCONNECTED, FAILED, RETRYING`. Embedded owner must specify which combinations/events are observable, which fields are nullable and whether source state maps cleanly to one enum or separate axes. Time should use a documented clock or relative time basis, not fabricate accuracy from an ESP32 timestamp.

## 7. Error model
| Proposed code | Meaning | UI action |
|---|---|---|
| `PERMISSION_REQUIRED` | Android permission missing (client-side, not firmware) | Explain/request permission |
| `BLE_DISABLED` | Radio switched off (client-side) | Enable Bluetooth |
| `HUB_NOT_READY` | Firmware not ready for command | Retry when ready |
| `PROTOCOL_MISMATCH` | Client/firmware versions incompatible | Explain/update via approved channel |
| `MAX_RECEIVERS` | Two-slot capacity reached for current build | Show limit, allow replace/disconnect |
| `RECEIVER_NOT_FOUND` | Requested opaque ID unknown | Refresh scan |
| `PAIR_FAILED` | Pairing failed | Support troubleshooting |
| `CONNECT_TIMEOUT` | Connection did not complete | Recover/retry thoughtfully |
| `COMMAND_UNSUPPORTED` | Requested operation not supported | Disable capability-dependent control |
| `HUB_LINK_LOST` | BLE link lost | Mark snapshots stale and reconnect |
| `INTERNAL_ERROR` | Unexpected firmware failure | Show safe message, redacted diagnostics |
These identifiers require joint approval; do not hardcode as actual firmware error values yet.

## 8. Protocol robustness and sequencing
- One command should have a unique correlation ID **if the firmware supports IDs**; otherwise specify compatible serialized command flow.
- Define timeout per operation and async discovery events; connection result may take longer than command receipt.
- Specify fragmented payload handling based on negotiated MTU and codec; validate length/CRC if selected.
- On reconnect, invalidate old request session, resubscribe and read authoritative snapshot; ignore old/stale notifications.
- If retries occur, explicitly specify idempotent actions and prevent duplicated pairing/connect operations.
- Sanitize receiver names and user-controlled strings; enforce maximum lengths and reject malformed/corrupt payloads.
- GATT must not depend on a cloud REST API; Angular website backend is a **separate system**, not this BLE protocol.

## 9. API freeze checklist for embedded + Flutter teams
- Exact hub firmware/AT revision and manufacturer-proven capabilities.
- UUIDs, characteristic properties, permissions, BLE security, packet encoding and size.
- Command/event dictionary, payload schemas, version migration, error/status codes.
- Snapshot/event ordering, ack vs completion semantics, timeouts, cancellation, reconnection and history retention.
- Test vectors (valid/invalid) and a fake GATT server/client with both teams running shared fixtures.
- Real-device acceptance: F01..F11 with logs, two-slot enforcement and no false streaming reports.

## Source references and document control

- [overview](https://github.com/X10THINK/BT-SHARE/blob/main/README.md)
- [status](https://github.com/X10THINK/BT-SHARE/blob/main/PROJECT_STATUS.md)
- [requirements](https://github.com/X10THINK/BT-SHARE/blob/main/REQUIREMENTS.md)
- [decisions](https://github.com/X10THINK/BT-SHARE/blob/main/DECISIONS.md)
- [brd](https://github.com/X10THINK/BT-SHARE/blob/main/Basic%20Documents/MD/BT_SHARE_BRD.md)
- [plan](https://github.com/X10THINK/BT-SHARE/blob/main/Basic%20Documents/MD/BT_SHARE_Execution_Plan.md)
- [catalogue](https://github.com/X10THINK/BT-SHARE/blob/main/docs/mobile-app/FEATURE_CATALOGUE.md)
- [x25](https://github.com/X10THINK/BT-SHARE/blob/main/docs/mobile-app/FEATURE_EXPANSION_25.md)
- [y17](https://github.com/X10THINK/BT-SHARE/blob/main/docs/mobile-app/FEATURE_EXPANSION_17.md)
- [feasibility](https://github.com/X10THINK/BT-SHARE/blob/main/docs/mobile-app/FEASIBILITY_REGISTER.md)
- [product](https://github.com/X10THINK/BT-SHARE/blob/main/docs/mobile-app/PRODUCT_SCOPE.md)

**Change control:** Before implementation, confirm current source commit, product scope, prototype firmware capabilities, Android device matrix, ownership and acceptance criteria. Revisions must log approver, date and affected requirement IDs. The existing repository baseline remains authoritative for recorded historical decisions; this new pack does not silently supersede it.
