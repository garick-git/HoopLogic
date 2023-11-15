// routes to call on load: 
// /api/games/search/<player_id>/<games_count
// for local purposes, Stephen Curry will be the object being worked on.

import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Graph from './Graph.js';

const PlayerStats = () => {
    const { playerId } = useParams();
    const [gameCount, setGameCount] = useState(5);
    const [selectedTeam, setSelectedTeam] = useState(1);
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

    const NBA_TEAMS = [
      'All',
      'Atlanta Hawks',
      'Boston Celtics',
      'Brooklyn Nets',
      'Charlotte Hornets',
      'Chicago Bulls',
      'Cleveland Cavaliers',
      'Dallas Mavericks',
      'Denver Nuggets',
      'Detroit Pistons',
      'Golden State Warriors',
      'Houston Rockets',
      'Indiana Pacers',
      'LA Clippers',
      'Los Angeles Lakers',
      'Memphis Grizzlies',
      'Miami Heat',
      'Milwaukee Bucks',
      'Minnesota Timberwolves',
      'New Orleans Pelicans',
      'New York Knicks',
      'Oklahoma City Thunder',
      'Orlando Magic',
      'Philadelphia 76ers',
      'Phoenix Suns',
      'Portland Trail Blazers',
      'Sacramento Kings',
      'San Antonio Spurs',
      'Toronto Raptors',
      'Utah Jazz',
      'Washington Wizards',
    ];

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

    const roundAttributesToDecimal = (object) => {
      const roundedObject = {};
      for (const key in object) {
        if (typeof object[key] === 'number') {
          roundedObject[key] = Math.round(object[key] * 10) / 10; // Round to 1 decimal point
        } else {
          roundedObject[key] = object[key];
        }
      }
      return roundedObject;
    };

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
              const roundedData = roundAttributesToDecimal(data);
              setLastXGames(roundedData);
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

      const handleRowClick = (player) => {
        navigate(`/playerStats/${player.id}`);
        window.location.reload();
      };

      const handleGoBack = () => {
        navigate(`/`);
      };

      const handleTeamChange = (selection) => {
        console.log('your team selection: ', selection)
        setSelectedTeam(selection);
      }

      const handleGameCountChange = (selection) => {
        console.log('your game count selected: ', selection);
        setGameCount(selection);
      }

      const refreshStats = () => {
        console.log('Last games: ', gameCount);
        console.log('Team selected: ', selectedTeam);
        if(selectedTeam != 1){
          fetch(`/api/games/search/${playerId}/${gameCount}/${selectedTeam - 1}`, {
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
              console.log('selected team was NOT 1. Fetched data: ', data)
              const roundedData = roundAttributesToDecimal(data);
              setLastXGames(roundedData);
            })
            .catch((error) => {
              console.error('Error:', error);
            });
        }

        else{
          fetch(`/api/games/search/${playerId}/${gameCount}/${selectedTeam - 1}`, {
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
              console.log('selected team was 1. Fetched data: ', data)
              const roundedData = roundAttributesToDecimal(data);
              setLastXGames(roundedData);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Stats could not be fetched! Switching to local gamesData...')
              setLastXGames(localLastXGames);
        });
        }
      }

      useEffect(() => {
        console.log('lastXGames has changed! New array: ', lastXGames)
      },[lastXGames])

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
                            {player.position === null ? 'N/A' : player.position === '' ? 'N/A' : player.position === 'G' ? 'Guard' : player.position === 'F' ? 'Forward' : player.position === 'C' ? 'Center' : ''}
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
                        ) : 'N/A'}
                      </p>
                  </tr>
                  <tr className="playerHeight">
                      <p className="playerHeightlbl">Height: </p>
                      <p className="playerHeightName">
                        {playerData.height_feet && playerData.height_in
                          ? `${playerData.height_feet}'${playerData.height_in}"`
                          : 'N/A'}
                      </p>
                  </tr>
                  </tbody>
                </table>
              </div>
              <div className="statsDiv">
                <div className="statsTableHeader">
                  <h3 className='statsTitle'>Stats</h3>
                  <p className="lastGamesLabel">Last Games: </p>
                  <input type="number" min="1" max= "50" className="lastGamesInput"  onChange={(e) => handleGameCountChange(e.target.value)}/>
                  <p className="vsLabel">VS. </p>
                  <select className="rivalSelection" onChange={(e) => handleTeamChange(e.target.value)}>
                    {NBA_TEAMS.map((team, index) => (
                      <option key={index} value={index + 1}>{team}</option>
                    ))}
                  </select>
                  <img
                    src={process.env.PUBLIC_URL + '/arrowIcon.png'}
                    alt="Refresh Button"
                    className="refreshButton"
                    onClick={refreshStats}
                  />
                </div>
                <table className="statsTable">
                  <tbody>
                  <div className="topStatsRow">
                    <div className="pointsCell">
                      <p className="pointsLabel">Points</p>
                      <p className="cellNumber" id='pointsNumber'>{lastXGames.average_points}</p>
                    </div>
                    <div className="spacerCell"></div>
                    <div className="freeThrowsCell">
                      <p className='freeThrowsLabel'>Free Throws</p>
                      <p className='cellNumber'>{lastXGames.free_throws}</p>
                    </div>
                  </div>
                  <div className="topStatsRow">
                    <div className="pointsCell">
                        <p className="pointsLabel">Rebounds</p>
                        <p className="cellNumber" id='pointsNumber'>{lastXGames.rebounds}</p>
                      </div>
                      <div className="spacerCell"></div>
                      <div className="freeThrowsCell">
                        <p className='freeThrowsLabel'>Three Pointers</p>
                        <p className='cellNumber'>{lastXGames.three_pointers}</p>
                      </div>
                  </div>
                  <div className="topStatsRow">
                      <div className="alternateCell1">
                        <p className="pointsLabel">Assists</p>
                        <p className="cellNumber" id='pointsNumber'>{lastXGames.assists}</p>
                      </div>
                      <div className="spacerCell"></div>
                      <div className="alternateCell2">
                        <p className='freeThrowsLabel' id='PRALabel'>P+R+A</p>
                        <p className='cellNumber'>{lastXGames.PRA}</p>
                      </div>
                  </div>
                  </tbody>
                </table>
              </div>
              <Graph/>
            </div>
          </div>
        ) : (
          <p>Loading player data...</p>
        )
      );            
}

export default PlayerStats;