from datetime import datetime
import numpy as np
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from ..models.playerStats import PlayerStats
from ..models.game import Game
from ..databaseRetrieval.astRebStatGetters import assistsByNumGames, assistsByNumGames_teams, reboundsByNumGames, reboundsByNumGames_teams
from ..databaseRetrieval.pointStatGetters import pointsByNumGames_teams, pointsByNumGames
from database import db


def average_and_recent_stat(player_id, num_games, stat_column, team_id=None):
    num_games = int(num_games)
    query = db.session.query(stat_column).join(Game)

    if team_id:
        query = query.filter(
            or_(
                Game.home_team_id == team_id,
                Game.visitor_team_id == team_id
            )
        )

    recent_stats = (
        query
        .filter(PlayerStats.player_id == player_id)
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00')
        .order_by(Game.date.desc())
        .limit(num_games)
        .all()
    )

    if not recent_stats:
        return [0.0, []]

    total_stat = sum(stat[0] for stat in recent_stats)
    average_stat = round(total_stat / num_games, 1)

    return [average_stat, [stat[0] for stat in recent_stats]]

def PRAByNumGames(player_id, num_games):
    avgPoints = average_and_recent_stat(player_id, num_games, PlayerStats.pts)
    avgReb = average_and_recent_stat(player_id, num_games, PlayerStats.reb)
    avgAst = average_and_recent_stat(player_id, num_games, PlayerStats.ast)
    print(avgPoints[0])
    print(avgReb[0])
    print(avgAst[0])


    avgPRA = round((avgAst[0] + avgReb[0] + avgPoints[0]), 1)
    recentPRA = [list(sum(values)) for values in zip(list(avgPoints[1]), list(avgReb[1]), list(avgAst[1]))]


    result = {
        'PRA': [avgPRA, recentPRA]
    }

    return result

def PRAByNumGames_team(player_id, num_games, team_id):
    avgPoints = average_and_recent_stat(player_id, num_games, PlayerStats.pts, team_id)
    avgReb = average_and_recent_stat(player_id, num_games, PlayerStats.reb, team_id)
    avgAst = average_and_recent_stat(player_id, num_games, PlayerStats.ast, team_id)

    avgPRA = round((avgAst[0]+avgReb[0]+avgPoints[0]),1)
    recentPRA = [list(sum(values)) for values in zip(list(avgPoints[1]), list(avgReb[1]), list(avgAst[1]))]

    result = {
        'PRA': [avgPRA, recentPRA]
    }

    return result
