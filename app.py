from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

QR_FOLDER = "static/qr_codes"


if not os.path.exists(QR_FOLDER):
    os.makedirs(QR_FOLDER)


@app.route("/", methods=["GET", "POST"])
def index():
    qr_image = None

    if request.method == "POST":
        data = request.form.get("data")

        if data:
            img = qrcode.make(data)
            file_path = os.path.join(QR_FOLDER, "generated_qr.png")
            img.save(file_path)
            qr_image = file_path

    return render_template("index.html", qr_image=qr_image)


@app.route("/download")
def download_qr():
    path = os.path.join(QR_FOLDER, "generated_qr.png")
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

