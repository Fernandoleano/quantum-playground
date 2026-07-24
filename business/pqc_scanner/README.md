# 🔍 PQC Scanner

Finds quantum-vulnerable cryptography in a codebase and tells you how to
fix it. Zero dependencies — pure Python standard library.

## Usage

```bash
python scanner.py /path/to/project            # human-readable report
python scanner.py /path/to/project --json report.json   # + JSON output
```

Try it on the included demo:

```bash
python scanner.py demo_target
```

## What it detects

| Severity | What | Why |
|----------|------|-----|
| 🔴 CRITICAL | RSA, ECDSA/ECDH, Diffie-Hellman, DSA, vulnerable key files | Broken outright by Shor's algorithm on a large quantum computer. Exposed to "harvest now, decrypt later" **today**. |
| 🟡 WARNING | AES-128, SHA-1, MD5, DES/3DES | Weakened by Grover's algorithm (or already classically broken). Fix by doubling key sizes / upgrading hashes. |
| 🟢 INFO | ML-KEM/Kyber, ML-DSA/Dilithium, SLH-DSA, AES-256 | Quantum-safe primitives already present. |

## Known limitations (MVP)

- Regex-based: flags comments and docs, not just live code — by design
  (an audit wants human review of every hit), but expect some noise.
- `generate_private_key` currently matches under the RSA rule even for
  EC keys — duplicate findings on such lines.
- No dependency scanning yet (lockfiles, transitive deps) — planned.
- No TLS endpoint probing — planned.

## Roadmap

- [ ] Dependency manifest scanning (requirements.txt, package.json, go.mod)
- [ ] Certificate parsing (real X.509 inspection, not just PEM headers)
- [ ] Severity scoring by data-lifetime context
- [ ] PyPI release: `pip install pqc-scanner`
