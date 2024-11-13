import pytesseract
from PIL import Image
import pillow_heif
import re
import io

def extract_receipt_data(file):
    # Check if the file is a HEIC/HEIF image based on extension or MIME type
    if file.filename.endswith(('.heic', '.heif')) or file.mimetype == 'application/octet-stream':
        # Use pillow_heif to open HEIC file directly
        file.seek(0)  # Ensure the file pointer is at the start
        heif_file = pillow_heif.open_heif(io.BytesIO(file.read()))
        image = heif_file.to_pillow()  # Convert HeifFile to PIL Image
    else:
        # For other image types, use PIL directly
        file.seek(0)  # Reset pointer to start in case it's needed again
        image = Image.open(file)

    # Extract text using Tesseract OCR
    text = pytesseract.image_to_string(image)

    # Process the extracted text to find item details, date, and total
    items = re.findall(r'Item: (.+) Price: (\d+\.\d{2})', text)
    date = re.search(r'Date: (\d{2}/\d{2}/\d{4})', text)
    total = re.search(r'Total: (\d+\.\d{2})', text)

    # Organize data in a structured format
    data = {
        'items': [{'name': item[0], 'price': float(item[1])} for item in items],
        'date': date.group(1) if date else None,
        'total': float(total.group(1)) if total else None
    }

    return data
