import pytesseract
import pdfplumber
import re
import pandas as pd

def extract_receipt_data(file):
    # Example logic for text extraction
    with pdfplumber.open(file) as pdf:
        text = ''.join(page.extract_text() for page in pdf.pages)

    # Process the extracted text
    items = re.findall(r'Item: (.+) Price: (\d+\.\d{2})', text)
    date = re.search(r'Date: (\d{2}/\d{2}/\d{4})', text)
    total = re.search(r'Total: (\d+\.\d{2})', text)

    # Convert to dictionary
    data = {
        'items': [{'name': item[0], 'price': float(item[1])} for item in items],
        'date': date.group(1),
        'total': float(total.group(1))
    }
    return data
