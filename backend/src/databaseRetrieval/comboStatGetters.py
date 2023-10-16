from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
from astRebStatGetters import assistsByNumGames, assistsByNumGames_teams, reboundsByNumGames, reboundsByNumGames_team
from pointStatGetters import getPointsByNumGames, pointsByNumGames_teams
from database import db

def getAverageAndRecentPRA(player_id, num_games):
    average_points, recent_points = getPointsByNumGames(player_id, num_games)
    average_assists, recent_assists = assistsByNumGames(player_id, num_games)
    average_rebounds, recent_rebounds = reboundsByNumGames(player_id, num_games)
    
    average_PRA = round((average_points + average_assists + average_rebounds) / 3, 2)
    recent_PRA = [round((p + a + r) / 3, 2) for p, a, r in zip(recent_points, recent_assists, recent_rebounds)]
    
    return [average_PRA, recent_PRA]


def getAverageAndRecentPRAWithTeam(player_id, team_id, num_games):
    average_points, recent_points = pointsByNumGames_teams(player_id, team_id, num_games)
    average_assists, recent_assists = assistsByNumGames_teams(player_id, team_id, num_games)
    average_rebounds, recent_rebounds = reboundsByNumGames_team(player_id, team_id, num_games)
    
    average_PRA = round((average_points + average_assists + average_rebounds) / 3, 2)
    recent_PRA = [round((p + a + r) / 3, 2) for p, a, r in zip(recent_points, recent_assists, recent_rebounds)]
    
    return [average_PRA, recent_PRA]


def getAverageAndRecentRA(player_id, num_games):
    average_assists, recent_assists = assistsByNumGames(player_id, num_games)
    average_rebounds, recent_rebounds = reboundsByNumGames(player_id, num_games)
    
    average_PRA = round((average_assists + average_rebounds) / 3, 2)
    recent_PRA = [round((a + r) / 2, 2) for a, r in zip(recent_assists, recent_rebounds)]
    
    return [average_PRA, recent_PRA]


def getAverageAndRecentRAWithTeam(player_id, team_id, num_games):
    average_assists, recent_assists = assistsByNumGames_teams(player_id, team_id, num_games)
    average_rebounds, recent_rebounds = reboundsByNumGames_team(player_id, team_id, num_games)
    
    average_PRA = round((average_assists + average_rebounds) / 3, 2)
    recent_PRA = [round((a + r) / 2, 2) for a, r in zip(recent_assists, recent_rebounds)]
    
    return [average_PRA, recent_PRA]

