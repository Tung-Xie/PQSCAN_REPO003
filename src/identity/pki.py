from cryptography.hazmat.primitives.asymmetric import rsa, dsa
def call():
    rsa.generate_private_key(65537, 1024); rsa.generate_private_key(65537, 3072)
    dsa.generate_private_key(1024)
