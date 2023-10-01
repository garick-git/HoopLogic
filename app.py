import logging
from flask import Flask, jsonify
# from models.team import Team
# from models.player import Player
# from models.game import Game
# from models.playerStats import PlayerStats
# from models.seasonAverages import SeasonAverages
from flask_sqlalchemy import SQLAlchemy
from backend.playerSearching import getAllPlayers


app = Flask(__name__)

# Configure the logging format and level
log = logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.DEBUG)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@143.110.147.30/hooplogic'
# db = SQLAlchemy(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    logging.info("Request received: /api/data")
    data = {'message': 'Hello from Flask API!'}
    response = jsonify(data)
    logging.info("Sending response: /api/data")
    return response

# @app.route('/api/player/search/<input_text>', methods=['GET'])
# def search_players(input_text):
#     return jsonify(playerNameSearch(input_text))

# @app.route('/api/player/id/<player_name>', methods=['GET'])
# def get_player_id(player_name):
#     return jsonify(playerIDFromName(player_name))

# @app.route('/api/player/info/<player_id>', methods=['GET'])
# def player_details(player_id):
#    return jsonify(getCommonPlayerInfoByID(player_id))

@app.route('/api/player/search/<search_input>', methods=['GET'])
def getPlayers(search_input):
    return jsonify(getAllPlayers(search_input))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)    
    print(log)