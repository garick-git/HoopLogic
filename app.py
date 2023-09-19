from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    print("Request received: /api/data")
    data = {'message': 'Hello from Flask API!'}
    response = jsonify(data)
    print("Sending response: /api/data")
    return response

if __name__ == '__main__':
    app.run(debug=True)
