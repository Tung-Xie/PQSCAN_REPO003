from Crypto.Cipher import AES, DES, DES3, ARC4, Blowfish, ChaCha20
def call():
    k = b'16bytekey_legacy'
    DES.new(b'8bytekey', 1); DES3.new(b'24bytekeyfor3desisneeded', 2, iv=b'8byteiv_')
    ARC4.new(k); AES.new(k, 6); ChaCha20.new(key=b'32bytekeyforchacha20isrequired!!')
