from flask import Flask, render_template

app = Flask(__name__)

@app.route('/money')
def index():
    return render_template('index.html')

# @app.route('/api/data')
# def get_data():
#     # Your API logic here
#     data = {'message': 'Hello from Flask API!'}
#     return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
