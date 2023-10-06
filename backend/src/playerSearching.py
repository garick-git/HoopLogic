import requests

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



