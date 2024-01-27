from datetime import datetime
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
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
    average_stat = round(total_stat / num_games, 2)

    return [average_stat, [stat[0] for stat in recent_stats]]

def PRAByNumGames(player_id, num_games):
    result = {
        'average_points': (average_and_recent_stat(player_id, num_games, PlayerStats.pts)),
        'assists': average_and_recent_stat(player_id, num_games, PlayerStats.ast),
        'rebounds': average_and_recent_stat(player_id, num_games, PlayerStats.reb)
    }

    result['PRA'] = round(result['average_points'] + result['rebounds'] + result['assists'], 2)

    return result

def PRAByNumGames_team(player_id, num_games, team_id):
    result = {
        'average_points': average_and_recent_stat(player_id, num_games, PlayerStats.pts, team_id),
        'assists': average_and_recent_stat(player_id, num_games, PlayerStats.ast, team_id),
        'rebounds': average_and_recent_stat(player_id, num_games, PlayerStats.reb, team_id)
    }

    result['PRA'] = round(result['average_points'] + result['rebounds'] + result['assists'], 2)

    return result