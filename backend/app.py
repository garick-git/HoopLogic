from flask import Flask, jsonify

app = Flask(__name__)

# Define a sample API endpoint
@app.route('/api/sample', methods=['GET'])
def sample_endpoint():
    data = {'message': 'Hello, World! This is your Flask backend.'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)