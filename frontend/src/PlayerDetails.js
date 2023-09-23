// PlayerDetails.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const PlayerDetails = () => {
  const { playerId } = useParams();
  const [playerInfo, setPlayerInfo] = useState(null);

  useEffect(() => {
    // Make an API request to get player details using playerId
    fetch(`/api/player/${playerId}`)
      .then((response) => response.json())
      .then((data) => {
        setPlayerInfo(data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }, [playerId]);

  if (!playerInfo) {
    return <div>Loading...</div>;
  }

  const {
    FIRST_NAME,
    LAST_NAME,
    BIRTHDATE,
    SCHOOL,
    COUNTRY,
    HEIGHT,
    WEIGHT,
    SEASON_EXP,
    JERSEY,
    POSITION,
    TEAM_NAME,
    TEAM_ABBREVIATION,
    TEAM_CITY,
    FROM_YEAR,
    TO_YEAR,
  } = playerInfo;

  return (
    <div>
      <h1>{`${FIRST_NAME} ${LAST_NAME}`}</h1>
      <p>Birthday: {BIRTHDATE}</p>
      <p>School: {SCHOOL}</p>
      <p>Country: {COUNTRY}</p>
      <p>Height: {HEIGHT} Weight: {WEIGHT}</p>
      <p>Position: {POSITION}</p>
      <p>Team: {TEAM_NAME} ({TEAM_ABBREVIATION})</p>
      {/* Add more player information */}
    </div>
  );
};

export default PlayerDetails;
