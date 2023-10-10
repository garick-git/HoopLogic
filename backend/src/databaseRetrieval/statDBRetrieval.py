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
            PlayerStats,
            func.row_number().over(order_by=Game.date.desc()).label('row_num')
        )
        .join(PlayerStats)
        .join(Player)
        .filter(Player.id == player_id)
        .filter(PlayerStats.game_id == Game.id)
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00')
        .order_by(Game.date.desc())
        .limit(num_games)
        .all()
    )

    recent_games = []
    for game, player_stats, row_num in games:
        recent_games.append({
            'date': game.date,
            'home_team': game.home_team.full_name,
            'visitor_team': game.visitor_team.full_name,
            'home_team_score': game.home_team_score,
            'visitor_team_score': game.visitor_team_score,
            'player_stats': {
                'ast': player_stats.ast,
                'blk': player_stats.blk,
                'dreb': player_stats.dreb,
                'fg3_pct': player_stats.fg3_pct,
                'fg3a': player_stats.fg3a,
                'fg3m': player_stats.fg3m,
                'fg_pct': player_stats.fg_pct,
                'fga': player_stats.fga,
                'fgm': player_stats.fgm,
                'ft_pct': player_stats.ft_pct,
                'fta': player_stats.fta,
                'ftm': player_stats.ftm,
                'min': player_stats.min,
                'oreb': player_stats.oreb,
                'pf': player_stats.pf,
                'pts': player_stats.pts,
                'reb': player_stats.reb,
                'stl': player_stats.stl,
                'turnover': player_stats.turnover,
            },
        })

    return recent_games


def getRecentGamesByOpponent(player_id, num_games, team_id):
    games = (
        db.session.query(
            Game,
            PlayerStats,
            func.row_number().over(order_by=Game.date.desc()).label('row_num')
        )
        .join(PlayerStats)
        .join(Player)
        .filter(Player.id == player_id)
        .filter(PlayerStats.game_id == Game.id)
        .filter(PlayerStats.min != '00:00')
        .filter(PlayerStats.min != '00') 
        .filter(
            or_(Game.home_team_id == team_id, Game.visitor_team_id == team_id)
        )
        .order_by(Game.date.desc())
        .limit(num_games)
        .all()
    )

    recent_games = []
    for game, player_stats, row_num in games:
        recent_games.append({
            'date': game.date,
            'home_team': game.home_team.full_name,
            'visitor_team': game.visitor_team.full_name,
            'home_team_score': game.home_team_score,
            'visitor_team_score': game.visitor_team_score,
            'player_stats': {
                'ast': player_stats.ast,
                'blk': player_stats.blk,
                'dreb': player_stats.dreb,
                'fg3_pct': player_stats.fg3_pct,
                'fg3a': player_stats.fg3a,
                'fg3m': player_stats.fg3m,
                'fg_pct': player_stats.fg_pct,
                'fga': player_stats.fga,
                'fgm': player_stats.fgm,
                'ft_pct': player_stats.ft_pct,
                'fta': player_stats.fta,
                'ftm': player_stats.ftm,
                'min': player_stats.min,
                'oreb': player_stats.oreb,
                'pf': player_stats.pf,
                'pts': player_stats.pts,
                'reb': player_stats.reb,
                'stl': player_stats.stl,
                'turnover': player_stats.turnover,
            },
        })

    return recent_games

