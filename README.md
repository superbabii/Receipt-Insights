# Receipt Spending Insights

Receipt Spending Insights is a web application that allows users to upload receipts (in `.HEIC` format) and extracts detailed spending information. The application uses OCR to extract data from the receipt, formats it, and displays it in a user-friendly interface.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Improving Accuracy](#improving-accuracy)
- [Acknowledgments](#acknowledgments)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload `.HEIC` receipt files.
- Extracts and formats receipt details, such as store information, transaction details, purchased items, and payment information.
- Displays extracted information in a structured and visually appealing format.
- Supports feedback links and VAT details.

## Technologies Used

- **Frontend**: React, CSS for styling
- **Backend**: Python, Flask
- **OCR**: PaddleOCR for extracting text from images
- **AI Model**: GPT-2 via Hugging Face Transformers for parsing and formatting text

## Installation

### Prerequisites

Ensure you have the following installed on your machine:
- Node.js and npm
- Python 3.x
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/superbabii/Receipt-Insights.git
cd Receipt-Insights
```

### Backend Setup

1. Navigate to the backend folder:
    ```bash
    cd backend
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the backend server:
    ```bash
    python app.py
    ```
   The backend should now be running at `http://localhost:5000`.

### Frontend Setup

1. Navigate to the frontend folder:
    ```bash
    cd ../frontend
    ```

2. Install the required npm packages:
    ```bash
    npm install
    ```

3. Start the React application:
    ```bash
    npm start
    ```
   The frontend should now be running at `http://localhost:3000`.

## Usage

1. Open the application in your browser at `http://localhost:3000`.
2. Click on the "Upload Receipt" button to select a `.HEIC` file.
3. Once uploaded, the backend processes the image, extracts data, and returns formatted information.
4. View the extracted details in the structured format provided in the `Dashboard`.

## Improving Accuracy

- **Language Model (LLM)**: For more accurate parsing and formatting, consider using OpenAI's GPT-3.5 or GPT-4 as the language model. These models provide improved understanding and extraction of structured information.
- **OCR**: To enhance OCR accuracy, consider using advanced OCR services like Google Cloud Vision, Amazon Textract, OpenAI GPT-4 with Vision, or Microsoft Azure OCR. These services generally provide better text extraction accuracy, especially for complex or low-quality images.

## Acknowledgments

- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) for OCR capabilities.
- [Hugging Face Transformers](https://huggingface.co/transformers/) for GPT-2 integration.
- Inspiration for UI/UX and styling from various open-source projects.

## Contributing

Contributions are welcome! If you'd like to improve this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
