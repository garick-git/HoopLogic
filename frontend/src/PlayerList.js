import React, { useState } from 'react';
import axios from 'axios';
import './PlayerList.css';

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
    <div>
      <h1>NBA Player Search</h1>
      <div>
        <input
          type="text"
          placeholder="Enter a player name..."
          value={searchInput}
          onChange={(e) => setSearchInput(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
      </div>
      {error && <p>{error}</p>}
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

export default PlayerSearch;
