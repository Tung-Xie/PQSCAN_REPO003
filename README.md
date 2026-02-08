# REPO 003: Python Legacy Cryptography Research
本專案為「傳統密碼學資產」盤點標竿，模擬企業中常見但具備量子風險的 Python 開發環境。

## 🛡️ 密碼學資產清單 (Cryptographic Inventory)

### 1. KEX / PKI (金鑰交換與公鑰基礎建設)
* **Critical (淘汰曲線):** secp160r1, secp192r1, secp224r1, secp256k1
* **Medium (現代標準):** secp256r1 (P-256), secp384r1 (P-384), secp521r1 (P-521)
* **Legacy RSA/DSA:** RSA-1024, RSA-2048, RSA-3072, DSA-1024
* **KEX:** Diffie-Hellman Group (1024-bit)

### 2. Cipher Suite (對稱加密)
* **Critical (嚴重風險):** DES (ECB), 3DES (CBC), ARC4 (RC4), Blowfish, CAST5
* **Medium (標準加密):** AES-128 (GCM), ChaCha20

### 3. Hash & Integrity (雜湊與完整性)
* **Critical (碰撞風險):** MD5, SHA-1, SHA-224
* **Medium (標準雜湊):** SHA-256, SHA-384, SHA-512, HMAC-SHA256

## 📂 專案結構
* `src/network/`: 金鑰交換與傳輸加密
* `src/identity/`: 數位簽章與證書管理
* `src/storage/`: 資料存儲加密
* `src/integrity/`: 資料雜湊校驗
* `src/utils/`: 填充模式 (Padding) 輔助工具
