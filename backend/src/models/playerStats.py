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
        BASE_URL = "https://www.balldontlie.io/api/v1/stats?seasons[]=2021"
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
                    player_stats_data = data['data']

                    for player_stat_data in player_stats_data:
                        player_stat_id = player_stat_data['id']

                        try:
                            player_stat = PlayerStats(
                                id=player_stat_id,
                                ast=player_stat_data.get('ast', 0),
                                blk=player_stat_data.get('blk', 0),
                                dreb=player_stat_data.get('dreb', 0),
                                fg3_pct=player_stat_data.get('fg3_pct', 0.0),
                                fg3a=player_stat_data.get('fg3a', 0),
                                fg3m=player_stat_data.get('fg3m', 0),
                                fg_pct=player_stat_data.get('fg_pct', 0.0),
                                fga=player_stat_data.get('fga', 0),
                                fgm=player_stat_data.get('fgm', 0),
                                ft_pct=player_stat_data.get('ft_pct', 0.0),
                                fta=player_stat_data.get('fta', 0),
                                ftm=player_stat_data.get('ftm', 0),
                                min=player_stat_data.get('min', '0'),
                                oreb=player_stat_data.get('oreb', 0),
                                pf=player_stat_data.get('pf', 0),
                                pts=player_stat_data.get('pts', 0),
                                reb=player_stat_data.get('reb', 0),
                                stl=player_stat_data.get('stl', 0),
                                turnover=player_stat_data.get('turnover', 0),
                                player_id=player_stat_data['player']['id'],
                                game_id=player_stat_data['game']['id'],
                                team_id=player_stat_data['team']['id']
                            )
                            db.session.add(player_stat)
                            db.session.commit()
                        except IntegrityError as e:
                            db.session.rollback()
                            print(f"IntegrityError: Skipping duplicate entry.")
                        except Exception as e:
                            print(f"An error occurred while processing data: {e}")

                    if page < total_pages:
                        page += 1
                        time.sleep(1)  # Add a delay to comply with rate limit (adjust as needed)
                    else:
                        break
                else:
                    print(f"Request failed with status code {response.status_code}")
                    break
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                break