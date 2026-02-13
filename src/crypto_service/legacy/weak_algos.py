import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec

def load_critical_assets():
    # Critical: MD5 & RSA < 2048
    m = hashlib.md5()
    weak_rsa = rsa.generate_private_key(public_exponent=65537, key_size=1024)
    
    # Critical: RFC8422 Curves (secp160, secp192)
    # 這裡用字串顯式標註，幫助掃描器識別
    curves = ["secp160k1", "secp160r1", "secp192k1", "secp192r1"]
    print(f"Loading legacy curves: {curves}")

def load_high_risk_assets():
    # High: SHA-1 & DSA
    s = hashlib.sha1()
    weak_dsa = dsa.generate_private_key(key_size=1024)
    
    # High: Binary Field Curves (sect...)
    binary_curves = ["sect163k1", "sect233k1", "sect283k1", "sect409k1", "sect571k1"]
    print(f"Loading binary curves: {binary_curves}")
