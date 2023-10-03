import requests
import time
import datetime
from .team import Team
from database import db


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    home_team_score = db.Column(db.Integer)
    visitor_team_score = db.Column(db.Integer)
    season = db.Column(db.Integer)
    period = db.Column(db.Integer)
    status = db.Column(db.String(20))
    time = db.Column(db.String(20))
    postseason = db.Column(db.Boolean)
    home_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    visitor_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    home_team = db.relationship('Team', foreign_keys=[home_team_id])
    visitor_team = db.relationship('Team', foreign_keys=[visitor_team_id])

    @staticmethod
    def fetch_and_insert_games():
        BASE_URL = "https://www.balldontlie.io/api/v1/games"
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
                    games_data = data['data']

                    # Insert data into the games table
                    for game_data in games_data:
                        # Convert ISO 8601 formatted date to datetime object
                        date_str = game_data['date']
                        date = datetime.fromisoformat(date_str)

                        game = Game(
                            id=game_data['id'],
                            date=date,  # Use the converted datetime object
                            home_team_score=game_data['home_team_score'],
                            visitor_team_score=game_data['visitor_team_score'],
                            season=game_data['season'],
                            period=game_data['period'],
                            status=game_data['status'],
                            time=game_data['time'],
                            postseason=game_data['postseason'],
                            home_team_id=game_data['home_team']['id'],
                            visitor_team_id=game_data['visitor_team']['id']
                        )
                        db.session.add(game)

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