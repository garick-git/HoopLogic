import logging
from flask import Flask, jsonify
from backend.playerSearching import playerNameSearch, playerIDFromName


app = Flask(__name__)

# Configure the logging format and level
log = logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.DEBUG)

@app.route('/api/data', methods=['GET'])
def get_data():
    logging.info("Request received: /api/data")
    data = {'message': 'Hello from Flask API!'}
    response = jsonify(data)
    logging.info("Sending response: /api/data")
    return response

# @app.route('/api/player/search/<input_text>', methods=['GET'])
# def search_players(input_text):
#     matching_players = playerNameSearch(input_text)
#     return jsonify(matching_players)

# @app.route('/api/player/id/<player_name>', methods=['GET'])
# def get_player_id(player_name):
#     player_id = playerIDFromName(player_name)
#     return jsonify(player_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)    
    print(log)