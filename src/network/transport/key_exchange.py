from cryptography.hazmat.primitives.asymmetric import ec, dh
def setup_network():
    ec.generate_private_key(ec.SECP160R1())
    ec.generate_private_key(ec.SECP192R1())
    ec.generate_private_key(ec.SECP224R1())
    ec.generate_private_key(ec.SECP256R1())
    dh.generate_parameters(generator=2, key_size=1024)
