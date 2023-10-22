import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
    const [players, setPlayers] = useState([]);
    const [timeoutFlag, setTimeoutFlag] = useState(null);
    const [inputValue, setInputValue] = useState('');
    const [emptySearchBar, setEmptySearchBar] = useState(true);
    const [selectedPlayer, setSelectedPlayer] = useState(null);
    const navigate = useNavigate();
    let timerId; // Store the timer ID 
    const teamLogos = {
      1: 'ATL_Hawks.png',
      2: 'BKN_Nets.png',
      3: 'BOS_Celtics.png',
      4: 'CHA_Hornet.png',
      5: 'CHI_Bulls.png',
      6: 'CLE_Cavaliers.png',
      7: 'DAL_Mavericks.png',
      8: 'DEN_Nuggets.png',
      9: 'DET_Pistons.png',
      10: 'GSW_Warriors.png',
      11: 'HOU_Rockets.png',
      12: 'IND_Pacers.png',
      13: 'LAC_Clippers.png',
      14: 'LAL_Lakers.png',
      15: 'MEM_Grizzlies.png',
      16: 'MIA_Heat.png',
      17: 'MIL_Bucks.png',
      18: 'MIN_Timberwolves.png',
      19: 'NOP_Pelicans.png',
      20: 'NYK_Knicks.png',
      21: 'OKC_Thunder.png',
      22: 'ORL_Magic.png',
      23: 'PHI_76ers.png',
      24: 'PHX_Suns.png',
      25: 'POR_Trailblazers.png',
      26: 'SAC_Kings.png',
      27: 'SAS_Spurs.png',
      28: 'TOR_Raptors.png',
      29: 'UTA_Jazz.png',
      30: 'WAS_Wizards.png',
    };    
      const fetchPlayers = (inputValue) => {
        const encodedInputValue = encodeURIComponent(inputValue); // Encode the input value
      
        console.log('fetching data for: ', inputValue);
      
        // Make the GET request to the backend API
        fetch(`/api/player/search/${encodedInputValue}`, {
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
            // Handle the data received from the backend (data may contain player information)
            setPlayers(data);
          })
          .catch((error) => {
            console.error('Error:', error);
          });
      };
      
        const handleInputChange = (event) => {
          setInputValue(event.target.value);
        };
        
        useEffect(() => {
          console.log('inputValue is: ', inputValue);
          if(inputValue.length > 1){
            console.log(`Search for players with at least 2 characters: ${inputValue}`);
            // Clear any previous timers to prevent multiple updates
            clearTimeout(timerId);
            timerId = setTimeout(() => {
              if(timeoutFlag == false){
                setEmptySearchBar(false)
                setTimeoutFlag(true);
              }
              else if(timeoutFlag == true){
                setEmptySearchBar(false)
                setTimeoutFlag(false);
              }
              else if(timeoutFlag == null){
                setEmptySearchBar(false)
                setTimeoutFlag(true);
              }
            }, 1000);
          }

          else{
            setEmptySearchBar(true);
          }
        }, [inputValue])

        useEffect(() => {
          console.log('timer just ended! The input was:', inputValue);
          if(timeoutFlag != null){
            fetchPlayers(inputValue);
          }
        }, [timeoutFlag])

        const handleRowClick = (player) => {
          setSelectedPlayer(player); // Set the selected player when a row is clicked
          console.log('Selected Player:', player, 'with ID: ', player.id);
          navigate(`/playerStats/${player.id}`);
        };

        return (
          <div className="homePageDiv">
            <div className="homePageLogoDiv">
              <img
                src={process.env.PUBLIC_URL + '/hoopLogicLogo1.png'}
                alt="Hoop Logic Logo"
                className="homePageLogo"
              />
            </div>
            <div className="searchBarDiv">
              <input
                type="text"
                placeholder="Search for players by name"
                className="searchBar"
                style={{ fontFamily: 'Norwester' }}
                onChange={handleInputChange}
              />
              </div>
              {!emptySearchBar && (
              <div className="suggestedPlayersDiv">
                <table className='playersTable'>
                  <tbody>
                    {players.map((player) => (
                      <tr className='playersRow'key={player.id} onClick={() => handleRowClick(player)}>
                        <td className="teamLogoCell">
                          <img
                            src={`/teamLogos/${teamLogos[player.team]}`}
                            alt={`Team Logo for Team ${player.team}`}
                            className="teamLogo"
                          />
                        </td>
                        <td className="playerNameCell">{player.first_name} {player.last_name}</td>
                        <td className="playerPositionCell">
                          {player.position === '' ? 'N/A' : player.position === 'G' ? 'Guard' : player.position === 'F' ? 'Forward' : player.position === 'C' ? 'Center' : ''}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
            </div>
              )}
          </div>
        );
};

export default Home;