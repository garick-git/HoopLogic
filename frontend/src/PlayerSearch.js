import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom'; // Import useHistory from react-router-dom
import './PlayerSearch.css';

const PlayerSearch = () => {
  const [searchInput, setSearchInput] = useState('');
  const [players, setPlayers] = useState([]);
  const history = useHistory(); // Create a history object

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

  // Function to navigate to player details page when a player is clicked
  const handlePlayerClick = (playerId) => {
    // Redirect to the player details page using player ID
    history.push(`/player/${playerId}`);
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
            onClick={() => handlePlayerClick(player.id)} // Call handlePlayerClick when clicked
            className="player-name" // Add a CSS class for styling
          >
            {player.full_name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PlayerSearch;
