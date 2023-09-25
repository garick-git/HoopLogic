import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './PlayerList.css';


function NBAPlayerList() {
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    // Define the URL of your Flask API
    const apiUrl = '/api/player/allplayers';

    // Make an HTTP GET request to fetch NBA players data
    axios.get(apiUrl)
      .then((response) => {
        // Set the player data in the state
        setPlayers(response.data.data);
      })
      .catch((error) => {
        console.error('Error fetching NBA players:', error);
      });
  }, []);

  return (
    <div>
      <h1>NBA Player List</h1>
      <ul>
        {players.map((player) => (
          <li key={player.id}>
            {player.first_name} {player.last_name} - {player.team.full_name}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default NBAPlayerList;
