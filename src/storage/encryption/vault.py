from Crypto.Cipher import AES, DES, DES3, ARC4, Blowfish, ChaCha20

def encrypt_data():
    key = b'sixteen_byte_key'
    # 嚴重風險對稱加密 (Critical)
    cipher_des = DES.new(b'8bytekey', DES.MODE_ECB)
    cipher_3des = DES3.new(b'24bytekeyfor3desisneeded', DES3.MODE_CBC, iv=b'8byteiv_')
    cipher_rc4 = ARC4.new(key)
    cipher_bf = Blowfish.new(key, Blowfish.MODE_CBC, iv=b'8byteiv_')
    
    # 現代標準但量子脆弱 (Medium)
    cipher_aes = AES.new(key, AES.MODE_GCM)
    cipher_chacha = ChaCha20.new(key=b'32bytekeyforchacha20isrequired!!')
