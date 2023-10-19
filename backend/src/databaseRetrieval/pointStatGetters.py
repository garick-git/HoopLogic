from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
from database import db


def pointsByNumGames_teams(player_id, team_id, num_games):
    recent_points = (
        db.session.query(PlayerStats.pts)
        .join(PlayerStats.game)
        .filter(PlayerStats.player_id == player_id)
        .filter(or_(
            PlayerStats.game.home_team_id == team_id,
            PlayerStats.game.visitor_team_id == team_id
        ))
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00')
        .order_by(PlayerStats.game.date.desc())
        .limit(num_games)
        .all()
    )

    if not recent_points:
        return [0.0, []]

    total_points = sum(point[0] for point in recent_points)
    average_points = round(total_points / num_games, 2)

    return [average_points, [point[0] for point in recent_points]]



def getPointsByNumGames(player_id, num_games):
    recent_points = (
        db.session.query(PlayerStats.pts)
        .join(PlayerStats.game)
        .filter(PlayerStats.player_id == player_id)
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00')
        .order_by(PlayerStats.game.date.desc())
        .limit(num_games)
        .all()
    )

    if not recent_points:
        return [0.0, []]

    total_points = sum(point[0] for point in recent_points)
    average_points = round(total_points / num_games, 2)

    return [average_points, [point[0] for point in recent_points]]