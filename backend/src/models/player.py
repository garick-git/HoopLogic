import requests
import time
from database import db
from .team import Team

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    position = db.Column(db.String(10))
    height_feet = db.Column(db.Integer)
    height_inches = db.Column(db.Integer)
    weight_pounds = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    team = db.relationship('Team', backref='players')

    @staticmethod
    def fetch_and_insert_players():
        BASE_URL = "https://www.balldontlie.io/api/v1/players"
        PER_PAGE = 100  

        page = 1
        total_pages = None

        while True:
            url = f"{BASE_URL}?per_page={PER_PAGE}&page={page}"

            try:
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    meta = data.get('meta', {})
                    total_pages = meta.get('total_pages')

                    players_data = data.get('data', [])

                    Player.insert_players(players_data)

                    print(f"Inserted data from page {page}/{total_pages}")

                    if total_pages is not None and page < total_pages:
                        page += 1
                        time.sleep(1)  
                    else:
                        break
                else:
                    print(f"Request failed with status code {response.status_code}")
                    break
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                break

    @staticmethod
    def fetch_and_insert_players():
        BASE_URL = "https://www.balldontlie.io/api/v1/players"
        PER_PAGE = 100  

        page = 1

        while True:
            url = f"{BASE_URL}?per_page={PER_PAGE}&page={page}"

            try:
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    players_data = data.get('data', [])

                    if not players_data:
                        break  # No more players to fetch

                    Player.insert_players(players_data)

                    print(f"Inserted data from page {page}")

                    page += 1
                    time.sleep(1)  # Add a delay to avoid hitting API rate limits
                else:
                    print(f"Request failed with status code {response.status_code}")
                    break
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                break

if __name__ == "__main__":
    Player.fetch_and_insert_players()
