import hashlib
import hmac
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, padding

# --- 強化點 1: 使用最原始的 hashlib 關鍵字 (CBOMkit 必抓) ---
def trigger_hash_detection():
    # 顯式寫出 MD5 和 SHA1
    weak_md5 = hashlib.md5(b"test").hexdigest()
    weak_sha1 = hashlib.sha1(b"test").hexdigest()
    return weak_md5, weak_sha1

# --- 強化點 2: 使用 RSA/DSA 的顯式初始化 ---
def trigger_asymmetric_detection():
    # 測試 RSA-512 (這是掃描器最愛的標誌)
    rsa_key = rsa.generate_private_key(public_exponent=65537, key_size=512)
    # 測試 DSA (通常掃描器會抓 'dsa' 這個關鍵字)
    dsa_key = dsa.generate_private_key(key_size=1024)
    return rsa_key, dsa_key

# --- 強化點 3: 顯式簽章演算法 ---
def trigger_signature_detection():
    # 故意將 hashes.SHA1() 賦值給變數，並在附近留下字串註解
    # 某些掃描器會掃描註解或鄰近字串
    algo_name = "SHA1withRSA"
    hash_obj = hashes.SHA1()
    hash_obj_md5 = hashes.MD5()
    
    # 模擬簽章行為
    print(f"Executing {algo_name} logic...")
    return hash_obj, hash_obj_md5

# 立即執行所有函數
trigger_hash_detection()
trigger_asymmetric_detection()
trigger_signature_detection()
