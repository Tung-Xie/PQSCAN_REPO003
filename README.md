# REPO 003: Python Comprehensive Crypto Matrix

## 📊 測試範圍 (NIST 2025 標準)
本專案包含 Python 環境下的全維度密碼學資產測試，嚴格區分風險等級：

### 🚨 Critical & High (遺留/棄用)
- **Hash**: MD5, SHA-1
- **Asymmetric**: RSA-1024, DSA-1024
- **Curves**: secp160, secp192, sect... (Binary curves)

### ✅ Medium (符合現行標準)
- **Hash**: SHA-256, SHA-512
- **Asymmetric**: RSA-3072, SECP256R1, Brainpool, X25519

### ✨ Low (抗量子 PQC)
- **NIST Standard**: ML-KEM, ML-DSA
- **Candidates**: Kyber, Dilithium, Falcon, FrodoKEM
- **Advanced**: MAYO, SNOVA, UOV, Hybrid (X25519_MLKEM768)
