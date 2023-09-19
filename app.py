import logging
from flask import Flask, jsonify

app = Flask(__name__)

# Configure the logging format and level
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.DEBUG)

@app.route('/api/data', methods=['GET'])
def get_data():
    logging.info("Request received: /api/data")
    data = {'message': 'Hello from Flask API!'}
    response = jsonify(data)
    logging.info("Sending response: /api/data")
    return response

if __name__ == '__main__':
    app.run(debug=True)
