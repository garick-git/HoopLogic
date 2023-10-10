from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
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
        })

    return recent_games


def getRecentGamesByOpponent(player_id, team_id, num_games):
    games = (
        db.session.query(
            Game,
            func.row_number().over(order_by=Game.date.desc()).label('row_num')
        )
        .join(PlayerStats)
        .join(Player)
        .filter(Player.id == player_id)
        .filter(PlayerStats.game_id == Game.id)
        .filter(
            or_(Game.home_team_id == team_id, Game.visitor_team_id == team_id)
        )
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
        })

    return recent_games
