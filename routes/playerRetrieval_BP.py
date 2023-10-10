from flask import Blueprint
from backend.src.models.player import Player
from backend.src.databaseRetrieval.playerDBRetrieval import searchPlayerByString
from backend.src.models.game import Game
from backend.src.models.playerStats import PlayerStats

playerRetrieval_BP = Blueprint("player_retrieval", __name__)

@app.route('/api/player/search/<search_input>', methods=['GET'])
def getPlayers(search_input):
    return jsonify(searchPlayerByString(search_input))