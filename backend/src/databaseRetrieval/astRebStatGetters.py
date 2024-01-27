from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from sqlalchemy import desc
from sqlalchemy import or_
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
    average_stat = round(total_stat / num_games, 2)

    return [average_stat, [stat[0] for stat in recent_stats]]


def assistsByNumGames(player_id, num_games):
    result = {
        'assists': (average_and_recent_stat(player_id, num_games, PlayerStats.ast))
    }
    return result
    

def assistsByNumGames_teams(player_id, num_games, team_id):
    result = {
        'assists': (average_and_recent_stat(player_id, num_games, PlayerStats.ast, team_id))
    }
    return result

def reboundsByNumGames(player_id, num_games):
    result = {
        'rebounds': (average_and_recent_stat(player_id, num_games, PlayerStats.reb))
    }
    return result

def reboundsByNumGames_teams(player_id, num_games, team_id):
    result = {
        'rebounds': (average_and_recent_stat(player_id, num_games, PlayerStats.reb, team_id))
    }
    return result
