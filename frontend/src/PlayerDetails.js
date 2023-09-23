import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import './PlayerDetails.css'; 

const PlayerDetails = () => {
  const { playerId } = useParams();
  const [playerInfo, setPlayerInfo] = useState(null);

  useEffect(() => {
    // Fetch player info by playerId
    fetch(`/api/player/info/${playerId}`)
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

  // Extract player information from playerInfo JSON
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
      <p>Height: {HEIGHT} inches</p>
      <p>Weight: {WEIGHT} lbs</p>
      <p>Seasons of Experience: {SEASON_EXP}</p>
      <p>Jersey Number: {JERSEY}</p>
      <p>Position: {POSITION}</p>
      <p>Team: {TEAM_NAME} ({TEAM_ABBREVIATION})</p>
      <p>Team City: {TEAM_CITY}</p>
      <p>From Year: {FROM_YEAR}</p>
      <p>To Year: {TO_YEAR}</p>
      {/* Add more player information as needed */}
    </div>
  );
};

export default PlayerDetails;
