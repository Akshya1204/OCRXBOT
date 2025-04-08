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

## 🏗️ Project Structure

. ├── backend/ │ ├── app.py # FastAPI app with OCR endpoints │ ├── edsr_model.py # EDSR super-resolution model │ ├── image_utils.py # Preprocessing functions │ ├── ocr_engine.py # Tesseract integration ├── flutter_app/ # Flutter mobile application ├── telegram_bot/ # Telegram Bot code ├

## 🧪 Tech Stack

- **OCR Engine**: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- **Language**: Python, Dart
- **Frontend**: Flutter (mobile), Flask/Streamlit (web)
- **Backend**: FastAPI
- **Image Enhancement**: **EDSR (Enhanced Deep Super-Resolution)**
- **Other**: OpenCV, NumPy, PyTesseract, Pillow

---

## 🧠 How It Works
- User uploads an image (via app, bot, or web).
- Image is sent to the FastAPI backend.
- Backend preprocesses the image and enhances it using EDSR.
- Tesseract performs OCR and returns the text.
- Optionally, the text can be converted to speech.
- Result is sent back to the user.
