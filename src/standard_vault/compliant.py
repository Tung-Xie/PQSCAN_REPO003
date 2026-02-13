import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding
from cryptography.hazmat.primitives import hashes

def load_modern_standards():
    # --- Medium: SHA-2 Family ---
    s224 = hashlib.sha224(b"data").hexdigest()
    s256 = hashlib.sha256(b"data").hexdigest()
    s512 = hashlib.sha512(b"data").hexdigest()
    
    # --- Medium: RSA 2048/3072 & PSS ---
    standard_rsa = rsa.generate_private_key(public_exponent=65537, key_size=3072)
    # 測試 rsa_pss_rsae_sha256 特徵
    print("Mode: rsa_pss_rsae_sha256")

    # --- Medium: Standard Curves & Brainpool ---
    # SECP & X25519
    curve_p256 = ec.generate_private_key(ec.SECP256R1())
    x25519_key = "x25519"
    
    # RFC 7027 Brainpool
    brainpool_curves = [
        "brainpoolP256r1", "brainpoolP384r1", "brainpoolP512r1"
    ]
    
    # RFC 9189 (GOST/Other)
    gost_ref = "GOST R 34.10"
    print(f"Standard Curves Loaded: {brainpool_curves}, {x25519_key}, {gost_ref}")

load_modern_standards()
