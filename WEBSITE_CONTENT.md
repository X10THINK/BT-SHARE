# Website Content Register — Draft

## Homepage
- Verified brand identity and official tagline (not auto-invented).
- What BT SHARE solves: audio-sharing prototype and software tools.
- Two clear paths: Explore Products; See Mobile App / Downloads.
- State whether prototype features are planned/tested/released.

## Hardware Product Detail
- Name, current version/status, what the hub accepts as source, receiver support, supported Bluetooth profiles, diagrams and honest limitations.
- Current repository prototype describes stereo AUX input → BM83 → **target two** Bluetooth A2DP sinks. This remains a **target**, not a verified shipped capability.
- Future receiver expansion and optional Bluetooth-input modes must not be represented as verified baseline without an approved updated architecture and tests.

## Mobile Application Detail
- Flutter Android app is planned as a standalone audio workspace plus hub control.
- Pull feature descriptions from `docs/mobile-app/FEATURE_CATALOGUE.md`, `FEATURE_EXPANSION_25.md`, and `FEATURE_EXPANSION_17.md`.
- Distinguish app-owned audio features from hub hardware control, and identify Android/firmware-limited features.
- Only link APKs that are approved and actually published in release system.

## Documentation
- Start with public-safe guides such as quick start, mobile setup, supported devices, pairing guide, release notes, troubleshooting and safety.
- Internal engineering designs, supplier quotes, private secrets, unpublished source, credentials or drafts are not automatically public documentation.
- Every document has owner, target product, version, status, approver, published date and revision history.

## Downloads
- Application, version name/code, release channel, signature provenance, SHA-256, build date/publish date, size, architecture, minimum Android, notes, warnings.
- Download page must explain Android sideload warning and encourage only verified official APK releases.

## Admin-managed content
- About/contact, product and application records, media, published documentation and releases. All content requiring legal review remains draft until approved.
