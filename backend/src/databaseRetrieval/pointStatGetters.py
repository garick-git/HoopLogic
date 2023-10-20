from datetime import datetime
from sqlalchemy import or_
from sqlalchemy import desc
from sqlalchemy.orm import joinedload
from ..models.playerStats import PlayerStats
from ..models.game import Game
from database import db

def average_and_recent_stat(player_id, num_games, stat_column, team_id=None):
    num_games = int(num_games)
    query = db.session.query(stat_column)
    query = query.join(Game)
    
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


def pointsByNumGames(player_id, num_games):
    return average_and_recent_stat(player_id, num_games, PlayerStats.pts)

def pointsByNumGames_teams(player_id, num_games, team_id):
    return average_and_recent_stat(player_id, num_games, team_id, PlayerStats.pts)
