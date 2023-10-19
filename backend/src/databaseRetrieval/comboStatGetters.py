from datetime import datetime
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
from database import db

def average_and_recent_PRA(player_id, num_games, team_id=None):
    num_games = int(num_games)

    query = db.session.query(PlayerStats, Game)
    
    if team_id:
        query = query.filter(
            or_(PlayerStats.game.home_team_id == team_id, PlayerStats.game.visitor_team_id == team_id)
        )

    pra_combo = (
        query
        .join(PlayerStats.game)
        .filter(PlayerStats.player_id == player_id)
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00')
        .order_by(Game.date.desc())
        .limit(num_games)
        .all()
    )

    if not pra_combo:
        return [0.0, []]

    total_PRA = sum(game.PlayerStats.pts + game.PlayerStats.reb + game.PlayerStats.ast for player_stats, game in pra_combo)
    average_PRA = round(total_PRA / num_games, 2)

    pra_combo_list = [game.PlayerStats.pts + game.PlayerStats.reb + game.PlayerStats.ast for player_stats, game in pra_combo]

    return [average_PRA, pra_combo_list]

def getPRAComboForNumGames(player_id, num_games):
    return average_and_recent_PRA(player_id, num_games)

def getPRAComboForNumGamesWithTeam(player_id, team_id, num_games):
    return average_and_recent_PRA(player_id, num_games, team_id)
