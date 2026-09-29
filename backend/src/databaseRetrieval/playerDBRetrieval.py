import os
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc
from ..models.player import Player
from ..models.playerStats import PlayerStats
from decimal import Decimal

engine = create_engine(os.environ["DATABASE_URL"])
Session = sessionmaker(bind=engine)
session = Session()

player_points = (
    session.query(
        Player.id,
        Player.first_name,
        Player.last_name,
        Player.position,
        Player.team_id,
        Player.height_feet,
        Player.height_inches,
        Player.height_feet,
        func.sum(PlayerStats.pts).label("total_points"),
    )
    .join(PlayerStats)
    .group_by(Player.id, Player.first_name, Player.last_name, Player.position)
    .order_by(func.sum(PlayerStats.pts).desc())
    .all()
)

players_dict_sorted = [
    {
        "id": player.id,
        "first_name": player.first_name,
        "last_name": player.last_name,
        "position": player.position,
        "team": player.team_id,
        "total_points": player.total_points,
    }
    for player in player_points
]

session.close()


def searchPlayerByString(search_string):
    found_players = []

    for player in players_dict_sorted:
        if (
            search_string.lower() in player["first_name"].lower()
            or search_string.lower() in player["last_name"].lower()
        ):
            found_players.append(player)

    if found_players:
        # Handle the case where 'total_points' might be None or a Decimal
        found_players_sorted = sorted(
            found_players,
            key=lambda x: (
                x.get("total_points", Decimal(0))
                if x.get("total_points") is not None
                else Decimal(0)
            ),
            reverse=True,
        )
    else:
        found_players_sorted = []

    return found_players_sorted


def get_player_by_id(player_id):
    session = Session()
    player = session.query(Player).filter_by(id=player_id).first()
    session.close()

    if player:
        player_info = {
            "first_name": player.first_name,
            "last_name": player.last_name,
            "position": player.position,
            "height_in": player.height_inches,
            "height_feet": player.height_feet,
            "weight": player.weight_pounds,
            "team_id": player.team_id,
        }
        return player_info
    else:
        return None
