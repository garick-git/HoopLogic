from flask import Flask, render_template

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
