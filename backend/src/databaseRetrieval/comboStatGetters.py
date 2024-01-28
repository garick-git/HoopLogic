from datetime import datetime
import numpy as np
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
from ..databaseRetrieval.astRebStatGetters import assistsByNumGames, assistsByNumGames_teams, reboundsByNumGames, reboundsByNumGames_teams
from ..databaseRetrieval.pointStatGetters import pointsByNumGames_teams, pointsByNumGames
from database import db

def PRAByNumGames(player_id, num_games):
    avgPoints = pointsByNumGames(player_id, num_games)
    avgReb = reboundsByNumGames(player_id, num_games)
    avgAst = assistsByNumGames(player_id, num_games)

    recent_PRA = np.add(avgPoints[1] + avgAst[1] + avgReb[1])
    average_PRA = round((avgAst[0]+avgReb[0]+avgPoints[0]),2)

    return [average_PRA,recent_PRA]

def PRAByNumGames_team(player_id, num_games, team_id):
    avgPoints = pointsByNumGames_teams(player_id, num_games, team_id)
    avgReb = reboundsByNumGames_teams(player_id, num_games, team_id)
    avgAst = assistsByNumGames_teams(player_id, num_games, team_id)

    recent_PRA = np.add(avgPoints[1] + avgAst[1] + avgReb[1])
    average_PRA = round((avgAst[0]+avgReb[0]+avgPoints[0]),2)

    return [average_PRA,recent_PRA]
