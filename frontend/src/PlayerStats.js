// route to call on load: /api/games/search/<player_id>/<games_count>
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const PlayerStats = () => {
    const { playerId } = useParams();
    const { gameCount } = useState(5);
    const [player, setPlayer] = useState(null);

    useEffect(() => {
        console.log('the received player id is: ', playerId);
        fetchPlayer(playerId, gameCount);
    },[])

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
              setPlayer(data);
            })
            .catch((error) => {
              console.error('Error:', error);
            });
    };
    return(
        <div className='playerStatsPage'>
            <p>Hello, world! The player you just selected:</p>
            {player ? (
                <div>
                    <p>Player ID: {player.id}</p>
                    <p>Player Name: {player.name}</p>
                </div>
            ) : (
                <p>Loading player data...</p>
            )}
        </div>
    );
}

export default PlayerStats;