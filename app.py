from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS from flask-cors

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def api():
    response = {'message': 'Hello, World from Flask API!'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
