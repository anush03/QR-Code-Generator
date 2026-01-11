from flask import Flask, render_template, request, send_file
from validators import validate_input
from qr_service import generate_qr
from utils import ensure_qr_directory
from config import QR_IMAGE_NAME
import os

app = Flask(__name__)

ensure_qr_directory()


@app.route("/", methods=["GET", "POST"])
def index():
    qr_image = None
    error = None

    if request.method == "POST":
        data = request.form.get("data")

        if validate_input(data):
            path = generate_qr(data)
            qr_image = path.replace(os.getcwd(), "")
        else:
            error = "Invalid input. Please enter valid text or URL."

    return render_template("index.html", qr_image=qr_image, error=error)


@app.route("/download")
def download_qr():
    path = os.path.join("static", "qr_codes", QR_IMAGE_NAME)
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
