import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import './PlayerSearch.css';

const PlayerSearch = () => {
  const [searchInput, setSearchInput] = useState('');
  const [players, setPlayers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const history = useHistory();

  const handleInputChange = (e) => {
    setSearchInput(e.target.value);
  };

  const searchPlayers = () => {
    if (searchInput.trim() === '') {
      setPlayers([]);
      return;
    }

    setLoading(true);
    setError(null);

    fetch(`/api/player/search/${searchInput}`)
      .then((response) => response.json())
      .then((data) => {
        setPlayers(data);
      })
      .catch((error) => {
        setError('An error occurred while fetching data.');
        console.error('Error:', error);
      })
      .finally(() => {
        setLoading(false);
      });
  };

  useEffect(() => {
    searchPlayers();
  }, [searchInput]);

  const handlePlayerClick = (playerId) => {
    history.push(`/playerinfo/${playerId}`);
  };

  return (
    <div className="PlayerSearch">
      <h1>NBA Player Search</h1>
      <input
        type="text"
        placeholder="Search for players by name"
        value={searchInput}
        onChange={handleInputChange}
      />
      <button onClick={searchPlayers}>Search</button>
      {loading && <p>Loading...</p>}
      {error && <p className="error">{error}</p>}
      <ul>
        {players.map((player) => (
          <li
            key={player.id}
            onClick={() => handlePlayerClick(player.id)}
            className="player-name"
          >
            {player.full_name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PlayerSearch;
