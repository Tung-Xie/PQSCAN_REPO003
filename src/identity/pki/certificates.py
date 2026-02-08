from cryptography.hazmat.primitives.asymmetric import rsa, dsa
def issue_certs():
    rsa.generate_private_key(65537, 1024)
    rsa.generate_private_key(65537, 2048)
    rsa.generate_private_key(65537, 3072)
    dsa.generate_private_key(key_size=1024)
