from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from .models import Player, PlayerStats

engine = create_engine('mysql+mysqlconnector://root:REMOVED@DB_HOST:3306/hooplogic')
Session = sessionmaker(bind=engine)
session = Session()

player_points = (
    session.query(Player.id, Player.first_name, Player.last_name, func.sum(PlayerStats.pts).label('total_points'))
    .join(PlayerStats)
    .group_by(Player.id, Player.first_name, Player.last_name)
    .order_by(func.sum(PlayerStats.pts).desc())
    .all()
)

players_dict_sorted = [{'id': player.id, 'first_name': player.first_name, 'last_name': player.last_name, 'total_points': player.total_points} for player in player_points]

def searchPlayerByString(search_string):
    found_players = []
    
    # Search for players whose first or last name matches the search string
    for player in players_dict_sorted:
        if search_string.lower() in player['first_name'].lower() or search_string.lower() in player['last_name'].lower():
            found_players.append(player)
    
    # Sort the found players by total points in descending order
    found_players_sorted = sorted(found_players, key=lambda x: x['total_points'], reverse=True)
    
    return found_players_sorted


def get_player_by_id(player_id):
        player = Player.query.filter_by(id=player_id).first()
        return player


