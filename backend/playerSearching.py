from nba_api.stats.static import players

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
