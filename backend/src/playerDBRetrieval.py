from .models import Player  

def searchPlayerByString(search_string):
    players = Player.query.filter(
        (Player.first_name.ilike(f"%{search_string}%"))
        (Player.last_name.ilike(f"%{search_string}%"))
    ).all()

    return players