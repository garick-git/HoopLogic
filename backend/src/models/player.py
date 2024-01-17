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

    @staticmethod
    def insert_players(players_data):
        for player_data in players_data:
            if 'position' not in player_data:
                continue  # Skip players without a position

            # Extract team data (if available)
            team_data = player_data.get('team', {})
            team = Team.query.filter_by(id=team_data.get('id')).first()

            # Check if the player is already in the database
            existing_player = Player.query.filter_by(id=player_data['id']).first()

            if not existing_player:
                # Insert the player into the database
                player = Player(
                    id=player_data['id'],
                    first_name=player_data['first_name'],
                    last_name=player_data['last_name'],
                    position=player_data['position'],
                    height_feet=player_data.get('height_feet'),
                    height_inches=player_data.get('height_inches'),
                    weight_pounds=player_data.get('weight_pounds'),
                    team=team
                )
                db.session.add(player)
                db.session.commit()

                print(f"Added player: {player.first_name} {player.last_name}, Position: {player.position}")

if __name__ == "__main__":
    Player.fetch_and_insert_players()
