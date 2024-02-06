from flask import Blueprint
from backend.src.models.player import Player
from backend.src.models.game import Game
from backend.src.models.playerStats import PlayerStats
from backend.src.models.gamesUpdater import GameDateUpdater

databasePopulate_BP = Blueprint("data_populate", __name__)

@databasePopulate_BP.route('/populate_data', methods=['GET'])
def populate_data():
    PlayerStats.fetch_and_insert_stats()
    return "Data population process initiated."

@databasePopulate_BP.route('/populate_players', methods=['GET'])
def populate_players():
    Player.fetch_and_insert_players()
    return "Player population process initiated."

@databasePopulate_BP.route('/populate_games', methods=['GET'])
def populate_games():
    Game.fetch_and_insert_games()
    return "Game population process initiated."

@databasePopulate_BP.route('/update_games', methods=['GET'])
def update_games():
    GameDateUpdater.update_game_dates()
    return "Game update process initiated."
