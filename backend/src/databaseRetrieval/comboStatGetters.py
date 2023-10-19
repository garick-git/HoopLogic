from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from ..models.player import Player
from ..models.game import Game
from ..models.playerStats import PlayerStats
from .astRebStatGetters import assistsByNumGames, assistsByNumGames_teams, reboundsByNumGames, reboundsByNumGames_team
from .pointStatGetters import getPointsByNumGames, pointsByNumGames_teams
from database import db

#Points, Rebounds, Assists
def getAverageAndRecentPRA(player_id, num_games):
    pra_combo = (
        db.session.query(
            func.sum(PlayerStats.pts).label('total_points'),
            func.sum(PlayerStats.reb).label('total_rebounds'),
            func.sum(PlayerStats.ast).label('total_assists'),
        )
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

    total_points, total_rebounds, total_assists = pra_combo[0]
    average_pra = round(
        (total_points + total_rebounds + total_assists) / len(pra_combo), 2
    )

    return [average_pra, pra_combo]

#Points, Rebounds, Assists
#WITH TEAM
def getAverageAndRecentPRAWithTeam(player_id, team_id, num_games):
    average_points, recent_points = pointsByNumGames_teams(player_id, team_id, num_games)
    average_assists, recent_assists = assistsByNumGames_teams(player_id, team_id, num_games)
    average_rebounds, recent_rebounds = reboundsByNumGames_team(player_id, team_id, num_games)

    if not recent_points or not recent_assists or not recent_rebounds:
        return [0.0, []]

    average_points = round(average_points, 2)
    average_assists = round(average_assists, 2)
    average_rebounds = round(average_rebounds, 2)

    average_PRA = round(
        (average_points + average_assists + average_rebounds) / 3, 2
    )

    recent_PRA = [
        round((p + a + r) / 3, 2)
        for p, a, r in zip(recent_points, recent_assists, recent_rebounds)
    ]

    return [average_PRA, recent_PRA]



#Implementation can be further considered later on....

# #Rebounds, Assists
# def getAverageAndRecentRA(player_id, num_games):
#     average_assists, recent_assists = assistsByNumGames(player_id, num_games)
#     average_rebounds, recent_rebounds = reboundsByNumGames(player_id, num_games)
    
#     average_PRA = round((average_assists + average_rebounds) / 3, 2)
#     recent_PRA = [round((a + r) / 2, 2) for a, r in zip(recent_assists, recent_rebounds)]
    
#     return [average_PRA, recent_PRA]

# #Rebounds, Assists
# #WITH TEAM
# def getAverageAndRecentRAWithTeam(player_id, team_id, num_games):
#     average_assists, recent_assists = assistsByNumGames_teams(player_id, team_id, num_games)
#     average_rebounds, recent_rebounds = reboundsByNumGames_team(player_id, team_id, num_games)
    
#     average_PRA = round((average_assists + average_rebounds) / 2, 2)
#     recent_PRA = [round((a + r) / 2, 2) for a, r in zip(recent_assists, recent_rebounds)]
    
#     return [average_PRA, recent_PRA]

# #Points, Rebounds
# def getAverageAndRecentPR(player_id, num_games):
#     average_points, recent_points = pointsByNumGames_teams(player_id, num_games)
#     average_rebounds, recent_rebounds = reboundsByNumGames(player_id, num_games)
    
#     average_PRA = round((average_points + average_rebounds) / 3, 2)
#     recent_PRA = [round((a + r) / 2, 2) for a, r in zip(recent_points, recent_rebounds)]
    
#     return [average_PRA, recent_PRA]

# #Points, Rebounds
# #WITH TEAM
# def getAverageAndRecentPRWithTeam(player_id, team_id, num_games):
#     average_points, recent_points = pointsByNumGames_teams(player_id, team_id, num_games)
#     average_rebounds, recent_rebounds = reboundsByNumGames_team(player_id, team_id, num_games)
    
#     average_PRA = round((average_points + average_rebounds) / 2, 2)
#     recent_PRA = [round((a + r) / 2, 2) for a, r in zip(recent_points, recent_rebounds)]
    
#     return [average_PRA, recent_PRA]
# #Points, Assists
# def getAverageAndRecentPA(player_id, num_games):
#     average_points, recent_points = pointsByNumGames_teams(player_id, num_games)
#     average_assists, recent_assists = assistsByNumGames_teams(player_id, num_games)
    
#     average_PRA = round((average_points + average_assists) / 3, 2)
#     recent_PRA = [round((a + r) / 2, 2) for a, r in zip(recent_points, recent_assists)]
    
#     return [average_PRA, recent_PRA]

# #Points, Assists
# #WITH TEAM
# def getAverageAndRecentPAWithTeam(player_id, team_id, num_games):
#     average_points, recent_points = pointsByNumGames_teams(player_id, team_id, num_games)
#     average_assists, recent_assists = assistsByNumGames_teams(player_id, team_id, num_games)
    
#     average_PRA = round((average_points + average_assists) / 2, 2)
#     recent_PRA = [round((a + r) / 2, 2) for a, r in zip(recent_points, recent_assists)]
    
#     return [average_PRA, recent_PRA]


