import cv2
import numpy as np
import pytesseract
from PIL import Image

# Set Tesseract path (if needed)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def load_image(image_path):
    # Load image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)  # Load with alpha channel if present
    if image is None:
        raise ValueError("Image not found or path is incorrect.")

    # Handle PNG transparency (if alpha channel exists)
    if image.shape[2] == 4:  # Check if the image has an alpha channel
        alpha = image[:, :, 3]  # Extract the alpha channel
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)  # Convert to 3-channel BGR
        # Create a white background and blend the image
        white_bg = np.ones_like(image, dtype=np.uint8) * 255
        mask = alpha / 255.0  # Normalize alpha to [0, 1]
        image = (image * mask[:, :, np.newaxis] + white_bg * (1 - mask[:, :, np.newaxis])).astype(np.uint8)

    return image

def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Noise reduction using Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Contrast enhancement using CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(blurred)

    # Binarization using Otsu's thresholding
    _, binary = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return binary


def main(image_path):
    # Step 1: Load and handle PNG transparency
    image = load_image(image_path)

    # Step 2: Preprocess the image
    preprocessed = preprocess_image(image)
    # Display results
    cv2.imwrite("preprocessed.jpg",preprocessed)
    
    return "preprocessed.jpg"




def enhance_with_edsr(input_path, output_path="output_edsr.jpg", model_path="EDSR_x4.pb"):
    # Initialize super-resolution model
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(model_path)
    sr.setModel("edsr", 4)  # 4x upscaling

    # Read and process image
    img = cv2.imread(input_path)
    result = sr.upsample(img)

    # Save result
    cv2.imwrite(output_path, result)
    # Example usage
    image_path = output_path  # Replace with your PNG image path
    output_path = main(image_path)
    return output_path

# Usage
if __name__ == "__main__":
    enhance_with_edsr(r"C:\Users\WIN\OneDrive\Desktop\project\telegram_bot_final\test_images\textimage2.jpg", "output_edsr.jpg")