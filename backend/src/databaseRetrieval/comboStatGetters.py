from datetime import datetime
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
from ..databaseRetrieval.astRebStatGetters import assistsByNumGames, assistsByNumGames_teams, reboundsByNumGames, reboundsByNumGames_teams
from ..databaseRetrieval.pointStatGetters import pointsByNumGames_teams, pointsByNumGames
from database import db


def average_and_recent_stat(player_id, num_games, stat_column1, stat_column2, stat_column3, team_id=None):
    num_games = int(num_games)
    query = db.session.query(stat_column1, stat_column2, stat_column3).join(Game)

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

    total_stat1 = sum(stat[0] for stat in recent_stats)
    total_stat2 = sum(stat[1] for stat in recent_stats)
    total_stat3 = sum(stat[2] for stat in recent_stats)

    average_stat = round((total_stat1 + total_stat2 + total_stat3) / num_games, 2)

    return [average_stat, [(stat[0], stat[1], stat[2]) for stat in recent_stats]]

def PRAByNumGames(player_id, num_games):
    result = {
        'PRA': (average_and_recent_stat(player_id, num_games, PlayerStats.pts, PlayerStats.reb, PlayerStats.ast))
    }
    return result

def PRAByNumGames_teams(player_id, num_games, team_id):
    result = {
        'PRA': (average_and_recent_stat(player_id, num_games, PlayerStats.pts, PlayerStats.reb, PlayerStats.ast, team_id))
    }
    return result