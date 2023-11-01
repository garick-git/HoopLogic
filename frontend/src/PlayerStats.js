// routes to call on load: 
// /api/games/search/<player_id>/<games_count
// for local purposes, Stephen Curry will be the object being worked on.

import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

const PlayerStats = () => {
    const { playerId } = useParams();
    const [gameCount, setGameCount] = useState(5);
    const [lastXGames, setLastXGames] = useState(null);
    const [playerData, setPlayerData] = useState(null);
    const [emptySearchBar, setEmptySearchBar] = useState(true);
    const [inputValue, setInputValue] = useState('');
    const [timeoutFlag, setTimeoutFlag] = useState(null);
    const [players, setPlayers] = useState([]);
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

    const teamNames = {
      1: 'Atlanta Hawks',
      2: 'Brooklyn Nets',
      3: 'Boston Celtics',
      4: 'Charlotte Hornets',
      5: 'Chicago Bulls',
      6: 'Cleveland Cavaliers',
      7: 'Dallas Mavericks',
      8: 'Denver Nuggets',
      9: 'Detroit Pistons',
      10: 'Golden State Warriors',
      11: 'Houston Rockets',
      12: 'Indiana Pacers',
      13: 'LA Clippers',
      14: 'Los Angeles Lakers',
      15: 'Memphis Grizzlies',
      16: 'Miami Heat',
      17: 'Milwaukee Bucks',
      18: 'Minnesota Timberwolves',
      19: 'New Orleans Pelicans',
      20: 'New York Knicks',
      21: 'Oklahoma City Thunder',
      22: 'Orlando Magic',
      23: 'Philadelphia 76ers',
      24: 'Phoenix Suns',
      25: 'Portland Trail Blazers',
      26: 'Sacramento Kings',
      27: 'San Antonio Spurs',
      28: 'Toronto Raptors',
      29: 'Utah Jazz',
      30: 'Washington Wizards',
    };
    
    const localPlayerData = {
      first_name: "Stephen",
      height_feet: 6,
      height_in: 3,
      last_name: "Curry",
      position: "G",
      team_id: 10,
      weight: 190
    };    

    const localLastXGames =
      {PRA:40.4,assists:8.4,average_points:26.6,free_throws:2.8,rebounds:5.4,three_pointers:3.4};    

    useEffect(() => {
        fetchPlayer(playerId, gameCount);
    }, [])

    const fetchPlayer = (playerId, gameCount) => {
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
                console.log('Data fetched! LastXGames set to: ', data);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Stats could not be fetched! Switching to local gamesData...')
              setLastXGames(localLastXGames);
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
              console.error('Player could not be fetched! Switching to local playerData...')
              setPlayerData(localPlayerData);
        });
    };

    const fetchPlayers = (inputValue) => {
      const encodedInputValue = encodeURIComponent(inputValue); // Encode the input value
    
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
        if(inputValue.length > 1){
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
        if(timeoutFlag != null){
          fetchPlayers(inputValue);
        }
      }, [timeoutFlag])

      // useEffect(() => {
      //   console.log('lastXGames: ', lastXGames)
      //   console.log('PRA: ', lastXGames[0])
      //   // console.log('localLastXGames.PRA: ', localLastXGames.PRA)
      // }, [renderData])

      const handleRowClick = (player) => {
        navigate(`/playerStats/${player.id}`);
        window.location.reload();
      };

      const handleGoBack = () => {
        navigate(`/`);
      };
      return (
        playerData && lastXGames ? (
          <div className='playerStatsPage'>
            <img
              src={process.env.PUBLIC_URL + '/hoopLogicLogo2.png'}
              alt="Hoop Logic Logo"
              id="secondaryLogo"
              onClick={handleGoBack}
            />
            <div className='searchBarBigDiv'>
              <div className="searchBarDiv">
                <input
                  type="text"
                  placeholder="Search Again"
                  className="searchBar2"
                  style={{ fontFamily: 'Norwester' }}
                  onChange={handleInputChange}
                />
              </div>
              {emptySearchBar ? null : (
                <div className="suggestedPlayersDiv">
                  <table className='playersTable'>
                    <tbody>
                      {players.map((player) => (
                        <tr className='playersRow' key={player.id} onClick={() => handleRowClick(player)}>
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
            <div className="pageHeader">
              <img
                src={`/teamLogos/${teamLogos[playerData.team_id]}`}
                alt={`Team Logo for Team ${playerData.team_id}`}
                className="headerLogo"
              />
              <h1 className="playerName">{playerData.first_name} {playerData.last_name}</h1>
            </div>
            <div className="pageContent">
              <div className="biographyDiv">
                <h3 className='biographyTitle'>Bio</h3>
                <table className='biographyTable'>
                  <tbody>
                  <tr className="playerTeam">
                    <p className='playerTeamlbl'>Team: </p>
                    <p className='playerTeamName'>{teamNames[playerData.team_id]}</p>
                  </tr>
                  <tr className="playerPosition">
                      <p className='playerPositionlbl'>Position: </p>
                      <p className="playerPositionName">{playerData ? (
                          playerData.position === 'F'
                            ? 'Forward'
                            : playerData.position === 'C'
                            ? 'Center'
                            : playerData.position === 'G'
                            ? 'Guard'
                            : ''
                        ) : ''}
                      </p>
                  </tr>
                  <tr className="playerHeight">
                      <p className="playerHeightlbl">Height: </p>
                      <p className="playerHeightName">{playerData.height_feet}'{playerData.height_in}"</p>
                  </tr>
                  </tbody>
                </table>
              </div>
              <div className="statsDiv">
                <h3 className='statsTitle'>Stats</h3>
                <table className="statsTable">
                  <tbody>
                  <div className="topStatsRow">
                    <div className="pointsCell">
                      <p className="pointsLabel">Points</p>
                      <p className="pointsNumber">{lastXGames.average_points}</p>
                    </div>
                    <div className="spacerCell"></div>
                    <div className="freeThrowsCell">
                      <p>Free Throws</p>
                      <p>{lastXGames.free_throws}</p>
                  </div>
                  </div>
                    <tr>
                      <td>
                        <p>Rebounds</p>
                        <p>{lastXGames.rebounds}</p>
                      </td>
                      <td>
                        <p>Three Pointers</p>
                        <p>{lastXGames.three_pointers}</p>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <p>Assists</p>
                        <p>{lastXGames.assists}</p>
                      </td>
                      <td>
                        <p>P+R+A</p>
                        <p>{lastXGames.PRA}</p>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div className="graphDiv">
        
              </div>
            </div>
          </div>
        ) : (
          <p>Loading player data...</p>
        )
      );            
}

export default PlayerStats;