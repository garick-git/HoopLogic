import requests
import time
from datetime import datetime, timezone
from .game import Game
from .team import Team  # Assuming the Team class is defined in team.py
from database import db  # Assuming db is the SQLAlchemy object

class GameDateUpdater:
    @staticmethod
    def parse_iso8601_date(date_str):
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print(f"Failed to parse date string: {date_str}")
            return None

        return date_obj

    @staticmethod
    def update_game_dates():
        BASE_URL = "https://www.balldontlie.io/api/v1/games"
        PER_PAGE = 100
        page = 1
        total_updated = 0

        while True:
            url = f"{BASE_URL}?per_page={PER_PAGE}&page={page}&start_date=2023-07-01"

            try:
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json().get('data', [])

                    for game_data in data:
                        game_id = game_data.get('id')
                        game = Game.query.get(game_id)

                        if game:
                            date_str = game_data.get('date')
                            date = GameDateUpdater.parse_iso8601_date(date_str)

                            if date:
                                game.date = date
                                db.session.commit()
                                total_updated += 1
                                print(f"Updated date for Game ID {game_id}")

                    print(f"Page {page}: Updated dates for {total_updated} games")

                    if data:
                        page += 1
                        time.sleep(1)  # Adjust delay to comply with rate limit
                    else:
                        print("No more games to update.")
                        break
                else:
                    print(f"Request failed with status code {response.status_code}")
                    break
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                break


