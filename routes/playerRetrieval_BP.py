from flask import Blueprint, jsonify
from backend.src.databaseRetrieval.playerDBRetrieval import searchPlayerByString, get_player_by_id

databaseRetrieval_BP = Blueprint("db_retrieval", __name__)

@databaseRetrieval_BP.route('/api/player/search/<search_input>', methods=['GET'])
def getPlayers(search_input):
    return jsonify(searchPlayerByString(search_input))

@databaseRetrieval_BP.route('/api/player/search/id/<player_id>', methods=['GET'])
def getPlayersByID(player_id):
    return jsonify(get_player_by_id(player_id))

