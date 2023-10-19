from datetime import datetime
from sqlalchemy import or_
from ..models.playerStats import PlayerStats
from ..models.game import Game
from database import db

def average_and_recent_points(player_id, num_games, team_id=None):
    num_games = int(num_games)

    query = db.session.query(PlayerStats.pts)
    
    if team_id:
        query = query.join(Game).filter(
            or_(
                Game.home_team_id == team_id,
                Game.visitor_team_id == team_id
            )
        )

    recent_points = (
        query
        .filter(PlayerStats.player_id == player_id)
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00')
        .order_by(Game.date.desc())
        .limit(num_games)
        .all()
    )

    if not recent_points:
        return [0.0, []]

    total_points = sum(point[0] for point in recent_points)
    average_points = round(total_points / num_games, 2)

    return [average_points, [point[0] for point in recent_points]]

def pointsByNumGames_teams(player_id, team_id, num_games):
    return average_and_recent_points(player_id, num_games, team_id)

def getPointsByNumGames(player_id, num_games):
    return average_and_recent_points(player_id, num_games)
