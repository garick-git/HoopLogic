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
    def fetch_and_insert_stats():
        BASE_URL = "https://www.balldontlie.io/api/v1/stats?start_date=2003-10-28"
        PER_PAGE = 100  

        page = 1
        total_pages = None
        new_records = 0  # Counter for new records
        duplicate_records = 0  # Counter for duplicate records

        while True:
            url = f"{BASE_URL}&per_page={PER_PAGE}&page={page}"

            try:
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    total_pages = data['meta']['total_pages']
                    players_data = data['data']

                    # Insert data into the playerStats table
                for player_data in players_data:
                    player_info = player_data.get('player')

                # Check if player_info is not None
                if player_info:
                    # Check if the player with the given ID already exists in the database
                    existing_player = Player.query.filter_by(id=player_info['id']).first()

                    if existing_player == None or existing_player == "":
                        duplicate_records += 1
                        continue  # Skip adding the stats if player not in the database

                    # Insert player stats data
                    player_stats = PlayerStats(
                        ast=player_data.get('ast'),
                        blk=player_data.get('blk'),
                        dreb=player_data.get('dreb'),
                        fg3_pct=player_data.get('fg3_pct'),
                        fg3a=player_data.get('fg3a'),
                        fg3m=player_data.get('fg3m'),
                        fg_pct=player_data.get('fg_pct'),
                        fga=player_data.get('fga'),
                        fgm=player_data.get('fgm'),
                        ft_pct=player_data.get('ft_pct'),
                        fta=player_data.get('fta'),
                        ftm=player_data.get('ftm'),
                        min=player_data.get('min'),
                        oreb=player_data.get('oreb'),
                        pf=player_data.get('pf'),
                        pts=player_data.get('pts'),
                        reb=player_data.get('reb'),
                        stl=player_data.get('stl'),
                        turnover=player_data.get('turnover'),
                        player=existing_player  # Assign the existing Player object
                    )
                    db.session.add(player_stats)
                    new_records += 1  # Increment the counter


                    db.session.commit()

                    print(f"Inserted data from page {page}/{total_pages}. New records added: {new_records}")

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