import requests
import time
from datetime import datetime, timezone
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
    def parse_iso8601_date(date_str):
        # Parse ISO 8601 date and time string to a datetime object
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
            date_obj = date_obj.replace(tzinfo=timezone.utc)  # Set the timezone to UTC
            return date_obj
        except ValueError:
            return None

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
                        home_team_data = game_data.get('home_team', {})
                        visitor_team_data = game_data.get('visitor_team', {})

                        home_team = Team.query.filter_by(id=home_team_data.get('id')).first()
                        visitor_team = Team.query.filter_by(id=visitor_team_data.get('id')).first()

                        # Parse the date using the custom function
                        date_str = game_data['date']
                        date = Game.parse_iso8601_date(date_str)

                        if date:
                            game = Game(
                                id=game_data['id'],
                                date=date,
                                home_team_score=game_data['home_team_score'],
                                visitor_team_score=game_data['visitor_team_score'],
                                season=game_data['season'],
                                period=game_data['period'],
                                status=game_data['status'],
                                time=game_data['time'],
                                postseason=game_data['postseason'],
                                home_team=home_team,
                                visitor_team=visitor_team
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