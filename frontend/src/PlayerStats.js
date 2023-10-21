// routes to call on load: 
// /api/games/search/<player_id>/<games_count
// 
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const PlayerStats = () => {
    const { playerId } = useParams();
    const [gameCount, setGameCount] = useState(5);
    const [lastXGames, setLastXGames] = useState(null);
    const [playerData, setPlayerData] = useState(null);

    useEffect(() => {
        fetchPlayer(playerId, gameCount);
    }, [])
    
    useEffect(() => {
        console.log('Last ', gameCount, ' games: ', lastXGames)
    }, [lastXGames])

    useEffect(() => {
        console.log('Player object fetched: ', playerData)
    }, [playerData])

    const fetchPlayer = (playerId, gameCount) => {
        console.log('Fetching player with ID: ', playerId, ' for ', gameCount, ' games.');
        fetch(`/api/games/search/${playerId}/${gameCount}`, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
            },
          })
            .then((response) => {
              if (!response.ok) {
                throw new Error('Network response was not ok');
              }
              return response.json();
            })
            .then((data) => {
                setLastXGames(data);
            })
            .catch((error) => {
              console.error('Error:', error);
        });

        fetch(`/api/player/search/id/${playerId}`, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
            },
          })
            .then((response) => {
              if (!response.ok) {
                throw new Error('Network response was not ok');
              }
              return response.json();
            })
            .then((data) => {
                setPlayerData(data);
            })
            .catch((error) => {
              console.error('Error:', error);
        });
    };
    return(
        <div className='playerStatsPage'>
            <p>Hello, world! The player you just selected:</p>
            {playerData ? (
                <div>
                    <p>Player ID: {playerData.id}</p>
                    <p>Player Name: {playerData.first_name} {playerData.last_name}</p>
                </div>
            ) : (
                <p>Loading player data...</p>
            )}
        </div>
    );
}

export default PlayerStats;