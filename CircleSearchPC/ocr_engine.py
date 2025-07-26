import pytesseract
from PIL import Image
from config import TESSERACT_PATH

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extract_text(image_path):
    """
    Extracts text from an image file using Tesseract OCR.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The extracted text.
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except FileNotFoundError:
        return "Error: Image file not found."
    except Exception as e:
        return f"An error occurred: {e}"