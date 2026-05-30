---
artifact_id: SEC-POLICY-SIGNED-RELEASE-001
title: Signed Release Policy
status: candidate
created: 2026-05-28
owner: council
tags: [security, release, signing, supply-chain]
---

# Signed Release Policy

> Defines requirements for signing releases and verifying artifact integrity.

status: candidate

---

## Why Sign Releases?

Signed releases enable users to verify that a release artifact was produced by the Atlas Lattice Foundation and has not been tampered with. This is a critical supply chain security control.

---

## What Gets Signed

| Artifact | Signing method | Format |
|----------|---------------|--------|
| GitHub Releases | GitHub's built-in release signing (GPG) | `.sigstore` or `.asc` |
| Python packages (if published) | Sigstore `cosign` | `.sigstore` |
| Schema bundles | SHA-256 checksum file + GPG signature | `SHA256SUMS`, `SHA256SUMS.asc` |
| SBOM | SHA-256 checksum | Included in release assets |

---

## Sigstore / Cosign (Preferred)

For software artifacts, use Sigstore's `cosign` for keyless signing via GitHub OIDC:

```bash
# Sign during GitHub Actions workflow
cosign sign-blob --yes --output-certificate cert.pem --output-signature sig.pem artifact.json
```

This creates a transparent, auditable signature entry in the Sigstore transparency log — no private key management required.

---

## Checksum Files

Every release must include a `SHA256SUMS` file:

```
sha256sum *.json *.spdx > SHA256SUMS
```

And a GPG signature of the checksum file:

```
gpg --armor --detach-sign SHA256SUMS
```

---

## Release Signing Authority

| Role | Permission |
|------|-----------|
| @atlaslattice | Authorized to sign all releases |
| Council members | May sign minor releases with @atlaslattice delegation |
| Automated CI | May sign artifacts via Sigstore keyless OIDC (no human key) |

---

## Verification Instructions (for consumers)

```bash
# Verify SHA256 checksum
sha256sum -c SHA256SUMS

# Verify GPG signature (requires Atlas Lattice public key)
gpg --verify SHA256SUMS.asc SHA256SUMS

# Verify Sigstore signature
cosign verify-blob --certificate cert.pem --signature sig.pem artifact.json
```

Public keys are published in `security/PUBLIC_KEYS.md` (planned).

---

*Atlas Lattice Foundation · status: candidate*
