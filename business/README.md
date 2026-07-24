# 💼 The Business — Post-Quantum Cryptography Migration

Working name: **Shorproof** ("proof against Shor's algorithm").
Not final — candidates:

| Name | Why | Check before committing |
|------|-----|------------------------|
| **Shorproof** | Explains itself to technical buyers, memorable pun | domain + trademark search |
| LatticeGuard | References lattice crypto (ML-KEM), serious tone | same |
| QuantaSafe | Broader, less technical audience | same |

## The offer

**PQC Readiness Audit** — fixed scope, fixed price ($1,500–3,000 to start):

1. **Inventory** — scan client code/configs/certs for quantum-vulnerable crypto
2. **Plan** — risk-ranked migration plan to NIST standards (ML-KEM, ML-DSA)
3. **Migrate** (upsell) — hands-on migration work alongside their team

Why this sells: NIST finalized FIPS 203/204/205 in 2024, federal deadlines
exist, "harvest now decrypt later" makes it urgent for anyone with
long-lived sensitive data. Big consultancies ignore companies under
~500 people — that's the niche.

## Assets in this folder

- `pqc_scanner/` — the open-source scanner. Credibility engine + lead magnet.
  Free tool finds the problem; the audit sells the solution.
- `website/` — landing page (static HTML, deploy to GitHub Pages / Netlify free).

## Next actions (matches ROADMAP.md phases)

- [ ] Pick final name, register domain
- [ ] Deploy website (GitHub Pages: free, 10 minutes)
- [ ] Harden scanner: fewer false positives, dependency scanning (requirements.txt / package.json)
- [ ] Publish scanner as own repo + PyPI package (`pip install pqc-scanner`)
- [ ] Write cornerstone content piece: "The Post-Quantum Migration, explained for CTOs"
- [ ] First 20 outreach conversations

## Positioning line

> Quantum computers will break the encryption your business runs on.
> We find where you're exposed — before someone else does.
