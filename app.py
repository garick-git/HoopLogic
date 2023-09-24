import logging
import requests
from flask import Flask, jsonify
from backend.playerSearching import playerNameSearch, playerIDFromName, getCommonPlayerInfoByID


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

@app.route('/api/player/search/<input_text>', methods=['GET'])
def search_players(input_text):
    return jsonify(playerNameSearch(input_text))

@app.route('/api/player/id/<player_name>', methods=['GET'])
def get_player_id(player_name):
    return jsonify(playerIDFromName(player_name))

@app.route('/api/player/info/<int:player_id>', methods=['GET'])
def getCommonPlayerInfoByID(player_id):
    base_url = "https://stats.nba.com/api/v1/commonplayerinfo"
    params = {'PlayerID': player_id}
    request_headers = {'User-Agent': 'Your User Agent'}
    proxies = {'http': 'http://proxy.example.com:8080', 'https': 'https://proxy.example.com:8080'}

    try:
        response = requests.get(url=base_url, params=params, headers=request_headers, proxies=proxies, timeout=60)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        return response.json()

    except requests.exceptions.RequestException as e:
        return {'error': 'Request to external service failed: {}'.format(str(e))}
    except requests.exceptions.Timeout as e:
        return {'error': 'Request to external service timed out: {}'.format(str(e))}

    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)    
    print(log)