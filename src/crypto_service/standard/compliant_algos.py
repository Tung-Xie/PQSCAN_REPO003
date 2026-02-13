import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, ec

def load_standard_assets():
    # Medium: SHA-256, SHA-512
    s256 = hashlib.sha256()
    s512 = hashlib.sha512()
    
    # Medium: NIST P-256, P-384, X25519
    modern_rsa = rsa.generate_private_key(public_exponent=65537, key_size=3072)
    modern_ec = ec.generate_private_key(ec.SECP256R1())
    
    # Brainpool (RFC 7027)
    brainpool = ["brainpoolP256r1", "brainpoolP384r1", "brainpoolP512r1"]
