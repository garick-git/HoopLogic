from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
from database import db

def getRecentGames(player_id, num_games):
    games = (
        db.session.query(
            Game,
            func.row_number().over(order_by=Game.date.desc()).label('row_num')
        )
        .join(PlayerStats)
        .join(Player)
        .filter(Player.id == player_id)
        .filter(PlayerStats.game_id == Game.id)
        .order_by(Game.date.desc())
        .limit(num_games)
        .all()
    )

    recent_games = []
    for game, row_num in games:
        recent_games.append({
            'date': game.date,
            'home_team': game.home_team.full_name,
            'visitor_team': game.visitor_team.full_name,
            'home_team_score': game.home_team_score,
            'visitor_team_score': game.visitor_team_score,
            'period': game.period,
            'status': game.status,
            'time': game.time,
            'postseason': game.postseason,
        })

    return recent_games