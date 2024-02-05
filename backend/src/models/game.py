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
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
            date_obj = date_obj.replace(tzinfo=timezone.utc)
            return date_obj
        except ValueError:
            return None

    @staticmethod
    def fetch_and_insert_games():
        BASE_URL = "https://www.balldontlie.io/api/v1/games"
        PER_PAGE = 100
        page = 1
        total_added = 0
        # seasons = [2002, 2003, 2004, 2005, 2006,
        #            2007, 2008, 2009, 2010, 2011,
        #            2012, 2013, 2014, 2015, 2016,
        #            2017, 2018, 2019, 2020, 2021,
        #            2022, 2023]
        seasons = [2023]

        while True:
            url = f"{BASE_URL}?per_page={PER_PAGE}&page={page}&seasons[]=2033"

            try:
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json().get('data', [])

                    for game_data in data:
                        game_id = game_data.get('id')
                        if Game.query.get(game_id):
                            print(f"Game with ID {game_id} already exists. Skipping...")
                            continue

                        home_team_data = game_data.get('home_team', {})
                        visitor_team_data = game_data.get('visitor_team', {})

                        home_team = Team.query.filter_by(id=home_team_data.get('id')).first()
                        visitor_team = Team.query.filter_by(id=visitor_team_data.get('id')).first()

                        date_str = game_data.get('date')
                        date = Game.parse_iso8601_date(date_str)

                        game = Game(
                            id=game_id,
                            date=date,
                            home_team_score=game_data.get('home_team_score'),
                            visitor_team_score=game_data.get('visitor_team_score'),
                            season=game_data.get('season'),
                            period=game_data.get('period'),
                            status=game_data.get('status'),
                            time=game_data.get('time'),
                            postseason=game_data.get('postseason'),
                            home_team=home_team,
                            visitor_team=visitor_team
                        )
                        db.session.add(game)
                        total_added += 1

                    db.session.commit()

                    print(f"Page {page}: Added {len(data)} games. Total added: {total_added}")

                    if data:
                        page += 1
                        time.sleep(1)  # Adjust delay to comply with rate limit
                    else:
                        print("No more games to fetch.")
                        break
                else:
                    print(f"Request failed with status code {response.status_code}")
                    break
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                break
