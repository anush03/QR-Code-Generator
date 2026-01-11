# 📱 QR Code Generator (Flask Web App)

## 📌 Description

A **Flask-based QR Code Generator** web application that dynamically generates and allows users to download QR codes for any text or URL. The application uses Python’s `qrcode` library for QR generation and provides a simple, responsive web interface built with HTML and CSS.

This project demonstrates backend development using Flask, server-side image generation, and basic web deployment readiness.

---

## 🚀 Features

* Generate QR codes from **text or URLs**
* Preview generated QR code instantly
* Download QR code as an image (`.png`)
* Clean and user-friendly UI
* Ready for deployment on cloud platforms

---

## 🛠️ Technologies Used

* **Python 3**
* **Flask** – Web framework
* **qrcode** – QR code generation
* **HTML & CSS** – Frontend UI
* **Gunicorn** – Production WSGI server (for deployment)



## ⚙️ Local Setup & Run Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔧 Code Changes for Deployment

Before deploying to a cloud platform:

### ✅ Update `app.py`

Make sure Flask listens on all interfaces:

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### ✅ Add `gunicorn` to `requirements.txt`

```
gunicorn
```

### ✅ Deployment Start Command

```bash
gunicorn app:app
```

---



