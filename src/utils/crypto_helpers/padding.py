from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def get_padding():
    # 脆弱的 Padding 模式
    legacy_pad = padding.PKCS1v15()
    modern_pad = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)
