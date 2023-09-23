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
    print(playerID[0]['id'])

def getCommonPlayerInfoByID(id):
    # Nikola Jokić
    career = commonplayerinfo.CommonPlayerInfo(id) 

    # json
    career.get_json()

    # dictionary
    retDict = career.get_normalized_dict()
    
    # Extract specific information from the retDict
    player_info = retDict['CommonPlayerInfo'][0]
    player_id = player_info['PERSON_ID']
    first_name = player_info['FIRST_NAME']
    last_name = player_info['LAST_NAME']
    birthdate = player_info['BIRTHDATE']
    school = player_info['SCHOOL']
    country = player_info['COUNTRY']
    height = player_info['HEIGHT']
    weight = player_info['WEIGHT']
    season_exp = player_info['SEASON_EXP']
    jersey = player_info['JERSEY']
    position = player_info['POSITION']
    team_name = player_info['TEAM_NAME']
    team_abbreviation = player_info['TEAM_ABBREVIATION']
    team_city = player_info['TEAM_CITY']
    from_year = player_info['FROM_YEAR']
    to_year = player_info['TO_YEAR']

if __name__ == "__main__":
    # Input text to search for
    search_text = input("Enter a search term for player names (Enter 'exit' to quit): ")

    # Call the function to search for players
    matching_players = playerNameSearch(search_text)

    # Print the matching players
    if matching_players:
        print(f"Players matching '{search_text}':")
        for player in matching_players:
            print(f"{player['first_name']} {player['last_name']}")
    else:
        print(f"No players found matching '{search_text}'.")
    # playerIDFromName("LeBron James")
