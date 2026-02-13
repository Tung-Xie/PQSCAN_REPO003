# REPO 003: Python PKI & Identity Security Lab

## 📌 測試目標
驗證掃描器對於 Python  庫中非對稱加密與數位簽章的偵測能力。

## 🎯 預期偵測資產 (Expected Assets)
1. **RSA-512**: 超短金鑰長度 (Critical)。
2. **DSA-1024**: 過時的數位簽章標準 (High)。
3. **SHA1withRSA**: 不安全的簽章雜湊組合 (High)。
4. **MD5 (Certificate Signing)**: 憑證簽署時使用的弱雜湊 (Critical)。

## 🛠 偵測強化技術
- **Direct Instantiation**: 代碼末端直接呼叫函數，模擬運行狀態。
- **Library Diversity**: 同時測試  (底層 API) 的呼叫特徵。
