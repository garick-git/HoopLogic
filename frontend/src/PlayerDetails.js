import React, { useState, useEffect } from 'react';

const PlayerDetails = ({ playerId }) => {
  const [playerDetails, setPlayerDetails] = useState(null);

  useEffect(() => {
    // Fetch player details based on playerId
    if (playerId) {
      fetch(`/api/playerinfo/id/${playerId}`)
        .then((response) => response.json())
        .then((data) => {
          setPlayerDetails(data); // Set player details data
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    }
  }, [playerId]);

  if (!playerDetails) {
    // Loading state
    return <div>Loading...</div>;
  }

  // Render player details
  return (
    <div className="PlayerDetails">
      <h1>Player Details</h1>
      <div>
        <h2>{playerDetails.full_name}</h2>
        <p>Birthdate: {playerDetails.birthdate}</p>
        {/* Add more player details here */}
      </div>
    </div>
  );
};

export default PlayerDetails;
