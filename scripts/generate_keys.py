from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os

def generate_rsa_keypair(key_size: int = 4096):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
    )
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    return private_pem, public_pem

def main():
    priv, pub = generate_rsa_keypair(4096)

    with open('student_private.pem', 'wb') as f:
        f.write(priv)
    with open('student_public.pem', 'wb') as f:
        f.write(pub)

    # Ensure readable permissions (Windows ignores chmod but safe for Linux later)
    try:
        os.chmod('student_private.pem', 0o600)
        os.chmod('student_public.pem', 0o644)
    except Exception:
        pass

    print('Generated student_private.pem and student_public.pem')

if __name__ == '__main__':
    main()
