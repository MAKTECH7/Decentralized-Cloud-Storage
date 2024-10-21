from flask import Flask, request, jsonify, render_template
from appwrite_client import signup, login, upload_chunk, download_chunk
from file_handler import split_file, reassemble_file
from encryption import encrypt_file, decrypt_file
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def home():
    return render_template('index.html')  # Render the index.html file when accessing the home route

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    # Handle file split, encryption, upload to Appwrite, blockchain metadata
    return jsonify({'status': 'File uploaded successfully'})

@app.route('/download', methods=['GET'])
def download_file():
    file_id = request.args.get('file_id')
    # Handle file retrieval, decryption, and reassembly
    return jsonify({'status': 'File downloaded successfully'})

if __name__ == '__main__':
    app.run(debug=True)
