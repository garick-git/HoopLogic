import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';

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

    // Fetch matching players
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

  const handlePlayerClick = (playerName) => {
    // Redirect to PlayerDetails with the selected player name
    history.push(`/playerinfo/${playerName}`);
  };

  return (
    <div>
      <h1>NBA Player Search</h1>
      <input
        type="text"
        placeholder="Search for players by name"
        value={searchInput}
        onChange={handleInputChange}
      />
      <ul>
        {players.map((player) => (
          <li
            key={player.id}
            onClick={() => handlePlayerClick(player.full_name)}
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
