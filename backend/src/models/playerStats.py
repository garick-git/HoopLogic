from sqlalchemy.exc import IntegrityError
from database import db
from .player import Player
from .team import Team
from .game import Game
import requests
import time

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
        new_records = 0
        duplicate_records = 0

        ids_array = [
            460, 462, 464, 472, 473, 475, 480, 486, 487, 489, 
            490, 491, 493, 666940, 666950, 666956, 666960, 666965, 
            666969, 666971, 1603383, 3547240, 3547246, 3547248, 11891374, 
            17896026, 17896027, 17896078, 17896120, 24489167, 38017693, 
            38017698, 38017703, 38017706, 38017711, 38017721, 38017731, 
            47738533, 56677722, 56677822, 56677831, 56677832, 56677833, 
            56677864
        ]

        while True:
            url = f"{BASE_URL}?per_page={PER_PAGE}&page={page}&player_ids={','.join(map(str, ids_array))}"

            try:
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    player_stats_data = data.get('data', [])

                    if not player_stats_data:
                        print("No more records to fetch. Exiting.")
                        break

                    new_records_page = 0
                    duplicate_records_page = 0

                    for player_stat_data in player_stats_data:
                        player_stat_id = player_stat_data.get('id')

                        if not player_stat_id:
                            print("Invalid player data. Skipping.")
                            continue

                        player_info = player_stat_data.get('player', {})
                        player_id = player_info.get('id')

                        if not player_id:
                            print("Invalid player ID. Skipping.")
                            continue

                        existing_player = Player.query.get(player_id)

                        if existing_player is None:
                            print(f"Player with ID {player_id} does not exist. Skipping.")
                            continue

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
                                player_id=player_id,
                                game_id=player_stat_data.get('game', {}).get('id', 0),
                                team_id=player_stat_data.get('team', {}).get('id', 0)
                            )

                            db.session.add(player_stat)
                            db.session.commit()
                            new_records += 1
                            new_records_page += 1
                        except IntegrityError:
                            db.session.rollback()
                            print(f"Duplicate record found for player ID {player_id}. Skipping.")
                            duplicate_records += 1
                            duplicate_records_page += 1
                        except Exception as e:
                            print(f"An error occurred while processing data: {e}")

                    print(f"Page {page}: New records added: {new_records_page}, Duplicate records skipped: {duplicate_records_page}")
                    page += 1
                    time.sleep(1)  # Add a delay to comply with rate limit (adjust as needed)
                else:
                    print(f"Request failed with status code {response.status_code}")
                    break
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                break

        print(f"Overall: New records inserted: {new_records}, Duplicate records skipped: {duplicate_records}")

if __name__ == "__main__":
    PlayerStats.fetch_and_insert_stats()
