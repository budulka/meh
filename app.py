from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, supports_credentials=True, origins="https://lab6web-production.up.railway.app")

STORAGE_FILE = 'technical_objects.json'

def load_objects():
    try:
        with open(STORAGE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_objects(objects):
    with open(STORAGE_FILE, 'w') as f:
        json.dump(objects, f)

@app.route('/save', methods=['POST'])
def save_technical_objects():
    try:
        data = request.get_json()
        if not isinstance(data, list):
            return jsonify({'error': 'Invalid data format'}), 400
        
        save_objects(data)
        return jsonify({'message': 'Objects saved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_objects', methods=['GET'])
def get_technical_objects():
    try:
        objects = load_objects()
        return jsonify(objects), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run('0.0.0.0', port=3000)
