import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

const PlayerDetails = () => {
  const { playerId } = useParams();
  const [playerInfo, setPlayerInfo] = useState({});

  useEffect(() => {
    // Fetch player details using playerId and update state
    fetch(`/api/playerinfo/id/${playerId}`)
      .then((response) => response.json())
      .then((data) => {
        setPlayerInfo(data); // Update state with player details
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }, [playerId]);

  // Render player details in the JSX
  return (
    <div className="PlayerDetails">
      <h1>Player Details</h1>
      <p>Name: {playerInfo.full_name}</p>
      <p>Team: {playerInfo.team_name}</p>
      {/* Add more details as needed */}
    </div>
  );
};

export default PlayerDetails;
