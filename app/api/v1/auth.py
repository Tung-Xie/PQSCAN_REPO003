import hashlib
from cryptography.hazmat.primitives.asymmetric import ec
# 測試標準現代加密（尚未 PQC）
def standard_auth():
    # [Medium] 現代 ECC
    curve1 = "secp256r1"
    curve2 = "curve25519"
    # [Medium] 現代對稱加密字串
    cipher = "AES-256-GCM"
    # [Medium] 現代 Hash
    m = hashlib.sha256()
    print(f"Service running on {curve1} with {cipher}")
