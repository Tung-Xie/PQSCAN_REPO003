from cryptography.hazmat.primitives.asymmetric import rsa, dsa

def issue_certs():
    # RSA 不同長度的風險對比
    weak_rsa = rsa.generate_private_key(public_exponent=65537, key_size=1024)
    standard_rsa = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    enterprise_rsa = rsa.generate_private_key(public_exponent=65537, key_size=3072)
    
    # 舊式 DSA
    legacy_dsa = dsa.generate_private_key(key_size=1024)
