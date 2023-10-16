from flask import Blueprint, jsonify
from backend.src.databaseRetrieval.statDBRetrieval import getRecentGames, getRecentGamesByOpponent
from backend.src.databaseRetrieval.astRebStatGetters import assistsByNumGames, assistsByNumGames_teams, reboundsByNumGames, reboundsByNumGames_team
from backend.src.databaseRetrieval.ft3PMStatGetters import threesByNumGames, threesByNumGames_team, FTMByNumGames, FTMByNumGames_team
from backend.src.databaseRetrieval.pointStatGetters import pointsByNumGames_teams, getPointsByNumGames
from backend.src.databaseRetrieval.comboStatGetters import getAverageAndRecentPA, getAverageAndRecentPAWithTeam, getAverageAndRecentPRA,\
      getAverageAndRecentPRAWithTeam, getAverageAndRecentPR, getAverageAndRecentPRWithTeam, getAverageAndRecentRA, getAverageAndRecentRAWithTeam

statRetrieval_BP = Blueprint("stat_retrieval", __name__)

#ALL Game Stats for a player_id for games_count amount of games
@statRetrieval_BP.route('/api/games/search/<player_id>/<games_count>', methods=['GET'])
def getGames(player_id, games_count):
    return jsonify(getRecentGames(player_id, games_count))

#ALL Game Stats for a player_id for games_count amount of games
#Uses opponent ID to bring up ^ vs. a specfic team
@statRetrieval_BP.route('/api/games/search/<player_id>/<games_count>/<opponent_id>', methods=['GET'])
def getGamesVsOpponent(player_id, games_count, opponent_id):
    return jsonify(getRecentGamesByOpponent(player_id, games_count, opponent_id))

#Assists for a player_id for games_count amount of games
@statRetrieval_BP.route('/api/games/search/assists/<player_id>/<games_count>', methods=['GET'])
def getAssistsByNumGames(player_id, games_count):
    return jsonify(assistsByNumGames(player_id, games_count))

#Assistsfor a player_id for games_count amount of games
#Uses opponent ID to bring up ^ vs. a specfic team
@statRetrieval_BP.route('/api/games/search/assists/<player_id>/<games_count>/<opponent_id>', methods=['GET'])
def getAssistsByNumGames_Teams(player_id, games_count, opponent_id):
    return jsonify(assistsByNumGames_teams(player_id, games_count, opponent_id))

#Rebounds for a player_id for games_count amount of games
@statRetrieval_BP.route('/api/games/search/rebounds/<player_id>/<games_count>', methods=['GET'])
def getReboundsByNumGames(player_id, games_count):
    return jsonify(reboundsByNumGames(player_id, games_count))

#Rebounds for a player_id for games_count amount of games
#Uses opponent ID to bring up ^ vs. a specfic team
@statRetrieval_BP.route('/api/games/search/rebounds/<player_id>/<games_count>/<opponent_id>', methods=['GET'])
def getReboundsByNumGames_Teams(player_id, games_count, opponent_id):
    return jsonify(reboundsByNumGames_team(player_id, games_count, opponent_id))

#3PM for a player_id for games_count amount of games
@statRetrieval_BP.route('/api/games/search/3PM/<player_id>/<games_count>', methods=['GET'])
def getThreesByNumGames(player_id, games_count):
    return jsonify(threesByNumGames(player_id, games_count))

#3PM for a player_id for games_count amount of games
#Uses opponent ID to bring up ^ vs. a specfic team
@statRetrieval_BP.route('/api/games/search/3PM/<player_id>/<games_count>/<opponent_id>', methods=['GET'])
def getThreesByNumGames_Teams(player_id, games_count, opponent_id):
    return jsonify(threesByNumGames_team(player_id, games_count, opponent_id))

@statRetrieval_BP.route('/api/games/search/FTM/<player_id>/<games_count>', methods=['GET'])
def getFTMByNumGames(player_id, games_count):
    return jsonify(FTMByNumGames(player_id, games_count))

#FTM for a player_id for games_count amount of games
#Uses opponent ID to bring up ^ vs. a specfic team
@statRetrieval_BP.route('/api/games/search/FTM/<player_id>/<games_count>/<opponent_id>', methods=['GET'])
def getFTMByNumGames_Teams(player_id, games_count, opponent_id):
    return jsonify(FTMByNumGames_team(player_id, games_count, opponent_id))

#Points for a player_id for games_count amount of games
@statRetrieval_BP.route('/api/games/search/points/<player_id>/<games_count>', methods=['GET'])
def getPointsByNumGames(player_id, games_count):
    return jsonify(getPointsByNumGames(player_id, games_count))

#Points for a player_id for games_count amount of games
#Uses opponent ID to bring up ^ vs. a specfic team
@statRetrieval_BP.route('/api/games/search/points/<player_id>/<games_count>/<opponent_id>', methods=['GET'])
def getPointsByNumGames_Teams(player_id, games_count, opponent_id):
    return jsonify(pointsByNumGames_teams(player_id, games_count, opponent_id))

#PRA for a player_id for games_count amount of games
@statRetrieval_BP.route('/api/games/search/points/<player_id>/<games_count>', methods=['GET'])
def getPRAByNumGames(player_id, games_count):
    return jsonify(getPRAByNumGames(player_id, games_count))

#PRA for a player_id for games_count amount of games
#Uses opponent ID to bring up ^ vs. a specfic team
@statRetrieval_BP.route('/api/games/search/points/<player_id>/<games_count>/<opponent_id>', methods=['GET'])
def getPRAByNumGames_Teams(player_id, games_count, opponent_id):
    return jsonify(getPRAByNumGames_Teams(player_id, games_count, opponent_id))