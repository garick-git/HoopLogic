import requests
import time
from database import db
from .player import Player
from .team import Team
from .game import Game
from sqlalchemy.exc import IntegrityError 

class PlayerStats(db.Model):
    __tablename__ = 'playerStats'

    id = db.Column(db.Integer, primary_key=True)
    ast = db.Column(db.Integer)
    blk = db.Column(db.Integer)
    dreb = db.Column(db.Integer)
    fg3_pct = db.Column(db.Float)
    fg3a = db.Column(db.Integer)
    fg3m = db.Column(db.Integer)
    fg_pct = db.Column(db.Float)
    fga = db.Column(db.Integer)
    fgm = db.Column(db.Integer)
    ft_pct = db.Column(db.Float)
    fta = db.Column(db.Integer)
    ftm = db.Column(db.Integer)
    min = db.Column(db.String(10))
    oreb = db.Column(db.Integer)
    pf = db.Column(db.Integer)
    pts = db.Column(db.Integer)
    reb = db.Column(db.Integer)
    stl = db.Column(db.Integer)
    turnover = db.Column(db.Integer)

    # Use ForeignKey references to establish relationships
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    # Define the relationships
    player = db.relationship('Player', backref='player_stats')
    game = db.relationship('Game', backref='player_stats')
    team = db.relationship('Team', backref='player_stats')

    @staticmethod
    def fetch_and_insert_players():
        BASE_URL = "https://www.balldontlie.io/api/v1/stats?start_date={start}&end_date={end}"
        start = "2003-10-28"
        end = "2023-11-27"
        PER_PAGE = 100  

        page = 1
        total_pages = None
        players_added = 0  # Counter for tracking the number of players added
        new_records = 0  # Counter for new records
        duplicate_records = 0  # Counter for duplicate records

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

                        # Check if the player with the given ID already exists in the database
                        existing_player = Player.query.filter_by(id=player_data['id']).first()

                        if existing_player:
                            duplicate_records += 1
                            continue  # Skip adding the player if already in the database

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
                        players_added += 1  # Increment the counter
                        new_records += 1  # Increment the counter

                    db.session.commit()

                    print(f"Inserted data from page {page}/{total_pages}. Players added: {players_added}")

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

        print(f"New records inserted: {new_records}")
        print(f"Duplicate records skipped: {duplicate_records}")
