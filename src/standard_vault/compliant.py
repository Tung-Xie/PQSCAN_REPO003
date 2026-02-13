import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding, ed25519, ed448, x25519, x448
from cryptography.hazmat.primitives import hashes

def load_modern_standards():
    # --- Medium: SHA-2 Family (直接呼叫 hashlib) ---
    s224 = hashlib.sha224(b"data").digest()
    s256 = hashlib.sha256(b"data").digest()
    s384 = hashlib.sha384(b"data").digest()
    s512 = hashlib.sha512(b"data").digest()
    
    # --- Medium: RSA-3072 & PSS (具體實例化) ---
    standard_rsa = rsa.generate_private_key(public_exponent=65537, key_size=3072)
    # 這裡加入 PSS 填充特徵，觸發 rsa_pss 掃描
    pss_padding = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)

    # --- Medium: SECP & Edwards Curves (具體類別呼叫) ---
    curve_p256 = ec.generate_private_key(ec.SECP256R1())
    curve_p384 = ec.generate_private_key(ec.SECP384R1())
    curve_p521 = ec.generate_private_key(ec.SECP521R1())
    
    # RFC 8032 / 7748 (EdDSA & Montgomery)
    x25519_key = x25519.X25519PrivateKey.generate()
    x448_key = x448.X448PrivateKey.generate()
    ed25519_key = ed25519.Ed25519PrivateKey.generate()
    ed448_key = ed448.Ed448PrivateKey.generate()

    # --- Medium: RFC 7027 Brainpool (透過 Name 呼叫) ---
    # 許多掃描器會抓 ec.derive_private_key 搭配特定名稱
    bp256 = "brainpoolP256r1"
    bp384 = "brainpoolP384r1"
    bp512 = "brainpoolP512r1"
    
    # 這裡模擬呼叫 (強迫掃描器看到這些字串跟加密物件在一起)
    print(f"Applying: {bp256}, {bp384}, {bp512}")
    
    # --- Medium: GOST (顯式註解搭配庫特徵) ---
    # 即使 Python cryptography 不直接支援，寫出 OID 或關鍵字也能增加命中率
    gost_oid = "1.2.643.7.1.1.1.1" # GOST R 34.10-2012
    print(f"Legacy GOST Support: {gost_oid}")

# 🔥 最重要的一步：在最外層 Call 它
if __name__ == "__main__":
    load_modern_standards()
    
