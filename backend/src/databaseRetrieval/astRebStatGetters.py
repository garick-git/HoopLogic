from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
from database import db

def assistsByNumGames(player_id, num_games):
    recent_assists = (
        db.session.query(PlayerStats.ast)
        .join(PlayerStats.game)
        .filter(PlayerStats.player_id == player_id)
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00')
        .order_by(PlayerStats.game.date.desc())
        .limit(num_games)
        .all()
    )

    if not recent_assists:
        return [0.0, []]

    total_assists = sum(assist[0] for assist in recent_assists)
    average_assists = round(total_assists / num_games, 2)

    return [average_assists, [assist[0] for assist in recent_assists]]

def assistsByNumGames_teams(player_id, team_id, num_games):
    recent_assists = (
        db.session.query(PlayerStats.ast)
        .join(PlayerStats.game)
        .filter(PlayerStats.player_id == player_id)
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00')
        .filter(
            (PlayerStats.game.home_team_id == team_id) | (PlayerStats.game.visitor_team_id == team_id)
        )
        .order_by(PlayerStats.game.date.desc())
        .limit(num_games)
        .all()
    )

    if not recent_assists:
        return [0.0, []]

    total_assists = sum(assist[0] for assist in recent_assists)
    average_assists = round(total_assists / num_games, 2)

    return [average_assists, [assist[0] for assist in recent_assists]]

def reboundsByNumGames(player_id, num_games):
    recent_rebounds = (
        db.session.query(PlayerStats.reb)
        .join(PlayerStats.game)
        .filter(PlayerStats.player_id == player_id)
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00')
        .order_by(PlayerStats.game.date.desc())
        .limit(num_games)
        .all()
    )

    if not recent_rebounds:
        return [0.0, []]

    total_rebounds = sum(rebound[0] for rebound in recent_rebounds)
    average_rebounds = round(total_rebounds / num_games, 2)

    return [average_rebounds, [rebound[0] for rebound in recent_rebounds]]

def reboundsByNumGames_team(player_id, team_id, num_games):
    recent_rebounds = (
        db.session.query(PlayerStats.reb)
        .join(PlayerStats.game)
        .filter(PlayerStats.player_id == player_id)
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00')
        .filter(
            (PlayerStats.game.home_team_id == team_id) | (PlayerStats.game.visitor_team_id == team_id)
        )
        .order_by(PlayerStats.game.date.desc())
        .limit(num_games)
        .all()
    )

    if not recent_rebounds:
        return [0.0, []]

    total_rebounds = sum(rebound[0] for rebound in recent_rebounds)
    average_rebounds = round(total_rebounds / num_games, 2)

    return [average_rebounds, [rebound[0] for rebound in recent_rebounds]]
