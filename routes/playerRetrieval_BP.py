from flask import Blueprint, jsonify
from backend.src.databaseRetrieval.playerDBRetrieval import searchPlayerByString

databaseRetrieval_BP = Blueprint("db_retrieval", __name__)

@databaseRetrieval_BP.route('/api/player/search/<search_input>', methods=['GET'])
def getPlayers(search_input):
    return jsonify(searchPlayerByString(search_input))