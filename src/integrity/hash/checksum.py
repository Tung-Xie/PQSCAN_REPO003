import hashlib
def verify():
    hashlib.md5(b"data").hexdigest()
    hashlib.sha1(b"data").hexdigest()
    hashlib.sha256(b"data").hexdigest()
    hashlib.sha512(b"data").hexdigest()
