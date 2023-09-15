from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/members')
def get_data():
    return {"members": ["Member1", "Member2", "Member3"]}

if __name__ == '__main__':
    app.run(debug=True)
