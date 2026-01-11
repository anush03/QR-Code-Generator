import os
from config import QR_FOLDER

def ensure_qr_directory():
    if not os.path.exists(QR_FOLDER):
        os.makedirs(QR_FOLDER)


def get_qr_path(filename: str) -> str:
    return os.path.join(QR_FOLDER, filename)
