import React, { useState, useEffect } from 'react';
import './PlayerSearch.css';

const PlayerSearch = ({ onPlayerSelect }) => {
  const [searchInput, setSearchInput] = useState('');
  const [players, setPlayers] = useState([]);

  const handleInputChange = (e) => {
    setSearchInput(e.target.value);
  };

  const searchPlayers = () => {
    if (searchInput.trim() === '') {
      setPlayers([]);
      return;
    }

    // Make an API request to fetch matching players
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

  return (
    <div className="PlayerSearch">
      <h1>NBA Player Search</h1>
      <input
        type="text"
        placeholder="Search for players by name"
        value={searchInput}
        onChange={handleInputChange}
      />
      <ul>
        {players.map((player, index) => (
          <li
            key={index}
            onClick={() => onPlayerSelect(player.full_name)}
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
