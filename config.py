import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

QR_FOLDER = os.path.join(BASE_DIR, "static", "qr_codes")

QR_IMAGE_NAME = "generated_qr.png"

ALLOWED_EXTENSIONS = {"png"}
