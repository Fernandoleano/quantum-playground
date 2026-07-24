"""Demo target: intentionally quantum-vulnerable code for scanner demos."""

from cryptography.hazmat.primitives.asymmetric import rsa, ec

# CRITICAL: RSA key generation — Shor-breakable
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# CRITICAL: elliptic curve signature — Shor-breakable
ec_key = ec.generate_private_key(ec.SECP256R1())

# WARNING: Grover-weakened cipher choice
CIPHER = "aes-128-gcm"

# WARNING: broken hash
LEGACY_HASH = "sha1"

# INFO: this line is already quantum-safe
SAFE_CIPHER = "aes-256-gcm"
