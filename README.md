# REPO 003: Python Crypto Inventory Matrix (Classic Edition)

## 📊 Inventory Breakdown

### 🚨 Critical Risk
- **Hash**: MD5
- **Asymmetric**: RSA-1024
- **Curves**: secp160k1, secp160r1, secp160r2, secp192k1, secp192r1 (RFC 8422)

### ⚠️ High Risk
- **Hash**: SHA-1
- **Asymmetric**: DSA-1024
- **Curves**: sect163k1, sect233k1, sect239k1, sect283k1, sect409k1, sect571k1 (Binary Fields)

### ✅ Medium Risk (Current Standards)
- **Hash**: SHA-224, SHA-256, SHA-512
- **Asymmetric**: RSA-3072, rsa_pss_rsae_sha256
- **Curves**: SECP256R1, SECP384R1, BrainpoolP256r1, X25519, X448, Ed25519
