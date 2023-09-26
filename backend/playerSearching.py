import requests



# def playerNameSearch(input_text):
#     # Get a list of all NBA players
#     nba_players_first = players.find_players_by_first_name(input_text)
#     nba_players_last = players.find_players_by_last_name(input_text)
#     matching_players = nba_players_first + nba_players_last

#     return matching_players

def getAllPlayers(input_text):
    url = f"https://www.balldontlie.io/api/v1/players?search={input_text}"

    try:
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            players_data = response.json()
            return players_data
        else:
            print(f"Request failed with status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# def isActive(player):
#     activePlayers = players.get_active_players()
    

# #Takes a player FULL name and returns their associated ID in the API
# def playerIDFromName(playerName):
#     playerID = players.find_players_by_full_name(playerName)
#     return (playerID[0]['id'])

# def getCommonPlayerInfoByID(id):
#     time.sleep(.6)
#     custom_headers = {
#         'Host': 'stats.nba.com', 
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0', 
#         'Accept': 'application/json, text/plain, */*', 
#         'Accept-Language': 'en-US,en;q=0.5', 
#         'Accept-Encoding': 'gzip, deflate, br', 
#         'x-nba-stats-origin': 'stats', 
#         'x-nba-stats-token': 'true', 
#         'Connection': 'keep-alive', 
#         'Referer': 'https://stats.nba.com/', 
#         'Pragma': 'no-cache', 
#         'Cache-Control': 'no-cache'
#      }
    
#     player_info = commonplayerinfo.CommonPlayerInfo(player_id=id, headers=custom_headers)
#     playerJson = player_info.common_player_info.get_dict()
#     return playerJson


