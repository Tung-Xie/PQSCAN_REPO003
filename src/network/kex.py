from cryptography.hazmat.primitives.asymmetric import ec, dh
def call():
    [ec.generate_private_key(c) for c in [ec.SECP160R1(), ec.SECP192R1(), ec.SECP256R1()]]
    dh.generate_parameters(generator=2, key_size=1024)
