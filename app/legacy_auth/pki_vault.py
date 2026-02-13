from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
import datetime

def generate_self_signed_cert():
    # --- 強制觸發點 4: 建立不安全的自簽憑證 ---
    key = rsa.generate_private_key(public_exponent=65537, key_size=1024)
    subject = issuer = x509.Name([x509.NameAttribute(x509.NameOID.COMMON_NAME, u"Legacy CA")])
    
    # 故意使用 MD5 作為憑證雜湊 (Critical)
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=365)
    ).sign(key, hashes.MD5()) # 這裡的 MD5 應該會被標紅
    
    return cert

# 執行呼叫
generate_self_signed_cert()
