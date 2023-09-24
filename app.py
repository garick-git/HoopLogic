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
def player_details(player_id):
    try:
        # Specify the base URL, parameters, headers, and proxies
        base_url = 'https://stats.nba.com/api/v1/commonplayerinfo'
        parameters = {'PlayerID': player_id}
        request_headers = {'User-Agent': 'YourUserAgentHere'}
        proxies = {
            'http': 'http://your_proxy_server',
            'https': 'https://your_proxy_server',
        }

        # Make the request with an increased timeout of 60 seconds
        response = requests.get(url=base_url, params=parameters, headers=request_headers, proxies=proxies, timeout=60)

        # Check if the response was successful and handle it accordingly
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            # Handle other response codes or errors here
            return jsonify({'error': 'Request to external service failed'})

    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., timeouts) here
        return jsonify({'error': f'Request to external service failed: {str(e)}'})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)    
    print(log)