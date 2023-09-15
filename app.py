from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder="react-app/build")

# Serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Serve static files from the 'build' directory
@app.route('/static/<path:path>')
def serve_static(path):
    static_folder = os.path.join(os.getcwd(), 'react-app/build/static')
    return send_from_directory(static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
