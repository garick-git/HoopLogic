// PlayerSearch.js
import React, { useState } from 'react';
import axios from 'axios';
import './PlayerList.css'; // Import the CSS file

function PlayerSearch() {
  const [searchInput, setSearchInput] = useState('');
  const [players, setPlayers] = useState([]);
  const [error, setError] = useState(null);

  const apiUrl = `/api/player/search/${searchInput}`;

  const handleSearch = async () => {
    try {
      const response = await axios.get(apiUrl);

      if (response.data) {
        setPlayers(response.data.data);
        setError(null);
      } else {
        setError('No players found.');
        setPlayers([]);
      }
    } catch (error) {
      setError('Error fetching players.');
      setPlayers([]);
    }
  };

  return (
    <div className="player-search-container">
      <h1 className="search-heading">NBA Player Search</h1>
      <div>
        <input
          className="search-input"
          type="text"
          placeholder="Enter a player name..."
          value={searchInput}
          onChange={(e) => setSearchInput(e.target.value)}
        />
        <button className="search-button" onClick={handleSearch}>
          Search
        </button>
      </div>
      {error && <p className="error-message">{error}</p>}
      <ul className="player-list">
        {players.map((player) => (
          <li key={player.id} className="player-item">
            {player.first_name} {player.last_name} - {player.team.full_name} {player.id}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PlayerSearch;
