from datetime import datetime
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
from ..databaseRetrieval.astRebStatGetters import assistsByNumGames, assistsByNumGames_teams, reboundsByNumGames, reboundsByNumGames_teams
from ..databaseRetrieval.pointStatGetters import pointsByNumGames_teams, pointsByNumGames
from database import db

def average_and_recent_PRA(player_id, num_games, team_id=None):
    num_games = int(num_games)

    query = db.session.query(PlayerStats.pts, PlayerStats.ast, PlayerStats.reb).join(Game)

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

    total_PRA = []
    for stats in recent_stats:
        PRA = sum(stats)
        total_PRA.append(PRA)

    average_PRA = round(sum(total_PRA) / num_games, 2)

    return [average_PRA, total_PRA]

def PRAByNumGames(player_id, num_games):
    average_PRA, recent_PRA = average_and_recent_PRA(player_id, num_games)

    return {
        'average_PRA': average_PRA,
        'recent_PRA': recent_PRA
    }

def PRAByNumGames_team(player_id, num_games, team_id):
    average_PRA, recent_PRA = average_and_recent_PRA(player_id, num_games, team_id)

    return {
        'average_PRA': average_PRA,
        'recent_PRA': recent_PRA
    }
