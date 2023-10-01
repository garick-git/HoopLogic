import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './PlayerSearch.css';

const PlayerSearch = () => {
  const [searchInput, setSearchInput] = useState('');
  const [players, setPlayers] = useState([]);
  const navigate = useNavigate();

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

  const handlePlayerClick = (playerId) => {
    // Navigate to player details page with the selected player's ID
    navigate(`/playerdetails/${playerId}`);
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
            onClick={() => handlePlayerClick(player.id)} // Pass player ID
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
