from datetime import datetime
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
from ..databaseRetrieval.astRebStatGetters import assistsByNumGames, assistsByNumGames_teams, reboundsByNumGames, reboundsByNumGames_team
from ..databaseRetrieval.pointStatGetters import pointsByNumGames_teams, pointsByNumGames
from database import db

def getPRAComboForNumGames(player_id, num_games):
    num_games = int(num_games)

    pointsArr = pointsByNumGames(player_id, num_games)
    reboundsArr = reboundsByNumGames(player_id, num_games)
    assistsArr = assistsByNumGames(player_id, num_games)

    pra_combo = []
    for i in range(num_games):
        pra_game = pointsArr[1][i] + reboundsArr[1][i] + assistsArr[1][i]
        pra_combo.append(pra_game)
    
    average_PRA = round(sum(pra_combo) / num_games, 2)
    
    return [average_PRA, pra_combo]

def getPRAComboForNumGamesWithTeam(player_id, num_games, team_id):
    num_games = int(num_games)

    pointsArr = pointsByNumGames_teams(player_id, num_games, team_id)
    reboundsArr = reboundsByNumGames_team(player_id, num_games, team_id)
    assistsArr = assistsByNumGames_teams(player_id, num_games, team_id)

    pra_combo = []
    for i in range(num_games):
        pra_game = pointsArr[1][i] + reboundsArr[1][i] + assistsArr[1][i]
        pra_combo.append(pra_game)
    
    average_PRA = round(sum(pra_combo) / num_games, 2)
    
    return [average_PRA, pra_combo]
#basketbalzzz