import React, { useState, useEffect } from 'react';

const PlayerSearch = () => {
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
    searchPlayers(); // Initially fetch data when the component mounts.
  }, []); // An empty dependency array means this effect runs once after the initial render.

  return (
    <div>
      <h1>NBA Player Search</h1>
      <input
        type="text"
        placeholder="Search for players by name"
        value={searchInput}
        onChange={handleInputChange}
      />
      <button onClick={searchPlayers}>Search</button>
      <ul>
        {players.map((player, index) => (
          <li key={index}>{player.full_name}</li>
        ))}
      </ul>
    </div>
  );
};

export default PlayerSearch;
