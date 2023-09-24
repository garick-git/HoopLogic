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
    custom_headers = {
        'Host': 'stats.nba.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language' : 'en-US,en;q=0.8,af;q=0.6',
    }
    
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=id, headers=custom_headers)
    playerJson = player_info.common_player_info.get_dict()
    return playerJson


