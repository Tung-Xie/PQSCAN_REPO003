import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, ec, ed25519, ed448, x25519, x448
from cryptography.hazmat.primitives import hashes

# 1. 不要封裝在 def 裡面，直接寫在最外層 (Global)
# --- Hashes (hashlib 是 Python 掃描器的首要目標) ---
sha224_instance = hashlib.sha224(b"init")
sha256_instance = hashlib.sha256(b"init")
sha384_instance = hashlib.sha384(b"init")
sha512_instance = hashlib.sha512(b"init")

# 2. 顯式呼叫 Asymmetric Key Generation (這會觸發 Key Size 識別)
# RSA-3072
standard_rsa_key = rsa.generate_private_key(
    public_exponent=65537, 
    key_size=3072
)

# 3. 橢圓曲線 (不要用變數，直接把 ec.SECP... 寫出來)
p256_key = ec.generate_private_key(ec.SECP256R1())
p384_key = ec.generate_private_key(ec.SECP384R1())
p521_key = ec.generate_private_key(ec.SECP521R1())

# 4. Edwards 曲線與 Montgomery 曲線 (RFC 8032 / 7748)
x25519_inst = x25519.X25519PrivateKey.generate()
x448_inst = x448.X448PrivateKey.generate()
ed25519_inst = ed25519.Ed25519PrivateKey.generate()
ed448_inst = ed448.Ed448PrivateKey.generate()

# 5. 強制字串標記 (某些掃描器會掃描變數名稱與值的對照)
# 這裡把 Brainpool 寫成變數名稱，並賦予字串，這是最後的保險
ALGO_BRAINPOOL_P256 = "brainpoolP256r1"
ALGO_BRAINPOOL_P384 = "brainpoolP384r1"
ALGO_BRAINPOOL_P512 = "brainpoolP512r1"
ALGO_GOST_3410 = "GOST R 34.10"

print("✅ Modern Standard Assets Initialized.")
