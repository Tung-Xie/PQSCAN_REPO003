from Crypto.Cipher import AES, DES, DES3, ARC4, Blowfish, ChaCha20
def encrypt_data():
    k = b'sixteen_byte_key'
    DES.new(b'8bytekey', DES.MODE_ECB)
    DES3.new(b'24bytekeyfor3desisneeded', DES3.MODE_CBC, iv=b'8byteiv_')
    ARC4.new(k)
    AES.new(k, AES.MODE_GCM)
    ChaCha20.new(key=b'32bytekeyforchacha20isrequired!!')
