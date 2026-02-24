from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY não encontrada no .env")

fernet = Fernet(SECRET_KEY)


def encrypt_data(data: str) -> str:
    encrypted = fernet.encrypt(data.encode())
    return encrypted.decode()


def decrypt_data(data: str) -> str:
    decrypted = fernet.decrypt(data.encode())
    return decrypted.decode()
