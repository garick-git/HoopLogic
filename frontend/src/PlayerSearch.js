import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import './PlayerSearch.css';

const PlayerSearch = () => {
  const [searchInput, setSearchInput] = useState('');
  const [players, setPlayers] = useState([]);
  const history = useHistory();

  const handleInputChange = (e) => {
    setSearchInput(e.target.value);
  };

  const searchPlayers = () => {
    if (searchInput.trim() === '') {
      setPlayers([]);
      return;
    }

    fetch(`/api/player/search/${searchInput}`)
      .then((response) => response.json())
      .then((data) => {
        setPlayers(data);
      })
      .catch((error) => {
        console.error('Error:', error);
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
