import hashlib
from cryptography.hazmat.primitives import hashes, hmac

def verify_files():
    # 碰撞風險雜湊 (Critical)
    md5 = hashlib.md5(b"legacy").hexdigest()
    sha1 = hashlib.sha1(b"legacy").hexdigest()
    
    # 現代雜湊 (Medium)
    sha256 = hashlib.sha256(b"standard").hexdigest()
    sha512 = hashlib.sha512(b"high_security").hexdigest()
    
    # HMAC 呼叫
    h = hmac.HMAC(b"secret_key", hashes.SHA256())
