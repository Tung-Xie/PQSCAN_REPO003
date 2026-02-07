from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

def standard_auth_flow():
    # [Medium] 現代但非 PQC
    curve = ec.SECP256R1() # NIST P-256
    cipher = "AES-256-GCM"
    
    # 模擬簽章調用
    digest = hashes.Hash(hashes.SHA256())
    print(f"Standard Auth: {cipher} over {curve.name}")
