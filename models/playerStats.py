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
                            ast=stat['ast'],
                            blk=stat['blk'],
                            dreb=stat['dreb'],
                            fg3_pct=stat['fg3_pct'],
                            fg3a=stat['fg3a'],
                            fg3m=stat['fg3m'],
                            fg_pct=stat['fg_pct'],
                            fga=stat['fga'],
                            fgm=stat['fgm'],
                            ft_pct=stat['ft_pct'],
                            fta=stat['fta'],
                            ftm=stat['ftm'],
                            min=stat['min'],
                            oreb=stat['oreb'],
                            pf=stat['pf'],
                            pts=stat['pts'],
                            reb=stat['reb'],
                            stl=stat['stl'],
                            turnover=stat['turnover'],
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