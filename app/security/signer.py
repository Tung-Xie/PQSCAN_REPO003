from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa, dsa, ec

class SignatureService:
    def __init__(self):
        # --- 強制觸發點 1: 極短的 RSA 金鑰 (512-bit) ---
        self.weak_rsa_key = rsa.generate_private_key(public_exponent=65537, key_size=512)
        
        # --- 強制觸發點 2: 淘汰的 DSA 演算法 ---
        self.dsa_key = dsa.generate_private_key(key_size=1024)

    def sign_legacy(self, data: bytes):
        # --- 強制觸發點 3: 使用 SHA1 進行簽章 (High Risk) ---
        signature = self.weak_rsa_key.sign(
            data,
            padding.PKCS1v15(),
            hashes.SHA1()
        )
        return signature

# 立即實例化，防止掃描器認為這只是無用的定義
service = SignatureService()
test_data = b"Tony_Security_Demo"
service.sign_legacy(test_data)
