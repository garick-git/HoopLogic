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
                    total_pages = data['meta']['total_pages']
                    players_data = data['data']

                    # Insert data into the players table
                    for player_data in players_data:
                        if 'position' not in player_data:
                            continue  # Skip players without a position

                        # Extract team data (if available)
                        team_data = player_data.get('team', {})
                        team = Team.query.filter_by(id=team_data.get('id')).first()

                        player = Player(
                            id=player_data['id'],
                            first_name=player_data['first_name'],
                            last_name=player_data['last_name'],
                            position=player_data['position'],
                            height_feet=player_data.get('height_feet'),  # Handle nullable value
                            height_inches=player_data.get('height_inches'),  # Handle nullable value
                            weight_pounds=player_data.get('weight_pounds'),  # Handle nullable value
                            team=team  # Assign the Team object
                        )
                        db.session.add(player)
                        db.session.commit()  # Commit after each player to reflect in the database

                        print(f"Added player: {player.first_name} {player.last_name}, Position: {player.position}")

                    print(f"Inserted data from page {page}/{total_pages}")

                    if page < total_pages:
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
