from flask import Blueprint, jsonify
from backend.src.databaseRetrieval.statDBRetrieval import getRecentGames, getRecentGamesByOpponent

statRetrieval_BP = Blueprint("stat_retrieval", __name__)

@statRetrieval_BP.route('/api/games/search/<player_id>/<games_count>', methods=['GET'])
def getGames(player_id, games_count):
    return jsonify(getRecentGames(player_id, games_count))

@statRetrieval_BP.route('/api/games/search/<player_id>/<games_count>/<opponent_id>', methods=['GET'])
def getGamesVsOpponent(player_id, games_count, opponent_id):
    return jsonify(getRecentGamesByOpponent(player_id, games_count, opponent_id))