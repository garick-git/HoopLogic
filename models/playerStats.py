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
        BASE_URL = "https://www.balldontlie.io/api/v1/stats"
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
                        # Check if the 'player' key is present and not None
                        if 'player' in player_stat_data and player_stat_data['player'] is not None:
                            player_id = player_stat_data['player']['id']
                        else:
                            player_id = None

                        # Extract data from the player_stat_data dictionary
                        ast = player_stat_data['ast']
                        blk = player_stat_data['blk']
                        dreb = player_stat_data['dreb']
                        fg3_pct = player_stat_data['fg3_pct']
                        fg3a = player_stat_data['fg3a']
                        fg3m = player_stat_data['fg3m']
                        fg_pct = player_stat_data['fg_pct']
                        fga = player_stat_data['fga']
                        fgm = player_stat_data['fgm']
                        ft_pct = player_stat_data['ft_pct']
                        fta = player_stat_data['fta']
                        ftm = player_stat_data['ftm']
                        min = player_stat_data['min']
                        oreb = player_stat_data['oreb']
                        pf = player_stat_data['pf']
                        pts = player_stat_data['pts']
                        reb = player_stat_data['reb']
                        stl = player_stat_data['stl']
                        turnover = player_stat_data['turnover']

                        # Create a new PlayerStats object
                        player_stat = PlayerStats(
                            id=player_stat_data['id'],
                            ast=ast,
                            blk=blk,
                            dreb=dreb,
                            fg3_pct=fg3_pct,
                            fg3a=fg3a,
                            fg3m=fg3m,
                            fg_pct=fg_pct,
                            fga=fga,
                            fgm=fgm,
                            ft_pct=ft_pct,
                            fta=fta,
                            ftm=ftm,
                            min=min,
                            oreb=oreb,
                            pf=pf,
                            pts=pts,
                            reb=reb,
                            stl=stl,
                            turnover=turnover,
                            player_id=player_id,
                            # Add other columns and relationships here
                        )

                        # Add the player_stat object to the session
                        db.session.add(player_stat)

                    # Commit the changes to the database
                    db.session.commit()

                    print(f"Inserted data from page {page}/{total_pages}")

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