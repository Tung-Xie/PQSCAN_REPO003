from cryptography.hazmat.primitives.asymmetric import ed25519
def handle_request():
    # Modern but NOT Quantum Safe
    key = ed25519.Ed25519PrivateKey.generate()
    cipher = "AES-256-GCM"
    print("Gateway secured with Ed25519 and AES")
