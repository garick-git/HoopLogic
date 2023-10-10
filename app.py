import logging
from flask import Flask, jsonify
from database import db
from backend.src.databaseRetrieval.playerDBRetrieval import searchPlayerByString
from backend.src.databaseRetrieval.statDBRetrieval import getRecentGames, getRecentGamesByOpponent
from backend.src.models.team import Team
from backend.src.models.player import Player
from backend.src.models.game import Game
from backend.src.models.playerStats import PlayerStats

# Create the Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.DEBUG)

# Configure the SQLAlchemy database connection
app.config['SECRET_KEY'] = 'SuperSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:REMOVED@DB_HOST:3306/hooplogic'
db.init_app(app)

# Create all tables before running the Flask app
with app.app_context():
    db.create_all()

# Define your routes and view functions

@app.route('/api/populate_data', methods=['GET'])
def populate_data():
    PlayerStats.fetch_and_insert_stats()
    return "Data population process initiated."

@app.route('/api/populate_players', methods=['GET'])
def populate_players():
    Player.fetch_and_insert_players()
    return "Player population process initiated."

@app.route('/api/populate_games', methods=['GET'])
def populate_games():
    Game.fetch_and_insert_games()
    return "Game population process initiated."


@app.route('/api/player/search/<search_input>', methods=['GET'])
def getPlayers(search_input):
    return jsonify(searchPlayerByString(search_input))

@app.route('/api/games/search/<player_id>/<games_count>', methods=['GET'])
def getGames(player_id, games_count):
    return jsonify(getRecentGames(player_id, games_count))

@app.route('/api/games/search/<player_id>/<games_count>/<opponent_id>', methods=['GET'])
def getGamesByOpponent(player_id, opponent_id, games_count):
    return jsonify(getRecentGamesByOpponent(player_id, opponent_id, games_count))

# Add more routes as needed

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
