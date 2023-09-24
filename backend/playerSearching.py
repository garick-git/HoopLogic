from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo



def playerNameSearch(input_text):
    # Get a list of all NBA players
    nba_players_first = players.find_players_by_first_name(input_text)
    nba_players_last = players.find_players_by_last_name(input_text)
    matching_players = nba_players_first + nba_players_last

    return matching_players


def isActive(player):
    activePlayers = players.get_active_players()
    

#Takes a player FULL name and returns their associated ID in the API
def playerIDFromName(playerName):
    playerID = players.find_players_by_full_name(playerName)
    return (playerID[0]['id'])

def getCommonPlayerInfoByID(id):
    career = commonplayerinfo.CommonPlayerInfo(id)
    return career.common_player_info.get_dict()

