# CertNode: Verified Nonfiction Trust System

**CertNode** is a sovereign, runtime-sealed certification infrastructure for nonfiction outputs. It provides structural validation, immutable traceability, and verifiable authorship for documents published across digital and federated environments.

This repository contains the public trust layer and runtime assets used to deploy, verify, and inspect CertNode-issued certifications.

---

## Contents

| File | Description |
|------|-------------|
| `index.html` | Public homepage |
| `vault.html` | Certified document vault viewer |
| `ics_registry.html` | ICS hash registry display |
| `ledger.html` | Chronological trust ledger |
| `constitution.html` | Governance constitution viewer |
| `signature.html` | Runtime signature manifest |
| `capsule.html` | Final Authority Capsule download link |
| `badge.html` | Trust badge generator interface |

| Trust Files | Purpose |
|-------------|---------|
| `vault.json` | Live certified document list |
| `ics_registry.json` | ICS ID registry for certification lookup |
| `vault_ledger.jsonl` | Immutable certification ledger (append-only) |
| `runtime_snapshot.json` | Versioned metadata of the active trust system |
| `signature_manifest.json` | SHA256 seal of trust components |
| `certificate_template.pdf` | Branded PDF trust certificate scaffold |
| `governance_constitution.txt` | Structural and licensing constitution |
| `seal.png` | Visual trust badge icon |

---

## Verification + Certification

- Each output certified by CertNode includes an **ICS identifier**, metadata seal, and inclusion in the public ledger.
- Verifiers can access `/vault.html` or `/signature.html` to inspect runtime traceability.
- The trust ledger (`vault_ledger.jsonl`) forms the canonical chain of certification events.

---

## Federation + Licensing

Federated vault operators may:
- Maintain their own `vault.json` under the CertNode schema
- Participate in sync and registry coordination
- Follow licensing terms defined in the governance constitution

To request federation or become a recognized certification partner, contact the CertNode operator listed on the public site.

---

## Legal + Trust Status

This repository is part of the **CertNode Final Authority Trust Capsule (v3.9)**.  
It is sealed, cryptographically traceable, and runtime-frozen.

- All certification logic and governance terms are bound to this version unless superseded by an explicitly declared update.
- Redistribution, licensing, and federation are subject to the terms inside `governance_constitution.txt`.

---

© 2025 CertNode. All rights reserved.