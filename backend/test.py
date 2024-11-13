# Required Libraries
from paddleocr import PaddleOCR
from PIL import Image
import pillow_heif
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Register HEIF format with Pillow
pillow_heif.register_heif_opener()

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # Set `lang` to support other languages

# Path to your HEIC image
image_path = 'test.HEIC'

# Open HEIC image using pillow-heif
try:
    image = Image.open(image_path)
    # Convert to RGB format if needed
    image = image.convert("RGB")
except Exception as e:
    print(f"Error opening image: {e}")
    exit(1)

# Save as a temporary PNG for PaddleOCR (or use directly if supported)
temp_image_path = "temp_image.png"
image.save(temp_image_path, format="PNG")

# Extract text using PaddleOCR
ocr_result = ocr.ocr(temp_image_path, cls=True)

# Prepare extracted text for the MobiLlama model
extracted_text = "\n".join([f"Text: {line[1][0]} | Confidence: {line[1][1]}" for line in ocr_result[0]])
print("Extracted Text:\n", extracted_text)  # Displaying the OCR output for reference

# Load MobiLlama model and tokenizer with CUDA support if available
model_name = "MBZUAI/MobiLlama-05B"
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load model and tokenizer
try:
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True).to(device)
except Exception as e:
    print(f"Error loading model or tokenizer: {e}")
    exit(1)

# Tokenize and encode the OCR text for MobiLlama
inputs = tokenizer(extracted_text, return_tensors="pt").to(device)

# Generate response or analyze the text with MobiLlama
try:
    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"],
            max_length=200,
            repetition_penalty=1.2,
            pad_token_id=tokenizer.eos_token_id
        )
except Exception as e:
    print(f"Error during text generation: {e}")
    exit(1)

# Decode the output tokens
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Generated Output:", generated_text)
