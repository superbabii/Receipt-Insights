from flask import Flask, request, jsonify
from receipt_extraction import extract_receipt_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_receipt():
    file = request.files['file']
    data = extract_receipt_data(file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
