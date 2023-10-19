from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
from database import db

def FTMByNumGames(player_id, num_games):
    recent_ftm = (
        db.session.query(PlayerStats.ftm)
        .join(PlayerStats.game)
        .filter(PlayerStats.player_id == player_id)
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00')
        .order_by(PlayerStats.game.date.desc())
        .limit(num_games)
        .all()
    )

    if not recent_ftm:
        return [0.0, []]

    total_ftm = sum(ftm[0] for ftm in recent_ftm)
    average_ftm = round(total_ftm / num_games, 2)

    return [average_ftm, [ftm[0] for ftm in recent_ftm]]


def FTMByNumGames_team(player_id, team_id, num_games):
    recent_ftm = (
        db.session.query(PlayerStats.ftm)
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

    if not recent_ftm:
        return [0.0, []]

    total_ftm = sum(ftm[0] for ftm in recent_ftm)
    average_ftm = round(total_ftm / num_games, 2)

    return [average_ftm, [ftm[0] for ftm in recent_ftm]]

def threesByNumGames(player_id, num_games):
    recent_3pm = (
        db.session.query(PlayerStats.fg3m)
        .join(PlayerStats.game)
        .filter(PlayerStats.player_id == player_id)
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00')
        .order_by(PlayerStats.game.date.desc())
        .limit(num_games)
        .all()
    )

    if not recent_3pm:
        return [0.0, []]

    total_3pm = sum(fg3pm[0] for fg3pm in recent_3pm)
    average_3pm = round(total_3pm / num_games, 2)

    return [average_3pm, [fg3pm[0] for fg3pm in recent_3pm]]

def threesByNumGames_team(player_id, team_id, num_games):
    recent_3pm = (
        db.session.query(PlayerStats.fg3m)
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

    if not recent_3pm:
        return [0.0, []]

    total_3pm = sum(fg3pm[0] for fg3pm in recent_3pm)
    average_3pm = round(total_3pm / num_games, 2)

    return [average_3pm, [fg3pm[0] for fg3pm in recent_3pm]]
