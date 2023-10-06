import requests
import time
from flask_sqlalchemy import SQLAlchemy
from database import db


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    abbreviation = db.Column(db.String(10))
    city = db.Column(db.String(50))
    conference = db.Column(db.String(20))
    division = db.Column(db.String(20))
    full_name = db.Column(db.String(100))
    name = db.Column(db.String(50))


    @staticmethod
    def fetch_and_insert_teams():
        BASE_URL = "https://www.balldontlie.io/api/v1/teams"
        PER_PAGE = 30  # Adjust this as needed

        page = 1
        total_pages = None

        while True:
            url = f"{BASE_URL}?per_page={PER_PAGE}&page={page}"

            try:
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    total_pages = data['meta']['total_pages']
                    teams_data = data['data']

                    # Insert data into the teams table
                    for team_data in teams_data:
                        team = Team(
                            id=team_data['id'],
                            abbreviation=team_data['abbreviation'],
                            city=team_data['city'],
                            conference=team_data['conference'],
                            division=team_data['division'],
                            full_name=team_data['full_name'],
                            name=team_data['name']
                        )
                        db.session.add(team)

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
    