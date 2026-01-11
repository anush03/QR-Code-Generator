import qrcode
from config import QR_IMAGE_NAME
from utils import get_qr_path
from logger import logger

def generate_qr(data: str) -> str:
    logger.info("Generating QR Code")

    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    file_path = get_qr_path(QR_IMAGE_NAME)
    img.save(file_path)

    logger.info("QR Code saved successfully")
    return file_path
