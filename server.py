from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import pytesseract
import tempfile
import os
import base64  # Add this import
from preProcessing import enhance_with_edsr

app = Flask(__name__)
CORS(app)

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file format'}), 400

    try:
        # Save uploaded image to temporary file
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            file.save(tmp.name)
            temp_image_path = tmp.name

        # Preprocess image and get the output path
        processed_img_path = enhance_with_edsr(temp_image_path)

        # Read the processed image as bytes
        with open(processed_img_path, 'rb') as img_file:
            processed_image_bytes = img_file.read()

        # Convert processed image to base64 string
        processed_image_base64 = base64.b64encode(processed_image_bytes).decode('utf-8')

        # Perform OCR on the processed image
        text = pytesseract.image_to_string(processed_img_path)

        # Clean up temporary files
        os.unlink(temp_image_path)
        os.unlink(processed_img_path)

        return jsonify({
            'text': text.strip(),
            'processed_image': processed_image_base64  # Include base64 string
        }), 200

    except Exception as e:
        # Clean up temporary files if they exist
        if 'temp_image_path' in locals() and os.path.exists(temp_image_path):
            os.unlink(temp_image_path)
        if 'processed_img_path' in locals() and os.path.exists(processed_img_path):
            os.unlink(processed_img_path)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)