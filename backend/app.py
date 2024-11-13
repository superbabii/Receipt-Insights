from flask import Flask, request, jsonify
from receipt_extraction import extract_receipt_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_receipt():
    # Check if the file part is in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    # Get the file from the request
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Pass the file directly to the extraction function
    data = extract_receipt_data(file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=False)
