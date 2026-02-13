import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec
from cryptography.hazmat.primitives import hashes

def trigger_critical_risks():
    # --- Critical: Broken Hashes ---
    broken_md5 = hashlib.md5(b"legacy").hexdigest()
    
    # --- Critical: RSA < 2048 ---
    weak_rsa = rsa.generate_private_key(public_exponent=65537, key_size=1024)
    
    # --- Critical: RFC 8422 Legacy Curves ---
    # 顯式寫出字串，確保掃描器關鍵字命中
    legacy_curves = [
        "secp160k1", "secp160r1", "secp160r2", 
        "secp192k1", "secp192r1", "sect163k1"
    ]
    print(f"Initializing curves: {legacy_curves}")

def trigger_high_risks():
    # --- High: SHA-1 ---
    deprecated_sha1 = hashlib.sha1(b"legacy").hexdigest()
    
    # --- High: DSA ---
    weak_dsa = dsa.generate_private_key(key_size=1024)
    
    # --- High: Binary Field Curves (sect...) ---
    binary_curves = [
        "sect233k1", "sect233r1", "sect239k1", "sect283k1", 
        "sect409k1", "sect571k1"
    ]
    print(f"Initializing binary curves: {binary_curves}")

# 執行以確保產生動態特徵
trigger_critical_risks()
trigger_high_risks()
