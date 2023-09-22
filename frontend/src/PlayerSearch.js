  // render() {
  //   return (
  //     <div>
  //       <h1>NBA Player Search</h1>
  //       <input
  //         type="text"
  //         placeholder="Search for players by name"
  //         value={this.state.searchInput}
  //         onChange={this.handleInputChange}
  //       />
  //       <button onClick={this.searchPlayers}>Search</button>
  //       <ul>
  //         {this.state.players.map((player, index) => (
  //           <li key={index}>{player.full_name}</li>
  //         ))}
  //       </ul>
  //     </div>
  //   );
  // }



  import React, { useState, useEffect } from 'react';

  const PlayerSearch = () => {
    const [searchInput, setSearchInput] = useState('');
    const [players, setPlayers] = useState([]);
  
    const handleInputChange = (e) => {
      setSearchInput(e.target.value);
    };
  
    useEffect(() => {
      if (searchInput.trim() === '') {
        setPlayers([]); // Clear the players list when the input is empty.
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
    }, [searchInput]); // This effect should run whenever searchInput changes.
  
    return (
      <div>
        <h1>NBA Player Search</h1>
        <input
          type="text"
          placeholder="Search for players by name"
          value={searchInput}
          onChange={handleInputChange}
        />
        <button onClick={() => {}}>Search</button>
        <ul>
          {players.map((player, index) => (
            <li key={index}>{player.full_name}</li>
          ))}
        </ul>
      </div>
    );
  };
  
  export default PlayerSearch;