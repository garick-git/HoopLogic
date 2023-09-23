import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './PlayerDetails.css';


const PlayerDetails = () => {
  const { playerName } = useParams();
  const [playerInfo, setPlayerInfo] = useState(null);

  useEffect(() => {
    if (playerName) {
      // Fetch player details by name
      fetch(`/api/player/id/${playerName}`)
        .then((response) => response.json())
        .then((data) => {
          // Assuming the API returns the player ID
          const playerId = data.id;

          // Fetch player details by ID
          fetch(`/api/playerinfo/id/${playerId}`)
            .then((response) => response.json())
            .then((info) => {
              setPlayerInfo(info);
            })
            .catch((error) => {
              console.error('Error:', error);
            });
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    }
  }, [playerName]);

  if (!playerInfo) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Player Details</h2>
      <p>Name: {playerInfo.FIRST_NAME} {playerInfo.LAST_NAME}</p>
      <p>Birthday: {playerInfo.BIRTHDATE}</p>
      <p>School: {playerInfo.SCHOOL}</p>
      <p>Country: {playerInfo.COUNTRY}</p>
      {/* Add more player information fields here */}
    </div>
  );
};

export default PlayerDetails;
