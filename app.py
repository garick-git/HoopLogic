from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data')
def get_data():
    data = {'message': 'Hello from Flask API!'}
    return jsonify(data)


