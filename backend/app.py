from flask import Flask, request, jsonify
from receipt_extraction import extract_receipt_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_receipt():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    data = extract_receipt_data(file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=False)
