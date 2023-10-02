import logging
from flask import Flask, jsonify
from backend.playerSearching import getAllPlayers
from models.team import Team
from models.player import Player
from models.game import Game
from models.playerStats import PlayerStats
from models.seasonAverages import SeasonAverages

# Create the Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.DEBUG)

# Define your routes and view functions

@app.route('/api/populate_data', methods=['GET'])
def populate_data():
    PlayerStats.fetch_and_insert_stats()
    return "Data population process initiated."

@app.route('/api/data', methods=['GET'])
def get_data():
    logging.info("Request received: /api/data")
    data = {'message': 'Hello from Flask API!'}
    response = jsonify(data)
    logging.info("Sending response: /api/data")
    return response

@app.route('/api/player/search/<search_input>', methods=['GET'])
def getPlayers(search_input):
    return jsonify(getAllPlayers(search_input))

# Add more routes as needed

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
