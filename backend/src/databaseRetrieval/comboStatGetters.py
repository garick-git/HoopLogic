from datetime import datetime
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
from ..databaseRetrieval.astRebStatGetters import assistsByNumGames, assistsByNumGames_teams, reboundsByNumGames, reboundsByNumGames_team
from ..databaseRetrieval.pointStatGetters import pointsByNumGames_teams, getPointsByNumGames
from database import db

def getPRAComboForNumGames(player_id, num_games):
    num_games = int(num_games)

    pointsArr = getPointsByNumGames(player_id, num_games)
    reboundsArr = reboundsByNumGames(player_id, num_games)
    assistsArr = assistsByNumGames(player_id, num_games)
    
    pra_combo = [
        point[0] + rebound[0] + assist[0]
        for point, rebound, assist in zip(pointsArr, reboundsArr, assistsArr)
    ]
    
    average_PRA = round(sum(pra_combo) / num_games, 2)
    
    return [average_PRA, pra_combo]

def getPRAComboForNumGamesWithTeam(player_id, team_id, num_games):
    num_games = int(num_games)

    pointsArr = pointsByNumGames_teams(player_id, team_id, num_games)
    reboundsArr = reboundsByNumGames_team(player_id, team_id, num_games)
    assistsArr = assistsByNumGames_teams(player_id, team_id, num_games)
    
    pra_combo = [
        point[0] + rebound[0] + assist[0]
        for point, rebound, assist in zip(pointsArr, reboundsArr, assistsArr)
    ]
    
    average_PRA = round(sum(pra_combo) / num_games, 2)
    
    return [average_PRA, pra_combo]
