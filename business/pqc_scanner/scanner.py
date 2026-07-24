#!/usr/bin/env python3
"""PQC Scanner — find quantum-vulnerable cryptography in a codebase.

Usage:
    python scanner.py /path/to/project
    python scanner.py /path/to/project --json report.json

Scans source files and configs for cryptographic algorithms that a
large-scale quantum computer would break (Shor's algorithm) or weaken
(Grover's algorithm), and reports what it finds with file:line
locations and migration recommendations.

Severity model:
  CRITICAL  — public-key crypto broken outright by Shor (RSA, ECC, DH).
              "Harvest now, decrypt later" makes this urgent today.
  WARNING   — symmetric crypto / hashes weakened by Grover
              (AES-128, SHA-1, 3DES). Fix by doubling key sizes.
  INFO      — post-quantum or quantum-safe primitives detected
              (ML-KEM/Kyber, ML-DSA/Dilithium, AES-256). Good news.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

# File types worth scanning: source code, configs, certificates.
SCAN_EXTENSIONS = {
    ".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".go", ".rs", ".rb",
    ".php", ".c", ".cc", ".cpp", ".h", ".hpp", ".cs", ".swift", ".kt",
    ".scala", ".sh", ".yaml", ".yml", ".json", ".toml", ".ini", ".cfg",
    ".conf", ".pem", ".crt", ".tf", ".env.example", ".txt", ".md",
}

SKIP_DIRS = {
    ".git", ".venv", "venv", "node_modules", "__pycache__", "dist",
    "build", ".idea", ".vscode", "vendor", "target",
}

# Each rule: (regex, severity, algorithm label, recommendation).
RULES: list[tuple[re.Pattern, str, str, str]] = [
    # --- CRITICAL: Shor-broken public-key crypto -----------------------
    (re.compile(r"\bRSA[-_ ]?(512|1024|2048|3072|4096)?\b|generate_private_key|RSA\.generate|rsa\.GenerateKey|KeyPairGenerator\.getInstance\(\s*[\"']RSA", re.I),
     "CRITICAL", "RSA",
     "RSA is broken by Shor's algorithm. Migrate key exchange to ML-KEM (Kyber), signatures to ML-DSA (Dilithium)."),
    (re.compile(r"\bECDSA\b|\bECDH\b|secp256k1|secp256r1|prime256v1|\bP-(256|384|521)\b|ed25519|curve25519|X25519", re.I),
     "CRITICAL", "Elliptic-curve crypto",
     "Elliptic-curve crypto is broken by Shor's algorithm. Migrate signatures to ML-DSA, key agreement to ML-KEM (or hybrid X25519+ML-KEM during transition)."),
    (re.compile(r"diffie[-_ ]?hellman|\bDHE?\b(?!AD)|createDiffieHellman", re.I),
     "CRITICAL", "Diffie-Hellman",
     "Finite-field Diffie-Hellman is broken by Shor's algorithm. Replace with ML-KEM key encapsulation."),
    (re.compile(r"BEGIN (RSA|EC|DSA) PRIVATE KEY"),
     "CRITICAL", "Quantum-vulnerable key material",
     "Key file uses RSA/EC/DSA. Plan re-issuance with post-quantum or hybrid certificates."),
    (re.compile(r"\bDSA\b(?!_)", re.I),
     "CRITICAL", "DSA",
     "DSA signatures are broken by Shor's algorithm. Migrate to ML-DSA (Dilithium) or SLH-DSA (SPHINCS+)."),

    # --- WARNING: Grover-weakened or generally deprecated ---------------
    (re.compile(r"\bAES[-_ ]?128\b|aes-128-", re.I),
     "WARNING", "AES-128",
     "Grover's algorithm halves effective key strength (128 -> 64 bits). Move to AES-256."),
    (re.compile(r"\bSHA-?1\b(?![0-9])|\bMD5\b", re.I),
     "WARNING", "Weak hash (SHA-1/MD5)",
     "Already classically broken; quantum makes it worse. Use SHA-256 minimum, SHA-384 for long-term security."),
    (re.compile(r"\b3DES\b|\bDES\b(?!ign)|triple[-_ ]?des", re.I),
     "WARNING", "DES/3DES",
     "Small key space, Grover-vulnerable. Replace with AES-256."),

    # --- INFO: quantum-safe primitives already present ------------------
    (re.compile(r"ML-KEM|Kyber|ML-DSA|Dilithium|SLH-DSA|SPHINCS|FALCON|FrodoKEM|liboqs|pqcrypto", re.I),
     "INFO", "Post-quantum crypto",
     "Post-quantum primitive detected — good. Verify parameter sets match NIST FIPS 203/204/205."),
    (re.compile(r"\bAES[-_ ]?256\b|aes-256-", re.I),
     "INFO", "AES-256",
     "AES-256 retains ~128-bit security against Grover. Quantum-safe for the foreseeable future."),
]


@dataclass
class Finding:
    file: str
    line: int
    severity: str
    algorithm: str
    snippet: str
    recommendation: str


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and (path.suffix.lower() in SCAN_EXTENSIONS or path.name == ".env.example"):
            yield path


def scan_file(path: Path, root: Path) -> list[Finding]:
    findings = []
    try:
        text = path.read_text(errors="ignore")
    except OSError:
        return findings
    for lineno, line in enumerate(text.splitlines(), start=1):
        for pattern, severity, algo, rec in RULES:
            if pattern.search(line):
                findings.append(Finding(
                    file=str(path.relative_to(root)),
                    line=lineno,
                    severity=severity,
                    algorithm=algo,
                    snippet=line.strip()[:120],
                    recommendation=rec,
                ))
    return findings


def scan(root: Path) -> list[Finding]:
    findings = []
    for path in iter_files(root):
        findings.extend(scan_file(path, root))
    return findings


SEVERITY_ORDER = {"CRITICAL": 0, "WARNING": 1, "INFO": 2}
SEVERITY_ICON = {"CRITICAL": "🔴", "WARNING": "🟡", "INFO": "🟢"}


def print_report(findings: list[Finding], root: Path) -> None:
    print(f"\nPQC Scanner report for: {root}")
    print("=" * 60)
    if not findings:
        print("No cryptographic usage detected. (Absence of evidence is")
        print("not evidence of absence — check dependencies and infra too.)")
        return

    findings.sort(key=lambda f: (SEVERITY_ORDER[f.severity], f.file, f.line))
    counts = {"CRITICAL": 0, "WARNING": 0, "INFO": 0}
    for f in findings:
        counts[f.severity] += 1

    for f in findings:
        print(f"\n{SEVERITY_ICON[f.severity]} {f.severity}: {f.algorithm}")
        print(f"   {f.file}:{f.line}")
        print(f"   > {f.snippet}")
        print(f"   Fix: {f.recommendation}")

    print("\n" + "=" * 60)
    print(f"Summary: {counts['CRITICAL']} critical, "
          f"{counts['WARNING']} warnings, {counts['INFO']} quantum-safe hits")
    if counts["CRITICAL"]:
        print("\nCritical items are exposed to 'harvest now, decrypt later':")
        print("adversaries can record encrypted traffic today and decrypt it")
        print("once quantum hardware matures. Migration planning should start now.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan a codebase for quantum-vulnerable cryptography.")
    parser.add_argument("path", help="Directory to scan")
    parser.add_argument("--json", metavar="FILE", help="Also write findings as JSON")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.is_dir():
        sys.exit(f"Not a directory: {root}")

    findings = scan(root)
    print_report(findings, root)

    if args.json:
        Path(args.json).write_text(json.dumps([asdict(f) for f in findings], indent=2))
        print(f"\nJSON report written to {args.json}")


if __name__ == "__main__":
    main()
