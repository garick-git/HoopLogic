import requests
import time
from database import db
from .player import Player
from .team import Team
from .game import Game


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
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    player = db.relationship('Player', backref='playerStats')
    game = db.relationship('Game', backref='playerStats')
    team = db.relationship('Team', backref='playerStats')

    @staticmethod
    def fetch_and_insert_stats():
        base_url = "https://www.balldontlie.io/api/v1/stats"
        per_page = 100
        total_pages = None
        page = 1

        while True:
            url = f"{base_url}?per_page={per_page}&page={page}"

            try:
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    total_pages = data['meta']['total_pages']
                    stats_data = data['data']

                    # Insert data into the player_stats table
                    for stat in stats_data:
                        player_stat = PlayerStats(
                            ast=stat.get('ast', 0),
                            blk=stat.get('blk', 0),
                            dreb=stat.get('dreb', 0),
                            fg3_pct=stat.get('fg3_pct', 0.0),
                            fg3a=stat.get('fg3a', 0),
                            fg3m=stat.get('fg3m', 0),
                            fg_pct=stat.get('fg_pct', 0.0),
                            fga=stat.get('fga', 0),
                            fgm=stat.get('fgm', 0),
                            ft_pct=stat.get('ft_pct', 0.0),
                            fta=stat.get('fta', 0),
                            ftm=stat.get('ftm', 0),
                            min=stat.get('min', '0'),
                            oreb=stat.get('oreb', 0),
                            pf=stat.get('pf', 0),
                            pts=stat.get('pts', 0),
                            reb=stat.get('reb', 0),
                            stl=stat.get('stl', 0),
                            turnover=stat.get('turnover', 0),
                            player_id=stat['player']['id'],
                            game_id=stat['game']['id'],
                            team_id=stat['team']['id']
                        )
                        db.session.add(player_stat)

                    db.session.commit()

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
