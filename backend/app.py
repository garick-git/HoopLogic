from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/api/data', methods=['GET'])

@app.route('/')
def index():
    return render_template("Home.js")

if __name__ == '__main__':
    app.run()
