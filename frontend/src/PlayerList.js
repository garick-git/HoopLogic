import React, { useState } from 'react';
import axios from 'axios';
import './PlayerList.css';

function NBAPlayerList() {
  const [players, setPlayers] = useState([]);
  const [searchText, setSearchText] = useState(''); // State for input text

  // Update the URL to include the searchText as a parameter
  const apiUrl = `/api/player/search/${searchText}`;

  const fetchPlayers = async () => {
    try {
      const response = await axios.get(apiUrl);

      // Set the player data in the state
      setPlayers(response.data);
    } catch (error) {
      console.error('Error fetching NBA players:', error);
    }
  };

  const handleSearch = () => {
    // Trigger a new search when the button is clicked
    fetchPlayers();
  };

  return (
    <div>
      <h1>NBA Player List</h1>
      <div>
        <input
          type="text"
          placeholder="Search players..."
          value={searchText}
          onChange={(e) => setSearchText(e.target.value)} // Update searchText state on input change
        />
        <button onClick={handleSearch}>Search</button>
      </div>
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
