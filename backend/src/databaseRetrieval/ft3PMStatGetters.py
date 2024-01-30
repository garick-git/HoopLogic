from datetime import datetime
from sqlalchemy import func, or_
from sqlalchemy.orm import joinedload
from sqlalchemy import desc
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
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


def FTMByNumGames(player_id, num_games):
    result = {
        'ftm': (average_and_recent_stat(player_id, num_games, PlayerStats.ftm))
    }
    return result

def FTMByNumGames_team(player_id, num_games, team_id):
    result = {
        'ftm': (average_and_recent_stat(player_id, num_games, PlayerStats.ftm, team_id))
    }
    return result

def threesByNumGames(player_id, num_games):
    result = {
        'threepm': (average_and_recent_stat(player_id, num_games, PlayerStats.fg3m))
    }
    return result

def threesByNumGames_team(player_id, num_games, team_id):
    result = {
        'threepm': (average_and_recent_stat(player_id, num_games, PlayerStats.fg3m, team_id))
    }
    return result
