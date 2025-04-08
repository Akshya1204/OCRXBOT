# OCRXBOT

This project enhances OCR accuracy using Tesseract by integrating custom image preprocessing, CNN-based denoising, and a seamless multi-platform interface (Flutter app, Telegram bot, and web UI). The backend is built with Python and FastAPI to handle image processing and OCR tasks.

---

## 🚀 Features

- 📷 Extracts text from images using Tesseract OCR
- 🧹 Image preprocessing: denoising, binarization, resizing
- 🧠 CNN model to improve OCR accuracy (optional but integrated)
- 🌐 Web interface using Flask / Streamlit
- 📱 Mobile app with Flutter (calls FastAPI backend)
- 🤖 Telegram Bot interface for OCR on the go
- 🔄 FastAPI endpoints for scalable backend processing

---


## 🧪 Tech Stack

- **OCR Engine**: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- **Language**: Python, Dart
- **Frontend**: Flutter (mobile), Flask/Streamlit (web)
- **Backend**: FastAPI
- **Image Enhancement**: **EDSR (Enhanced Deep Super-Resolution)**
- **Other**: OpenCV, NumPy, PyTesseract, Pillow

---
## (Optional) Activate Virtual Environment
- If you're using a virtual environment (recommended):
```sh
venv\Scripts\activate
```

## 🧠 How It Works
- User uploads an image (via app, bot, or web).
- Image is sent to the FastAPI backend.
- Backend preprocesses the image and enhances it using EDSR.
- Tesseract performs OCR and returns the text.
- Optionally, the text can be converted to speech.
- Result is sent back to the user.

## Requirments 
```sh
pip install fastapi pillow pytesseract opencv-python
```

## How to run
## 1. Open Command Prompt
-Press Win + R, type cmd, and hit Enter.

## 2. Navigate to Your Project Directory
-Replace the path below with the actual location of your web folder.
```sh
cd C:\Users\YourUsername\path\to\your\project\backend
```
-RUN
```sh
pythom -m server 1234
```

## 3.Open other command prompt 
- replace the path below with remaining files folder 
- RUN
```sh
prepocessing.py
```
