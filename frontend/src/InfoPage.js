import React, { useState } from 'react';
import axios from 'axios';

function NBAPlayerInfoPage() {
  // Create a state variable to store player information
  const [playerInfo, setPlayerInfo] = useState(null);

  // Function to fetch NBA player information
  const fetchPlayerInfo = () => {
    const apiUrl = 'https://stats.nba.com/stats/commonplayerinfo?LeagueID=&PlayerID=2544';

    axios.get(apiUrl)
      .then((response) => {
        // Set the player information in the state
        setPlayerInfo(response.data);
      })
      .catch((error) => {
        // Handle errors, e.g., network issues or API errors
        console.error('Error fetching NBA data:', error);
      });
  };

  return (
    <div>
      <h1>NBA Player Information</h1>
      <button onClick={fetchPlayerInfo}>Fetch Player Info</button>

      {playerInfo && (
        <div>
          <h2>Player Name: {playerInfo.PlayerName}</h2>
          <p>Team: {playerInfo.TeamName}</p>
          {/* Display other player information here */}
        </div>
      )}
    </div>
  );
}

export default NBAPlayerInfoPage;
