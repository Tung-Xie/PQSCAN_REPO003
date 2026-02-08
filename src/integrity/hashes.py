import hashlib
def call():
    [hashlib.new(n, b"data") for n in ["md5", "sha1", "sha224", "sha256", "sha512"]]
