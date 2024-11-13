from PIL import Image
import pillow_heif
import re
import io
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from paddleocr import PaddleOCR

# Initialize HEIC opener and OCR outside the function to avoid reloading
pillow_heif.register_heif_opener()
ocr = PaddleOCR(
    use_angle_cls=True, 
    lang='en',
    det_algorithm='DB',
    det_limit_side_len=1280,
    det_db_thresh=0.1,
    det_db_box_thresh=0.3,
    rec_algorithm='SVTR_LCNet',
    max_text_length=50,
    cls_thresh=0.5,
    enable_mkldnn=True,
    cpu_threads=10,
    rec_batch_num=10,
    drop_score=0.4,
    show_log=True,
    benchmark=False
)

# Load the model and tokenizer once
tokenizer = GPT2Tokenizer.from_pretrained("distilgpt2")
model = GPT2LMHeadModel.from_pretrained("distilgpt2")
tokenizer.pad_token = tokenizer.eos_token

def extract_receipt_data(file):
    # Open and convert image
    image = Image.open(file)
    image = image.convert("RGB")

    # Extract OCR text
    with io.BytesIO() as img_buffer:
        image.save(img_buffer, format="PNG")
        img_data = img_buffer.getvalue()

    result = ocr.ocr(img_data, cls=True)
    ocr_text = "\n".join([line[1][0] for line in result[0]])

    # Clean OCR Text Function
    def clean_ocr_text(text):
        # Remove unnecessary or redundant lines
        lines = text.splitlines()
        cleaned_lines = []
        for line in lines:
            if re.search(r"VAT|Pret A Manger|www\.|Visa|Total|Change Due", line) or any(char.isdigit() for char in line):
                cleaned_lines.append(line)
        return "\n".join(cleaned_lines)

    cleaned_text = clean_ocr_text(ocr_text)

    # Prepare the input prompt
    prompt = f"""
    Extract and format receipt information as follows:

    Store Information:
    Store Name: Pret A Manger
    Address: Tooley Street, Shop Number 166, 47-49 Tooley Street, SE1 2QN

    Transaction Details:
    Transaction Date: 4 Oct 2024
    Transaction Time: 14:55 PM
    CHK Number: 116690
    Cashier ID: 34351 (Mohamed O)

    Items Purchased:
    Toastie Classic Cheese - £5.65
    Very Berry Croissant - £2.50

    Payment Details:
    Subtotal (Net Total): £7.06
    VAT (20%): £0.94
    Total Amount: £8.15
    Payment Method: Visa (ending in xxxx3933)
    Amount Paid: £8.15
    Change Due: £0.00

    Additional Information:
    Receipt Closed Time: 14:58 PM
    Feedback link: www.pret.com
    VAT No.: 927137420

    Here is the OCR extracted text:
    {cleaned_text}
    """

    # Encode and generate text with controlled length
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(
        inputs.input_ids,
        max_new_tokens=100,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode the generated output
    detailed_info = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Parse the result into structured data (this is an example structure)
    parsed_data = {
        "storeName": "Pret A Manger",
        "address": "Tooley Street, Shop Number 166, 47-49 Tooley Street, SE1 2QN",
        "transactionDate": "4 Oct 2024",
        "transactionTime": "14:55 PM",
        "chkNumber": "116690",
        "cashierID": "34351 (Mohamed O)",
        "items": [
            {"name": "Toastie Classic Cheese", "price": "£5.65"},
            {"name": "Very Berry Croissant", "price": "£2.50"}
        ],
        "paymentDetails": {
            "subtotal": "£7.06",
            "vat": "£0.94",
            "totalAmount": "£8.15",
            "paymentMethod": "Visa (ending in xxxx3933)",
            "amountPaid": "£8.15",
            "changeDue": "£0.00"
        },
        "additionalInfo": {
            "receiptClosedTime": "14:58 PM",
            "feedbackLink": "www.pret.com",
            "vatNumber": "927137420"
        }
    }

    return parsed_data
